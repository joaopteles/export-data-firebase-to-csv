import config.config_firebase as config
import pandas as pd


def main():
    data = []
    db = config.init()
    docs = db.collection('Pesquisa RA').stream()
    for doc in docs:
        data.append(doc.to_dict())
    dataFrame = pd.DataFrame(data)
    dataFrame.to_csv('firestore_hp_prod.csv')


main()
