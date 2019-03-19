from Helper.HelperFunctions import mysqlConnexion


# On crée la base et la table si elles n'existent pas
def createIfNotExist():
    db = mysqlConnexion()
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS vdmdb")

    cur.execute("CREATE TABLE IF NOT EXISTS reservation_spectateur ("
                "id int auto_increment primary key,"
                "id_reservation int(11) not null,"
                "id_spectateur int(11) not null,"
                "tarif varchar(25) not null)")
    db.close()


def addReservationSpectateurToSQL(reservation_spectateur):
    db = mysqlConnexion()
    query = "insert into reservation_spectateur (id_reservation, id_spectateur, tarif) " \
            "values('%d', '%d', '%s')" % (reservation_spectateur.idReservation, reservation_spectateur.idSpectateur, reservation_spectateur.tarif)
    print(query)
    cur = db.cursor()
    cur.execute(query)
    reservation_spectateur_id = db.insert_id()
    db.commit()
    db.close()

    return reservation_spectateur_id


createIfNotExist()
