from django.db.models import Q, Sum, Count
from .models import *


# Prend en paramètre le type de PI
# Retourne un dictionnaire de PI par pays
def get_ompi_data(pi, type_pi, annee):
    dict_ompi = {}

    # Filtre données
    if pi == 'Brevets':
        data = Brevets.objects.filter(Q(type_brevets=type_pi) & Q(annee_brevets=annee))
        for d in data:
            dict_ompi[d.pays_brevets.code_pays] = [d.nombre_cp, d.nombre_pct]
    if pi == 'DMI Origin':
        data = DMI.objects.filter(Q(type_dmi=type_pi) & Q(annee_dmi=annee))
        for d in data:
            dict_ompi[d.pays_dmi.code_pays] = [d.nombre_dmi, d.somme_classes]
    if pi == 'DMI Classes':
        data = DMI.objects.filter(Q(type_dmi=type_pi) & Q(annee_dmi=annee))
        for d in data:
            dict_ompi[d.pays_dmi.code_pays] = [
                d.somme_classes,
                d.classe_1, d.classe_2, d.classe_3, d.classe_4, d.classe_5,
                d.classe_6, d.classe_7, d.classe_8, d.classe_9, d.classe_10,
                d.classe_11, d.classe_12, d.classe_13, d.classe_14, d.classe_15,
                d.classe_16, d.classe_17, d.classe_18, d.classe_19, d.classe_20,
                d.classe_21, d.classe_22, d.classe_23, d.classe_24, d.classe_25,
                d.classe_26, d.classe_27, d.classe_28, d.classe_29, d.classe_30,
                d.classe_31, d.classe_32, 0
            ]
    if pi == 'Marque Origin':
        for p in Pays.objects.all().order_by('code_pays'):
            if type_pi == 'Demande':
                data = Marques.objects.filter(
                    Q(pays_marques=p.id) & Q(type_marques__contains=type_pi) & Q(annee_marques=annee))
            else:
                data = Marques.objects.filter(
                    Q(pays_marques=p.id) & Q(type_marques__contains='Enreg') & Q(annee_marques=annee))
            if data.exists():
                dict_ompi[p.code_pays] = [data.aggregate(Sum('nombre_marques'))['nombre_marques__sum'],
                                          sum([d.somme_classes for d in data])]
    if pi == 'Marque Classes':
        for p in Pays.objects.all():
            if type_pi == 'Demande':
                data = Marques.objects.filter(
                    Q(pays_marques=p.id) & Q(type_marques__contains=type_pi) & Q(annee_marques=annee))
            else:
                data = Marques.objects.filter(
                    Q(pays_marques=p.id) & Q(type_marques__contains='Enreg') & Q(annee_marques=annee))
            dict_ompi[p.code_pays] = [
                sum([d.somme_classes for d in data]),
                data.aggregate(Sum('classe_1'))['classe_1__sum'], data.aggregate(Sum('classe_2'))['classe_2__sum'],
                data.aggregate(Sum('classe_3'))['classe_3__sum'], data.aggregate(Sum('classe_4'))['classe_4__sum'],
                data.aggregate(Sum('classe_5'))['classe_5__sum'], data.aggregate(Sum('classe_6'))['classe_6__sum'],
                data.aggregate(Sum('classe_7'))['classe_7__sum'], data.aggregate(Sum('classe_8'))['classe_8__sum'],
                data.aggregate(Sum('classe_9'))['classe_9__sum'], data.aggregate(Sum('classe_10'))['classe_10__sum'],
                data.aggregate(Sum('classe_11'))['classe_11__sum'], data.aggregate(Sum('classe_12'))['classe_12__sum'],
                data.aggregate(Sum('classe_13'))['classe_13__sum'], data.aggregate(Sum('classe_14'))['classe_14__sum'],
                data.aggregate(Sum('classe_15'))['classe_15__sum'], data.aggregate(Sum('classe_16'))['classe_16__sum'],
                data.aggregate(Sum('classe_17'))['classe_17__sum'], data.aggregate(Sum('classe_18'))['classe_18__sum'],
                data.aggregate(Sum('classe_19'))['classe_19__sum'], data.aggregate(Sum('classe_20'))['classe_20__sum'],
                data.aggregate(Sum('classe_21'))['classe_21__sum'], data.aggregate(Sum('classe_22'))['classe_22__sum'],
                data.aggregate(Sum('classe_23'))['classe_23__sum'], data.aggregate(Sum('classe_24'))['classe_24__sum'],
                data.aggregate(Sum('classe_25'))['classe_25__sum'], data.aggregate(Sum('classe_26'))['classe_26__sum'],
                data.aggregate(Sum('classe_27'))['classe_27__sum'], data.aggregate(Sum('classe_28'))['classe_28__sum'],
                data.aggregate(Sum('classe_29'))['classe_29__sum'], data.aggregate(Sum('classe_30'))['classe_30__sum'],
                data.aggregate(Sum('classe_31'))['classe_31__sum'], data.aggregate(Sum('classe_32'))['classe_32__sum'],
                data.aggregate(Sum('classe_33'))['classe_33__sum'], data.aggregate(Sum('classe_34'))['classe_34__sum'],
                data.aggregate(Sum('classe_35'))['classe_35__sum'], data.aggregate(Sum('classe_36'))['classe_36__sum'],
                data.aggregate(Sum('classe_37'))['classe_37__sum'], data.aggregate(Sum('classe_38'))['classe_38__sum'],
                data.aggregate(Sum('classe_39'))['classe_39__sum'], data.aggregate(Sum('classe_40'))['classe_40__sum'],
                data.aggregate(Sum('classe_41'))['classe_41__sum'], data.aggregate(Sum('classe_42'))['classe_42__sum'],
                data.aggregate(Sum('classe_43'))['classe_43__sum'], data.aggregate(Sum('classe_44'))['classe_44__sum'],
                data.aggregate(Sum('classe_45'))['classe_45__sum'], 0
            ]
    return dict_ompi


