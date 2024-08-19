from datetime import date

Base = declarative_base()
from sqlalchemy import create_engine , Column, Integer, String, Boolean, Date , ForeignKey 
from sqlalchemy.orm import relationship, sessionmaker, declarative_base 

class Livre(Base):
    __tablename__ = 'livres'
    
    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)
    auteur = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    disponible = Column(Boolean, default=True)
    date_emprunt = Column(Date)
    date_retour = Column(Date)

    def emprunter(self, date_emprunt):
        if self.disponible:
            self.disponible = False
            self.date_emprunt = date_emprunt
            self.date_retour = date_emprunt + timedelta(days=14)  # 14 jours d'emprunt
        else:
            raise Exception("Livre déjà emprunté")

    def retourner(self):
        if not self.disponible:
            self.disponible = True
            self.date_emprunt = None
            self.date_retour = None
        else:
            raise Exception("Livre déjà disponible")


class Membre(Base):
    __tablename__ = 'membres'
    
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    identifiant = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)

    emprunts = relationship('Livre', backref='emprunteur')

    def emprunter_livre(self, livre):
        livre.emprunter(date.today())

    def retourner_livre(self, livre):
        livre.retourner()

