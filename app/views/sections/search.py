import requests

from reactpy import component, use_state, html, use_effect
from reactpy_material import grid, text_field, button, icon, typography, stack, pagination

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

    pg_count, set_pg_count = use_state(0)
    pg_page, set_pg_page = use_state(1)

    def call_search(offset):
        response = requests.get(
            f"https://{API_HOST}/recipes/complexSearch",
            headers=get_req_headers(),
            params={
                "query": search_text,
                "offset": offset
            }
        )

        if response.status_code == 200:
            response_data = response.json()
            set_recipes(response_data["results"])
            set_pg_count(response_data["totalResults"])
    
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

    def handle_page_change(e, pg):
        set_pg_page(pg)

        call_search(10*(pg-1))
    
    def render_pagination():
        return stack(
            pagination(
                attrs={
                    "count": pg_count,
                    "page": pg_page,
                    "onChange": handle_page_change
                }
            )
        )

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
                    "onClick": lambda e: call_search(0)
                }
            ),
            attrs={
                "item": True,
                "xs": 3
            }
        ),
        grid(
            *render_recipes(),
            render_pagination(),
            attrs={
                "container": True
            }
        ) if len(recipes) > 0 else None,
        attrs={
            "container": True
        }
    ).render()