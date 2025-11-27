import os
from app import app, db
from models import User
from werkzeug.security import generate_password_hash

def import_initial_data():
    with app.app_context():
        print("🗃️ Creating admin user...")
        
        # Vérifier si l'admin existe déjà
        existing_admin = User.query.filter_by(email='ambroiseguehi@gmail.com').first()
        if existing_admin:
            print(f"✅ Admin already exists: {existing_admin.email}")
            return
        
        # Créer le nouvel admin avec VOS identifiants
        admin = User(
            email='ambroiseguehi@gmail.com',
            username='ambroise',
            nom_complet='Ambroise Guehi',
            role='admin',
            mot_de_passe_hash=generate_password_hash('@Riel16@8')
        )
        
        db.session.add(admin)
        db.session.commit()
        
        # Vérifier la création
        new_admin = User.query.filter_by(email='ambroiseguehi@gmail.com').first()
        if new_admin:
            print("✅ Admin created successfully!")
            print(f"   Email: {new_admin.email}")
            print(f"   Username: {new_admin.username}")
            print(f"   Name: {new_admin.nom_complet}")
        else:
            print("❌ Failed to create admin")
            
        print("🎉 Admin setup completed!")

if __name__ == "__main__":
    import_initial_data()