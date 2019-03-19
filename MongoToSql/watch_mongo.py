from DTO.GameDTO import generateGame
from DTO.ReservationDTO import generateReservation
from DTO.ReservationSpectateurDTO import generateReservationSpectateur
from DTO.SpectateurDTO import generateSpectateur
from Helper.HelperFunctions import isAcheteur, mongoClient, mongoDB

mongoClient = mongoClient()
db = mongoDB(mongoClient, "test")
myTest = db['mytest']

with myTest.watch() as stream:
    for change in stream:
        collectionId = change['documentKey']['_id']
        if change['operationType'] in ['delete']:
            print(change['operationType'])
            print(change['ns'])
        if change['operationType'] in ['insert']:
            # On récupère l'acheteur puis on init l'id de l'acheteur à null
            newAcheteur = change['fullDocument']['Acheteur']
            newAcheteur_id = None
            # On récupère les games puis l'ajoute dans la base
            newGame = change['fullDocument']['Game']
            newGame_id = generateGame(newGame, collectionId)
            # On récupère les spectateurs puis on les ajoute dans la base
            reservation = change['fullDocument']['Reservation']
            listSpectateurs = []
            for spectateur in reservation:
                newSpectateur_id = generateSpectateur(spectateur['Spectateur'], collectionId)
                listSpectateurs.append({'newSpectateur_id': newSpectateur_id, 'tarif': spectateur['Tarif']})
                if isAcheteur(spectateur['Spectateur'], newAcheteur):
                    newAcheteur_id = newSpectateur_id
            # On ajoute la réservation dans la base
            newReservation_id = generateReservation(
                collectionId,
                newAcheteur_id,
                newGame_id,
                change['fullDocument']['Game']['Jour'],
                change['fullDocument']['Game']['Horaire'],
                change['fullDocument']['Acheteur']['Email'])
            # On ajoute la réservation_spectateur dans la base
            generateReservationSpectateur(
                collectionId,
                newReservation_id,
                listSpectateurs
            )
mongoClient.close()


# TODO Stocker l'id de la collection  change['documentKey']['_id'] ??
# Exemple affichage "horizontal"
# print(dumps(change, sort_keys=True, indent=4))
