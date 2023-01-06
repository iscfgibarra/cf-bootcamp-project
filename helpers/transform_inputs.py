dict_transform = {
    "Sí": "yes",
    "No": "no",
    "Masculino": "male",
    "Femenino": "female",
    "Sin Teléfono": "no_phone_service",
    "DSL": "dsl",
    "Fibra Óptica": "fiber_optic",
    "Sin Internet": "no_internet_service",
    "Mensual": "month-to-month",
    "Anual": "one_year",
    "Bianual": "two_year",
    "Cheque": "electronic_check",
    "Cheque por Correo": "mailed_check",
    "Transferencia Bancaria": "bank_transfer_(automatic)",
    "Tarjeta de Crédito": "credit_card_(automatic)"
}


def input_transform(value: str) -> str:
    if value in dict_transform.keys():
        return dict_transform[value]

    return ""
