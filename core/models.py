from django.db import models


# Create your models here.

class Pays(models.Model):
    nom_pays = models.CharField(max_length=50)
    code_pays = models.CharField(max_length=5)
    specification_pays = models.CharField(max_length=30, default='Etrangers')
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_pays


class Brevets(models.Model):
    type_brevets = models.CharField(max_length=30)
    annee_brevets = models.IntegerField()
    nombre_pct = models.IntegerField(default=0)
    nombre_cp = models.IntegerField(default=0)
    date_updated = models.DateTimeField(auto_now=True)
    pays_brevets = models.ForeignKey(Pays, on_delete=models.CASCADE)

    def __str__(self):
        return self.pays_brevets.nom_pays


class Marques(models.Model):
    type_marques = models.CharField(max_length=30)
    annee_marques = models.IntegerField()
    nombre_marques = models.IntegerField()
    date_updated = models.DateTimeField(auto_now=True)
    pays_marques = models.ForeignKey(Pays, on_delete=models.CASCADE)
    classe_1 = models.IntegerField()
    classe_2 = models.IntegerField()
    classe_3 = models.IntegerField()
    classe_4 = models.IntegerField()
    classe_5 = models.IntegerField()
    classe_6 = models.IntegerField()
    classe_7 = models.IntegerField()
    classe_8 = models.IntegerField()
    classe_9 = models.IntegerField()
    classe_10 = models.IntegerField()
    classe_11 = models.IntegerField()
    classe_12 = models.IntegerField()
    classe_13 = models.IntegerField()
    classe_14 = models.IntegerField()
    classe_15 = models.IntegerField()
    classe_16 = models.IntegerField()
    classe_17 = models.IntegerField()
    classe_18 = models.IntegerField()
    classe_19 = models.IntegerField()
    classe_20 = models.IntegerField()
    classe_21 = models.IntegerField()
    classe_22 = models.IntegerField()
    classe_23 = models.IntegerField()
    classe_24 = models.IntegerField()
    classe_25 = models.IntegerField()
    classe_26 = models.IntegerField()
    classe_27 = models.IntegerField()
    classe_28 = models.IntegerField()
    classe_29 = models.IntegerField()
    classe_30 = models.IntegerField()
    classe_31 = models.IntegerField()
    classe_32 = models.IntegerField()
    classe_33 = models.IntegerField()
    classe_34 = models.IntegerField()
    classe_35 = models.IntegerField()
    classe_36 = models.IntegerField()
    classe_37 = models.IntegerField()
    classe_38 = models.IntegerField()
    classe_39 = models.IntegerField()
    classe_40 = models.IntegerField()
    classe_41 = models.IntegerField()
    classe_42 = models.IntegerField()
    classe_43 = models.IntegerField()
    classe_44 = models.IntegerField()
    classe_45 = models.IntegerField()

    def __str__(self):
        return self.pays_marques.nom_pays

    @property
    def somme_classes(self):
        total = 0
        if self.classe_1 != 0:
            total += self.classe_1
        if self.classe_2 != 0:
            total += self.classe_2
        if self.classe_3 != 0:
            total += self.classe_3
        if self.classe_4 != 0:
            total += self.classe_4
        if self.classe_5 != 0:
            total += self.classe_5
        if self.classe_6 != 0:
            total += self.classe_6
        if self.classe_7 != 0:
            total += self.classe_7
        if self.classe_8 != 0:
            total += self.classe_8
        if self.classe_9 != 0:
            total += self.classe_9
        if self.classe_10 != 0:
            total += self.classe_10
        if self.classe_11 != 0:
            total += self.classe_11
        if self.classe_12 != 0:
            total += self.classe_12
        if self.classe_13 != 0:
            total += self.classe_13
        if self.classe_14 != 0:
            total += self.classe_14
        if self.classe_15 != 0:
            total += self.classe_15
        if self.classe_16 != 0:
            total += self.classe_16
        if self.classe_17 != 0:
            total += self.classe_17
        if self.classe_18 != 0:
            total += self.classe_18
        if self.classe_19 != 0:
            total += self.classe_19
        if self.classe_20 != 0:
            total += self.classe_20
        if self.classe_21 != 0:
            total += self.classe_21
        if self.classe_22 != 0:
            total += self.classe_22
        if self.classe_23 != 0:
            total += self.classe_23
        if self.classe_24 != 0:
            total += self.classe_24
        if self.classe_25 != 0:
            total += self.classe_25
        if self.classe_26 != 0:
            total += self.classe_26
        if self.classe_27 != 0:
            total += self.classe_27
        if self.classe_28 != 0:
            total += self.classe_28
        if self.classe_29 != 0:
            total += self.classe_29
        if self.classe_30 != 0:
            total += self.classe_30
        if self.classe_31 != 0:
            total += self.classe_31
        if self.classe_32 != 0:
            total += self.classe_32
        if self.classe_33 != 0:
            total += self.classe_33
        if self.classe_34 != 0:
            total += self.classe_34
        if self.classe_35 != 0:
            total += self.classe_35
        if self.classe_36 != 0:
            total += self.classe_36
        if self.classe_37 != 0:
            total += self.classe_37
        if self.classe_38 != 0:
            total += self.classe_38
        if self.classe_39 != 0:
            total += self.classe_39
        if self.classe_40 != 0:
            total += self.classe_40
        if self.classe_41 != 0:
            total += self.classe_41
        if self.classe_42 != 0:
            total += self.classe_42
        if self.classe_43 != 0:
            total += self.classe_43
        if self.classe_44 != 0:
            total += self.classe_44
        if self.classe_45 != 0:
            total += self.classe_45
        return total

    @property
    def somme_classes_produits(self):
        total = 0
        if self.classe_1 != 0:
            total += self.classe_1
        if self.classe_2 != 0:
            total += self.classe_2
        if self.classe_3 != 0:
            total += self.classe_3
        if self.classe_4 != 0:
            total += self.classe_4
        if self.classe_5 != 0:
            total += self.classe_5
        if self.classe_6 != 0:
            total += self.classe_6
        if self.classe_7 != 0:
            total += self.classe_7
        if self.classe_8 != 0:
            total += self.classe_8
        if self.classe_9 != 0:
            total += self.classe_9
        if self.classe_10 != 0:
            total += self.classe_10
        if self.classe_11 != 0:
            total += self.classe_11
        if self.classe_12 != 0:
            total += self.classe_12
        if self.classe_13 != 0:
            total += self.classe_13
        if self.classe_14 != 0:
            total += self.classe_14
        if self.classe_15 != 0:
            total += self.classe_15
        if self.classe_16 != 0:
            total += self.classe_16
        if self.classe_17 != 0:
            total += self.classe_17
        if self.classe_18 != 0:
            total += self.classe_18
        if self.classe_19 != 0:
            total += self.classe_19
        if self.classe_20 != 0:
            total += self.classe_20
        if self.classe_21 != 0:
            total += self.classe_21
        if self.classe_22 != 0:
            total += self.classe_22
        if self.classe_23 != 0:
            total += self.classe_23
        if self.classe_24 != 0:
            total += self.classe_24
        if self.classe_25 != 0:
            total += self.classe_25
        if self.classe_26 != 0:
            total += self.classe_26
        if self.classe_27 != 0:
            total += self.classe_27
        if self.classe_28 != 0:
            total += self.classe_28
        if self.classe_29 != 0:
            total += self.classe_29
        if self.classe_30 != 0:
            total += self.classe_30
        if self.classe_31 != 0:
            total += self.classe_31
        if self.classe_32 != 0:
            total += self.classe_32
        if self.classe_33 != 0:
            total += self.classe_33
        if self.classe_34 != 0:
            total += self.classe_34
        if self.classe_35 != 0:
            total += self.classe_35
        return total

    @property
    def somme_classes_services(self):
        total = 0
        if self.classe_36 != 0:
            total += self.classe_36
        if self.classe_37 != 0:
            total += self.classe_37
        if self.classe_38 != 0:
            total += self.classe_38
        if self.classe_39 != 0:
            total += self.classe_39
        if self.classe_40 != 0:
            total += self.classe_40
        if self.classe_41 != 0:
            total += self.classe_41
        if self.classe_42 != 0:
            total += self.classe_42
        if self.classe_43 != 0:
            total += self.classe_43
        if self.classe_44 != 0:
            total += self.classe_44
        if self.classe_45 != 0:
            total += self.classe_45
        return total

    @property
    def nombre_classes(self):
        total = 0
        if self.classe_1 != 0:
            total += 1
        if self.classe_2 != 0:
            total += 1
        if self.classe_3 != 0:
            total += 1
        if self.classe_4 != 0:
            total += 1
        if self.classe_5 != 0:
            total += 1
        if self.classe_6 != 0:
            total += 1
        if self.classe_7 != 0:
            total += 1
        if self.classe_8 != 0:
            total += 1
        if self.classe_9 != 0:
            total += 1
        if self.classe_10 != 0:
            total += 1
        if self.classe_11 != 0:
            total += 1
        if self.classe_12 != 0:
            total += 1
        if self.classe_13 != 0:
            total += 1
        if self.classe_14 != 0:
            total += 1
        if self.classe_15 != 0:
            total += 1
        if self.classe_16 != 0:
            total += 1
        if self.classe_17 != 0:
            total += 1
        if self.classe_18 != 0:
            total += 1
        if self.classe_19 != 0:
            total += 1
        if self.classe_20 != 0:
            total += 1
        if self.classe_21 != 0:
            total += 1
        if self.classe_22 != 0:
            total += 1
        if self.classe_23 != 0:
            total += 1
        if self.classe_24 != 0:
            total += 1
        if self.classe_25 != 0:
            total += 1
        if self.classe_26 != 0:
            total += 1
        if self.classe_27 != 0:
            total += 1
        if self.classe_28 != 0:
            total += 1
        if self.classe_29 != 0:
            total += 1
        if self.classe_30 != 0:
            total += 1
        if self.classe_31 != 0:
            total += 1
        if self.classe_32 != 0:
            total += 1
        if self.classe_33 != 0:
            total += 1
        if self.classe_34 != 0:
            total += 1
        if self.classe_35 != 0:
            total += 1
        if self.classe_36 != 0:
            total += 1
        if self.classe_37 != 0:
            total += 1
        if self.classe_38 != 0:
            total += 1
        if self.classe_39 != 0:
            total += 1
        if self.classe_40 != 0:
            total += 1
        if self.classe_41 != 0:
            total += 1
        if self.classe_42 != 0:
            total += 1
        if self.classe_43 != 0:
            total += 1
        if self.classe_44 != 0:
            total += 1
        if self.classe_45 != 0:
            total += 1
        return total


