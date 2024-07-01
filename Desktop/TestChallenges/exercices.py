"""#Exercice 1:
#J’ai fait des courses : j’ai payé un total de 119,95 € pour un jeu vidéo à 49,95 €, un livre à 25€ et des manettes de jeux vidéo. Combien ai-je payé les manettes ?
total_courses=119.95 ; prix_jeu_video=49.95 ; prix_livre=25 ; prix_manettes=0 ; prix_manettes=total_courses-(prix_jeu_video+prix_livre)
print(prix_manettes)

#Exercice 2:
#J’ai acheté 3 kg de bananes à 1€30 le kg, 5 kg d’orange à 1,5 € le kg et 4 mangues à 1,3€ l’unité. J’ai payé avec un billet de 50€. Combien de monnaie dois-je récupérer ?
prix_banann=3*1.30
prix_orange=5*1.5 
prix_mangue4=4*1.3 
billet=50 
monnaie=billet-(prix_banann+prix_orange+prix_banann)
print(monnaie)

#Exercice 3:
#Le garagiste a fini de réparer la voiture. Il a fait une vidange à 189€, changé les 4 plaquettes de frein (55€ l’une) et changé tous les pneus à 85 € le pneu. Combien cela va-t-il couter au total ?
prix_vidage=189 ; prix_plaquettes=4*55 ; prix_pneus=4*85 ; total_depence=prix_plaquettes+prix_vidage+prix_pneus ;
print(total_depence)

#Exercice 4:
#J’ai acheté un pantalon à 45 € et une veste qui coute 25€ de plus. A la caisse, j’utilise un bon de réduction pour payer 10€ de moins. Combien ai-je payé au total ?
prix_pantalon=45 ; prix_veste=25+prix_pantalon ; réduction=10 ; total_payé=(prix_pantalon+prix_veste)-réduction
print(total_payé)

#Exercice 5:
#Trois enfants ramassent des mûres : le premier en récolte 380 g, le deuxième 200g de moins et le troisième 240g. Puis ils se partagent équitablement l’ensemble la récolte. Combien reçoivent-ils chacun ?
enfant1=380
enfan2=200-enfant1
enfant3=240
partage_equitable=(enfant1+enfan2+enfant3)/3
print(partage_equitable)

33
#Exercice 6:
#La maitresse a reçu 5 cartons avec des crayons de couleur. Chaque carton contient 4 sachets de 12 crayons. Combien y a-t-il de crayons au total ?
Q_crayon_carton=4*12
Nb_total_crayon=Q_crayon_carton*5
print(Nb_total_crayon)

#Exercice 7:
#En 2017, la ville de Paris a reçu 33 630 000 touristes. Le nombre de touristes a été multiplié par 3 en 10 ans. Combien la ville a-t-elle reçu de touristes en 2007 ?
Nb_total_touristes_2017=33630000
Nb_touristes_2007=Nb_total_touristes_2017/3
print(Nb_touristes_2007)

#Exercice 8:
#Le vendeur de pizzas a vendu 50 petites pizzas à 7€, 95 pizzas normales à 9,5 € et 65 pizzas géantes à 13,9 €. Combien d’argent a-t-il gagné au total ?
petits_pizzas=50*7.95
pizzas_normal=9.5
pizzas_géantes=65*13.9
total_argent_gagné=petits_pizzas+pizzas_normal+pizzas_géantes
print(f"il a gagné {total_argent_gagné}")


#Exercice 9:
#Le Louvre est le plus grand musée de France. En 2017, il a reçu environ 8,1 millions de visiteurs. Combien cela fait-il de visiteurs par jour environ, sachant que le musée ferme tous les mardis ?
Nb_total_visiteur_2017=8100000
Nb_jours_an=365
Nb_mardi_an=52
Nb_jour_an_restant=Nb_jours_an-Nb_mardi_an
Nb_visiteur_jour=Nb_total_visiteur_2017//Nb_jour_an_restant
print(Nb_visiteur_jour)

#Exercice 10:
#Pour sa fête d’anniversaire, Enzo a vidé toutes les bouteilles en remplissant 8 verres de 25cl, trois carafes d’un litre et 5 petits verres de 20 cl. Combien de bouteilles de 2 l avait-il ?
verres=8*0.25
carefes=3*1
petits_verres=5*0.20
Nb_bouteilles=(verres+carefes+petits_verres)/2
print(Nb_bouteilles)

#Exercice 11:
#Papa regarde tous les épisodes de sa série préférée. Le premier épisode dure 1h20 puis il y a 15 épisodes de 44 min. Combien dure la totalité de sa série ?
P_épisode=80
Autres_épisode=44*15
D_total_série=(P_épisode+Autres_épisode)//60
print(f"{D_total_série}H {D_total_série%60} minutes")

#Exercice 12:
#Pour payer leur voiture, les parents de Léo ont donné 2 900€ puis ils doivent payer 290€ par mois pendant 3 ans et demi. Combien coute la voiture au total ?
P_léo_donné=2900
D_payer_mois=42*290
C_total_voiture=P_léo_donné+D_payer_mois
print(C_total_voiture)
"""
#Exercice 13:
#Un cycliste est parti à 9h15. Il suit un parcours de 12,5 km qui lui demande 37 min
# . Il réalise trois fois ce parcours. A quelle heure revient-il chez lui ?
Xi=12.5*3
T_total=37*6
Temps_effectuer=T_total/60
print(Temps_effectuer)

