# Francky Vincent, le Restaurant

Vous avez été contacté par Francky Vincent, star de la chanson. Ce dernier souhaite créer une application qui lui permettrait d'automatiser le passage de commandes de son nouveau restaurant.

​En effet, Francky Vincent avait déjà ouvert un restaurant par le passé, mais a eu une mauvaise expérience avec son personnel. Après plusieurs années à travailler sur une solution, il a enfin eu une idée de génie : il souhaite tout automatiser, du passage de la commande jusqu'à la préparation des plats. Ainsi, plus de problèmes avec le personnel !

La première étape de la création de ce restaurant nouvelle génération réside dans le passage des commandes sur tablette tactile : il vous a donc embauché pour réaliser un prototype d'API (la partie frontend de l'application ne sera pas réalisée dans ce brief).

## Les spécifications

Un client doit pouvoir passer une commande, en sélectionnant des plats dans une liste. Un plat possède un nom, une description et un prix affiché en TTC (mais stocké en HT).

À la création de la commande, un identifiant unique lui est attribué. Il servira à la génération d'un QR Code, mais vous n'avez pas à vous en préoccuper.

Une commande possède un statut parmi la sélection suivante : En attente, En cours, Terminée, Délivrée, Annulée.

Les paiements se feront uniquement en espèces et vous n'avez pas à gérer cette partie-là.

Un client connecté devra obligatoirement créer ou posséder un compte pour passer commande, avec un email unique et un mot de passe (le mot de passe devra être "haché").

Dans un premier temps, le restaurant ne souhaite pas proposer de menus, juste des plats à la carte.

## Ce que vous devez faire

### 1 - Modélisation

​Réaliser la modélisation (MCD) de la base de données afin de représenter les entités identifiées dans le brief.

### 2 - Initialisation du dépôt

- Initialiser un projet Flask avec les dépendances suivantes :
  - flask
  - flask-sqlalchemy
- Vous pouvez utiliser le SGBD de votre choix (cependant, pour plus de facilité, je conseille sqlite)
- Versionnez votre projet avec git et poussez vos modifications sur un dépôt distant (ex: GitHub ou GitLab)

### 3 - Modèles

Créez les modèles User, Dish et Order en vous basant sur votre modélisation.

Testez que les tables sont bien créées en base de données.

### 4 - API RESTful

Réalisez les routes d'API suivantes, en respectant les conventions RESTful (elles enverront des contenus JSON ainsi que des codes de statut appropriés) :​

#### Les plats

- POST /dishes : créer un plat
- GET /dishes : récupérer tous les plats
- GET /dishes/:dish_id : récupérer un plat à partir de son identifiant
- PUT /dishes/:dish_id : modifier un plat à partir de son identifiant
- DELETE /dishes/:dish_id : supprimer un plat à partir de son identifiant

#### Les utilisateurs

- POST /users : créer un utilisateur avec un email unique et son mot de passe hashé avec bcrypt

#### Les commandes

- POST /orders : créer une commande, ne pas oublier d'y associer l'utilisateur qui a commandé et d'y ajouter les plats
- GET /orders : récupérer la liste de toutes les commandes
- GET /orders/:order_id : récupérer une commande à partir de son identifiant unique
- GET /orders/status/:status : récupérer la liste des commandes filtrées sur un statut
- PUT /orders/:order_id/status/:status : permet de modifier le statut d'une commande

### 5 - Authentification

- Installez les dépendances suivantes :
  - flask-bcrypt
  - pyjwt

Créez la route suivante :

- POST /login : permet à un utilisateur de se connecter, doit renvoyer un JSON Web Token (JWT)

Modifiez les routes suivantes :

- POST /orders : seul un utilisateur connecté peut effectuer une commande
- POST /orders/:order_id/dishes/:dish_id : seul l'utilisateur possédant la commande a le droit d'y ajouter un plat

##### Conseils

- Récupérez l'utilisateur actuel à partir du JWT
- Créez un décorateur `token_required` pour faire cette vérification, puis passez l'utilisateur connecté à la méthode décorée

#### Gestion des rôles

Ajouter un champ permettant de gérer les rôles, dans la table de l'utilisateur : un rôle peut-être USER ou ADMIN.

Modifier les routes suivantes, afin que seul un administrateur y ait accès :

- GET /orders
- GET /orders/:order_id
- GET /orders/status/:status
- PUT /orders/:order_id/status/:status

##### Conseils

- Faites en sorte que cette vérification soit faite grâce à une donnée stockée dans le JWT (il faudra donc modifier la création d'un JWT pour y ajouter le rôle de l'utilisateur)
- Créez un décorateur `is_admin` pour faire cette vérification

### 6 - Tests

- Installez les dépendances suivantes :
  - pytest
  - requests
- POST /dishes : testez qu'il est possible de créer un plat et que le statut renvoyé est 201
- GET /dishes/1 : testez qu'il est possible de récupérer un plat avec l'identifiant 1
- POST /login : testez que la connexion d'un utilisateur, avec de mauvais identifiants, renvoie le statut 401
- POST /login : testez que la connexion d'un utilisateur, avec de bons identifiants, renvoie un JWT
- POST /orders : testez que la route renvoie 403 si aucun JWT n'est fourni
- POST /orders : testez que la route renvoie 403 si un JWT incorrect est fourni
- POST /orders : testez que la route renvoie 201 si un JWT correct est fourni