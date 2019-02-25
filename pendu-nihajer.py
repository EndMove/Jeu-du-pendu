#  pendu-nihajer.py
#  Powered By EndMove
#  Copyright 2019 Jérémi_NIHART_-_classe5tc

from random import randrange
from utils import *
import os
import time

#Remarque: Pour le design du pendu en mode graphique lorsqu'un mot 
#est faux le système affiche un "-" dans la liste des mots erronés.
#================================================================#
#Paramètres:
debug = False 			#Débogage complèt.
system = "auto"			#Système d'exploitation ('win' ou 'lin' ou 'auto' -> pour détecter automatiquement le système)
d_l_show = False 		#Afficher le mot dans découvrir lettre.
vie = 10 				#Nombre de vies (ne peuvent pas êtres choisie si mode dessin activé).
mode_dessin = True		#Affichage grafique du jeu avec un petit pendu.
sleep_time = 1.5 		#Temps avant clear consol/avant action importantes.
#================================================================#

#Formatage:
er1 = "Erreur: Synthax incorrecte !"
er2 = "Erreur: Lettre déja essayée !"
er3 = "Erreur: Mot déja essayé !"
er4 = "Erreur: Réponce incorrecte !"
er5 = "Erreur: Ce nombre ne respecte pas les limite !"
er6 = "Error 500 ! Please contact EndMove at contact@melend-studio.eu."
er7 = "Erreur: Mode dessin activé ! le nombre de vie est donc par défault 10.\nPour pouvoir choisir le nombre de vie désactivé le mode dessin"

#Liste/dico/dessins:
dico = ["fromage","alambique","casserole","programme","television","logiciel",
        "avion","gourmandise", "telechargement","illegalite","instrument",
        "tondeuse","ordinateur","programmation","technologie","diffusion",
        "estampage","navigation","hasardeux","fondations","artistique",
        "utilisation","imbuvable", "legume","innovation","constitution",
        "iconique","evidence","invitation","cavite","lampadaire","limonade",
        "bouteille","concours","culture","psychologie","cardiologue",
        "pharmaceutique","laboratoire","scolaire","rasoir","medicament",
        "perfusion","pansement","forage","aiguille","costume","danser",
        "contemporain","mondialisation","environnement","ombrelle","vetement",
        "sentiment","congelateur","spatule","chandelier","bateau","commandant",
        "paquerette","coquelicot","robinetterie","armoiries","boutique",
        "fantome","plaisanterie","ironique","electricite","ingenieur",
        "infirmiere","informatique","biologie","citoyennete","chaussette",
        "confiseries","glacier","bistrot","opticien","elegant","aquatique",
        "piscine","romantique","antiquite","automobile","italienne"]
wrong_l = []
wrong_m = []
pendu_num = """  +----------+
  |          0
  |          1
  |         324
  |        5 2 6
  |         728
  |       97   89
 /|\\
/ | \\
~~~~~~~~~~~~~~~~~~~
~~~~~~*******~~~~~~~~
~x~x~x~x~x~x~x~x~x~x~~~"""
pendu = """  +----------+
  |          |
  |          0
  |         /|\\
  |        ° | °
  |         /'\\
  |       _/   \\_
 /|\\
/ | \\
~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~"""

#ENDCOL powered by endmove.eu
class endcol:
	#berlingo
	aff_mot = '\033[1;32m' 
	aff_mau = '\033[1;31m'
	#form
	BOLD = '\033[1m'
	#couleur
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	RESET = '\033[0;39m'
	
#ENDCLEAR powered by endmove.eu
def endclear():
	if system == "auto":
		os.system('cls' if os.name=='nt' else 'clear')
	elif system == "win":
		os.system("cls")
	elif system == "lin":
		os.system("clear")
		
def tirer_mot(dico: list):
	i = randrange(0, len(dico))
	return dico[i]
	
