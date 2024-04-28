import streamlit as st
import joblib
import time
from PIL import Image

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
st.set_page_config(page_title="Aplikasi Prediksi Jenis Kelamin", page_icon=":busts_in_silhouette:", layout="wide")
st.title(':busts_in_silhouette: Aplikasi Prediksi Jenis Kelamin')

col1, col2 = st.columns(2)
with col1:
    st.image("https://www.publicdomainpictures.net/pictures/320000/nahled/gender-equality-symbol.jpg", width=200)
    fav_color = st.selectbox(
    "Warna Favorit",
    color_op,
    index=None,
    placeholder="Pilih Warna Favorit...",
    )
    fav_music_genre = st.selectbox(
    "Genre Musik Favorit",
    music_genre_op,
    index=None,
    placeholder="Pilih Genre Musik Favorit...",
    )
with col2:
    fav_beverage = st.selectbox(
    "Minuman Favorit",
    beverage_op,
    index=None,
    placeholder="Pilih Minuman Favorit...",
    )
    fav_soft_drink = st.selectbox(
    "Soft Drink Favorit",
    soft_drink_op,
    index=None,
    placeholder="Pilih Soft Drink Favorit...",
    )

bt1, bt2, bt3 = st.columns(3)
with bt2:
    if st.button("Prediksi", type="primary"):
        # Display loading animation
        with st.spinner('Melakukan Processing...'):
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
            predicted_value = "Wanita"
            st.title(f':pink[{predicted_value}]')
        else:
            predicted_value = "Pria"
            st.title(f':green[{predicted_value}]')
