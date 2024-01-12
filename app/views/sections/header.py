from reactpy import component
from reactpy_material import typography, box

@component
def HeaderTop():
    return box(
        typography(
            "Spoonacular",
            attrs={
                "variant": "h1"
            }
        )
    ).render()