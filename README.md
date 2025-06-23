# 🏠 MLOps House Price Predictor

This project demonstrates a complete MLOps workflow for predicting **house prices** based on input features using a machine learning model, with deployment and version control integrations.

🔗 **GitHub Repository:** [mlops-house-price-predictor-task](https://github.com/Ushna-Nadeem/mlops-house-price-predictor-task)

---

## 📌 Overview

This project includes:

* **📊 Model Training:** A regression model trained to predict house prices
* **⚙️ Flask API:** Backend service that handles prediction requests
* **🖥️ Frontend Interface:** User-friendly form to input house details
* **📁 DVC Integration:** Data versioning and experiment tracking using DVC
* **🐳 Docker Support:** Containerized setup using Docker and Docker Compose

---

## 📁 Project Structure

```
mlops-house-price-predictor-task/
├── app.py              # Flask API for predictions
├── model.py            # Model training and saving
├── templates/
│   └── index.html      # Frontend form
├── data/
│   └── housing.csv     # Dataset (tracked with DVC)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image config
├── docker-compose.yml  # Docker Compose setup
└── .gitignore / .dvc / README.md
```

---

## 🚀 How to Use

### 🔧 Local Setup

```bash
# Clone the repository
git clone https://github.com/Ushna-Nadeem/mlops-house-price-predictor-task.git
cd mlops-house-price-predictor-task

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Open your browser at `http://localhost:5000` and enter house details to get a predicted price.

---

### 🐳 Docker Usage

```bash
# Build and run using Docker Compose
docker-compose up --build
```

---

### 📂 DVC Workflow

```bash
# Pull the dataset tracked with DVC
dvc pull

# Track new data or changes
dvc add data/housing.csv
git add data/housing.csv.dvc
git commit -m "Track dataset with DVC"
```

---

## ✅ Features

* Predict house prices based on key features
* ML workflow with data versioning (DVC)
* Clean UI with real-time prediction
* Dockerized for consistent deployment