def affiche_coups(nb: int):
	print("Chances: ", end="")
	for i in range(0, nb):
		if i < nb-1:
			print("|", end="")
		elif i >= nb-1:
			print("|")
			
def affiche_mot_a_trouver(mot: str):
	print(endcol.aff_mot,end="")
	print(mot.capitalize(),endcol.RESET)
	
def affiche_mauvaises_lettres(wrong: list):
	n = len(wrong)
	print(endcol.aff_mau,end="")
	print("[",end="")
	if n == 0:
		print("]",endcol.RESET)
	for i in range(0,n):
		if i+1 !=  n:
			print("{}, ".format(wrong[i].upper()),end="")
		else:
			print("{}]".format(wrong[i].upper()),endcol.RESET)

def proposition_lettre(wrong: list):
	y = True
	while y == True:
		x = False		
		lettre = input("Entrez une lettre: ").lower()
		if lettre != "" and lettre.isalpha():
			n = removeAccent(lettre[0])
			for i in wrong:
				if i == n:
					print(er2)
					x = True
			if x == False:
				y = False
				return n
		else:
			print(er1)
			
def proposition_mot(wrong: list):
	y = True
	while y == True:
		x = False
		n = mot = input("Entrez un mot: ").lower()
		if mot != "" and len(mot) > 2 and mot.isalpha():
			for i in wrong:
				if i == n:
					print(er3)
					x = True
			if x == False:
				y = False
				return n
		else:
			print(er1)	

def check_lettre(lettre: str, secret: str):
	x = False
	for i in secret.lower():
		if i == lettre.lower():
			x = True
	return x
			
	
def check_mot(mot: str, secret: str):
	if mot.lower() == secret.lower():
		return True
	else:
		return False
	
def decouvrir_lettre(lettre: str, cache: str, secret: str):
	if lettre == "generate":
		cache_g = ""
		x = 0
		for i in secret:
			cache_g += "*"
		return cache_g
	elif len(lettre) == 1:
		cache_reg = ""
		y = len(secret)
		for i in range(0,y):
			if lettre.lower() == secret[i].lower():
				cache_reg += secret[i]
			else:
				cache_reg += cache[i]
		if d_l_show == True:	
			print(endcol.GREEN,end="")
			for y in range(0, len(cache_reg)):
				if y == len(cache_reg)-1:
					print("{}".format(cache_reg[y]))
				else:
					print("{}".format(cache_reg[y]), end=" ")
			print(endcol.RESET,end="")
		return cache_reg

def questionOI(msg: str):
	bcl = True
	while bcl == True:
		print(msg, " (o/n): ",end="")
		i = (input()).lower()
		if i == "o" or i == "n" or i == "":
			bcl = False
			if i == "o":
				return True
			elif i == "n" or i == "":
				return False
		else:
			print(er4)

def afficher_mot(mot: str):
	band = ""
	for i in range(0, len(mot)):
		if i == len(mot)-1:
			band += "--+"
		if i == 0:
			band += "+--+"
		elif i != len(mot)-1:
			band += "-+"
	print(endcol.GREEN,end="")
	print(band)
	for y in range(0, len(mot)):
		if y == len(mot)-1:
			print("{} |".format(mot[y]))
		if y == 0:
			print("| {}".format(mot[y]), end=" ")
		elif y != len(mot)-1:
			print("{}".format(mot[y]), end=" ")
	print(band,endcol.RESET)

def afficher_pendu(n: int, wrong: list, gagne: bool = False):
	fin_success = "Gagné !"
	fin_lose = "Perdu !"
	dessin_pendu = ""
	id_wrong = 1
	tail_mot = 0
	tail = len(pendu_num)
	for i in range(0, len(pendu_num)):
		if pendu_num[i].isdecimal():
			if int(pendu_num[i]) <= n-1:
				dessin_pendu += pendu[i]
			elif int(pendu_num[i]) > n-1:
				dessin_pendu += " "
		elif pendu_num[i] == "x":
			if len(wrong) >= id_wrong:
				dessin_pendu += wrong[id_wrong-1].upper()
				id_wrong += 1
			else:
				dessin_pendu += pendu[i]
		elif pendu_num[i] == "*":
			if gagne == True:
				if len(wrong) == 10:
					dessin_pendu += fin_lose[tail_mot]
					tail_mot += 1
				else:
					dessin_pendu += fin_success[tail_mot]
					tail_mot += 1
			else:
				dessin_pendu += pendu[i]
		else:
			dessin_pendu += pendu[i]
	return(dessin_pendu)

