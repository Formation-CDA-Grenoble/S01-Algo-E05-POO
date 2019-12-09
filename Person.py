import datetime

# Simulation de données que l'on pourrait récupérer d'une base de données
data = [
    ["Josette", "Martin", 25, False],
    ["Robert", "Durand", 45, True],
    ["Lucien", "Pinard", 33, True],
]

# Modèle permettant de créer des objets (instances) représentant des personnes
class Person:
    # Propriétés des objets de type "personne"
    firstName = ""
    age = 0
    lastName = ""
    isMale = False

    # Méthodes : fonctions encapsulées dans une classe, qui permettent à chacune de ses instances
    # de connaître un comportement spécifique à elle-même
    # En Python, chaque méthode prend comme premier paramètre une référence vers l'objet qui l'appelle,
    # appelée "self" (soi-même) par convention

    # Méthode permettant de renvoyer le nom complet d'une personne
    def fullName(self):
        return self.firstName + " " + self.lastName

    # Méthode permettant de renvoyer un message de salutation de la part d'une personne
    def sayHello(self):
        return "Bonjour, je m'appelle " + self.fullName()
    
    # Méthode permettant à une personne de saluer une autre personne
    def sayHelloTo(self, otherPerson):
        return "Bonjour " + otherPerson.firstName + ", je m'appelle " + self.fullName()


# Modèle permettant de créer des objets (instances) représentant des articles
class Article:
    # Propriété des objets de type "article"
    createdAt = datetime.datetime.now()
    title = ""
    content = ""
    # La variable "auteur" de chaque article contient un objet de type "personne"
    author = None


# Génère des objets de type "personne" en adéquation avec le tableau de données récupéré plus haut
people = []
for personData in data:
    # Crée un objet de type "personne"
    person = Person()
    # Remplit les propriétés de l'objet nouvellement créé avec les données du tableau
    person.firstName = personData[0]
    person.lastName = personData[1]
    person.age = personData[2]
    person.isMale = personData[3]
    # Ajoute l'objet nouvellement créé à une liste
    people.append(person)


# Crée un nouvel objet de type "article"
article = Article()
article.title = "Le Python ça déchire"
article.content = "texte texte texte texte texte texte texte "
# Définit Robert comme auteur de cet article
article.author = people[1]
# Affiche le nom complet de l'auteur de l'article
print(article.author.fullName())


# Pour chaque personne générée
for person in people:
    # Demande à cette personne de saluer Josette
    print(person.sayHelloTo(people[0]))
    