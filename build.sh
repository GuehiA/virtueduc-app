#!/bin/bash
set -o errexit

echo "🚀 Starting build process..."

# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Créer les tables directement
echo "🗃️ Creating database tables..."
python -c "
from app import app, db
with app.app_context():
    db.create_all()
    print('✅ Database tables created successfully')
"

echo "✅ Build completed successfully!"