# 🌍 AirGuard AI

## AI-Powered Air Quality Risk Assistant

AirGuard AI is a machine-learning-based air-quality risk assessment system that analyzes major air pollutants and predicts the corresponding air-quality risk category.

The project combines **Machine Learning, Data Science, Explainable AI, Sustainability, and an interactive Streamlit dashboard** to help users understand air-quality conditions and take practical environmental actions.

---

## 🎯 Problem Statement

Air pollution is a major environmental challenge, particularly in urban areas. Air-quality measurements contain multiple pollutants, making it difficult for users to quickly understand the overall pollution risk.

AirGuard AI addresses this problem by:

- Analyzing major air pollutants
- Predicting an air-quality risk category
- Showing prediction probabilities
- Identifying influential model features
- Providing understandable pollutant information
- Suggesting practical environmental actions

---

## 💡 Objectives

- Develop a machine-learning model for air-quality risk classification.
- Analyze major pollutants associated with air-quality risk.
- Provide model explainability through feature importance.
- Build an interactive Streamlit dashboard.
- Promote awareness of air pollution.
- Encourage environmentally responsible actions.
- Support UN Sustainable Development Goals 11 and 13.

---

## 🏗️ System Architecture

```text
                 Air Quality Data
                        │
                        ▼
                Data Preprocessing
                        │
                        ▼
                Feature Selection
                        │
                        ▼
               Random Forest Model
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      Risk Classification    Probability Analysis
             │
             ▼
       Feature Importance
             │
             ▼
      AirGuard AI Assessment
             │
             ▼
      Pollutant Analysis
             │
             ▼
    Recommended Environmental
           Actions
             │
             ▼
       Streamlit Dashboard
```

## 📊 Dataset

AirGuard AI uses the Air_quality_data.csv dataset.

### Dataset Information

| Property | Value |
|---|---|
| Records | 18,265 |
| Columns | 13 |
| Target | AQI_Bucket |
| Time information | Datetime |
| Location information | City |
### Available Variables

- City
- Datetime
- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- AQI
- AQI_Bucket
## 🧹 Data Preprocessing

The dataset was processed using clean_data.py.

The preprocessing workflow includes:

1. Loading the dataset
2. Checking missing values
3. Checking the dataset structure
4. Cleaning the data
5. Saving the cleaned dataset

Output:

air_quality_cleaned.csv

The cleaned dataset contains:

18,265 records
13 columns
## 🤖 Machine Learning
Algorithm

AirGuard AI uses a:

Random Forest Classifier

### Input Features
PM2.5
PM10
NO2
SO2
CO
O3
### Target
AQI_Bucket
## ⚙️ Model Configuration
Algorithm: Random Forest
Number of estimators: 200
Random state: 42
Class weighting: Balanced
CPU jobs: -1

The dataset was divided using an 80/20 train-test split with stratification.

## 📈 Model Performance
| Metric | Result |
|---|---:|
| Test Accuracy | 99.15% |
| Macro F1 Score | 0.81 |
| Weighted F1 Score | 0.99 |

Important Note

The dataset is imbalanced across AQI categories.

The Good category has very few observations. Therefore, the overall accuracy should not be considered alone when evaluating the model.

The macro F1 score of 0.81 provides a more balanced view of performance across the classes.

## 🔎 Feature Importance

The Random Forest model produced the following global feature importance values:

| Pollutant | Importance |
|---|---:|
| PM2.5 | 0.322 |
| PM10 | 0.239 |
| CO | 0.142 |
| O3 | 0.138 |
| NO2 | 0.095 |
| SO2 | 0.064 |

PM2.5 is the most influential feature in the trained model.

Feature importance represents the influence of a feature within the trained model. It does not prove that the feature caused the predicted risk.

## 🖥️ Application Features
1. Air Quality Measurements

Users can enter:

PM2.5
PM10
NO₂
SO₂
CO
O₃
2. Risk Prediction

The model predicts:

Good
Satisfactory
Moderate
Poor
Very Poor
Severe
3. Prediction Confidence

The application displays the probability distribution across the possible risk categories.

4. Model Explainability

The dashboard displays feature importance to show which input features have greater influence on the trained model.

5. Pollutant Analysis

The application provides basic information about the pollutants used by the model.

6. Recommended Actions

The application provides practical environmental actions based on the predicted risk category.

7. Sustainability Connection

The project connects air-quality awareness with:

SDG 11 – Sustainable Cities and Communities
SDG 13 – Climate Action
## 🤖 AirGuard AI Assessment

The dashboard generates an understandable assessment based on the predicted risk category.

Example:

The model predicts a Moderate air-quality risk category.
Reducing unnecessary exposure and local emission sources
can help limit pollution.

The assessment is intended for environmental awareness and decision support.

## 🌫️ Prediction Flow
```text
User Input
    │
    ▼
Pollutant Measurements
    │
    ├── PM2.5
    ├── PM10
    ├── NO2
    ├── SO2
    ├── CO
    └── O3
    │
    ▼
Random Forest Classifier
    │
    ▼
AQI Risk Prediction
    │
    ├── Probability Distribution
    │
    ├── Feature Importance
    │
    └── Recommended Actions
```
## 🌱 Sustainability
SDG 11 — Sustainable Cities and Communities

