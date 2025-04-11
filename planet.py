import hashlib

class MyPlanet:
    def __init__(self):
        self.fichiers = ["planet.py","git.py","launcher.py"]
        self.elementsvitaux = ["https" "internet", "github" , "descripteur"]
        self.fonction = ["stockage","descripteur","modeles","passerelle","source"]
        self.chaine = ["local","descripteurs","git","descripteur"]
        self.version = "v0.01z" # ou r pour release
        self.sum = "planet.md5"

    def create_sum(self):
        """ genere le code a executer pour obteir un tuple avec les signatures de fichiers """
        """ il est deja  genere """
        """ ne pas utiliser sans effacer les append sinon doublons """
        for elt in self.fichiers:
            with open(elt,"rb") as file:
                hash_object = hashlib.sha1()
                hash_object.update(file.read())
                pbHash = hash_object.hexdigest()
                with open("planet.py","a") as file:
                    file.write("        self.sha1.append([\""+elt+"\",\""+pbHash+"\"])\n")

    def sha_read(self):
        # sommes de controles
        self.sha1 = []
