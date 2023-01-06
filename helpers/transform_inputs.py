def input_transform(value: str) -> str:
    if value == "Sí":
        return "yes"

    if value == "No":
        return "no"

    if value == "Masculino":
        return "male"

    if value == "Femenino":
        return "female"

