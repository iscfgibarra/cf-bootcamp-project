import streamlit as st
from helpers import input_transform

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
    internet_service = cols[1].radio("Servicio Internet:", key="internet_service",
                                     options=["DSL", "Fibra Óptica", "No"],
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
    streaming_tv = cols[0].radio("TV Streaming:", key="streaming_tv",
                                 options=["Sí", "No"],
                                 horizontal=True)
    streaming_movies = cols[1].radio("Películas Streaming:", key="streaming_movies",
                                     options=["Sí", "No", "Sin Internet"],
                                     horizontal=True)
    cols = st.columns((1, 1))
    contract = cols[0].radio("Contrato:", key="contract",
                             options=["Mensual", "Anual", "Bianual"],
                             horizontal=True)
    paperless_billing = cols[1].radio("Facturación Sin Papel:", key="paperless_billing",
                                      options=["Sí", "No"],
                                      horizontal=True)
    cols = st.columns((1, 1))
    payment_method = cols[0].selectbox("Método Pago:", ["Cheque", "Cheque por Correo", "Transferencia Bancaria",
                                                        "Tarjeta de Crédito"], 0)
    dependants = cols[1].radio("Dependientes:", key="dependants",
                               options=["Sí", "No", "Sin Internet"],
                               horizontal=True)
    cols = st.columns((1, 1))
    antiguedad = cols[0].number_input("Antigüedad en Meses:", step=1, min_value=0)
    monthly_charges = cols[1].number_input("Cargos por mes:", min_value=0.00)
    cols = st.columns((1, 1))
    total_charges = cols[0].number_input("Cargos Totales:", min_value=0.00)

    submitted = st.form_submit_button(label="Predecir")

    if submitted:
        st.write(online_security)

        customer = {
            "gender": input_transform(gender),
            "seniorcitizen": 1 if input_transform(senior_citizen) == "yes" else 0,
            "partner": input_transform(partner)
            
        }


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
