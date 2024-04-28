import streamlit as st
import joblib
import time

# Load model
model = joblib.load('Klasifikasi_Model_Gender.pkl')

# Map options
color_op = ('Cool', 'Neutral', 'Warm')
music_genre_op = ('Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic','R&B and soul')
beverage_op = ('Vodka', 'Wine', 'Whiskey',"Doesn't drink",'Beer', 'Other')
soft_drink_op = ('7UP/Sprite', 'Coca Cola/Pepsi','Fanta','Other')

# Encode options
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

color_encoded = label_encoder.fit_transform(color_op)
music_genre_encoded = label_encoder.fit_transform(music_genre_op)
beverage_encoded = label_encoder.fit_transform(beverage_op)
soft_drink_encoded = label_encoder.fit_transform(soft_drink_op)

# Streamlit app
st.title('Gender Prediction App')

col1, col2 = st.columns(2)
with col1:
    fav_color = st.selectbox(
    "Favorite Color",
    color_op,
    index=None,
    placeholder="Select Favorite Color...",
    )
    fav_music_genre = st.selectbox(
    "Favorite Music Genre",
    music_genre_op,
    index=None,
    placeholder="Select Favorite Music Genre...",
    )
with col2:
    fav_beverage = st.selectbox(
    "Favorite Beverage",
    beverage_op,
    index=None,
    placeholder="Select Favorite Beverage...",
    )
    fav_soft_drink = st.selectbox(
    "Favorite Soft Drink",
    soft_drink_op,
    index=None,
    placeholder="Select Favorite Soft Drink...",
    )

bt1, bt2, bt3 = st.columns(3)
with bt2:
    if st.button("Predict", type="primary"):
        # Display loading animation
        with st.spinner('Processing...'):
            # Lengthy process or time-consuming task
            time.sleep(2)  # Example of a 2-second process

        # Convert user choices to numeric values
        color_selected = color_encoded[color_op.index(fav_color)]
        music_genre_selected = music_genre_encoded[music_genre_op.index(fav_music_genre)]
        beverage_selected = beverage_encoded[beverage_op.index(fav_beverage)]
        soft_drink_selected = soft_drink_encoded[soft_drink_op.index(fav_soft_drink)]

        # Use the loaded model to predict gender
        predicted_rest = model.predict([[color_selected, music_genre_selected, beverage_selected, soft_drink_selected]])

        if predicted_rest[0] == 1:
            predicted_value = "Female"
            st.title(f':red[{predicted_value}]')
        else:
            predicted_value = "Man"
            st.title(f':blue[{predicted_value}]')
