import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("tfidf.pkl")

# Title
st.title("📰 Fake News Detection App")

# Text input box
user_input = st.text_area("Enter News Article Text Here:")

# Prediction button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        # Transform input and predict
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]
        
        # Optional: Show confidence
        confidence = model.decision_function(transformed_input)[0]
        
        # Display result
        if prediction == "FAKE":
            st.error(f"❌ Prediction: FAKE (Confidence Score: {confidence:.2f})")
        else:
            st.success(f"✅ Prediction: REAL (Confidence Score: {confidence:.2f})")

