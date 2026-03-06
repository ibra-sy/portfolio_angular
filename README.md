# Portfolio – SYLLA SCHEICKNA IBRAHIM

Ce projet est mon portfolio développeur, construit avec **Angular** pour le frontend et **Django REST Framework** pour le backend.  
Il présente mon profil, mon expérience, mes projets GitHub et permet de me contacter.

## ⚙️ Stack technique

- **Frontend** : Angular 17+ (standalone components, SCSS)
- **Backend** : Django 5 + Django REST Framework
- **Base de données** : SQLite (dev)
- **Déploiement prévu**
  - Frontend : Vercel (`frontend/`)
  - Backend : Render (`backend/`)

---

## 🧩 Structure du projet

- `frontend/` : application Angular (`portfolio`)
  - `src/app/home` : sections Home / About / Services / Portfolio / Resume / Blog / Contact
  - `src/app/shared` : services Angular (API REST) et modèles TypeScript
  - `src/assets` : images du portfolio + CV (`SYLLA SCHEICKNA resume .pdf`)
- `backend/` : projet Django (`portfolioAngularBackend`)
  - `portfolio/` : API portfolio (projets, expériences, services, réseaux sociaux, localisation…)
  - `utilisateur/` : modèle utilisateur personnalisé
  - `requirements.txt` : dépendances backend

---

## 🚀 Lancer le projet en local

### 1. Backend Django

```bash
cd backend

# (optionnel mais recommandé)
python -m venv .venv
.\.venv\Scripts\activate  # Windows PowerShell

pip install -r requirements.txt

python manage.py migrate
python manage.py seed_portfolio  # insère mes données (expériences, services, projets, réseaux)
python manage.py runserver
```

Le backend sera disponible sur `http://127.0.0.1:8000/`  
Quelques endpoints utiles :

- `http://127.0.0.1:8000/api/v1/experiences/`
- `http://127.0.0.1:8000/api/v1/services/`
- `http://127.0.0.1:8000/api/v1/projects/`
- `http://127.0.0.1:8000/api/` (documentation Swagger)

### 2. Frontend Angular

Dans un deuxième terminal :

```bash
cd frontend
npm install
npm start
```

Le frontend sera disponible sur `http://localhost:4200`.

---

## 🌐 Déploiement

### Frontend – Vercel

- **Root Directory** : `frontend`
- **Build Command** : `npm run build`
- **Output Directory** : `dist/portfolio/browser`
- **Framework Preset** : Angular

### Backend – Render

- **Root Directory** : `backend`
- **Build Command** :

  ```bash
  pip install -r requirements.txt && python manage.py migrate
  ```

- **Start Command** :

  ```bash
  gunicorn portfolioAngularBackend.wsgi:application
  ```

Pense à ajouter le domaine Render dans `ALLOWED_HOSTS` et à configurer CORS pour le domaine Vercel.

---

## 👤 À propos

- **Nom** : SYLLA SCHEICKNA IBRAHIM  
- **Domaine** : Computer Science (Network & Telecommunications)  
- **Email** : `hamahoullah.sylla@gmail.com`  
- **GitHub** : [https://github.com/ibra-sy](https://github.com/ibra-sy)  
- **LinkedIn** : [Profil LinkedIn](https://www.linkedin.com/in/scheickna-ibrahim-sylla-50a916315)

Le CV est disponible dans le site via le bouton **Download CV** (fichier `frontend/src/assets/SYLLA SCHEICKNA resume .pdf`).

# portfolio-angular
