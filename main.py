from app.service_val import quefaire, commerce
from app.service.convert import get_table, get_table_id
from app.service.elastic import get_autocompletion
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-all-activities', methods=['GET'])
def get_all_activities():
    columns_header= ["id",
            "titre",
            "coordonnees"]
    return jsonify(get_table(columns_header, "V_D_SIMPLE_ACTIVITE"))

@app.route('/get-all-commerces', methods=['GET'])
def get_all_commerces():
    columns_header= ["id",
            "titre",
            "coordonnees"]
    return jsonify(get_table(columns_header, "V_D_SIMPLE_COMMERCE"))

@app.route('/get-activity', methods=['GET'])
def get_activity():
    id = request.args.get('id')
    id_name = "id_act"
    columns_header = [
        "id",
        "url",
            "titre",
            "chapeau",
            "description",
            "date_de_debut",
            "date_de_fin",
            "occurrences",
            "image",
            "mots_cles",
            "lieu",
            "adresse",
            "code_postal",
            "ville",
            "coordonnees",
            "contact",
            "phone",
            "email",
            "facebook",
            "twitter",
            "type_prix",
            "detail_prix",
            "reservation",
            "audience"]
    return jsonify(get_table_id(columns_header, "V_D_ACTIVITE", id_name, id))

@app.route('/get-commerce', methods=['GET'])
def get_commerce():
    id = request.args.get('id')
    id_name = "id_com"
    columns_header = [
        "id",
        "titre",
        "adresse",
        "code_postal",
        "type_commerce",
        "fabriquer_paris",
        "service",
        "description",
        "precision",
        "website",
        "phone",
        "email",
        "coordonnees"]
    return jsonify(get_table_id(columns_header, "V_D_COMMERCE", id_name, id))

@app.route("/autocomplete", methods=['GET', 'POST'])
def autocomplete():
    if request.method == 'POST':
        # process post data
        data = request.get_json()
        pass
    else:
        # process get data
        data = request.args.get('text')
        pass

    return jsonify(get_autocompletion(data))

@app.route("/que-faire", methods=['GET'])
def quefaire_paris():
    quefaire()
    return ""

@app.route("/commerce", methods=['GET'])
def commerce_paris():
    commerce()
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7899,debug=True)