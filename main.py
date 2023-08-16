from bs4 import BeautifulSoup
from my_request_class import MyRequest
import json

reference_id = [
    "ref334731",
    "ref334732",
    "ref334733",
    "ref334734",
    "ref334735",
    "ref334736",
    "ref334737"
]

my_instance = MyRequest(url = "https://www.britannica.com/topic/list-of-games-2072482")
html_text = my_instance.request_text()

# --------------------------------

def init_soup(html_text: str, id_ref: str) -> list[tuple]:
    restricted = ["FIFA", "Pac-Man"]

    soup = BeautifulSoup(html_text, "html.parser")
    target_box = soup.find("section", id = id_ref)
    list_of_games = target_box.find_all("li")
    
    list_tuple = list(map(
        lambda section: 
        (section.get_text(), section.a["href"]) if section.get_text() not in restricted and section.a is not None else ("none ", "none"), 
        list_of_games))
   
    return list_tuple

def store_to_dict(reference_id) -> dict[list[tuple]]:
    return {reference: init_soup(html_text, reference) for reference in reference_id}
    
# ---------------------------------


def main() -> None:
    """
    Create a json file
    """
    dictionary_data = store_to_dict(reference_id)

    final_results = []
    for key, value in dictionary_data.items():
        for name, link in value:
            sample_text =  f'<li><a href={link}target="_blank"><strong>{name}</strong></a></li><br>'
            data = {key: sample_text}
            final_results.append(data)

    with open("result.json", "w") as file:
        json.dump(final_results, file, indent = 2)

main()