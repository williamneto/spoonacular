import requests

from reactpy import component, use_state, html, use_effect
from reactpy_material import grid, text_field, button, icon, typography

from configs import API_KEY, API_HOST
def get_req_headers():
    return {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

@component
def Search():
    search_text, set_search_text = use_state("")
    recipes, set_recipes = use_state([])

    def handle_text_change(event):
        set_search_text(event["target"]["value"])
    
    def handle_search(event):
        response = requests.get(
            f"https://{API_HOST}/recipes/complexSearch",
            headers=get_req_headers(),
            params={
                "query": search_text
            }
        )

        if response.status_code == 200:
            response_data = response.json()
            set_recipes(response_data["results"])
    
    def render_recipes():
        result = []
        for recipie in recipes:                
            result.append(grid(
                grid(
                    html.img({"src": recipie["image"]}),
                    attrs={
                        "item": True,
                        "xs": 4
                    }
                ),
                grid(
                    typography(
                        recipie["title"],
                        attrs={
                            "variant": "h5"
                        }
                    ),
                    attrs={
                        "item": True,
                        "xs": 4
                    }
                ),
                attrs={
                    "container": True
                }
            ))
        
        return result

    return grid(
        grid(
            text_field(
                attrs={
                    "value": search_text,
                    "onChange": lambda e: set_search_text(e["target"]["value"]),
                    "label": "Search recipes",
                    "fullWidth": True
                }
            ),
            attrs={
                "item": True,
                "xs": 9
            }
        ),
        grid(
            button(
                icon(attrs={"icon": "Save"}).render(),
                attrs={
                    "fullWidth": True,
                    "fullheight": "true",
                    "variant": "outlined",
                    "size": "large",
                    "onClick": handle_search
                }
            ),
            attrs={
                "item": True,
                "xs": 3
            }
        ),
        grid(
            *render_recipes(),
            attrs={
                "container": True
            }
        ) if len(recipes) > 0 else None,
        attrs={
            "container": True
        }
    ).render()