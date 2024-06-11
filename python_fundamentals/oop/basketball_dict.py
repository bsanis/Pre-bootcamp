class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.age = player_data['age']
        self.position = player_data['position']
        self.team = player_data['team']

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
# Create kevin instance
player_kevin = Player(kevin)
print(player_kevin)

jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
# Create jason instance
player_jason = Player(jason)
print(player_jason)

kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
# Create kyrie instance
player_kyrie = Player(kyrie)
print(player_kyrie)


players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

new_team = []
for player in players:
    player = player(player_data)
    new_team.append(player)


    '''
     @classmethod
    def get_team(cls, team_list):
        for dict in player_data:
            player_objects.append(cls(dict))
        return player_objects
    '''