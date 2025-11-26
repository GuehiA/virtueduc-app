#!/bin/bash
set -o errexit

echo "🚀 Starting build process..."

# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Initialiser les migrations si elles n'existent pas
if [ ! -d "migrations" ]; then
    echo "🗃️ Initializing database migrations..."
    python -m flask db init
fi

# Créer les tables directement (au cas où les migrations échouent)
echo "🗃️ Creating database tables..."
python -c "
from app import app, db
with app.app_context():
    db.create_all()
    print('✅ Database tables created successfully')
"

echo "✅ Build completed successfully!"