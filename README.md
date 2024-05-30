# discord-py-piracy-bot
simple bot/library made in python to fetch pirated games, and if possible, share a torrent link for them

# requirements
`pip install requests discord.py asyncio`

# usage
this only contains a search feature and a popular feature right now, but you can add more using [this link](https://gamestatus.info/back/api/gameinfo/game/search_title/).

import the package (gamesearcher.py, or whatever the name is)
```py
from gamesearcher import Search
```
add this line of code to anywhere (not needed, but if you wanna simplify things 🤷‍♂️)
`search = Search()`

now, to search a game, you can use:
```py
game_info = search.search_game(game)
```

to get popular games, use:
```py
popular_games_info = game_search.popular_games()
```

game_info can be any variable. to check if it's working, just
`print(game_info)`
this will output a json string

feel free to modify anything about the library. the code is REALLY simple
