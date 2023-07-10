import random

from faker import Faker
from .models import *

fake = Faker()
liste_type_brevets = ['Demande', 'Delivrance']
liste_type_pi = ['Demande', 'Enregistrement']
liste_type_pi_ = ['Demande - Madrid', 'Demande Regionale - Nationale', 'Demande Regionale - Etranger', 'Enreg Madrid',
                  'Enreg Regionale - Etranger', 'Enreg Regionale - Nationale']
pays = Pays.objects.all()


def populate_pays(value):
    for i in range(value):
        nom = fake.country()
        code_pays = fake.country_code()
        Pays.objects.get_or_create(
            nom_pays=nom,
            code_pays=code_pays
        )


def populate_brevets(value):
    for i in range(value):
        Brevets.objects.get_or_create(
            type_brevets=random.choice(liste_type_brevets),
            nombre_pct=random.randint(0, 200),
            nombre_cp=random.randint(0, 200),
            annee_brevets=random.randint(2010, 2021),
            pays_brevets=random.choice(pays)
        )


def populate_dmi(value):
    for i in range(value):
        DMI.objects.get_or_create(
            pays_dmi=random.choice(pays),
            type_dmi=random.choice(liste_type_pi),
            nombre_dmi=random.randint(0, 200),
            annee_dmi=random.randint(2010, 2021),
            classe_1=random.randint(0, 10),
            classe_2=random.randint(0, 10),
            classe_3=random.randint(0, 10),
            classe_4=random.randint(0, 10),
            classe_5=random.randint(0, 10),
            classe_6=random.randint(0, 10),
            classe_7=random.randint(0, 10),
            classe_8=random.randint(0, 10),
            classe_9=random.randint(0, 10),
            classe_10=random.randint(0, 10),
            classe_11=random.randint(0, 10),
            classe_12=random.randint(0, 10),
            classe_13=random.randint(0, 10),
            classe_14=random.randint(0, 10),
            classe_15=random.randint(0, 10),
            classe_16=random.randint(0, 10),
            classe_17=random.randint(0, 10),
            classe_18=random.randint(0, 10),
            classe_19=random.randint(0, 10),
            classe_20=random.randint(0, 10),
            classe_21=random.randint(0, 10),
            classe_22=random.randint(0, 10),
            classe_23=random.randint(0, 10),
            classe_24=random.randint(0, 10),
            classe_25=random.randint(0, 10),
            classe_26=random.randint(0, 10),
            classe_27=random.randint(0, 10),
            classe_28=random.randint(0, 10),
            classe_29=random.randint(0, 10),
            classe_30=random.randint(0, 10),
            classe_31=random.randint(0, 10),
            classe_32=random.randint(0, 10)
        )


def populate_marque(value):
    for i in range(value):
        Marques.objects.get_or_create(
            pays_marques=random.choice(pays),
            type_marques=random.choice(liste_type_pi_),
            nombre_marques=random.randint(0, 200),
            annee_marques=random.randint(2010, 2021),
            classe_1=random.randint(0, 10),
            classe_2=random.randint(0, 10),
            classe_3=random.randint(0, 10),
            classe_4=random.randint(0, 10),
            classe_5=random.randint(0, 10),
            classe_6=random.randint(0, 10),
            classe_7=random.randint(0, 10),
            classe_8=random.randint(0, 10),
            classe_9=random.randint(0, 10),
            classe_10=random.randint(0, 10),
            classe_11=random.randint(0, 10),
            classe_12=random.randint(0, 10),
            classe_13=random.randint(0, 10),
            classe_14=random.randint(0, 10),
            classe_15=random.randint(0, 10),
            classe_16=random.randint(0, 10),
            classe_17=random.randint(0, 10),
            classe_18=random.randint(0, 10),
            classe_19=random.randint(0, 10),
            classe_20=random.randint(0, 10),
            classe_21=random.randint(0, 10),
            classe_22=random.randint(0, 10),
            classe_23=random.randint(0, 10),
            classe_24=random.randint(0, 10),
            classe_25=random.randint(0, 10),
            classe_26=random.randint(0, 10),
            classe_27=random.randint(0, 10),
            classe_28=random.randint(0, 10),
            classe_29=random.randint(0, 10),
            classe_30=random.randint(0, 10),
            classe_31=random.randint(0, 10),
            classe_32=random.randint(0, 10),
            classe_33=random.randint(0, 10),
            classe_34=random.randint(0, 10),
            classe_35=random.randint(0, 10),
            classe_36=random.randint(0, 10),
            classe_37=random.randint(0, 10),
            classe_38=random.randint(0, 10),
            classe_39=random.randint(0, 10),
            classe_40=random.randint(0, 10),
            classe_41=random.randint(0, 10),
            classe_42=random.randint(0, 10),
            classe_43=random.randint(0, 10),
            classe_44=random.randint(0, 10),
            classe_45=random.randint(0, 10),
        )
