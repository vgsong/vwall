import os
import csv

def get_project_csv(abasedir, fname):
    with open(os.path.join(abasedir,fname), 'r', encoding='utf-8-sig') as cd:
        csv_data = csv.DictReader(cd)
        result = list(csv_data)
    return result
