#!/bin/bash
set -o errexit

echo "🚀 Starting build process..."

# Installer les dépendances
pip install -r requirements.txt

# Exécuter les migrations de base de données
echo "📦 Running database migrations..."
python -m flask db upgrade

echo "✅ Build completed successfully!"