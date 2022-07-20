import requests
import csv
import datetime
import uuid


def download_file_csv(url, output_file):
    data = requests.request('get', url)
    decoded_content = data.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=';')
    content = list(cr)
    with open(output_file, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f,delimiter=";")
        for row in content:
            writer.writerow(row)
    return "API IS DONE"

def set_file_name(name):
        uid = uuid.uuid4().hex
        date = datetime.datetime.now()
        datestr = date.strftime("%Y%m%d")
        end_file_name = name.split('.')[1]
        return f"{name}_{datestr}_{uid}.{end_file_name}"