def menus(var: str):
	if var == "finish":
		sec = 10
		while sec != 0:
			if mode_dessin == True:
				endclear()
				print(endcol.CYAN,end="")
				print(afficher_pendu(10-vie, wrong_l, True),endcol.RESET)
				time.sleep(10)
				sec = 0
			else:
				endclear()
				print(endcol.CYAN,end="")
				print("""#====================[ {:02} ]====================#
						\n   Vous avez gagné ! Le mot était: {}
						\n        Il restait {} vies, félicitaion !
						\n#==============================================#""".format(sec, mot_claire, vie))
				time.sleep(1)
				sec -= 1
		print(endcol.RESET)
		endclear()
	if var == "lose":
		sec = 10
		while sec != 0:
			if mode_dessin == True:
				endclear()
				print(endcol.RED,end="")
				print(afficher_pendu(10-vie, wrong_l, True),endcol.RESET)
				time.sleep(10)
				sec = 0
			else:
				endclear()
				print(endcol.RED,end="")
				print("""#====================[ {:02} ]====================#
						\n   Vous avez perdu ! Le mot était: {}
						\n         Domage ! Tu y étais presque !
						\n#==============================================#""".format(sec, mot_claire, vie))
				time.sleep(1)
				sec -= 1
		print(endcol.RESET)
		endclear()
	if var == "home":
		p = True
		while p:
			endclear()
			print(endcol.YELLOW,end="")
			print("""#====================[ EndPendu ]====================#\n#    Bonjour joueur ! Bienvenue dans mon univers !   #\n#               Jeu Powered By EndMove               #\n#                                                    #\n#        s: start | v: choix vies | q: quitter       #\n#====================================================#""".format())
			print(endcol.RESET,end="")
			cmd = input("CHOIX: ").lower()
			if cmd == "v" or cmd == "s" or cmd == "" or cmd == "q":
				if cmd == "s" or cmd == "":
					print("Démarrage...")
					p = False
					time.sleep(1)
				elif cmd == "v":
					if mode_dessin == True:
						print(er7)
						time.sleep(5)
					else:
						print("Vous avez acctuelment {} vie(s)".format(vie))
						n = input("Entrez le nombre de vies souhaitées (min:1 max:20): ")
						if n.isdecimal():
							if 20 >= int(n) >= 1:
								if gameset("vie", n):
									print("<=> Nombre de vies mise à jour.")
								else:
									print(er6)
								time.sleep(1)
							else:
								print(er5)
								time.sleep(1)
						else:
							print("<=> Modification annulée.")
							time.sleep(1)
				elif cmd == "q":
					if gameset("quitte", 0):
						print("Fermeture du jeu...")
						time.sleep(1)
						p = False
					else:
						print(er6)
						time.sleep(1)
			else:
				print(er1)
				time.sleep(1)

def gameset(var: str, num: int):
	global vie
	global game
	if var == "vie":
		vie = int(num)
		return True
	if var == "reboot":
		vie = int(num)
		global wrong_l
		wrong_l = []
		global wrong_m
		wrong_m	= []
		game = True
		return True
	if var == "quitte":
		global s
		s = False
		game = False
		return True
			
