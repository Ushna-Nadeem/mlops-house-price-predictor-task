# 🏠 House Price Predictor – MLOps Task

A complete machine learning pipeline for predicting house prices, built with **Flask**, integrated with **Docker**, and structured for **MLOps** workflows including automated formatting, linting, and deployment support.

---

## 📌 Overview

This project includes:

* 📊 **Model Training:** Trains a regression model on housing data (`house_prices.csv`)
* ⚙️ **Flask API:** Serves real-time predictions via HTTP POST requests
* 🌐 **Frontend:** Simple HTML form for user input
* 🐳 **Docker Support:** Containerized for consistent deployment
* ✅ **CI/CD Ready:** Includes GitHub Actions workflow
* 🧪 **Testing & Linting:** Automated with `pytest`, `flake8`, and `black`

---

## 📁 Project Structure

```
mlops-house-price-predictor-task/
├── .github/workflows/     # GitHub Actions CI/CD configs
├── modeldata/             # Contains house_prices.csv
├── app.py                 # Flask backend for serving predictions
├── main.py                # Model training and loading
├── test.py                # Unit tests
├── index.html             # Frontend form
├── Dockerfile             # Docker image definition
├── vercel.json            # Vercel deployment config
├── requirements.txt       # Project dependencies
├── pyproject.toml         # Formatter config (black)
├── .flake8                # Linter config
├── .gitignore             # Git ignore rules
├── .dockerignore          # Docker ignore rules
└── README.md              # Project documentation
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Ushna-Nadeem/mlops-house-price-predictor-task.git
cd mlops-house-price-predictor-task
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Visit **`http://localhost:5000`** in your browser.

---

## 🐳 Run with Docker

```bash
# Build the Docker image
docker build -t house-price-predictor .

# Run the container
docker run -p 5000:5000 house-price-predictor
```

---

## 🧪 Testing & Linting

```bash
# Run tests
pytest test.py

# Linting
flake8 .

# Format code
black .
```

---

## 🌐 Deployment

* **Vercel:** Deployment config via `vercel.json`
* **CI/CD:** GitHub Actions set up for auto-deployment and formatting checks

---

## 🧠 How It Works

* The user enters house features through a web form
* The form sends a request to the Flask API
* The model (trained in `main.py`) predicts the price
* Result is displayed instantly on the web page

---

## ✅ Features

* Simple and responsive UI
* Dockerized for portability
* Clean code practices with black, flake8
* Automated testing and GitHub Actions support
