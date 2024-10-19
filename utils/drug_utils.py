import pandas as pd

def get_drug_info(drug_name):
    drugs = pd.read_csv('data/drugs.csv')
    result = drugs[drugs['drug_name'].str.contains(drug_name, case=False, na=False)]
    return result if not result.empty else None
