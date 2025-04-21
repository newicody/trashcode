import hashlib

class MyPlanet:
    def __init__(self):
        self.fichiers = ["planet.py","planet.md5","getgit.py","putgit.py","comparegit.py"]
        self.elementsvitaux = ["https" "internet", "github" , "descripteur"]
        self.fonction = ["stockage","descripteur","modeles","passerelle","source"]
        self.chaine = ["local","descripteurs","git","descripteur"]
        self.version = "v0.01z" # branche = n.nn - version = x
        self.sum = "planet.md5"

    def create_sum(self):
        """ genere le code a executer pour obteir un tuple avec les signatures de fichiers """
        """ il est deja  genere """
        """ ne pas utiliser sans effacer les append sinon doublons """
        for elt in self.fichiers[2:]:
            with open(elt,"rb") as file:
                hash_object = hashlib.sha1()
                hash_object.update(file.read())
                pbHash = hash_object.hexdigest()
                with open("planet.py","a") as file:
                    file.write("        self.sha1.append([\""+elt+"\",\""+pbHash+"\"])\n")

    def sha_read(self):
        # sommes de controles
        self.sha1 = []
        self.sha1.append(["getgit.py","460cf733cc8c9048b4add9edd6b482a336ef802e"])
        self.sha1.append(["putgit.py","a5bee0859f7d7763f0bf0e0d0feb41d2ddb07fd3"])
        self.sha1.append(["comparegit.py","f84ebb65e3a9c6b75d71cbe3fd74feab14de63f1"])
