class Player:
    def __init__(self, name, position, specification):
        self.name = name
        self.position = position
        self.specification = specification


class Team:
    def __init__(self, team_name, player):
        self.team_name = team_name
        self.player = player


    def show(self):
        print(f'\nВ составе команды {self.team_name}:')
        for index, player in enumerate(self.player, start = 1):
            print(f'\n{index}) {player.name}')
            for key, value in player.specification.items():
                 print(f'•{key} - {value}')





mbappe = (Player('KYLIAN MBAPPE', 'defender', specification = {'speed': 10, 'strong': 5, 'shots' : 16  }))
messi = (Player('LIONEL MESSI', 'striker', specification = {'speed' : 9, 'strong': 4, 'shots' : 26  })) 
robert = (Player('ROBERT LEWANDOWSKI', 'defender', specification = {'speed' : 11, 'strong': 8, 'shots' : 18  })) 
karim = (Player('KARIM BENZEMA', 'striker', specification = {'speed' : 7, 'strong': 12, 'shots' : 10  })) 


chelsi = Team('Chelsi', [mbappe, messi])
barsa = Team('Barselona', [robert, karim ]) 

chelsi.show()
barsa.show()