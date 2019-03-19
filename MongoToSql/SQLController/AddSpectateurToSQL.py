from Helper.HelperFunctions import mysqlConnexion


# On crée la base et la table si elles n'existent pas
def createIfNotExist():
    db = mysqlConnexion()
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS vdmdb")
    # On crée la table si elle n'existe pas
    cur.execute("CREATE TABLE IF NOT EXISTS spectateur ("
                "id int auto_increment primary key,"
                "civilite varchar(10) not null,"
                "nom varchar(25) not null,"
                "prenom varchar(25),"
                "age int(2))")
    db.close()


def addSpectateurToSQL(spectateur):
    db = mysqlConnexion()
    query = "insert into spectateur (civilite, nom, prenom, age) " \
            "values('%s', '%s', '%s', %d)" % (spectateur.civilite, spectateur.nom, spectateur.prenom, int(spectateur.age))
    print(query)
    cur = db.cursor()
    cur.execute(query)
    spectateur_id = db.insert_id()
    db.commit()
    db.close()

    return spectateur_id


createIfNotExist()
