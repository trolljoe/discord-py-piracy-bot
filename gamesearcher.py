import requests

class Search:
    def __init__(self):
        self.search_url = "https://gamestatus.info/back/api/gameinfo/game/search_title/"
        self.popular_url = "https://gamestatus.info/back/api/gameinfo/game/referralsgame/"

    def search_game(self, title):
        # Prepare the payload with the title
        payload = {"title": title}
        
        # Make the POST request
        response = requests.post(self.search_url, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch game info. Status code: {response.status_code}")
            return None

    def popular_games(self): # this is a really big output
        response = requests.get(self.popular_url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch popular games. Status code: {response.status_code}")
            return None

# Example usage
if __name__ == "__main__":
    game_search = Search()
    popular_games_info = game_search.popular_games()
    if popular_games_info:
        print(popular_games_info)
