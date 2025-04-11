
from planet import MyPlanet
from github import Github, Auth
import os
from multiprocessing import Pool

class MyGit(MyPlanet):
    def config(self,fichier="etc/apikey.txt"):
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
   
    def writememory(self,x):
        print("copie en memoire de ",x)
        self.fichier_content = [x,self.connapi.get_user().get_repo("trashcode").get_contents(x)]
        print("Termine ",x)
        self.didi = self.writedisk(x)
        return self.fichier_content


    def writedisk(self,x):
        print(self.fichier_content)
        print("ecriture sur le disque")
        with open(x, "w") as file
            file.write(self.fichier_content[1].decoded_content.decode())
        print("termine")
        return os.walk("./",x)

    def clone(self):
        with Pool(len(self.fichiers)) as p:
            print("go")
            return p.map( self.writememory,self.fichiers)
            
    def representer(self):
        pass
    def envoyer(self):
        pass
git = MyGit()
git.config()
git.connect()
git.memory = git.clone()
git.disk = os.walk("./")
