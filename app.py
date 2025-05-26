# import streamlit as st
# from PIL import Image

# st.set_page_config(layout="wide", page_title="Emotion Trend Dashboard")

# # Title
# st.title("📊 Emotion Analysis Dashboard from Instagram Posts")
# st.markdown("Visual comparison between emotionally healthy and depressed individuals based on multimodal emotion scores.")

# # Sidebar
# user_type = st.sidebar.radio("Select View:", ("Normal User", "Depressed User", "Compare Side-by-Side"))

# # Analysis Texts
# def show_analysis(group):
#     if group == "Normal User":
#         st.subheader("Analysis for Emotionally Healthy (Normal) Users")
#         st.markdown("""
#         - **Happiness** remains consistently high (close to 1.0) over time.
#         - **Negative emotions** like sadness, fear, and anger are nearly absent.
#         - The radar chart is sharply spiked toward **happiness**, indicating emotional stability and positivity.
#         """)
#     elif group == "Depressed User":
#         st.subheader("Analysis for Users Showing Depressive Tendencies")
#         st.markdown("""
#         - **Happiness** gradually declines, while **sadness and fear** increase steadily.
#         - The positive-vs-negative emotion plot shows **negative emotions overtaking** positive ones after mid-September.
#         - The radar chart shows a **flatter profile**, indicating **emotional imbalance** with significant sadness and fear.
#         """)
#     else:
#         st.subheader("Comparison Summary")
#         st.markdown("""
#         - **Normal users** maintain high happiness and negligible negative emotion.
#         - **Depressed users** show a **rising trend in sadness** and drop in happiness over time.
#         - Radar plots clearly differentiate the **emotional polarity** between the two groups.
#         - Divergence in emotional profiles can be quantified via metrics like cosine similarity (optional).
#         """)

# # Image Loader
# def show_images(path_prefix):
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         st.image(Image.open(f"{path_prefix}/pos_neg.png"), caption="Positive vs Negative Emotion Trend", use_column_width=True)
#         st.image(Image.open(f"{path_prefix}/emotion_trend.png"), caption="Emotion-wise Time Series", use_column_width=True)
#         st.image(Image.open(f"{path_prefix}/radar.png"), caption="Average Emotion Profile (Radar Chart)", use_column_width=True)

# # Logic
# if user_type == "Normal User":
#     show_images("normal")
#     show_analysis("Normal User")
# elif user_type == "Depressed User":
#     show_images("depressed")
#     show_analysis("Depressed User")
# else:
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("😃 Normal User")
#         st.image("normal/pos_neg.png", caption="Positive vs Negative")
#         st.image("normal/emotion_trend.png", caption="Emotion Trend")
#         st.image("normal/radar.png", caption="Radar Chart")

#     with col2:
#         st.subheader("😞 Depressed User")
#         st.image("depressed/pos_neg.png", caption="Positive vs Negative")
#         st.image("depressed/emotion_trend.png", caption="Emotion Trend")
#         st.image("depressed/radar.png", caption="Radar Chart")

#     show_analysis("Compare Side-by-Side")


import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Emotion Trend Dashboard")

# Title
st.title("📊 Emotion Analysis Dashboard from Instagram Posts")
st.markdown("A visual and analytical comparison between emotionally healthy and depressed individuals using multimodal emotion scores extracted from posts over time.")

# Sidebar
user_type = st.sidebar.radio("Select View:", ("Normal User", "Depressed User", "Compare Side-by-Side"))

