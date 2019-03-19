from datetime import datetime

class Reservation:
  def __init__(self, id, idSpectateur, idGame, dateHeure, email):
    self.id = id
    self.idSpectateur = idSpectateur
    self.idGame = idGame
    self.dateHeure = datetime.strptime(dateHeure, '%Y-%m-%d %H:%M')
    self.email = email

  def toString(self):
    print("Reservation :\n"
          + str(self.idSpectateur) + "\n"
          + str(self.idGame) + "\n"
          + str(self.dateHeure) + "\n"
          + self.email)
