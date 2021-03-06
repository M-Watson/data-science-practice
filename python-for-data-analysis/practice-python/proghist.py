import geopy
import pandas as pd
from geopy.geocoders import Nominatim, GoogleV3

def get_latitude(x):
    return(x.latitude)

def get_longitude(x):
    return(x.longitude)



def main():
    df = pd.read_csv('census.csv', index_col=None, header=0, sep=",")
    df['Country'] = "United Kingdom"




    geolocator = Nominatim()

    '''
    geolocate_column = df['Area_Name'].apply(geolocator.geocode)
    df['Latitude'] = geolocate_column.apply(get_latitude)
    df['longitude'] = geolocate_column.apply(get_longitude)
    '''

    df['helper'] = df['Area_Name'].map(str) + " " + df['Country'].map(str)
    geolocate_column = df['helper'].apply(geolocator.geocode)
    df['latitude'] = geolocate_column.apply(get_latitude)
    df['longitude'] = geolocate_column.apply(get_longitude)


    df.to_csv('output_2.csv')


if __name__ == '__main__':
  main()
