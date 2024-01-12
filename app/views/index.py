from reactpy import component, html
from reactpy_material import container

from views.sections import HeaderTop
from views.sections import Footer
from views.sections import Search

@component
def Index():
    return container(
        html.link(
            {
                "rel": "stylesheet",
                "href": "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap"
            }
        ),
        HeaderTop(),
        Search(),
        Footer()
    )