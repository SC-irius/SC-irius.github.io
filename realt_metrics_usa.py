import os
def evaluer_bien_immobilier():
    # Demande des informations à l'utilisateur
    rue = input("\n\n______________________________\nEntrez la rue: ")
    prix = float(input("Entrez le prix de {} (Underlying Asset Price) en ($): ".format(rue)))
    expected_income = float(input("Quelle est le revenu attentu par annee (Expected Income) en (%) : "))
    surface = float(input("Entrez la surface de {} (Interior Size sqft) en (sqft): ".format(rue)))
    zone_prix_m2 = float(input("À combien s'élève le coût moyen par sqft dans cette région ? en ($/sqft): "))
    age = int(input("Combien d'années s'est-il écoulé depuis la construction de {} ? en (annees): ".format(rue)))
    presence_ecoles = int(input("{} est-il situe à proximite d'ecoles? \n| 1 | oui | 2 | non \n".format(rue)))
    presence_transports = int(input("{} est-il situe a proximite des transports en commun? \n| 1 | oui | 2 | non \n".format(rue)))
    presence_commerces = int(input("{} est-il situe a proximite de commerces? \n| 1 | oui | 2 | non \n".format(rue)))
    zone_inondable = int(input("{} est-il situe dans une zone inondable? \n| 1 | oui | 2 | non \n".format(rue)))
    # Demander si la rue est de section 8 ou 42
    s8 = int(input("{} est-il section 8? \n| 1 | oui | 2 | non \n".format(rue)))
    if s8 == 1 :
        s42 = 2
    if s8 == 2:
        s42 = int(input("{} est-il section 42? \n| 1 | oui | 2 | non \n".format(rue)))
    type_bien = int(input("Entrez le type de bien : \n| 1 | single family | 2 | multifamily | 3 | other \n"))
    etat = int(input("Entrez l'état de {} : \n| 1 | a renover | 2 | bon etat | 3 | excellent etat \n".format(rue)))
    tendance_marche_immobilier = int(input("Quelle est la tendance du marche immobilier dans la région? \n| 1 | baisse | 2 | stable | 3 | hause \n"))
    q_eau_ville = int(input("Quelle est la qualite de l'eau dans la région? \n| 1 | mauvaise | 2 | normal | 3 | bonne \n"))
    nb_immigrations = int(input("Quelle est la tendance d'imigrations dans la région? \n| 1 | baisse | 2 | stable | 3 | hause \n"))
    t_vacances_locatives = int(input("Quelle est le taux de vacances locatives dans la région? \n| 1 | baisse | 2 | stable | 3 | hause \n"))

    # Calcul du prix au mètre carré du bien
    prix_m2 = prix / surface

    # Comparaison avec le prix au mètre carré de la zone
    note_comparaison_prix = max(0, min(1, (zone_prix_m2 - prix_m2) / zone_prix_m2 + 0.5))


    # Attribution d'une note en fonction du type de bien
    if type_bien == 1:
        note_type_bien = 0.15
    elif type_bien == 2:
        note_type_bien = 0.4
    else:
        note_type_bien = 1

    # Prise en compte des critères supplémentaires
    note_age = max(1 - (age / 85), 0.25)

    if etat == 1:
        note_etat = 0.4
    elif etat == 2:
        note_etat = 0.7
    else:
        note_etat = 1

    if presence_ecoles == 1:
        note_ecoles = 0.7
    else:
        note_ecoles = 0.4

    if presence_transports == 1:
        note_transports = 0.7
    else:
        note_transports = 0.4

    if presence_commerces == 1:
        note_commerces = 0.7
    else:
        note_commerces = 0.4

    if zone_inondable == 1:
        note_zone_inondable = 0.4
    else:
        note_zone_inondable = 1

    if tendance_marche_immobilier == 1:
        note_tendance_marche_immobilier = 1
    elif tendance_marche_immobilier == 2:
        note_tendance_marche_immobilier = 0.7
    else:
        note_tendance_marche_immobilier = 0.4

    if s8 == 1:
        note_s8 = 0.7
    else :
        note_s8 = 0.1

    if s42 == 1:
        note_s42 = 1
    else :
        note_s42 = 0.2

    if q_eau_ville == 1:
        note_q_eau_ville = 0.4
    elif q_eau_ville ==2:
        note_q_eau_ville = 0.7
    else:
        note_q_eau_ville = 1

    if nb_immigrations == 1:
        note_nb_immigrations = 0.4
    elif nb_immigrations == 2:
        note_nb_immigrations = 0.7
    else :
        note_nb_immigrations = 1

    if t_vacances_locatives == 1:
        note_t_vacances_locatives = 0.7
    elif t_vacances_locatives == 2:
        note_t_vacances_locatives = 0.4
    else :
        note_t_vacances_locatives = 0.2

    # Calcul de la note globale

    note_globale =  (note_s8 * 0.05) + (note_s42 * 0.1) + (note_q_eau_ville * 0.1) + (note_nb_immigrations * 0.1) + (note_t_vacances_locatives * 0.05) + (note_comparaison_prix * 0.1) + (note_type_bien * 0.05) + (note_age * 0.05) + (note_etat * 0.1) + (note_ecoles * 0.05) + (note_transports * 0.05) + (note_commerces * 0.05) + (note_zone_inondable * 0.1) + (note_tendance_marche_immobilier * 0.05)

    # Affichage de la note globale
    # Résumé des critères du bien évalué
    print("\n\n>>> Résumé des criteres pour",rue,"<<<")
    print("\n- Prix de",rue,"    :", prix, "$")
    print("- Surface de",rue," :", surface, "sqft")
    if type_bien == 1 :
        print("-",rue,"est un      : Single family")
    elif type_bien == 2:
        print("-",rue,"est un      : Multifamily")
    else:
        print("-",rue,"est un      : Other")

    if age < 5:
        print("\n- La propriété", rue, "est évaluée à", round(prix/surface, 2), "$/sqft et a été construite il y a",age,"ans, \n  nous pouvons considérer qu'elle est très récente. Cela signifie que la plupart des éléments structurels et des installations \n  sont probablement encore en très bon état, nécessitant peu de maintenance. Cependant, \n  il convient de vérifier que les équipements tels que le système de chauffage, la plomberie et l'électricité sont toujours \n  conformes aux normes actuelles.")
    elif age >= 5 and age < 10:
        print("\n- La propriété", rue, "est évaluée à", round(prix/surface, 2), "$/sqft et a été construite il y a",age,"ans, \n  nous pouvons la considérer comme récente. Bien que les éléments structurels soient probablement encore en bon état, \n  certains équipements peuvent nécessiter une maintenance ou une mise à niveau pour s'adapter aux normes actuelles. \n  Il peut être judicieux de vérifier l'état de la toiture, des fenêtres, de l'isolation, ainsi que les équipements\n  tels que le système de climatisation et les appareils électroménagers.")
    elif age >= 10 and age < 20:
        print("\n- La propriété", rue, "est évaluée à", round(prix/surface, 2), "$/sqft et a été construite il y a",age,"ans, \n  nous pouvons la considérer comme presque neuve. Bien que les éléments structurels soient probablement encore en bon état, \n  certains équipements peuvent nécessiter une maintenance ou une mise à niveau pour s'adapter aux normes actuelles. \n  Il peut être judicieux de vérifier l'état de la toiture, des fenêtres, de l'isolation, \n  ainsi que les équipements tels que le système de climatisation et les appareils électroménagers.")
    elif age >= 20 and age < 30:
        print("\n- La propriété", rue, "est évaluée à", round(prix/surface, 2), "$/sqft et a été construite il y a", age, "ans, \n  nous pouvons considérer qu'elle est encore en bon état mais nécessite une maintenance régulière pour s'assurer que les \n  éléments structurels et les équipements fonctionnent correctement.")
    elif age >= 30 and age < 40:
        print("\n- La propriété", rue, "est évaluée à", round(prix/surface ,2), "$/sqft et commence à vieillir,\n  ayant été construite il y a", age, "ans. Des réparations et des mises à niveau régulières peuvent être nécessaires pour maintenir \n  la propriété en bon état.")
    elif age >= 40 and age < 60:
        print("\n- La propriété", rue, "est évaluée à", round(prix/surface, 2), "$/sqft et a été construite il y a",age,"ans, \n  la propriété commence à vieillir et peut nécessiter des réparations et des mises à niveau régulières.\n  Il est possible que des équipements tels que le système de climatisation, le chauffage et les appareils électroménagers \n  soient en fin de vie utile et doivent être remplacés. Il est également recommandé de vérifier \n  l'isolation et les fenêtres pour s'assurer qu'elles sont toujours efficaces.")
    else:
        print("\n- La propriété", rue, "est évaluée à", round(prix/surface, 2), "$/sqft et a été construite il y a",age,"ans, \n  la propriété peut nécessiter des rénovations importantes pour maintenir sa sécurité et sa valeur. \n  Les éléments structurels tels que la toiture, les fondations et la plomberie peuvent nécessiter une attention particulière. \n  De plus, il est possible que la propriété ne soit pas conforme aux normes de construction actuelles en matière d'isolation, \n  de sécurité et d'accessibilité. Il est donc recommandé d'évaluer l'état de la propriété et realiser les rénovations nécessaires.")

    age_rentabilitation_bien = round(100 / expected_income)
    new_age = age_rentabilitation_bien + age     
    print("\n- Pour que l'investissement dans la propriété",rue,"soit rentable, il faudra attendre",age_rentabilitation_bien,"ans.")
    if new_age <= 10:
        print("  Après cette période, l'âge de",rue,"sera de",new_age,"ans. La propriété sera relativement neuve et il n'y aura pas \n  de réparations importantes à prévoir à court terme.")
    elif new_age <= 20:
        print("  Après cette période, l'âge de",rue,"sera de",new_age,"ans. La propriété commencera à vieillir et il sera possible \n  qu'il y ait des réparations mineures à effectuer dans les années à venir.")
    elif new_age <= 30:
        print("  Après cette période, l'âge de",rue,"sera de",new_age,"ans. La propriété sera maintenant assez vieille et il sera probable qu'il \n  y ait des réparations importantes à effectuer dans les prochaines années.")
    elif new_age <= 40:
        print("  Après cette période, l'âge de",rue,"sera de",new_age,"ans. La propriété sera très ancienne et il sera probable \n  qu'il y ait des réparations majeures à effectuer dans un avenir proche.")
    else:
        print("  Après cette période, l'âge de",rue,"sera de",new_age,"ans. La propriété sera extrêmement vieille et il sera possible \n  qu'elle nécessite des réparations majeures ou une rénovation complète dans un avenir proche.")

    if zone_inondable == 1 :
        print("\n- Il convient de noter que la propriété",rue,"est située dans une zone sujette aux inondations\n  potentielles, ce qui peut entraîner des risques supplémentaires et des coûts d'assurance plus élevés.")

    elif zone_inondable == 2 :
        print("\n- Il convient de souligner que la propriété située",rue,"n'est pas exposée à des risques d'inondation\n  potentielle, ce qui peut permettre de bénéficier de coûts d'assurance plus bas et réduire les risques liés à la propriété.") 

    if tendance_marche_immobilier == 3:
        print("\n- Même si le marché immobilier de la région affiche une tendance haussière pour le moment, il est\n  important de rester attentif aux tendances futures pour prendre des décisions avisées.")

    elif tendance_marche_immobilier == 2:
        print("\n- Bien que le marché immobilier dans la région soit stable pour le moment, il est toujours important\n  de surveiller les tendances et les changements possibles pour prendre des décisions éclairées à l'avenir. ")

    elif tendance_marche_immobilier == 1:
        print("\n- Malgré la baisse actuelle du marché immobilier dans la région, il est impératif de rester\n  vigilant quant aux tendances et aux évolutions futures afin de prendre des décisions éclairées et réussies.")


    print("\n\nLa note globale de",rue,"est de :", round(note_globale *100 , 2), "%")
    # Affichage du résumé des résultats
    if note_globale > 0.805:
        print(rue,"est considere comme une excellente affaire.")
    elif note_globale > 0.605:
        print(rue,"est considere comme une bonne affaire.")
    elif note_globale > 0.405:
        print(rue,"est considere comme une affaire correcte.")
    else:
        print(rue,"est considere comme une mauvaise affaire.")


evaluer_bien_immobilier()

os.system("pause")
input("apuyer enter pour fermer la fenetre")
