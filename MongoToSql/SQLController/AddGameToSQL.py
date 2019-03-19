from Helper.HelperFunctions import mysqlConnexion


# On crée la base et la table si elles n'existent pas
def createIfNotExist():
    db = mysqlConnexion()
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS vdmdb")

    cur.execute("CREATE TABLE IF NOT EXISTS game ("
                "id int auto_increment primary key,"
                "nom varchar(255) not null,"
                "date datetime not null,"
                "vr tinyint(1) not null)")
    db.close()


def addGameToSQL(game):
    db = mysqlConnexion()
    query = "insert into game (nom, date, vr) " \
            "values('%s', '%s', '%d')" % (game.nom, game.date, game.vr)
    print(query)
    cur = db.cursor()
    cur.execute(query)
    game_id = db.insert_id()
    db.commit()
    db.close()

    return game_id


createIfNotExist()
