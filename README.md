# 🚨 Spam Detection — NLP & Machine Learning

An end-to-end **Spam Detection system** built using Natural Language Processing (NLP) and Machine Learning to classify SMS messages as **Spam** or **Ham**.

The project covers the complete machine learning workflow, from text preprocessing and TF-IDF feature extraction to model training, evaluation, pipeline creation, API serving, and public deployment.

---

## 🚀 Live Demo

Try the deployed **SpamGuard AI** application:

👉 [SpamGuard AI — Public Demo](https://fatmag104-spam-detection.hf.space/)

---

## 📌 Project Overview

The system receives an SMS message and predicts whether it is:

* 🚨 **Spam**
* ✅ **Ham**

It also returns the estimated probability that the message is spam.

---

## 🧠 Machine Learning Workflow

```text
SMS Dataset
     ↓
Data Cleaning
     ↓
Label Encoding
     ↓
Train / Test Split
     ↓
TF-IDF Vectorization
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Final ML Pipeline
     ↓
Prediction API
     ↓
Spam / Ham Prediction
```

---

## 📊 Dataset

The project uses an SMS Spam dataset containing:

* **5,572 SMS messages**
* **2 classes:** Ham and Spam
* **Input:** SMS message text
* **Target:** Spam / Ham

The dataset was obtained from the SMS Spam Collection used in the PyCon tutorial dataset repository.

---

## 🔧 Technologies Used

### Programming

* Python

### Data & Machine Learning

* Pandas
* NumPy
* Scikit-learn
* TF-IDF
* Logistic Regression
* Multinomial Naive Bayes

### API & Deployment

* FastAPI
* Uvicorn
* Pydantic
* Joblib
* Hugging Face Spaces
* Gradio

### Frontend

* HTML
* CSS
* JavaScript

---

## 🧹 Text Processing

The project converts raw SMS messages into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

The vectorizer produced:

**7,668 TF-IDF features**

The TF-IDF vectorizer is fitted only on the training data and then applied to the test data to avoid data leakage.

---

## 🤖 Models

Two classification models were evaluated.

### 1. Multinomial Naive Bayes

| Metric    |   Score |
| --------- | ------: |
| Accuracy  |  96.05% |
| Precision | 100.00% |
| Recall    |  70.47% |
| F1 Score  |  82.68% |

### 2. Logistic Regression

| Metric    |   Score |
| --------- | ------: |
| Accuracy  |  97.31% |
| Precision | 100.00% |
| Recall    |  79.87% |
| F1 Score  |  88.81% |

### Final Model

**Logistic Regression** was selected as the final model based on its performance on the held-out test set.

> These metrics are measured on the project's held-out test split and should not be interpreted as guaranteed real-world performance.

---

## 🔗 Machine Learning Pipeline

The final system uses a Scikit-learn Pipeline combining:

```text
SMS Message
     ↓
TfidfVectorizer
     ↓
LogisticRegression
     ↓
Prediction
```

The complete pipeline is saved as:

```text
spam_detection_pipeline.pkl
```

This allows preprocessing and prediction to be performed consistently when the model is used later.

---

## ⚡ FastAPI

The trained model is also exposed through a FastAPI backend.

### Available Endpoints

#### GET `/`

Checks whether the API is running.

#### POST `/predict`

Receives an SMS message and returns:

```json
{
  "prediction": "Spam",
  "spam_probability": 0.8281
}
```

---

## 🌐 Public Demo

For the public online demonstration, the trained pipeline is loaded into a **Gradio application hosted on Hugging Face Spaces**.

The public demo allows users to:

* Enter an SMS message
* Run the trained ML model
* View Spam / Ham prediction
* View confidence
* Interact with the model without running the project locally

---

## 🖥️ Web Interface

The project also includes a modern web interface called **SpamGuard AI**.

The interface allows users to:

* Enter an SMS message
* Analyze the message
* View Spam / Ham prediction
* View spam probability
* View model performance
* Understand the ML pipeline

---

## 📁 Project Structure

```text
spam-detection/
│
├── static/
│   └── index.html
│
├── app.py
├── requirements.txt
├── spam_detection_pipeline.pkl
├── README.md
└── .gitignore
```

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/FatmaGamalhamed/spam-detection.git
cd spam-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server

```bash
python -m uvicorn app:app --reload
```

### 4. Open the API documentation

```text
http://127.0.0.1:8000/docs
```

### 5. Open the web interface

Make sure the FastAPI server is running, then open the frontend in your browser.

---

## 🧪 Example Predictions

### Spam

```text
Congratulations! You won a $1000 prize. Click now to claim your reward!
```

Example output:

```text
Spam
Probability: 82.81%
```

### Ham

```text
hi
```

Example output:

```text
Ham
Probability: 5.44%
```

---

## 🎯 What I Learned

Through this project, I practiced:

* Natural Language Processing
* Text preprocessing
* TF-IDF feature extraction
* Train/Test splitting
* Data leakage prevention
* Naive Bayes classification
* Logistic Regression
* Classification metrics
* Confusion Matrix
* Precision, Recall and F1 Score
* Probability prediction
* Scikit-learn Pipelines
* Model serialization with Joblib
* FastAPI
* Gradio
* Hugging Face Spaces
* Connecting a machine learning model to a web interface

---

## 🚀 Future Improvements

Possible improvements include:

* More advanced text preprocessing
* Hyperparameter tuning
* Testing additional NLP models
* Using word and character n-grams
* Handling multilingual SMS messages
* Adding a larger and more diverse dataset
* Improving confidence calibration
* Adding a richer public demo interface

---

## 👩‍💻 Author

**Fatma Gamal**

Computer Science / Artificial Intelligence Student

Focused on:

* Machine Learning
* Data
* Computer Vision
* Artificial Intelligence

---

## ⭐ Project Goal

This project is part of my Machine Learning portfolio and demonstrates an end-to-end workflow for building, evaluating, serving, and deploying a real-world NLP classification system.
