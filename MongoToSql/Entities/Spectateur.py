class Spectateur:
  def __init__(self, id, civilite, nom, prenom, age):
    self.id = id
    self.civilite = civilite
    self.nom = nom
    self.prenom = prenom
    self.age = str(age)

  def toString(self):
    print("Spectateur :\n"
          + self.civilite + " "
          + self.nom + " "
          + self.prenom + "\n"
          + self.age + " ans")
