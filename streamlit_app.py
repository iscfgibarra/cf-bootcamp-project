import streamlit as st
import requests
from helpers import input_transform

st.set_page_config(page_title="Telco Customer Churn", page_icon="🚪", layout="centered")

st.title("🚪 Telco Customer Churn App")

st.sidebar.write(
    f"Esta aplicación muestra como podemos predecir la probabilidad de deserción de un cliente."
)

st.sidebar.write(
    """
    Los valores que maximizan la probabilidad de deserción:
    Donde 1 es el valor del promedio de Churn Rate
    
    | Feature          | Value      | Churn Index |
    | ---------------- | ---------- | ----------- |
    |gender            | female     | 1.025396    |
    |partner           |no          |1.221659     |
    |dependents        |no          |1.162212     |
    |phone_service     |yes         |1.011412     |
    |multiple_lines    |yes         |1.076948     |
    |internet_service  |fiber_optic |1.574895     |
    |online_security   |no          |1.559152     |
    |online_backup     |no          |1.497672     |
    |device_protection |no          |1.466379     |
    |tech_support      |no          |1.551717     |
    |streaming_tv      |no          |1.269897     |
    |streaming_tv      |yes         |1.121328     |
    |streaming_movies  |no          |1.255358     |
    |streaming_movies  |yes         |1.138182|
    |contract          |month-to-month|1.599082|
    |paperless_billing |yes|1.252560|
    |payment_method    |electronic_check|1.688682|
    """
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
                               options=["Sí", "No"],
                               horizontal=True)
    cols = st.columns((1, 1))
    antiguedad = cols[0].number_input("Antigüedad en Meses:", step=1, min_value=0)
    monthly_charges = cols[1].number_input("Cargos por mes:", min_value=0.00)
    cols = st.columns((1, 1))
    total_charges = cols[0].number_input("Cargos Totales:", min_value=0.00)

    submitted = st.form_submit_button(label="Predecir")

    if submitted:
        with st.spinner('Prediciendo...'):
            customer = {
                "gender": input_transform(gender),
                "seniorcitizen": "1" if input_transform(senior_citizen) == "yes" else "0",
                "partner": input_transform(partner),
                "dependents": input_transform(dependants),
                "phoneservice": input_transform(phone_service),
                "multiplelines": input_transform(multiple_lines),
                "internetservice": input_transform(internet_service),
                "onlinesecurity": input_transform(online_security),
                "onlinebackup": input_transform(online_backup),
                "deviceprotection": input_transform(device_protection),
                "techsupport": input_transform(tech_support),
                "streamingtv": input_transform(streaming_tv),
                "streamingmovies": input_transform(streaming_movies),
                "contract": input_transform(contract),
                "paperlessbilling": input_transform(paperless_billing),
                "paymentmethod": input_transform(payment_method),
                "tenure": antiguedad,
                "monthlycharges": monthly_charges,
                "totalcharges": total_charges
            }

            print(customer)
            url = "http://localhost:5006/predict"
            response = requests.post(url, json=customer)
            if response.status_code == 200:
                resp = response.json()
                print(resp)
                st.write("## Probablidad de deserción: " + str(round(resp['churnProb'],2)) + "%")
            st.success("¡Gracias por utilizarme!")
