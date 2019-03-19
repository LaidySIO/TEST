from datetime import datetime


class ReservationSpectateur:
  def __init__(self, id, idReservation, idSpectateur, tarif):
    self.id = id
    self.idReservation = idReservation
    self.idSpectateur = idSpectateur
    self.tarif = tarif

  def toString(self):
    print("Reservation-Spectateur :\n"
          + str(self.idReservation) + "\n"
          + str(self.idReservation) + "\n"
          + str(self.tarif))
