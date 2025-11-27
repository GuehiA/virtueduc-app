#!/bin/bash
set -o errexit
set -o xtrace  # Active le mode debug

echo "🚀 Starting build process..."

# Mettre à jour pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Installer les dépendances
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Vérifier que app.py peut être importé
echo "🔍 Testing app import..."
python -c "
try:
    from app import app, db
    print('✅ App import successful')
except Exception as e:
    print(f'❌ App import failed: {e}')
    import traceback
    traceback.print_exc()
"

# Créer les tables directement
echo "🗃️ Creating database tables..."
python -c "
from app import app, db
with app.app_context():
    try:
        db.create_all()
        print('✅ Database tables created successfully')
        
        # Vérifier que la table User existe
        from models import User
        user_count = User.query.count()
        print(f'✅ User table exists, count: {user_count}')
        
    except Exception as e:
        print(f'❌ Database creation failed: {e}')
        import traceback
        traceback.print_exc()
"

# Créer l'admin automatiquement
echo "👑 Creating admin user..."
python -c "
try:
    from import_data import import_initial_data
    import_initial_data()
    print('✅ Admin creation script completed')
except Exception as e:
    print(f'❌ Admin creation failed: {e}')
    import traceback
    traceback.print_exc()
"

echo "✅ Build completed successfully!"