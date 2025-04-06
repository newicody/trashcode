from planet import MyPlanet
from github import Github, Auth
import os

class MyGit(MyPlanet):
    def config(self,fichier="apikey.txt"):
        self.api = self.apiopen(fichier)
        self.repository = "trashcode"
        #in classs self.fichiers
        self.fichier_content = ""
        self.fichiers_content = []

    def apiopen(self,fichier):
        with open(fichier,"r") as file:
            key = file.read().split("\n",)[0]
        return key

    def connect(self):
        self.connapi = Github(auth=Auth.Token(self.api))

    def clone(self):
       for elt in self.fichiers:
           self.fichiers_content.append(self.connapi.get_user().get_repo("trashcode").get_contents(elt))
           print(self.fichier_content)
    def representer(self):
        pass
    def envoyer(self):
        pass
    
git = MyGit()
git.config()
git.connect()
git.clone()