#Exercice 14:
#Une abeille fabrique en moyenne 0,1 g de miel en un mois.
#  Quelle quantité de miel va produire une ruche de 25 000 abeilles en un an ?
abeille_fabrique_mois=0.1
Q_miels_produit_ruche_25000_abeille_mois_g=0.1*25000
Q_miel_P_Ruche_an=Q_miels_produit_ruche_25000_abeille_mois_g*12
print(Q_miel_P_Ruche_an)

#Exercice 15:
#L’agriculteur a récolté 3 tonnes de pommes de terre. 
#Il les met dans des sacs de 2,5 kg qu’il vend 3€ le sac. Combien va -t-il gagner en vendant toute sa récolte ?
sac= 3
Récolte_3tonnes=3000/2.5
Gain_V_récolte=Récolte_3tonnes*3
print(Gain_V_récolte)


#Exercice 16:
#Le soigneur du zoo prépare chaque jour 6 repas pour les petits singes composés à chaque fois de : 
# 1/3 de banane, ½ pomme, 1/6 poire. Combien de pommes, bananes et poires mange un singe en 3 semaines ?

"""
Exercice 17:
Un camion de 12,5 tonnes transporte 8 voitures de 1 450 kg chacune. Il doit passer sur un pont où le poids total est limité à 24 tonnes. Peut-il passer ?

Exercice 18:
Pour un anniversaire, on découpe le gâteau de 600 g en 12 parts. Les enfants prennent une ½ part et les adultes une part entière. Combien pèse la part d’un enfant ?

Exercice 19:
Les scientifiques envoient un satellite dans l’espace pour aller voir Mars, le soleil puis revenir directement sur Terre.

| -----------|-------------|

| Distance | Terre-Mars 76 millions de km | Distance Mars-Soleil 228 millions de km Distance Terre-Soleil (directe) 150 millions de km Le voyage prend environ 1 an pour 30 millions de km. Combien faudra-t-il de temps pour faire le voyage ?

Exercice 20:
Un vendeur a compté combien lui coute exactement un hotdog à fabriquer : Pain 0,42 € Saucisse 0,35 € Ketchup 0,05 € Moutarde 0,03 € Il vend les hotdogs à 4,5 € l’unité. Combien fait-il de bénéfice en vendant 1 000 hotdogs ?
"""