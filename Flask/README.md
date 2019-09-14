v1 : implementation du modele de Melody

/!\ Fonctionne uniquement sur linux en attendant le Docker

Pour lancer l'application :
  1. Telechargez le dossier 
  2. Sur votre CLI rendez vous sur : ```/project_simplon_w37/Flask/```, n'entrez pas dans le dossier project.
  3. tapez : ```export FLASK_APP=project``` 
  4. tapez : ```export FLASK_DEBUG=1```
  5. Creez un environement virtuel python, si vous utilisez virtualenv tapez : ```virtualenv .votre_nom_de_venv```
(vous pouvez aussi creer un environnement conda ou autre)
  6. Activez votre env (en tapant ```source .venv-flask/bin/activate``` si vous utilisez venv)
  7. tapez :  ```cd project```
  8. tapez : ```pip install -r requirements.txt```
  9. tapez : ```mkdir static```
  10. ouvrez le fichier customvision.py et remplacez les valeurs manquantes par celles du txt 'azure_customvision_access_keys.txt' (demandez le sur le Discord).
  11 tapez : ```cd ..``` pour retourner sur /project_simplon_w37/Flask/
  12. tapez : ```flask run```
  13. l'application tourne sur ```localhost:5000```

Pour utiliser l'application :
- Creez un compte utilisateur avec signup
- loggez vous
- Cliquez sur Album puis sur 'Create an album'
- Completez les champs, inserez le fichier zip cat_photos.zip (20 photos recommandees pour conserver une experience fluide)
- Cliquez sur albums et sur le nom de votre album qui vient d'etre ouvert
- La predicition est faite à ce moment (c'est moche mais rapide à livrer)

Recommandations :
Le modele de Melody utilise les services cognitifs azure pour faire la predicition du label, c'est super performant mais ca traite les photos une par une
Pour une experience otpimale il faudrait utiliser un fichier zip avec pas plus d'une vingtaine de photos.
Un fichier .zip de photos de chats est fournis pour tester l'application.
Ce serait cool de tester avec le modele de Val qui est capable de predire les labels plus vite.

Je vais essayer de commenter le code rapidement. 
Le front est fait en Bulma, vous pouvez le custom facilement en utilisant la doc : https://bulma.io/
Thanks !

les outils :
Flask login : https://flask-login.readthedocs.io/en/latest/
Blueprint : https://flask.palletsprojects.com/en/1.1.x/blueprints/
Flask SQLAlchemy : https://flask-sqlalchemy.palletsprojects.com/en/2.x/