def debugFunction(debug):
	if debug:
		print(endcol.RED,end="")
		print("Démarrage du débogage...\n\n",endcol.RESET)
		fauxTest = ["e", "r", "f", "k", "p"]
		print("debug - Mot aléatoire:",tirer_mot(dico))
		print("debug - Affichage vie: ",end="")
		affiche_coups(5)
		print("debug - Affichage mot type1: ",end="")
		affiche_mot_a_trouver(tirer_mot(dico))
		print("debug - Affichage mot type2:")
		afficher_mot(tirer_mot(dico))
		print("debug - Affichage mauvaises lettre: ",end="")
		affiche_mauvaises_lettres(fauxTest)
		print("debug - Proposition lettre: ",end="")
		n = proposition_lettre(wrong_l)
		print("debug - Proposition mot: ",end="")
		n = proposition_mot(wrong_m)
		print("debug - Check lettre 'm' in 'salut':",check_lettre("m","salut"))
		print("debug - Check mot 'salut' in 'salut':",check_mot("salut","Salut"))
		print("debug - Génération mot caché de 'salut':",decouvrir_lettre("generate","","salut"))
		print("debug - Découvrir lettre 'a' in 'salut':",decouvrir_lettre("a","*****","Salut"))
		print("debug - QuestionOI 'Bonjour veux tu jouers ?': ",end="")
		print(questionOI("Bonjour veux tu jouers ?"))
		print("debug - removeAccent 'é' -> 'e':", removeAccent("é"))
		print("debug - menus du jeu: ERREUR: les menus ne sont pas débogables !") 
		input("\nDébug effectué avec succès, pour charger la partie 'PRESS ENTER'")
	
if __name__ == "__main__":
	s = True
	game = True
	while s:
		gameset("reboot", 10)
		menus("home")
		print("Chargement des composants ...")
		auto_restart = True
		mot_claire = tirer_mot(dico)
		mot_cache = decouvrir_lettre("generate","",mot_claire)
		debugFunction(debug) #DebugVAR
		endclear() #(Clear)
		print(endcol.MAGENTA,end="")
		print("Jeu du pendu | Powered By EndMove",endcol.RESET)
		print("Un mot aléatoire a été tiré, maintenant le jeu peut commencer !\n")
		while game:
			if mode_dessin == True:
				print(endcol.MAGENTA,end="")
				print(afficher_pendu(10-vie, wrong_l),endcol.RESET)
				afficher_mot(mot_cache)
			else:
				affiche_coups(vie)
				afficher_mot(mot_cache)
				affiche_mauvaises_lettres(wrong_l)
			if questionOI("Voulez vous proposer un mot ?"):
				prop_mot = proposition_mot(wrong_m)
				if check_mot(prop_mot, mot_claire):
					if debug:
						print("oui") #DebugVAR
					menus("finish")
					game = False
				else:
					print("Oupss ! Raté... (-1)")
					wrong_m.append(prop_mot)
					if mode_dessin == True:
						wrong_l.append("-")
					vie -= 1
					if debug:
						print("non", wrong_m) #DebugVAR
					time.sleep(sleep_time)
					endclear()
			else:
				if debug:
					print("non") #DebugVAR
				prop_lettre = proposition_lettre(wrong_l)
				if check_lettre(prop_lettre, mot_claire):
					if debug:
						print("oui") #DebugVAR
					mot_cache = decouvrir_lettre(prop_lettre, mot_cache, mot_claire)
					if check_mot(mot_cache, mot_claire):
						print("Tu as découvert le mot propose le pour finir la partie !")
						time.sleep(sleep_time)
						endclear()
					else:
						print("Tu as trouvé une lettre suplémentaire !")
						time.sleep(sleep_time)
						endclear()
				else:
					print("Oupss ! Raté... (-1)")
					wrong_l.append(prop_lettre)
					vie -= 1
					if debug:
						print("non", wrong_l, vie) #DebugVAR
					time.sleep(sleep_time)
					endclear()
			if vie == 0:
				menus("lose")
				game = False
	endclear()
	print(endcol.BLUE,end="")
	print("]====[ Merci d'avoir joué ]====[",endcol.RESET)
