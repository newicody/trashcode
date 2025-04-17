import hashlib

class MyPlanet:
    def __init__(self):
        self.fichiers = ["myplanet.py","getgit.py","putgit.py","comparegit.py"]
        self.elementsvitaux = ["https" "internet", "github" , "descripteur"]
        self.fonction = ["stockage","descripteur","modeles","passerelle","source"]
        self.chaine = ["local","descripteurs","git","descripteur"]
        self.version = "v0.01z" # branche = n.nn - version = x
        self.sum = "planet.md5"

    def create_sum(self):
        """ genere le code a executer pour obteir un tuple avec les signatures de fichiers """
        """ il est deja  genere """
        """ ne pas utiliser sans effacer les append sinon doublons """
        for elt in self.fichiers[1:]:
            with open(elt,"rb") as file:
                hash_object = hashlib.sha1()
                hash_object.update(file.read())
                pbHash = hash_object.hexdigest()
                with open("myplanet.py","a") as file:
                    file.write("        self.sha1.append([\""+elt+"\",\""+pbHash+"\"])\n")

        with open("myplanet.py","rb") as file:
            hash_object = hashlib.md5(file.read())
            pbHash = hash_object.hexdigest()
            with open("myplanet.md5","w") as file2:
                file2.write(pbHash)

    def sha_read(self):
        # sommes de controles (myplanet.md5 pour myplanet.py)
        self.sha1 = []
        self.sha1.append(["getgit.py","6290fc2953985eecbdf892cb8b7a0067700018c0"])
        self.sha1.append(["putgit.py","fe9ea0fd83ad806e23860cc14e2c747cc7929ba1"])
        self.sha1.append(["comparegit.py","8e96a62079be5787192ef5df47e550060929979c"])
