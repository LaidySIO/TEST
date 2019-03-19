from datetime import datetime

class Game:
  def __init__(self, id, nom, date, vr):
    self.id = id
    self.nom = nom
    self.date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    if vr == "Oui":
        self.vr = 1
    else:
        self.vr = 0

  def toString(self):
    print("Game :\n"
          + self.nom + "\n"
          + str(self.date) + "\n"
          + str(self.vr))
