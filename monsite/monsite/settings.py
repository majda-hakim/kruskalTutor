from pathlib import Path

# === BASE DIR ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === SÉCURITÉ ===
SECRET_KEY = 'django-insecure-7^mn8d6y#-bdwd)$ag@8l^*8^=!yks@7^r))4l(n5n%@)4)_j8'
DEBUG = True
ALLOWED_HOSTS = []

# === APPLICATIONS INSTALLÉES ===
INSTALLED_APPS = [
    'corsheaders',                # 🔥 pour gérer le CORS
    'rest_framework',             # 🔥 pour créer l'API REST
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kruskalapi',                 # ✅ ton app contenant le modèle User
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 🔥 doit être en haut
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# === URLS & TEMPLATES ===
ROOT_URLCONF = 'monsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'monsite.wsgi.application'

# === BASE DE DONNÉES ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ UTILISATEUR PERSONNALISÉ
AUTH_USER_MODEL = 'kruskalapi.User'  # 👈 ton modèle User personnalisé

# === VALIDATION MOT DE PASSE ===
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# === LOCALISATION ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === FICHIERS STATIQUES ===
STATIC_URL = 'static/'

# === TYPE DE CLÉ PRIMAIRE PAR DÉFAUT ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ CONFIGURATION CORS (autorise React à appeler Django)
CORS_ALLOW_ALL_ORIGINS = True
