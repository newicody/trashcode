from planet import MyPlanet
from github import Github, Auth
import hashlib

class CompareGit(MyPlanet):
    def compare(self):
        for elt1 in self.sha1:
            print(elt1)
            with open(elt1[0],"rb") as file:
                hash_object = hashlib.sha1()
                hash_object.update(file.read())
                pbHash = hash_object.hexdigest()
                try:
                    if (pbHash == elt1[1]):
                        print("somme de controle ok pourr ", elt1[0])
                    else:
                        raise Exception(elt1[0])
                except Exception as a:
                    print("integrite compromise pour ", a)

localcompar = CompareGit()
localcompar.sha_read()
localcompar.compare()
