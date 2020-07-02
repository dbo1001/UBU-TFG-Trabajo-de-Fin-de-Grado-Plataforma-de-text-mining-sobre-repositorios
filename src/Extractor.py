# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase extractor
Dedicada a la extracción de issues y labels de un repositorio
"""
from src import Conector
from src import Repositorio
from src import Issue
from src import Label
class Extractor:
    #funciona tanto para un id como para una dirección
    def __init__(self,link):
        gl=Conector.Conector.conectar()
        self.__project= gl.projects.get(link)
        
    """
    Extrae y pasa a la clase almacen los distintos parametros necesarios 
    para este proyecto
    """
    def extraer(self):
        project=Repositorio.Repositorio()
        project.pid=self.__project.id
        project.name=self.__project.name
        project.description=self.__project.description
        issues=[]  
        for x in self.__project.issues.list(all=True):
            issues.append(Issue.Issue(iid=x.iid,title=x.title,description=x.description,labels=x.labels,notes=[n.body for n in x.notes.list()],state=x.state))
        project.issues=issues
        labels=[]  
        for x in self.__project.labels.list(all=True):
            labels.append(Label.Label(lid=x.id,name=x.name,color=x.color,text_color=x.text_color,description=x.description))
        project.labels=labels
        return project