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
    Makes prediction based on image content (deterministic)
    So same image = same result
    """

    # Read image bytes
    image_bytes = image_file.read()

    # Create deterministic seed from image
    seed = sum(image_bytes)
    random.seed(seed)

    # pick 20 random classes
    sample_20 = random.sample(range(TOTAL_CLASSES), min(20, TOTAL_CLASSES))

    # pick 1 from those
    pred = random.choice(sample_20)

    # reset pointer (VERY IMPORTANT 🔥)
    image_file.seek(0)

    return pred

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

@app.route('/submit', methods=['POST'])
def submit():
    image = request.files['image']

    # -------- get prediction BEFORE saving --------
    pred = fake_prediction(image)

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

    return render_template(
        'submit.html',
        title=title,
        desc=description,
        prevent=prevent,
        image_url=image_url,
        pred=pred,
        sname=supplement_name,
        simage=supplement_image_url,
        buy_link=supplement_buy_link
    )

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