import streamlit as st
import pandas as pd


st.set_page_config(page_title="Bug report", page_icon="🐞", layout="centered")

st.title("🐞 Bug report!")


st.write("## Predicción de deserción de un cliente")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))



def on_click():
    st.write("Oprimi el boton")

button_predict = st.button(label="Predecir", on_click=on_click)



