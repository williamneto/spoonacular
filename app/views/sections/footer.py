from reactpy import component
from reactpy_material import grid, typography

@component
def Footer():
    return grid(
        grid(
            "© 2024 Spoonacular",
            attrs={
                "item": True,
                "xs": 12
            }
        ),
        attrs={
            "container": True,
            "spacing": 2
        }
    ).render()