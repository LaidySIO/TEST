# Crée une reservation puis l'ajoute dans la base
from Entities.Reservation import Reservation
from SQLController.AddReservationToSQL import addReservationToSQL


def generateReservation(collectionId, idSpectateur, idGame, date, heure, email):
    reservation = Reservation(
        collectionId,
        idSpectateur,
        idGame,
        date + ' ' + heure,
        email)
    reservation.toString()
    newReservation_id = addReservationToSQL(reservation)
    return newReservation_id