# Retourne la liste des années des PI contenues dans la BD
def get_listing_year():
    # liste des annees retournées
    listing_year = []
    # Recupere les différentes années par PI
    brevets = Brevets.objects.values('annee_brevets').order_by('-annee_brevets')
    dmi = DMI.objects.values('annee_dmi').order_by('-annee_dmi')
    marques = Marques.objects.values('annee_marques').order_by('-annee_marques')
    # Ajout des annees
    # Brevets
    for pi in brevets:
        for k, v in pi.items():
            if v not in listing_year:
                listing_year.append(v)
    # DMI
    for pi in dmi:
        for k, v in pi.items():
            if v not in listing_year:
                listing_year.append(v)
    # Marques
    for pi in marques:
        for k, v in pi.items():
            if v not in listing_year:
                listing_year.append(v)

    return listing_year


# Retourne le nombre de PI pour une année, un type, ou une specification précise
def get_count_pi(choice_pi, type_pi, voie_pi, annee_pi, specif):
    # Nombre de PI retourné
    nbre = 0
    # Brevets
    if choice_pi == "Brevets":
        # Tous les types
        if type_pi == "tous":
            # Toutes les specif
            if specif == "tous":
                n_pct = \
                    Brevets.objects.filter(annee_brevets=annee_pi).values('nombre_pct').aggregate(Sum('nombre_pct'))[
                        'nombre_pct__sum']
                n_cp = Brevets.objects.filter(annee_brevets=annee_pi).values('nombre_cp').aggregate(Sum('nombre_cp'))[
                    'nombre_cp__sum']
                if (n_cp is not None) & (n_pct is not None):
                    nbre = n_cp + n_pct
                else:
                    nbre = 0
            else:
                n_pct = \
                    Brevets.objects.filter(
                        Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif)).values(
                        'nombre_pct').aggregate(Sum('nombre_pct'))['nombre_pct__sum']
                n_cp = \
                    Brevets.objects.filter(
                        Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif)).values(
                        'nombre_cp').aggregate(Sum('nombre_cp'))['nombre_cp__sum']
                if (n_cp is not None) & (n_pct is not None):
                    nbre = n_cp + n_pct
                else:
                    nbre = 0
        else:
            # Les différentes voies
            if voie_pi == "toutes":
                # Specification
                if specif == "tous":
                    n_pct = \
                        Brevets.objects.filter(Q(annee_brevets=annee_pi) & Q(type_brevets=type_pi)).values(
                            'nombre_pct').aggregate(
                            Sum('nombre_pct'))[
                            'nombre_pct__sum']
                    n_cp = \
                        Brevets.objects.filter(Q(annee_brevets=annee_pi) & Q(type_brevets=type_pi)).values(
                            'nombre_cp').aggregate(Sum('nombre_cp'))[
                            'nombre_cp__sum']
                    if (n_cp is not None) & (n_pct is not None):
                        nbre = n_cp + n_pct
                    else:
                        nbre = 0
                else:
                    n_pct = \
                        Brevets.objects.filter(
                            Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif) & Q(
                                type_brevets=type_pi)).values(
                            'nombre_pct').aggregate(Sum('nombre_pct'))['nombre_pct__sum']
                    n_cp = \
                        Brevets.objects.filter(
                            Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif) & Q(
                                type_brevets=type_pi)).values(
                            'nombre_cp').aggregate(Sum('nombre_cp'))['nombre_cp__sum']
                    if (n_cp is not None) & (n_pct is not None):
                        nbre = n_cp + n_pct
                    else:
                        nbre = 0
            else:
                if voie_pi == 'PCT':
                    # Specification
                    if specif == "tous":
                        n_pct = \
                            Brevets.objects.filter(Q(annee_brevets=annee_pi) & Q(type_brevets=type_pi)).values(
                                'nombre_pct').aggregate(
                                Sum('nombre_pct'))[
                                'nombre_pct__sum']
                        if n_pct is not None:
                            nbre = n_pct
                        else:
                            nbre = 0
                    else:
                        n_pct = \
                            Brevets.objects.filter(
                                Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif) & Q(
                                    type_brevets=type_pi)).values(
                                'nombre_pct').aggregate(Sum('nombre_pct'))['nombre_pct__sum']
                        if n_pct is not None:
                            nbre = n_pct
                        else:
                            nbre = 0
                else:
                    # Specification
                    if specif == "tous":
                        n_cp = \
                            Brevets.objects.filter(Q(annee_brevets=annee_pi) & Q(type_brevets=type_pi)).values(
                                'nombre_cp').aggregate(Sum('nombre_cp'))[
                                'nombre_cp__sum']
                        if n_cp is not None:
                            nbre = n_cp
                        else:
                            nbre = 0
                    else:
                        n_cp = \
                            Brevets.objects.filter(
                                Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif) & Q(
                                    type_brevets=type_pi)).values(
                                'nombre_cp').aggregate(Sum('nombre_cp'))['nombre_cp__sum']
                        if n_cp is not None:
                            nbre = n_cp
                        else:
                            nbre = 0
    elif choice_pi == "DMI":
        # Tous les types
        if type_pi == "tous":
            # Toutes les specif
            if specif == "tous":
                n_pi = \
                    DMI.objects.filter(annee_dmi=annee_pi).values('nombre_dmi').aggregate(Sum('nombre_dmi'))[
                        'nombre_dmi__sum']
                if n_pi is not None:
                    nbre = n_pi
                else:
                    nbre = 0
            else:
                n_pi = \
                    DMI.objects.filter(
                        Q(annee_dmi=annee_pi) & Q(pays_dmi__specification_pays=specif)).values(
                        'nombre_dmi').aggregate(Sum('nombre_dmi'))['nombre_dmi__sum']
                if n_pi is not None:
                    nbre = n_pi
                else:
                    nbre = 0
        else:
            # Specification
            if specif == "tous":
                n_pi = \
                    DMI.objects.filter(Q(annee_dmi=annee_pi) & Q(type_dmi=type_pi)).values(
                        'nombre_dmi').aggregate(
                        Sum('nombre_dmi'))[
                        'nombre_dmi__sum']
                if n_pi is not None:
                    nbre = n_pi
                else:
                    nbre = 0
            else:
                n_pi = \
                    DMI.objects.filter(
                        Q(annee_dmi=annee_pi) & Q(pays_dmi__specification_pays=specif) & Q(
                            type_dmi=type_pi)).values(
                        'nombre_dmi').aggregate(Sum('nombre_dmi'))['nombre_dmi__sum']
                if n_pi is not None:
                    nbre = n_pi
                else:
                    nbre = 0
    else:
        # Tous les types
        if type_pi == "tous":
            # Toutes les voies
            if voie_pi == 'toutes':
                # Toutes les specif
                if specif == "tous":
                    n_pi = \
                        Marques.objects.filter(annee_marques=annee_pi).values('nombre_marques').aggregate(Sum('nombre_marques'))[
                            'nombre_marques__sum']
                    if n_pi is not None:
                        nbre = n_pi
                    else:
                        nbre = 0
                else:
                    n_pi = \
                        Marques.objects.filter(
                            Q(annee_marques=annee_pi) & Q(pays_marques__specification_pays=specif)).values(
                            'nombre_marques').aggregate(Sum('nombre_marques'))['nombre_marques__sum']
                    if n_pi is not None:
                        nbre = n_pi
                    else:
                        nbre = 0
            elif voie_pi == 'Classe Produits':
                # Tous les pays
                if specif == 'tous':
                    pi = Marques.objects.filter(annee_marques=annee_pi)
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_produits
                else:
                    pi = Marques.objects.filter(Q(annee_marques=annee_pi) & Q(pays_marques__specification_pays=specif))
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_produits
            else:
                # Tous les pays
                if specif == 'tous':
                    pi = Marques.objects.filter(annee_marques=annee_pi)
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_services
                else:
                    pi = Marques.objects.filter(Q(annee_marques=annee_pi) & Q(pays_marques__specification_pays=specif))
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_services
        else:
            if type_pi != 'Demande':
                type_pi = 'Enreg'
            # Voie
            if voie_pi == 'toutes':
                # Specification
                if specif == "tous":
                    n_pi = \
                        Marques.objects.filter(Q(annee_marques=annee_pi) & Q(type_marques__icontains=type_pi)).values(
                            'nombre_marques').aggregate(
                            Sum('nombre_marques'))[
                            'nombre_marques__sum']
                    if n_pi is not None:
                        nbre = n_pi
                    else:
                        nbre = 0
                else:
                    n_pi = \
                        Marques.objects.filter(
                            Q(annee_marques=annee_pi) & Q(pays_marques__specification_pays=specif) & Q(
                                type_marques__icontains=type_pi)).values(
                            'nombre_marques').aggregate(Sum('nombre_marques'))['nombre_marques__sum']
                    if n_pi is not None:
                        nbre = n_pi
                    else:
                        nbre = 0
            elif voie_pi == 'Classe Produits':
                # Tous les pays
                if specif == 'tous':
                    pi = Marques.objects.filter(Q(annee_marques=annee_pi) & Q(type_marques__icontains=type_pi))
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_produits
                else:
                    pi = Marques.objects.filter(Q(annee_marques=annee_pi) & Q(type_marques__icontains=type_pi)
                                                & Q(pays_marques__specification_pays=specif))
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_produits
            else:
                # Tous les pays
                if specif == 'tous':
                    pi = Marques.objects.filter(Q(annee_marques=annee_pi) & Q(type_marques__icontains=type_pi))
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_services
                else:
                    pi = Marques.objects.filter(Q(annee_marques=annee_pi) & Q(type_marques__icontains=type_pi)
                                                & Q(pays_marques__specification_pays=specif))
                    # Données non vide
                    if len(pi) != 0:
                        for p in pi:
                            nbre += p.somme_classes_services
    return nbre


