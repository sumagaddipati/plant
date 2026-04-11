# 🌿 Plant Disease Detection System

A web-based application that identifies plant diseases from leaf images and provides detailed insights along with recommended supplements and preventive measures.

---

## 🚀 Overview

This project combines **computer vision** and **web development** to build an intelligent system capable of analyzing plant leaf images and predicting possible diseases. The application aims to assist farmers, researchers, and agricultural enthusiasts in early detection and treatment of plant diseases.

---

## 🧠 Features

* 📸 Upload leaf images for analysis
* 🌱 Detect plant diseases across multiple crops
* 📖 Get detailed disease descriptions
* 🛡️ View preventive measures
* 💊 Recommended supplements with purchase links
* 🌐 Fully deployed web application

---

## 🏗️ Tech Stack

### Backend

* Python
* Flask

### Machine Learning

* PyTorch
* Custom CNN / Deep Learning Model

### Frontend

* HTML
* CSS
* Jinja2 Templates

### Deployment

* Render (Cloud Hosting)

---

## 📂 Project Structure

```
project/
│── app.py
│── CNN.py
│── disease_info.csv
│── supplement_info.csv
│── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── submit.html
│   ├── contact-us.html
│   └── market.html
│
├── static/
│   ├── uploads/
│   ├── css/
│   └── images/
```

---

## ⚙️ How It Works

1. User uploads a leaf image
2. Image is processed and transformed
3. Model analyzes the image
4. Predicted disease is mapped to dataset
5. Application displays:

   * Disease name
   * Description
   * Preventive steps
   * Suggested supplements

---

## 📊 Dataset

The system is trained on a plant disease dataset containing multiple crops and disease categories. It includes:

* Apple
* Corn
* Grape
* Tomato
* Potato
* Strawberry
* And more

Each class contains labeled images for accurate learning.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/plant-disease-detection.git
cd plant-disease-detection
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```bash
python app.py
```

---

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🌍 Deployment

The application is deployed on **Render**, making it accessible online without any local setup.

---

## 📌 Use Cases

* 🌾 Farmers for early disease detection
* 🧪 Agricultural research
* 📚 Educational purposes
* 🌱 Smart farming solutions

---

## 🔮 Future Enhancements

* Improve model accuracy with larger datasets
* Add real-time camera detection
* Mobile application integration
* Multi-language support
* Advanced analytics dashboard

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit pull requests.

---

## 📜 License

This project is for educational and research purposes.

---

## 💡 Author

Developed by Sumalatha Gaddipati 🚀
