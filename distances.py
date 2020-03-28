
# %%
import requests
import numpy as np
from utils import haversine
import pandas as pd



def get_lat_long(postcode):
    """
    Krijg long lat coordinaten vanuit postcode

    Parameters
    ----------
    postcode : string
        string met postcode
    """    

    base_url = "https://nominatim.openstreetmap.org/search?"

    params = {
        "postalcode": postcode, 
        "format": "json"
    }

    response = requests.get(base_url, params=params)

    info = response.json()[0]
    coords = (float(info['lat']), float(info['lon']))
    return coords


# %%

vraag = pd.read_csv('vraag.csv', sep=';')
aanbod = pd.read_csv('aanbod.csv', sep=';')

distance_matrix = np.zeros((len(vraag), len(aanbod)))

# %%

for i, vrager in vraag.iterrows():
    for j, aanbieder in aanbod.iterrows():
        postcode1 = vrager['Postcode']
        postcode2 = aanbieder['Postcode']

        distance = haversine.haversine(get_lat_long(postcode1),
                            get_lat_long(postcode2))

        distance_matrix[i, j] = distance

