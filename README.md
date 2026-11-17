# Fontanges – Simulateur V2
Dépôt GitHub privé. Importer tous les fichiers et le dossier templates à la racine.
Sur Render, créer un Web Service Python relié au dépôt.
Build Command : pip install -r requirements.txt
Start Command : gunicorn app:app
Variables d'environnement : APP_USERNAME=fontanges ; APP_PASSWORD=mot de passe fort choisi par vous. Ne jamais mettre le mot de passe dans GitHub.
Utiliser exclusivement l'adresse HTTPS Render. / sélectionne la version selon la largeur de l'écran ; /ordinateur et /mobile permettent de choisir manuellement.
Authentification HTTP Basic : le navigateur peut conserver les identifiants pendant la session. Les sauvegardes restent locales, sans synchronisation entre appareils. L'offre gratuite Render peut se mettre en veille.
