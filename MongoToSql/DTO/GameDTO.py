# Crée un game puis l'ajoute dans la base
from Entities.Game import Game
from SQLController.AddGameToSQL import addGameToSQL


def generateGame(newGame, collectionId):
    game = Game(
        collectionId,
        newGame['Nom'],
        newGame['Jour'] + " " + newGame['Horaire'],
        newGame['VR'])
    game.toString()
    newGame_id = addGameToSQL(game)
    return newGame_id
