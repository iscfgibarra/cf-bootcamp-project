import streamlit as st
import pandas as pd

st.set_page_config(page_title="Telco Customer Churn", page_icon="🚪", layout="centered")

st.title("🚪 Telco Customer Churn App")

st.sidebar.write(
    f"Esta aplicación muestra como podemos predecir la probabilidad de deserción de un cliente."
)

form = st.form(key="customer")

with form:
    cols = st.columns((1, 1))
    gender = cols[0].radio("Género:", key="gender", options=["Masculino", "Femenino"], horizontal=True)
    senior_citizen = cols[1].radio("Persona Mayor:", key="senior_citizen", options=["Sí", "No"], horizontal=True)
    cols = st.columns((1, 1))
    partner = cols[0].radio("Vive con Pareja:", key="partner", options=["Sí", "No"], horizontal=True)
    phone_service = cols[1].radio("Servicio Telefónico:", key="phone_service", options=["Sí", "No"], horizontal=True)
    cols = st.columns((1, 1))
    multiple_lines = cols[0].radio("Multiples Lineas:",
                                   key="multiple_lines",
                                   options=["Sí", "No", "Sin Teléfono"], horizontal=True)
    internet_service = cols[1].radio("Servicio Internet:", key="internet_service", options=["Sí", "No"],
                                     horizontal=True)
    cols = st.columns((1, 1))
    online_security = cols[0].radio("Seguridad Online:", key="online_security", options=["Sí", "No", "Sin Internet"],
                                    horizontal=True)
    online_backup = cols[1].radio("Respaldo Online:", key="online_backup", options=["Sí", "No", "Sin Internet"],
                                  horizontal=True)
    cols = st.columns((1, 1))
    device_protection = cols[0].radio("Protección Dispositivos:", key="device_protection",
                                      options=["Sí", "No", "Sin Internet"],
                                      horizontal=True)
    tech_support = cols[1].radio("Soporte Técnico:", key="tech_support",
                                 options=["Sí", "No", "Sin Internet"],
                                 horizontal=True)
    cols = st.columns((1, 1))
    dependants = cols[0].number_input("Dependientes:", step=1, min_value=0)
    antiguedad = cols[1].number_input("Antigüedad en Meses:", step=1, min_value=0)
    # author = cols[0].text_input("Report author:")

    # bug_type = cols[1].selectbox(
    #     "Bug type:", ["Front-end", "Back-end", "Data related", "404"], index=2
    # )
    # comment = st.text_area("Comment:")
    # cols = st.columns(2)
    # date = cols[0].date_input("Bug date occurrence:")
    # bug_severity = cols[1].slider("Bug severity:", 1, 5, 2)
    submitted = st.form_submit_button(label="Predecir")

    if submitted:
        st.write(online_security)
# seniorcitizen: int
#     partner: str
#     dependents: str
#     phoneservice: str
#     multiplelines: str
#     internetservice: str
#     onlinesecurity: str
#     onlinebackup: str
#     deviceprotection: str
#     techsupport: str
#     streamingtv: str
#     streamingmovies: str
#     contract: str
#     paperlessbilling: str
#     paymentmethod: str
#     tenure: int
#     monthlycharges: float
#     totalcharges: float