AirGuard AI supports awareness of urban air-quality conditions and encourages actions that can contribute to cleaner and more sustainable communities.

SDG 13 — Climate Action

The project promotes environmental awareness and encourages actions that can reduce unnecessary pollution and emissions.

## 🧠 Explainable AI

AirGuard AI goes beyond simply producing a classification.

```text
Prediction
    ↓
Probability Distribution
    ↓
Feature Importance
    ↓
Pollutant Information
    ↓
Recommended Actions
```

This makes the model output easier to understand.

## 🛡️ Responsible AI

AirGuard AI follows several responsible-AI principles.

Transparency

Prediction probabilities and feature importance are displayed.

Model Limitations

Predictions depend on the data used to train the model.

Dataset Imbalance

Rare categories have fewer observations and require cautious interpretation.

No Medical Diagnosis

AirGuard AI is not a medical diagnostic system.

No Causal Claims

Feature importance is not treated as proof of causation.

Decision Support

The system provides environmental awareness and decision support rather than replacing official air-quality monitoring services.

## 🧰 Technologies Used

### Programming
- Python

### Machine Learning
- Scikit-learn
- Random Forest

### Data Processing
- Pandas
- NumPy

### Model Storage
- Joblib

### Visualization and Application
- Streamlit

### Development
- Visual Studio Code
- Git
- GitHub

### AI / Agent Architecture
- IBM watsonx Orchestrate
- IBM Granite
- Retrieval-Augmented Generation (RAG)
## 🧩 IBM watsonx Orchestrate Integration

During development, AirGuard AI was designed with an agent-based architecture using IBM watsonx Orchestrate.

The architecture included:
```text
Air Quality Data
       ↓
Machine Learning Model
       ↓
AirGuard AI Agent
       ↓
Knowledge Base
       ↓
Environmental Information
       ↓
Actionable Recommendations
```
The knowledge base included information from trusted environmental and public-health sources such as:

CPCB
WHO
U.S. EPA
United Nations SDG resources

The current Streamlit demonstration operates independently using the trained local machine-learning model and recommendation layer.

## 📁 Project Structure
```text
AirGuard-AI/
│
├── app.py
├── clean_data.py
├── train_model.py
├── airguard_model.pkl
├── Air_quality_data.csv
├── air_quality_cleaned.csv
├── requirements.txt
├── .gitignore
├── README.md
│
├── agents/
│   └── airguard_ai.yaml
│
└── knowledge-bases/
    ├── airguard_knowledge.yaml
    ├── download_docs.ps1
    │
    └── docs/
        ├── cpcb_air_pollution_control.html
        ├── cpcb_aqi_india.html
        ├── cpcb_naaqs.html
        ├── epa_co_basics.html
        ├── epa_no2_basics.html
        ├── epa_ozone_basics.html
        ├── epa_pm_basics.html
        ├── epa_so2_basics.html
        ├── sdg_goal11.html
        ├── sdg_goal13.html
        ├── who_air_pollution_topics.html
        └── who_ambient_air_quality.html
```
## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AirGuard-AI.git
cd AirGuard-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate on Windows

```powershell
venv\Scripts\activate
```

### Activate on Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```
## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.
## 📊 Train the Model

To clean the dataset:

```bash
python clean_data.py
```

To train the model:

```bash
python train_model.py
```

The trained model is saved as:

```text
airguard_model.pkl
```
## 🔐 Security

If external services are used, API credentials should be stored locally in a .env file.

Example:

WO_INSTANCE=your_instance_url
WO_API_KEY=your_api_key

Never upload API keys, passwords, or other secrets to GitHub.

The .gitignore file excludes:

.env
venv/
__pycache__/
*.pyc
.vscode/

## 🔮 Future Improvements
Real-time CPCB air-quality data integration
Location-based air-quality monitoring
Weather data integration
Air-quality forecasting
Time-series prediction
SHAP-based explainability
Interactive maps
Mobile application
Automated pollution alerts
More balanced training data
Real-time agent integration
Personalized environmental recommendations

## 🚀 Potential Applications

AirGuard AI could be extended for:

Smart city dashboards
Environmental monitoring
Educational applications
Pollution-awareness platforms
Community environmental programs
Sustainability dashboards
Public-awareness systems

## 📌 Project Highlights
```text
✔ Machine Learning
✔ Random Forest Classification
✔ Explainable AI
✔ Air Pollution Analysis
✔ Streamlit Dashboard
✔ Sustainability
✔ SDG 11
✔ SDG 13
✔ Responsible AI
✔ IBM watsonx Orchestrate Architecture
✔ RAG Knowledge Base
```
## 👩‍💻 Project Information
AirGuard AI

AI-Powered Air Quality Risk Assistant

Developed as part of the:

1M1B AI for Sustainability Virtual Internship

Focus Areas
Artificial Intelligence
Machine Learning
Data Science
Environmental Sustainability
Explainable AI
Responsible AI

## 📜 Disclaimer

AirGuard AI is an educational and environmental-awareness project.

Its predictions are generated by a machine-learning model trained on the available dataset. The results should not be considered a replacement for official air-quality monitoring systems, environmental authorities, or professional medical advice.