# Retourne le nombre de pays pour une PI
def get_count_countries(choice_pi, type_pi, annee_pi, specif):
    # Nombre de pays
    nbre = 0
    # Brevets
    if choice_pi == "Brevets":
        # Tous les types
        if type_pi == "tous":
            # Toutes les specif
            if specif == "tous":
                n_pays = \
                    Brevets.objects.filter(annee_brevets=annee_pi).values('pays_brevets').distinct().aggregate(
                        Count('pays_brevets'))[
                        'pays_brevets__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
            else:
                n_pays = \
                    Brevets.objects.filter(
                        Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif)).values(
                        'pays_brevets').distinct().aggregate(Count('pays_brevets'))['pays_brevets__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
        else:
            # Toutes les specif
            if specif == "tous":
                n_pays = \
                    Brevets.objects.filter(Q(annee_brevets=annee_pi) & Q(type_brevets=type_pi)).values(
                        'pays_brevets').distinct().aggregate(Count('pays_brevets'))[
                        'pays_brevets__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
            else:
                n_pays = \
                    Brevets.objects.filter(
                        Q(annee_brevets=annee_pi) & Q(pays_brevets__specification_pays=specif) & Q(
                            type_brevets=type_pi)).values(
                        'pays_brevets').distinct().aggregate(Count('pays_brevets'))['pays_brevets__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
    elif choice_pi == "DMI":
        # Tous les types
        if type_pi == "tous":
            # Toutes les specif
            if specif == "tous":
                n_pays = \
                    DMI.objects.filter(annee_dmi=annee_pi).values('pays_dmi').distinct().aggregate(
                        Count('pays_dmi'))[
                        'pays_dmi__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
            else:
                n_pays = \
                    DMI.objects.filter(
                        Q(annee_dmi=annee_pi) & Q(pays_dmi__specification_pays=specif)).values(
                        'pays_dmi').distinct().aggregate(Count('pays_dmi'))['pays_dmi__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
        else:
            # Toutes les specif
            if specif == "tous":
                n_pays = \
                    DMI.objects.filter(Q(annee_dmi=annee_pi) & Q(type_dmi=type_pi)).values(
                        'pays_dmi').distinct().aggregate(Count('pays_dmi'))[
                        'pays_dmi__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
            else:
                n_pays = \
                    DMI.objects.filter(
                        Q(annee_dmi=annee_pi) & Q(pays_dmi__specification_pays=specif) & Q(
                            type_dmi=type_pi)).values(
                        'pays_dmi').distinct().aggregate(Count('pays_dmi'))['pays_dmi__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
    else:
        # Tous les types
        if type_pi == "tous":
            # Toutes les specif
            if specif == "tous":
                n_pays = \
                    Marques.objects.filter(annee_marques=annee_pi).values('pays_marques').distinct().aggregate(
                        Count('pays_marques'))[
                        'pays_marques__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
            else:
                n_pays = \
                    Marques.objects.filter(
                        Q(annee_marques=annee_pi) & Q(pays_marques__specification_pays=specif)).values(
                        'pays_marques').distinct().aggregate(Count('pays_marques'))['pays_marques__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
        else:
            if type_pi != "Demande":
                type_pi = 'Enreg'
            # Toutes les specif
            if specif == "tous":
                n_pays = \
                    Marques.objects.filter(Q(annee_marques=annee_pi) & Q(type_marques__icontains=type_pi)).values(
                        'pays_marques').distinct().aggregate(Count('pays_marques'))[
                        'pays_marques__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
            else:
                n_pays = \
                    Marques.objects.filter(
                        Q(annee_marques=annee_pi) & Q(pays_marques__specification_pays=specif) & Q(
                            type_marques__icontains=type_pi)).values(
                        'pays_marques').distinct().aggregate(Count('pays_marques'))['pays_marques__count']
                if n_pays is not None:
                    nbre = n_pays
                else:
                    nbre = 0
    return nbre


# Retourne top 5 des pays d'une PI
def get_top_countries(choice_pi, type_pi, annee_pi, specif):
    # Liste des tops 5 pays
    liste_pays = []
    # Specif
    if specif == "tous":
        pays = Pays.objects.all()
    else:
        pays = Pays.objects.filter(specification_pays=specif)
    # Brevets
    if choice_pi == "Brevets":
        brevets = Brevets.objects.all()
        # On parcourt les Pays afin de charger les données à afficher
        for p in pays:
            # Dictionnaire de données de brevets
            dict_pi = {}
            # Si le pays a des brevets
            if brevets.filter(Q(pays_brevets=p.pk) & Q(annee_brevets=annee_pi)).exists():
                dict_pi['nom'] = p.nom_pays
                if type_pi == "tous":
                    dict_pi['total'] = \
                        p.brevets_set.filter(annee_brevets=annee_pi).values('nombre_pct').aggregate(Sum('nombre_pct'))[
                            'nombre_pct__sum'] \
                        + p.brevets_set.filter(annee_brevets=annee_pi).values('nombre_cp').aggregate(Sum('nombre_cp'))[
                            'nombre_cp__sum']
                else:
                    n_pct = p.brevets_set.filter(Q(annee_brevets=annee_pi) & Q(type_brevets=type_pi)).values(
                        'nombre_pct').aggregate(Sum('nombre_pct'))[
                        'nombre_pct__sum']
                    n_cp = p.brevets_set.filter(Q(annee_brevets=annee_pi) & Q(type_brevets=type_pi)).values(
                        'nombre_cp').aggregate(Sum('nombre_cp'))[
                        'nombre_cp__sum']
                    if (n_cp is not None) & (n_pct is not None):
                        dict_pi['total'] = n_cp + n_pct
                    else:
                        dict_pi['total'] = 0
                liste_pays.append(dict_pi)
            else:
                continue
    elif choice_pi == "DMI":
        dmi = DMI.objects.all()
        # On parcourt les Pays afin de charger les données à afficher
        for p in pays:
            # Dictionnaire de données de brevets
            dict_pi = {}
            # Si le pays a des brevets
            if dmi.filter(Q(pays_dmi=p.pk) & Q(annee_dmi=annee_pi)).exists():
                dict_pi['nom'] = p.nom_pays
                if type_pi == "tous":
                    dict_pi['total'] = \
                        p.dmi_set.filter(annee_dmi=annee_pi).values('nombre_dmi').aggregate(Sum('nombre_dmi'))[
                            'nombre_dmi__sum']
                else:
                    n_pi = p.dmi_set.filter(Q(annee_dmi=annee_pi) & Q(type_dmi=type_pi)).values(
                        'nombre_dmi').aggregate(Sum('nombre_dmi'))[
                        'nombre_dmi__sum']
                    if n_pi is not None:
                        dict_pi['total'] = n_pi
                    else:
                        dict_pi['total'] = 0
                liste_pays.append(dict_pi)
            else:
                continue
    else:
        pi = Marques.objects.all()
        # On parcourt les Pays afin de charger les données à afficher
        for p in pays:
            # Dictionnaire de données de brevets
            dict_pi = {}
            # Si le pays a des brevets
            if pi.filter(Q(pays_marques=p.pk) & Q(annee_marques=annee_pi)).exists():
                dict_pi['nom'] = p.nom_pays
                if type_pi == "tous":
                    dict_pi['total'] = \
                        p.marques_set.filter(annee_marques=annee_pi).values('nombre_marques').aggregate(Sum('nombre_marques'))[
                            'nombre_marques__sum']
                else:
                    if type_pi != 'Demande':
                        type_pi = 'Enreg'
                    n_pi = p.marques_set.filter(Q(annee_marques=annee_pi) & Q(type_marques__icontains=type_pi)).values(
                        'nombre_marques').aggregate(Sum('nombre_marques'))[
                        'nombre_marques__sum']
                    if n_pi is not None:
                        dict_pi['total'] = n_pi
                    else:
                        dict_pi['total'] = 0
                liste_pays.append(dict_pi)
            else:
                continue
    return sorted(liste_pays, key=lambda x: x["total"], reverse=True)[:5]


# Retourne True le PI existe pour les dernières années
def check_last_year(choice_pi, annee_pi, crit):
    # Booleen retourne
    exist = True
    # Brevets
    if choice_pi == "Brevets":
        # Verifie une seule année
        if crit == "recent":
            if not Brevets.objects.filter(annee_brevets=annee_pi).exists():
                exist = False
        elif crit == "one":
            if not Brevets.objects.filter(annee_brevets=annee_pi - 1).exists():
                exist = False
        else:
            boucle = 0  # Compteur de boucle
            while boucle < 5:
                if not Brevets.objects.filter(annee_brevets=annee_pi - boucle).exists():
                    exist = False
                    break
                else:
                    boucle += 1
                    continue
    elif choice_pi == 'DMI':
        # Verifie une seule année
        if crit == "recent":
            if not DMI.objects.filter(annee_dmi=annee_pi).exists():
                exist = False
        elif crit == "one":
            if not DMI.objects.filter(annee_dmi=annee_pi - 1).exists():
                exist = False
        else:
            boucle = 0  # Compteur de boucle
            while boucle < 5:
                if not DMI.objects.filter(annee_dmi=annee_pi - boucle).exists():
                    exist = False
                    break
                else:
                    boucle += 1
                    continue
    else:
        # Verifie une seule année
        if crit == "recent":
            if not Marques.objects.filter(annee_marques=annee_pi).exists():
                exist = False
        elif crit == "one":
            if not Marques.objects.filter(annee_marques=annee_pi - 1).exists():
                exist = False
        else:
            boucle = 0  # Compteur de boucle
            while boucle < 5:
                if not Marques.objects.filter(annee_marques=annee_pi - boucle).exists():
                    exist = False
                    break
                else:
                    boucle += 1
                    continue
    return exist


# Retourne le top 5 des classes d'une PI
def get_top_classe(choice_pi, annee_pi):
    # Dictionnaire de classe
    dict_classe = {}
    # Compteur de boucle
    i = 0

    # PI
    if choice_pi == 'DMI':
        # Recupere les DMI
        pi = DMI.objects.filter(annee_dmi=annee_pi)
        # Creation du dictionnaire
        for p in pi:
            if 'classe_1' not in dict_classe.keys():
                dict_classe['classe_1'] = p.classe_1
            else:
                dict_classe['classe_1'] += p.classe_1
            if 'classe_2' not in dict_classe.keys():
                dict_classe['classe_2'] = p.classe_2
            else:
                dict_classe['classe_2'] += p.classe_2
            if 'classe_3' not in dict_classe.keys():
                dict_classe['classe_3'] = p.classe_3
            else:
                dict_classe['classe_3'] += p.classe_3
            if 'classe_4' not in dict_classe.keys():
                dict_classe['classe_4'] = p.classe_4
            else:
                dict_classe['classe_4'] += p.classe_4
            if 'classe_5' not in dict_classe.keys():
                dict_classe['classe_5'] = p.classe_5
            else:
                dict_classe['classe_5'] += p.classe_5
            if 'classe_6' not in dict_classe.keys():
                dict_classe['classe_6'] = p.classe_6
            else:
                dict_classe['classe_6'] += p.classe_6
            if 'classe_7' not in dict_classe.keys():
                dict_classe['classe_7'] = p.classe_7
            else:
                dict_classe['classe_7'] += p.classe_7
            if 'classe_8' not in dict_classe.keys():
                dict_classe['classe_8'] = p.classe_8
            else:
                dict_classe['classe_8'] += p.classe_8
            if 'classe_9' not in dict_classe.keys():
                dict_classe['classe_9'] = p.classe_9
            else:
                dict_classe['classe_9'] += p.classe_9
            if 'classe_10' not in dict_classe.keys():
                dict_classe['classe_10'] = p.classe_10
            else:
                dict_classe['classe_10'] += p.classe_10
            if 'classe_11' not in dict_classe.keys():
                dict_classe['classe_11'] = p.classe_11
            else:
                dict_classe['classe_11'] += p.classe_11
            if 'classe_12' not in dict_classe.keys():
                dict_classe['classe_12'] = p.classe_12
            else:
                dict_classe['classe_12'] += p.classe_12
            if 'classe_13' not in dict_classe.keys():
                dict_classe['classe_13'] = p.classe_13
            else:
                dict_classe['classe_13'] += p.classe_13
            if 'classe_14' not in dict_classe.keys():
                dict_classe['classe_14'] = p.classe_14
            else:
                dict_classe['classe_14'] += p.classe_14
            if 'classe_15' not in dict_classe.keys():
                dict_classe['classe_15'] = p.classe_15
            else:
                dict_classe['classe_15'] += p.classe_15
            if 'classe_16' not in dict_classe.keys():
                dict_classe['classe_16'] = p.classe_16
            else:
                dict_classe['classe_16'] += p.classe_16
            if 'classe_17' not in dict_classe.keys():
                dict_classe['classe_17'] = p.classe_17
            else:
                dict_classe['classe_17'] += p.classe_17
            if 'classe_18' not in dict_classe.keys():
                dict_classe['classe_18'] = p.classe_18
            else:
                dict_classe['classe_18'] += p.classe_18
            if 'classe_19' not in dict_classe.keys():
                dict_classe['classe_19'] = p.classe_19
            else:
                dict_classe['classe_19'] += p.classe_19
            if 'classe_20' not in dict_classe.keys():
                dict_classe['classe_20'] = p.classe_20
            else:
                dict_classe['classe_20'] += p.classe_20
            if 'classe_21' not in dict_classe.keys():
                dict_classe['classe_21'] = p.classe_21
            else:
                dict_classe['classe_21'] += p.classe_21
            if 'classe_23' not in dict_classe.keys():
                dict_classe['classe_23'] = p.classe_23
            else:
                dict_classe['classe_23'] += p.classe_23
            if 'classe_24' not in dict_classe.keys():
                dict_classe['classe_24'] = p.classe_24
            else:
                dict_classe['classe_24'] += p.classe_24
            if 'classe_25' not in dict_classe.keys():
                dict_classe['classe_25'] = p.classe_25
            else:
                dict_classe['classe_25'] += p.classe_25
            if 'classe_26' not in dict_classe.keys():
                dict_classe['classe_26'] = p.classe_26
            else:
                dict_classe['classe_26'] += p.classe_26
            if 'classe_27' not in dict_classe.keys():
                dict_classe['classe_27'] = p.classe_27
            else:
                dict_classe['classe_27'] += p.classe_27
            if 'classe_28' not in dict_classe.keys():
                dict_classe['classe_28'] = p.classe_28
            else:
                dict_classe['classe_28'] += p.classe_28
            if 'classe_29' not in dict_classe.keys():
                dict_classe['classe_29'] = p.classe_29
            else:
                dict_classe['classe_29'] += p.classe_29
            if 'classe_30' not in dict_classe.keys():
                dict_classe['classe_30'] = p.classe_30
            else:
                dict_classe['classe_30'] += p.classe_30
            if 'classe_31' not in dict_classe.keys():
                dict_classe['classe_31'] = p.classe_31
            else:
                dict_classe['classe_31'] += p.classe_31
            if 'classe_32' not in dict_classe.keys():
                dict_classe['classe_32'] = p.classe_32
            else:
                dict_classe['classe_32'] += p.classe_32
    else:
        # Recupere les Marques
        pi = Marques.objects.filter(annee_marques=annee_pi)
        # Creation du dictionnaire
        for p in pi:
            if 'classe_1' not in dict_classe.keys():
                dict_classe['classe_1'] = p.classe_1
            else:
                dict_classe['classe_1'] += p.classe_1
            if 'classe_2' not in dict_classe.keys():
                dict_classe['classe_2'] = p.classe_2
            else:
                dict_classe['classe_2'] += p.classe_2
            if 'classe_3' not in dict_classe.keys():
                dict_classe['classe_3'] = p.classe_3
            else:
                dict_classe['classe_3'] += p.classe_3
            if 'classe_4' not in dict_classe.keys():
                dict_classe['classe_4'] = p.classe_4
            else:
                dict_classe['classe_4'] += p.classe_4
            if 'classe_5' not in dict_classe.keys():
                dict_classe['classe_5'] = p.classe_5
            else:
                dict_classe['classe_5'] += p.classe_5
            if 'classe_6' not in dict_classe.keys():
                dict_classe['classe_6'] = p.classe_6
            else:
                dict_classe['classe_6'] += p.classe_6
            if 'classe_7' not in dict_classe.keys():
                dict_classe['classe_7'] = p.classe_7
            else:
                dict_classe['classe_7'] += p.classe_7
            if 'classe_8' not in dict_classe.keys():
                dict_classe['classe_8'] = p.classe_8
            else:
                dict_classe['classe_8'] += p.classe_8
            if 'classe_9' not in dict_classe.keys():
                dict_classe['classe_9'] = p.classe_9
            else:
                dict_classe['classe_9'] += p.classe_9
            if 'classe_10' not in dict_classe.keys():
                dict_classe['classe_10'] = p.classe_10
            else:
                dict_classe['classe_10'] += p.classe_10
            if 'classe_11' not in dict_classe.keys():
                dict_classe['classe_11'] = p.classe_11
            else:
                dict_classe['classe_11'] += p.classe_11
            if 'classe_12' not in dict_classe.keys():
                dict_classe['classe_12'] = p.classe_12
            else:
                dict_classe['classe_12'] += p.classe_12
            if 'classe_13' not in dict_classe.keys():
                dict_classe['classe_13'] = p.classe_13
            else:
                dict_classe['classe_13'] += p.classe_13
            if 'classe_14' not in dict_classe.keys():
                dict_classe['classe_14'] = p.classe_14
            else:
                dict_classe['classe_14'] += p.classe_14
            if 'classe_15' not in dict_classe.keys():
                dict_classe['classe_15'] = p.classe_15
            else:
                dict_classe['classe_15'] += p.classe_15
            if 'classe_16' not in dict_classe.keys():
                dict_classe['classe_16'] = p.classe_16
            else:
                dict_classe['classe_16'] += p.classe_16
            if 'classe_17' not in dict_classe.keys():
                dict_classe['classe_17'] = p.classe_17
            else:
                dict_classe['classe_17'] += p.classe_17
            if 'classe_18' not in dict_classe.keys():
                dict_classe['classe_18'] = p.classe_18
            else:
                dict_classe['classe_18'] += p.classe_18
            if 'classe_19' not in dict_classe.keys():
                dict_classe['classe_19'] = p.classe_19
            else:
                dict_classe['classe_19'] += p.classe_19
            if 'classe_20' not in dict_classe.keys():
                dict_classe['classe_20'] = p.classe_20
            else:
                dict_classe['classe_20'] += p.classe_20
            if 'classe_21' not in dict_classe.keys():
                dict_classe['classe_21'] = p.classe_21
            else:
                dict_classe['classe_21'] += p.classe_21
            if 'classe_23' not in dict_classe.keys():
                dict_classe['classe_23'] = p.classe_23
            else:
                dict_classe['classe_23'] += p.classe_23
            if 'classe_24' not in dict_classe.keys():
                dict_classe['classe_24'] = p.classe_24
            else:
                dict_classe['classe_24'] += p.classe_24
            if 'classe_25' not in dict_classe.keys():
                dict_classe['classe_25'] = p.classe_25
            else:
                dict_classe['classe_25'] += p.classe_25
            if 'classe_26' not in dict_classe.keys():
                dict_classe['classe_26'] = p.classe_26
            else:
                dict_classe['classe_26'] += p.classe_26
            if 'classe_27' not in dict_classe.keys():
                dict_classe['classe_27'] = p.classe_27
            else:
                dict_classe['classe_27'] += p.classe_27
            if 'classe_28' not in dict_classe.keys():
                dict_classe['classe_28'] = p.classe_28
            else:
                dict_classe['classe_28'] += p.classe_28
            if 'classe_29' not in dict_classe.keys():
                dict_classe['classe_29'] = p.classe_29
            else:
                dict_classe['classe_29'] += p.classe_29
            if 'classe_30' not in dict_classe.keys():
                dict_classe['classe_30'] = p.classe_30
            else:
                dict_classe['classe_30'] += p.classe_30
            if 'classe_31' not in dict_classe.keys():
                dict_classe['classe_31'] = p.classe_31
            else:
                dict_classe['classe_31'] += p.classe_31
            if 'classe_32' not in dict_classe.keys():
                dict_classe['classe_32'] = p.classe_32
            else:
                dict_classe['classe_32'] += p.classe_32
            if 'classe_33' not in dict_classe.keys():
                dict_classe['classe_33'] = p.classe_33
            else:
                dict_classe['classe_33'] += p.classe_33
            if 'classe_34' not in dict_classe.keys():
                dict_classe['classe_34'] = p.classe_34
            else:
                dict_classe['classe_34'] += p.classe_34
            if 'classe_35' not in dict_classe.keys():
                dict_classe['classe_35'] = p.classe_35
            else:
                dict_classe['classe_35'] += p.classe_35
            if 'classe_36' not in dict_classe.keys():
                dict_classe['classe_36'] = p.classe_36
            else:
                dict_classe['classe_36'] += p.classe_36
            if 'classe_37' not in dict_classe.keys():
                dict_classe['classe_37'] = p.classe_37
            else:
                dict_classe['classe_37'] += p.classe_37
            if 'classe_38' not in dict_classe.keys():
                dict_classe['classe_38'] = p.classe_38
            else:
                dict_classe['classe_38'] += p.classe_38
            if 'classe_39' not in dict_classe.keys():
                dict_classe['classe_39'] = p.classe_39
            else:
                dict_classe['classe_39'] += p.classe_39
            if 'classe_40' not in dict_classe.keys():
                dict_classe['classe_40'] = p.classe_40
            else:
                dict_classe['classe_40'] += p.classe_40
            if 'classe_41' not in dict_classe.keys():
                dict_classe['classe_41'] = p.classe_41
            else:
                dict_classe['classe_41'] += p.classe_41
            if 'classe_42' not in dict_classe.keys():
                dict_classe['classe_42'] = p.classe_42
            else:
                dict_classe['classe_42'] += p.classe_42
            if 'classe_43' not in dict_classe.keys():
                dict_classe['classe_43'] = p.classe_43
            else:
                dict_classe['classe_43'] += p.classe_43
            if 'classe_44' not in dict_classe.keys():
                dict_classe['classe_44'] = p.classe_44
            else:
                dict_classe['classe_44'] += p.classe_44
            if 'classe_45' not in dict_classe.keys():
                dict_classe['classe_45'] = p.classe_45
            else:
                dict_classe['classe_45'] += p.classe_45

    return sorted(dict_classe.items(), key=lambda x: x[1], reverse=True)[:5]
