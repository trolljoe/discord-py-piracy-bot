import requests

class Search:
    def __init__(self):
        self.base_url = "https://gamestatus.info/back/api/gameinfo/game/search_title/"

    def search_game(self, title):
        # Prepare the payload with the title
        payload = {"title": title}
        
        # Make the POST request
        response = requests.post(self.base_url, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch game info. Status code: {response.status_code}")
            return None

# Example usage
if __name__ == "__main__":
    search = Search()
    game_info = search.search_game("gasasasas")
    if game_info:
        print(game_info)