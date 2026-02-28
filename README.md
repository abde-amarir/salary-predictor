# 💰 Developer Salary Predictor

> A machine learning model trained on **90,000+ real developer responses** from the Stack Overflow Annual Survey to predict developer salaries based on experience, skills, education, and location.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## 🎯 What This Project Does

This project walks through the **full machine learning lifecycle** — from raw, messy, real-world data to a deployed web application:

1. **Explore** messy survey data (90k+ rows, mixed types, missing values)
2. **Clean** it — handle nulls, inconsistent strings, outliers
3. **Engineer features** — transform survey answers into ML-usable numbers
4. **Train & evaluate** multiple regression models
5. **Deploy** a Streamlit web app where users can predict their own salary

This is a real project — not a tutorial dataset. The data is messy. The decisions are non-obvious. That's the point.

---

## 🚀 Live Demo

> 🔗 **[Try the app → coming soon]**

---

## 🗂️ Project Structure

```
salary-predictor/
│
├── data/
│   ├── raw/                    # Original downloaded survey data (not tracked by Git)
│   └── processed/              # Cleaned data saved after preprocessing
│
├── notebooks/
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_cleaning.ipynb       # Data cleaning & preprocessing
│   ├── 03_feature_engineering.ipynb
│   └── 04_modeling.ipynb       # Training & evaluating models
│
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py        # Reusable cleaning functions
│   ├── feature_engineering.py  # Feature transformation logic
│   └── model.py                # Model training and evaluation
│
├── app.py                      # Streamlit web application
├── model.pkl                   # Saved trained model (generated, not tracked)
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/abde-amarir/salary-predictor.git
cd salary-predictor
```

### 2. Create and activate a virtual environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the data

This project uses the **Stack Overflow Annual Developer Survey**.

1. Go to: https://survey.stackoverflow.co/
2. Download the **2023 survey results** (the CSV file)
3. Place the file inside `data/raw/` as `survey_results_public.csv`

> ⚠️ The raw data file is not tracked by Git due to its size. You need to download it manually.

---

## 🧪 Running the Notebooks

```bash
jupyter notebook
```

Open notebooks in order:
1. `notebooks/01_eda.ipynb` — Start here to explore the data
2. `notebooks/02_cleaning.ipynb`
3. `notebooks/03_feature_engineering.ipynb`
4. `notebooks/04_modeling.ipynb`

---

## 🌐 Running the Web App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📊 Data Source

- **Source:** [Stack Overflow Annual Developer Survey 2023](https://survey.stackoverflow.co/)
- **Size:** ~90,000 respondents
- **Key features used:** Country, Education level, Years of experience, Programming languages, Employment type, Company size

---

## 🤖 Models Explored

| Model | Description |
|-------|-------------|
| Linear Regression | Baseline model — fast, interpretable |
| Decision Tree | Non-linear, shows feature importance |
| Random Forest | Ensemble of trees — robust to noise |
| Gradient Boosting | High performance on tabular data |

---

## 📈 Results

> 🔜 Results will be updated as the project progresses.

| Model | MAE (USD) | R² Score |
|-------|-----------|----------|
| Linear Regression | TBD | TBD |
| Random Forest | TBD | TBD |
| Gradient Boosting | TBD | TBD |

---

## 🧠 Key Learnings

> 🔜 Will be updated with findings as the project progresses.

- What features matter most for salary prediction?
- How to handle 70+ columns of messy survey data?
- Why clean data is a skill, not a given.

---

## 📣 Follow Along

This project is being built **step by step in public**:

- 🐦 X (Twitter): [@AmarirLabs]
- 💼 LinkedIn: [ABDESSAMAD AMARIR]

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 🙏 Acknowledgements

- [Stack Overflow](https://stackoverflow.com/) for making the survey data publicly available.
- [scikit-learn](https://scikit-learn.org/) for the ML tools.
- [Streamlit](https://streamlit.io/) for making deployment incredibly easy.

## ⚠️ Known Limitations

- **Salaries are in USD without Purchasing Power Parity (PPP) adjustment.**  
  A $15,000 salary in Morocco represents very different living standards  
  than $15,000 in the United States. The model may undervalue developers  
  in countries with lower costs of living.  
  
  **Planned improvements:**
  - v2: Join a PPP index dataset to normalize salaries by country
  - v3: Train separate models per economic region