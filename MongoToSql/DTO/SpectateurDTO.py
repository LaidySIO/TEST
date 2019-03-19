from Entities.Spectateur import Spectateur
from SQLController.AddSpectateurToSQL import addSpectateurToSQL


# Crée un spectateur puis l'ajoute dans la base
def generateSpectateur(newSpectateur, collectionId):
            spectateur = Spectateur(
                collectionId,
                newSpectateur['Civilite'],
                newSpectateur['Nom'],
                newSpectateur['Prenom'],
                newSpectateur['Age'])
            spectateur.toString()
            newSpectateur_id = addSpectateurToSQL(spectateur)
            return newSpectateur_id
