import os
from app import app, db
from models import User
from werkzeug.security import generate_password_hash

def import_initial_data():
    with app.app_context():
        print("🗃️ Starting admin creation process...")
        
        try:
            # Vérifier la connexion à la base
            db.session.execute('SELECT 1')
            print("✅ Database connection OK")
            
            # Vérifier si l'admin existe déjà
            existing_admin = User.query.filter_by(email='ambroiseguehi@gmail.com').first()
            if existing_admin:
                print(f"✅ Admin already exists: {existing_admin.email}")
                print(f"   Username: {existing_admin.username}")
                print(f"   Role: {existing_admin.role}")
                return
            
            print("🆕 Creating new admin...")
            
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
            print("✅ Admin saved to database")
            
            # Vérifier la création
            new_admin = User.query.filter_by(email='ambroiseguehi@gmail.com').first()
            if new_admin:
                print("🎉 Admin created successfully!")
                print(f"   Email: {new_admin.email}")
                print(f"   Username: {new_admin.username}")
                print(f"   Name: {new_admin.nom_complet}")
                print(f"   Role: {new_admin.role}")
                
                # Tester le mot de passe
                from werkzeug.security import check_password_hash
                password_ok = check_password_hash(new_admin.mot_de_passe_hash, '@Riel16@8')
                print(f"   Password test: {'✅ OK' if password_ok else '❌ FAILED'}")
            else:
                print("❌ Admin created but not found in database")
                
        except Exception as e:
            print(f"❌ Error during admin creation: {str(e)}")
            import traceback
            traceback.print_exc()
            
        print("🏁 Admin setup process completed!")

if __name__ == "__main__":
    import_initial_data()