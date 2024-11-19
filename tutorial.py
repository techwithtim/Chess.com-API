#imports

from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests
#Set up pprints
printer = pprint.PrettyPrinter()
#prints leaderbaord
def print_leaderboards():
	#makes a data vairable for the data
	data = get_leaderboards().json
	#another variable for the data keys i think.
	categories = data.keys()
        #prints categorie	
	for category in categories:
		print('Category:', category)
		for idx, entry in enumerate(data[category]):
			print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')

# Gets the players rating
def get_player_rating(username):
	#data variable contains the data of the users		      
	data = get_player_stats(username)
	# It gets cateogires		      
	categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
	for category in categories:
		# prints out the info	      
		print('Category:', category)
		print(f'Current: {data[category]["last"]["rating"]}')
		print(f'Best: {data[category]["best"]["rating"]}')
		print(f'Best: {data[category]["record"]}')
#gets most recent game
def get_most_recent_game(username):
	# data variable gets the players history of games of chess.	      
	data = get_player_game_archives(username).json
	url = data['archives'][-1]
	games = requests.get(url).json()
	game = games['games'][-1]
	# Prints it out	      
	printer.pprint(game)

get_most_recent_game('timruscica')
		      
		      
