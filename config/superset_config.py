import os

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True,
    "GUEST_ROLE": "Public",
}

GUEST_TOKEN_JWT_SECRET = os.environ.get("GUEST_TOKEN_SECRET", "super-secret-key")

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

TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "content_security_policy": {
        "frame-ancestors": "'self' http://localhost:3000 https://your-frontend.com"
    },
    "force_https": False,
    "content_security_policy_nonce_in": ["script-src"],
}


ENABLE_PROXY_FIX = True

SECRET_KEY = os.environ.get("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE")