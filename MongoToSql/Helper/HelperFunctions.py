import MySQLdb
import pymongo


# Fonction qui verifie si le nouveau spectateur est l'acheteur de la réservation
def isAcheteur(newSpecateur, newAcheteur):
    if newSpecateur['Nom'] == newAcheteur['Nom'] \
        and newSpecateur['Prenom'] == newAcheteur['Prenom'] \
            and newSpecateur['Age'] == newAcheteur['Age']:
                return True


# ##############################  SQL  ################################## #
def mysqlConnexion():
    # Connexion Laidy RDS
    db = MySQLdb.connect(host="vdmdb.cxijwd9hvdpd.eu-west-1.rds.amazonaws.com",
                                   user="vdmuser",
                                   passwd="y2bgxL4DSFm7TrA",
                                   db="vdmdb")
    # connexion Samir 1
    # db = MySQLdb.connect(host="aayp33an1l8e6x.c86zfhejncrr.us-east-2.rds.amazonaws.com",
    #                                user="root",
    #                                passwd="jvxf29b3",
    #                                db="vdmdb")
    return db


# ##############################  MONGO  ################################## #
# fonction de connexion à la base
def mongoClient():
    client = pymongo.MongoClient("mongodb+srv://user:user@clustervmd0-sjvm4.mongodb.net/test?retryWrites=true")
    return client


# fonction recup' de la base
def mongoDB(client, db):
    db = client[db]
    return db
