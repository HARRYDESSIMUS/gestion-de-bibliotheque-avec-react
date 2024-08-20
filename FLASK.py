from flask import Flask, jsonify, request
from models import Livre, Membre
from database import SessionLocal

app = Flask(__name__)

# GET: Récupérer tous les livres
@app.route('/api/livres', methods=['GET'])
def get_livres():
    session = SessionLocal()
    livres = session.query(Livre).all()
    session.close()
    return jsonify([livre.__dict__ for livre in livres])

# POST: Ajouter un livre
@app.route('/api/livres', methods=['POST'])
def add_livre():
    session = SessionLocal()
    data = request.json
    livre = Livre(titre=data['titre'], auteur=data['auteur'], isbn=data['isbn'])
    session.add(livre)
    session.commit()
    session.close()
    return jsonify(livre.__dict__), 201

# POST: Emprunter un livre
@app.route('/api/livres/<int:livre_id>/emprunter', methods=['POST'])
def emprunter_livre(livre_id):
    session = SessionLocal()
    livre = session.query(Livre).filter(Livre.id == livre_id).first()
    if livre:
        try:
            livre.emprunter(date.today())
            session.commit()
            session.close()
            return jsonify(livre.__dict__), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Livre non trouvé'}), 404

# POST: Retourner un livre
@app.route('/api/livres/<int:livre_id>/retourner', methods=['POST'])
def retourner_livre(livre_id):
    session = SessionLocal()
    livre = session.query(Livre).filter(Livre.id == livre_id).first()
    if livre:
        try:
            livre.retourner()
            session.commit()
            session.close()
            return jsonify(livre.__dict__), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Livre non trouvé'}), 404

if __name__ == "__main__":
    app.run(debug=True)