# Detailed Analysis
def show_analysis(group):
    if group == "Normal User":
        st.subheader("Detailed Analysis: Emotionally Healthy Users")

        st.markdown("### 🔹 Positive vs Negative Emotion Trend")
        st.markdown("""
        - The **positive emotion line (green)** remains consistently high across the timeline, indicating a stable and optimistic emotional state.
        - The **negative emotion line (red)** is nearly zero throughout, suggesting minimal or no presence of sadness, fear, anger, or related emotions.
        - This trend signifies **emotional stability**, resilience, and general well-being.
        """)

        st.markdown("### 🔹 Smoothed Emotion Trends (Happiness, Sadness, etc.)")
        st.markdown("""
        - **Happiness** remains the dominant emotion, mostly above **0.85** with only slight dips.
        - **Negative emotions** (sadness, fear, anger) remain close to **zero**, with **surprise** having only minor, short-lived spikes.
        - This pattern reflects a generally happy and content user posting joyful or neutral content.
        """)

        st.markdown("### 🔹 Radar Chart (Average Emotion Profile)")
        st.markdown("""
        - The radar chart shows a **strong peak in happiness (~0.9)** with negligible values for other emotions.
        - This spiky pattern is typical of individuals with a **clear emotional polarity toward positivity**, reflecting psychological well-being.
        """)

    elif group == "Depressed User":
        st.subheader("Detailed Analysis: Users Showing Depressive Tendencies")

        st.markdown("### 🔹 Positive vs Negative Emotion Trend")
        st.markdown("""
        - The **positive emotion line** starts moderately high but **declines** steadily over time.
        - The **negative emotion line** increases gradually and eventually **surpasses positive emotion** around mid-September.
        - This crossover marks a critical transition, indicating a shift from positive to predominantly negative emotional expression — a **key indicator of emotional distress**.
        """)

        st.markdown("### 🔹 Smoothed Emotion Trends (Happiness, Sadness, etc.)")
        st.markdown("""
        - **Happiness** shows a downward trend from ~0.9 to ~0.4, reflecting **declining mood**.
        - **Sadness and fear** rise gradually, peaking toward the end of the timeline.
        - **Anger and disgust**, while lower in intensity, are also present — suggesting a mix of distress, frustration, and anxiety.
        - The rising trend of multiple negative emotions is consistent with patterns found in **depressive behavior**.
        """)

        st.markdown("### 🔹 Radar Chart (Average Emotion Profile)")
        st.markdown("""
        - The radar plot is **flatter** with **happiness ~0.5**, **sadness ~0.35**, and **fear ~0.2**.
        - This profile shows **emotional imbalance**, with significant presence of multiple negative emotions, unlike the sharp 'happiness-only' spike seen in healthy individuals.
        """)

    else:
        st.subheader("Detailed Comparison: Healthy vs Depressed Individuals")

        st.markdown("### 🔹 Cross-User Emotion Divergence")
        st.markdown("""
        - **Normal users** maintain emotional consistency with stable high happiness and nearly absent negative emotions.
        - **Depressed users** show a **temporal emotional shift** — happiness falls, and sadness + fear increase gradually.
        - The **positive-negative crossover** in depressed users (around 2022-09-09) is a red flag indicating mood reversal.
        """)

        st.markdown("### 🔹 Comparative Radar Chart Insights")
        st.markdown("""
        - Normal: Highly peaked toward **happiness (0.9+)**, negligible others.
        - Depressed: Flatter, with **sadness (~0.35)** and **fear (~0.2)** joining happiness (~0.5).
        - Indicates **diluted emotional positivity** and onset of negative emotions in depressed users.
        """)

        st.markdown("### 🔹 Summary Metrics")
        st.markdown("""
        | Emotion | Normal (avg) | Depressed (avg) |
        |---------|---------------|------------------|
        | Happiness | 0.90 | 0.50 |
        | Sadness | ~0.05 | 0.35 |
        | Fear | ~0.03 | 0.20 |
        | Disgust/Anger | ~0.01 | 0.05–0.08 |
        """)

# Image Display Function
def show_images(path_prefix):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(Image.open(f"{path_prefix}/pos_neg.png"), caption="Positive vs Negative Emotion Trend", use_container_width=True)
    with col2:
        st.image(Image.open(f"{path_prefix}/emotion_trend.png"), caption="Emotion-wise Time Series", use_container_width=True)

    st.image(Image.open(f"{path_prefix}/radar.png"), caption="Average Emotion Profile (Radar Chart)", use_container_width=False)

# Logic
if user_type == "Normal User":
    show_images("normal")
    show_analysis("Normal User")
elif user_type == "Depressed User":
    show_images("depressed")
    show_analysis("Depressed User")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("😃 Normal User")
        st.image("normal/pos_neg.png", caption="Positive vs Negative")
        st.image("normal/emotion_trend.png", caption="Emotion Trend")
        st.image("normal/radar.png", caption="Radar Chart")

    with col2:
        st.subheader("😞 Depressed User")
        st.image("depressed/pos_neg.png", caption="Positive vs Negative")
        st.image("depressed/emotion_trend.png", caption="Emotion Trend")
        st.image("depressed/radar.png", caption="Radar Chart")

    show_analysis("Compare Side-by-Side")
