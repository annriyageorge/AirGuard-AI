import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AirGuard AI",
    page_icon="🌍",
    layout="wide"
)


# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("airguard_model.pkl")


# -----------------------------
# Title
# -----------------------------
st.title("🌍 AirGuard AI")
st.subheader("AI-Powered Air Quality Risk Assistant")

st.write(
    "AirGuard AI analyzes pollutant measurements and predicts "
    "the corresponding air-quality risk category."
)

st.info(
    "The prediction is based on PM2.5, PM10, NO₂, SO₂, CO and O₃."
)


# -----------------------------
# User inputs
# -----------------------------
st.header("🌫️ Air Quality Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input(
        "PM2.5",
        min_value=0.0,
        value=50.0,
        step=1.0
    )

    pm10 = st.number_input(
        "PM10",
        min_value=0.0,
        value=80.0,
        step=1.0
    )

with col2:
    no2 = st.number_input(
        "NO₂",
        min_value=0.0,
        value=30.0,
        step=1.0
    )

    so2 = st.number_input(
        "SO₂",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

with col3:
    co = st.number_input(
        "CO",
        min_value=0.0,
        value=1.0,
        step=0.1
    )

    o3 = st.number_input(
        "O₃",
        min_value=0.0,
        value=30.0,
        step=1.0
    )


# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Analyze Air Quality", use_container_width=True):

    input_data = pd.DataFrame({
        "PM2.5": [pm25],
        "PM10": [pm10],
        "NO2": [no2],
        "SO2": [so2],
        "CO": [co],
        "O3": [o3]
    })

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    classes = model.classes_

    confidence = max(probabilities) * 100


    # =========================================================
    # 1. AIRGUARD AI ASSESSMENT
    # =========================================================

    st.header("🤖 AirGuard AI Assessment")

    if prediction == "Good":
        assessment = (
            "The model predicts a Good air-quality risk category. "
            "Continue practices that help maintain cleaner air."
        )

    elif prediction == "Satisfactory":
        assessment = (
            "The model predicts a Satisfactory air-quality risk category. "
            "Continue reducing unnecessary pollution sources."
        )

    elif prediction == "Moderate":
        assessment = (
            "The model predicts a Moderate air-quality risk category. "
            "Reducing unnecessary exposure and local emission sources "
            "can help limit pollution."
        )

    elif prediction == "Poor":
        assessment = (
            "The model predicts a Poor air-quality risk category. "
            "Consider limiting prolonged outdoor exposure and reducing "
            "activities that contribute to local emissions."
        )

    elif prediction == "Very Poor":
        assessment = (
            "The model predicts a Very Poor air-quality risk category. "
            "Reducing outdoor exposure and avoiding unnecessary emission "
            "sources is recommended."
        )

    elif prediction == "Severe":
        assessment = (
            "The model predicts a Severe air-quality risk category. "
            "Limit prolonged outdoor exposure where practical and avoid "
            "activities that generate additional pollution."
        )

    else:
        assessment = (
            "The model produced an air-quality risk prediction. "
            "Consider the predicted category together with the pollutant "
            "measurements."
        )

    st.write(assessment)


    # =========================================================
    # 2. PREDICTION RESULT
    # =========================================================

    st.header("📊 Prediction")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.success(
            f"Predicted Air Quality Risk: **{prediction}**"
        )

    with result_col2:
        st.metric(
            "Prediction Confidence",
            f"{confidence:.2f}%"
        )


    # =========================================================
    # 3. INPUT SUMMARY
    # =========================================================

    st.subheader("🌫️ Pollutant Measurements")

    pollutant_df = pd.DataFrame({
        "Pollutant": [
            "PM2.5",
            "PM10",
            "NO₂",
            "SO₂",
            "CO",
            "O₃"
        ],
        "Input Value": [
            pm25,
            pm10,
            no2,
            so2,
            co,
            o3
        ]
    })

    st.dataframe(
        pollutant_df,
        use_container_width=True,
        hide_index=True
    )


    # =========================================================
    # 4. PROBABILITY SECTION
    # =========================================================

    st.subheader("📈 Risk Category Probabilities")

    probability_df = pd.DataFrame({
        "Risk Category": classes,
        "Probability (%)": probabilities * 100
    })

    probability_df = probability_df.sort_values(
        "Probability (%)",
        ascending=False
    )

    display_df = probability_df.copy()

    display_df["Probability (%)"] = (
        display_df["Probability (%)"].round(2)
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        probability_df.set_index("Risk Category"),
        use_container_width=True
    )


    # =========================================================
    # 5. FEATURE IMPORTANCE
    # =========================================================

    st.subheader("🔎 Most Influential Model Features")

    feature_names = [
        "PM2.5",
        "PM10",
        "NO2",
        "SO2",
        "CO",
        "O3"
    ]

    importance_df = pd.DataFrame({
        "Pollutant": feature_names,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        "Importance",
        ascending=False
    )

    importance_display = importance_df.copy()

    importance_display["Importance"] = (
        importance_display["Importance"].round(3)
    )

    st.dataframe(
        importance_display,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        importance_df.set_index("Pollutant"),
        use_container_width=True
    )

    top_pollutant = importance_df.iloc[0]["Pollutant"]

    st.info(
        f"**Most influential feature in the trained model:** "
        f"{top_pollutant}"
    )

    st.caption(
        "Feature importance represents the model's learned influence "
        "of each input feature. It does not prove that a pollutant "
        "caused the predicted risk."
    )


    # =========================================================
    # 6. POLLUTANT-SPECIFIC INFORMATION
    # =========================================================

    st.subheader("🧪 Pollutant Analysis")

    pollutant_values = {
        "PM2.5": pm25,
        "PM10": pm10,
        "NO₂": no2,
        "SO₂": so2,
        "CO": co,
        "O₃": o3
    }

    descriptions = {
        "PM2.5":
            "Fine particulate matter that can remain suspended in air.",

        "PM10":
            "Particulate matter consisting of particles up to about "
            "10 micrometres in diameter.",

        "NO₂":
            "A nitrogen oxide commonly associated with combustion and "
            "vehicle emissions.",

        "SO₂":
            "A sulfur-containing gas associated with combustion of "
            "sulfur-containing fuels.",

        "CO":
            "A colorless gas produced by incomplete combustion.",

        "O₃":
            "Ozone present near the ground can contribute to air pollution."
    }

    for pollutant, value in pollutant_values.items():

        with st.expander(f"{pollutant} — {value}"):

            st.write(descriptions[pollutant])

            st.write(
                f"**Measured input:** {value}"
            )


    # =========================================================
    # 7. RECOMMENDATIONS
    # =========================================================

    st.subheader("🌱 Recommended Actions")

    recommendations = {

        "Good": [
            "Continue practices that help maintain good air quality.",
            "Prefer walking or cycling for suitable short-distance trips.",
            "Continue reducing unnecessary vehicle emissions."
        ],

        "Satisfactory": [
            "Reduce unnecessary vehicle use.",
            "Avoid open burning of waste.",
            "Prefer public transport where practical."
        ],

        "Moderate": [
            "Reduce prolonged outdoor exposure if you are sensitive "
            "to air pollution.",
            "Avoid unnecessary vehicle trips.",
            "Avoid open burning and unnecessary smoke."
        ],

        "Poor": [
            "Limit prolonged outdoor activities.",
            "Reduce exposure near busy roads when practical.",
            "Avoid open burning and activities that generate smoke."
        ],

        "Very Poor": [
            "Limit prolonged outdoor exposure.",
            "Avoid strenuous outdoor activities when air quality is poor.",
            "Reduce unnecessary vehicle use and other emission sources."
        ],

        "Severe": [
            "Avoid prolonged outdoor exposure when practical.",
            "Stay indoors when appropriate.",
            "Avoid activities that generate additional local pollution."
        ]
    }

    for recommendation in recommendations.get(prediction, []):
        st.write("•", recommendation)


    # =========================================================
    # 8. SUSTAINABILITY
    # =========================================================

    st.subheader("🌍 Sustainability Connection")

    st.write(
        "AirGuard AI supports **SDG 11 – Sustainable Cities and "
        "Communities** by helping users understand air-quality risks "
        "and encouraging actions that can reduce pollution."
    )

    st.write(
        "It also supports **SDG 13 – Climate Action** by promoting "
        "awareness of pollution and environmentally responsible actions."
    )


# =============================================================
# RESPONSIBLE AI NOTICE
# =============================================================

st.divider()

st.caption(
    "⚠️ AirGuard AI provides an environmental risk prediction for "
    "awareness and decision support. It is not a medical diagnostic "
    "tool. Predictions depend on the trained dataset and the pollutant "
    "measurements provided by the user."
)