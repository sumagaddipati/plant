import os
import random
import pandas as pd
from flask import Flask, render_template, request
from PIL import Image

# -------------------- PATH SETUP --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------- FILE PATHS --------------------
disease_path    = os.path.join(BASE_DIR, "disease_info.csv")
supplement_path = os.path.join(BASE_DIR, "supplement_info.csv")

# -------------------- LOAD CSV --------------------
disease_info    = pd.read_csv(disease_path, encoding='cp1252')
supplement_info = pd.read_csv(supplement_path, encoding='cp1252')

TOTAL_CLASSES = len(disease_info)

# -------------------- CONSISTENT FAKE PREDICTION --------------------
def fake_prediction(image_file):
    """
    SAME LOGIC — NOT TOUCHED
    """

    image_bytes = image_file.read()
    seed = sum(image_bytes)
    random.seed(seed)

    sample_20 = random.sample(range(TOTAL_CLASSES), min(20, TOTAL_CLASSES))
    pred = random.choice(sample_20)

    image_file.seek(0)

    return pred, sample_20   # ✅ ONLY ADDING sample_20 (safe extension)


# -------------------- FLASK APP --------------------
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')

# -------------------- SUBMIT --------------------
@app.route('/submit', methods=['POST'])
def submit():
    image = request.files['image']

    # -------- prediction --------
    pred, sample_20 = fake_prediction(image)

    # -------- save image --------
    upload_dir = os.path.join(BASE_DIR, "static", "uploads")
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, image.filename)
    image.save(file_path)

    # -------- disease --------
    title       = disease_info['disease_name'][pred]
    description = disease_info['description'][pred]
    prevent     = disease_info['Possible Steps'][pred]
    image_url   = disease_info['image_url'][pred]

    # -------- supplement --------
    supplement_name      = supplement_info['supplement name'][pred]
    supplement_image_url = supplement_info['supplement image'][pred]
    supplement_buy_link  = supplement_info['buy link'][pred]

    # ---------------- NEW UI FEATURES (SAFE ADD) ----------------

    # Fake confidence (based on seed logic, still deterministic)
    confidence = round((pred % 100) * 0.8 + 20, 2)   # always 20–100%

    # Top 3 from sampled 20
    top3 = sample_20[:3]

    top3_names  = [disease_info['disease_name'][i] for i in top3]
    top3_scores = [round(100 - (i*10), 2) for i in range(len(top3))]

    # ----------------------------------------------------------

    return render_template(
        'submit.html',
        title=title,
        desc=description,
        prevent=prevent,
        image_url=image_url,
        pred=pred,
        sname=supplement_name,
        simage=supplement_image_url,
        buy_link=supplement_buy_link,

        # NEW (UI support)
        confidence=confidence,
        top3_names=top3_names,
        top3_scores=top3_scores
    )


# -------------------- MARKET --------------------
@app.route('/market')
def market():
    return render_template(
        'market.html',
        supplement_image=list(supplement_info['supplement image']),
        supplement_name=list(supplement_info['supplement name']),
        disease=list(disease_info['disease_name']),
        buy=list(supplement_info['buy link'])
    )

# -------------------- RUN --------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)