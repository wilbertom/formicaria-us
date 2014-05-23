from pymongo import MongoClient
import soa_api

client = MongoClient()
db = client['ant_farm']
school_of_data = db['school_of_data']

def save_all():
    map(school_of_data.insert, map(soa_api.details, soa_api.lat_lons()))

if __name__ == '__main__':

    save_all()


