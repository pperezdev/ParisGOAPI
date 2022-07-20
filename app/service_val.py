from app.service.insert_file import s3Insert
from app.service.get_file import download_file_csv, set_file_name
from app.service.convert import csv_to_sql

def get_file(get_url, output_file, s3_folder):
    download_file_csv(get_url, output_file)
    s3 = s3Insert()

    file_binary = open(f"..\{output_file}", "rb").read()
    s3.upload_my_file("s3pa4dd01", s3_folder, file_binary, output_file.split('/')[1])

def quefaire():
    get_url = "https://opendata.paris.fr/explore/dataset/que-faire-a-paris-/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
    output_file = set_file_name("data/quefaireparis.csv")
    s3_folder = "raw_folder/paris_activite"
    get_file(get_url, output_file, s3_folder)
    header = ["URL",
            "Titre",
            "Chapeau",
            "Description",
            "Date de début",
            "Date de fin",
            "Occurrences",
            "URL de l\'image",
            "Mots clés",
            "Nom du lieu",
            "Adresse du lieu",
            "Code postal",
            "Ville",
            "Coordonnées géographiques",
            "Url de contact",
            "Téléphone de contact",
            "Email de contact",
            "URL Facebook associée",
            "URL Twitter associée",
            "Type de prix",
            "Détail du prix",
            "URL de réservation",
            "audience"]
    output = output_file.split("/")[1]
    header_sql = "(URL,TITRE,CHAPEAU,DESCRIPTION,DATE_DEBUT,DATE_FIN,OCCURENCE,IMAGE,MOTS_CLES,NOM_LIEU,ADRESSE,CODE_POSTAL,VILLE,COORDONNEES,WEBSITE,PHONE,EMAIL,FACEBOOK,TWITTER,TYPE_PRIX,DETAIL_PRIX,URL_RESERVATION,AUDIENCE,FILENAME)"
    csv_to_sql(output,header,"d_activite",header_sql)  

def commerce():
    get_url ="https://opendata.paris.fr/explore/dataset/coronavirus-commercants-parisiens-livraison-a-domicile/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
    output_file = set_file_name("data/commerceparis.csv")
    s3_folder = "raw_folder/paris_commerce"
    get_file(get_url, output_file, s3_folder)
    header = ["Nom du commerce",
    "Adresse",
    "Code postal",
    "Type de commerce",
    "Fabriqué à Paris",
    "Services",
    "Description",
    "Précisions",
    "Site internet",
    "Téléphone",
    "Mail",
    "geo_point_2d"]
    output = output_file.split("/")[1]
    header_sql = "(TITRE,ADRESSE,CODE_POSTAL,TYPE_COMMERCE,FABRIQUER_PARIS,SERVICE,DESCRIPTION,PRECISION,WEBSITE,PHONE,EMAIL,COORDONNEES,FILENAME)"
    csv_to_sql(output,header,"d_commerce",header_sql,mapped_column=['Code postal'])  
