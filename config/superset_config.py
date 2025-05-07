import os

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True
}

PUBLIC_ROLE_LIKE = "Gamma"

ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': [
        'http://localhost:3000',    # React dev
        'http://localhost:8088',    # Superset itself
        'http://localhost:8888',    # Jupyter/test
        'https://your-app.up.railway.app'  # Optional: production URL
    ],
}



ENABLE_PROXY_FIX = True


SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE")