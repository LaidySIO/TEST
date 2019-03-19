from Helper.HelperFunctions import mysqlConnexion


# On crée la base et la table si elles n'existent pas
def createIfNotExist():
    db = mysqlConnexion()
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS vdmdb")

    cur.execute("CREATE TABLE IF NOT EXISTS reservation ("
                "id int auto_increment primary key,"
                "id_acheteur int(11) not null,"
                "id_game int(11) not null,"
                "dateheure datetime not null,"
                "email varchar(50) not null)")
    db.close()


def addReservationToSQL(reservation):
    db = mysqlConnexion()
    query = "insert into reservation (id_acheteur, id_game, dateheure, email) " \
            "values('%d', '%d', '%s', '%s')" % (reservation.idSpectateur, reservation.idGame, reservation.dateHeure, reservation.email)
    print(query)
    cur = db.cursor()
    cur.execute(query)
    reservation_id = db.insert_id()
    db.commit()
    db.close()

    return reservation_id


createIfNotExist()