class DMI(models.Model):
    type_dmi = models.CharField(max_length=30)
    annee_dmi = models.IntegerField()
    nombre_dmi = models.IntegerField()
    date_updated = models.DateTimeField(auto_now=True)
    pays_dmi = models.ForeignKey(Pays, on_delete=models.CASCADE)
    classe_1 = models.IntegerField()
    classe_2 = models.IntegerField()
    classe_3 = models.IntegerField()
    classe_4 = models.IntegerField()
    classe_5 = models.IntegerField()
    classe_6 = models.IntegerField()
    classe_7 = models.IntegerField()
    classe_8 = models.IntegerField()
    classe_9 = models.IntegerField()
    classe_10 = models.IntegerField()
    classe_11 = models.IntegerField()
    classe_12 = models.IntegerField()
    classe_13 = models.IntegerField()
    classe_14 = models.IntegerField()
    classe_15 = models.IntegerField()
    classe_16 = models.IntegerField()
    classe_17 = models.IntegerField()
    classe_18 = models.IntegerField()
    classe_19 = models.IntegerField()
    classe_20 = models.IntegerField()
    classe_21 = models.IntegerField()
    classe_22 = models.IntegerField()
    classe_23 = models.IntegerField()
    classe_24 = models.IntegerField()
    classe_25 = models.IntegerField()
    classe_26 = models.IntegerField()
    classe_27 = models.IntegerField()
    classe_28 = models.IntegerField()
    classe_29 = models.IntegerField()
    classe_30 = models.IntegerField()
    classe_31 = models.IntegerField()
    classe_32 = models.IntegerField()

    def __str__(self):
        return self.pays_dmi.nom_pays

    # Retourne la somme des classes
    @property
    def somme_classes(self):
        total = 0
        if self.classe_1 != 0:
            total += self.classe_1
        if self.classe_2 != 0:
            total += self.classe_2
        if self.classe_3 != 0:
            total += self.classe_3
        if self.classe_4 != 0:
            total += self.classe_4
        if self.classe_5 != 0:
            total += self.classe_5
        if self.classe_6 != 0:
            total += self.classe_6
        if self.classe_7 != 0:
            total += self.classe_7
        if self.classe_8 != 0:
            total += self.classe_8
        if self.classe_9 != 0:
            total += self.classe_9
        if self.classe_10 != 0:
            total += self.classe_10
        if self.classe_11 != 0:
            total += self.classe_11
        if self.classe_12 != 0:
            total += self.classe_12
        if self.classe_13 != 0:
            total += self.classe_13
        if self.classe_14 != 0:
            total += self.classe_14
        if self.classe_15 != 0:
            total += self.classe_15
        if self.classe_16 != 0:
            total += self.classe_16
        if self.classe_17 != 0:
            total += self.classe_17
        if self.classe_18 != 0:
            total += self.classe_18
        if self.classe_19 != 0:
            total += self.classe_19
        if self.classe_20 != 0:
            total += self.classe_20
        if self.classe_21 != 0:
            total += self.classe_21
        if self.classe_22 != 0:
            total += self.classe_22
        if self.classe_23 != 0:
            total += self.classe_23
        if self.classe_24 != 0:
            total += self.classe_24
        if self.classe_25 != 0:
            total += self.classe_25
        if self.classe_26 != 0:
            total += self.classe_26
        if self.classe_27 != 0:
            total += self.classe_27
        if self.classe_28 != 0:
            total += self.classe_28
        if self.classe_29 != 0:
            total += self.classe_29
        if self.classe_30 != 0:
            total += self.classe_30
        if self.classe_31 != 0:
            total += self.classe_31
        if self.classe_32 != 0:
            total += self.classe_32
        return total

    @property
    def nombre_classes(self):
        total = 0
        if self.classe_1 != 0:
            total += 1
        if self.classe_2 != 0:
            total += 1
        if self.classe_3 != 0:
            total += 1
        if self.classe_4 != 0:
            total += 1
        if self.classe_5 != 0:
            total += 1
        if self.classe_6 != 0:
            total += 1
        if self.classe_7 != 0:
            total += 1
        if self.classe_8 != 0:
            total += 1
        if self.classe_9 != 0:
            total += 1
        if self.classe_10 != 0:
            total += 1
        if self.classe_11 != 0:
            total += 1
        if self.classe_12 != 0:
            total += 1
        if self.classe_13 != 0:
            total += 1
        if self.classe_14 != 0:
            total += 1
        if self.classe_15 != 0:
            total += 1
        if self.classe_16 != 0:
            total += 1
        if self.classe_17 != 0:
            total += 1
        if self.classe_18 != 0:
            total += 1
        if self.classe_19 != 0:
            total += 1
        if self.classe_20 != 0:
            total += 1
        if self.classe_21 != 0:
            total += 1
        if self.classe_22 != 0:
            total += 1
        if self.classe_23 != 0:
            total += 1
        if self.classe_24 != 0:
            total += 1
        if self.classe_25 != 0:
            total += 1
        if self.classe_26 != 0:
            total += 1
        if self.classe_27 != 0:
            total += 1
        if self.classe_28 != 0:
            total += 1
        if self.classe_29 != 0:
            total += 1
        if self.classe_30 != 0:
            total += 1
        if self.classe_31 != 0:
            total += 1
        if self.classe_32 != 0:
            total += 1
        return total


class Historique(models.Model):
    type_fichier = models.CharField(max_length=250)
    nature_fichier = models.CharField(max_length=250)
    type_pi = models.CharField(max_length=250)
    annee = models.IntegerField(default=2000)
    date_ajout = models.DateTimeField(auto_now=True)
    upload_file = models.FileField(null=True)

    def __str__(self):
        return self.type_fichier
