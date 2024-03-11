import menu
from menu import _Colors, _Styles
import requests
import json


def get_page_by_interface():
    x = requests.get(
        'https://fb-friends-23f0d-default-rtdb.europe-west1.firebasedatabase.app/friends.json')
    request_data = x.content
    data = json.loads(request_data)
    data_array = list(data.keys())

    # Use Colors.<color>  for color and style = Syles.<style> For pretext take dump of your currently displayed cmd and provide content as string
    menu_ex = menu.Menu(data_array, color=_Colors.CYAN, style=_Styles.DEFAULT, pretext=None)
    User_choice = menu_ex.launch(response="String")

    return data[menu_ex.selected]
