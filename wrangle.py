import pandas as pd
import numpy as np
import re

def get_art():
    art = pd.read_csv('MetObjects.txt')
    art.rename(columns=lambda c: c.lower().replace(' ','_'), inplace=True)

    return art

def filter_artist_cols(art):
    # separator value for filtering functions
    separator = '|'

    
    art.drop(columns=['artist_prefix', 'artist_display_name', 
                      'artist_display_bio','artist_suffix',
                      'artist_wikidata_url'], inplace=True)

    # Artist Role
    # Role of the artist related to the type of artwork or object that was created
    #      if null, change to ''
    #      if multiple roles keep first role
    #      keep only the top 5 roles plus N/A, all else are 'other'
    art.artist_role = art.artist_role.fillna('')
    role_list = ['Artist', 'Publisher', 'Designer', 'Maker', 'Author', 'N/A']
    art['artist_role'] = art['artist_role'].map(lambda x: x.split(separator, 1)[0]).map(lambda x: 'N/A' if x == '' else x)
    art['artist_role'] = art['artist_role'].map(lambda x:  'Other' if x not in (role_list) else x)

    # artist_alpha_sort	
    # Used to sort alphabetically by author last name. 
    #      if null, change to ''
    #      if multiple artists keep only primary artist
    art.artist_alpha_sort = art.artist_alpha_sort.fillna('N/A')
    art['artist_alpha_sort'] = art['artist_alpha_sort'].map(lambda x: x.split(separator, 1)[0])

    # artist nationality
    # nationality of artist
    ##      if null, change to ''
    #       if multiple artists keep primary artist
    #       keep only the top 6 nationalities, all else 'Other'
    art.artist_nationality = art.artist_nationality.fillna('')
    nationality_list = ['American', 'French', 'Italian', 'British', 'German', 'Japanese']
    art['artist_nationality'] = art['artist_nationality'].map(lambda x: x.split(separator, 1)[0]).str.strip()
    art['artist_nationality'] = art['artist_nationality'].map(lambda x:  'Other' if x not in (nationality_list) else x)


    # artist_begin_date
    # birth date of artist, filter to year only
    ##      if null, change to '' to allow string filters
    #       if multiple artists keep primary artist info
    #       keep only the '-' sign if it exists, then the first four digits
    #       change blanks to N/A
    art.artist_begin_date = art.artist_begin_date.fillna('')
    art['artist_begin_date'] = art['artist_begin_date'].map(lambda x: x.split(separator, 1)[0])
    art['artist_begin_date'] = art['artist_begin_date'].str.strip()
    # filter down to year only, remove invalid values, keep negative sign. 
    regexp = r'(-?\d+)'
    art['artist_begin_date'] = art['artist_begin_date'].map(lambda x: re.findall(regexp, x)[0] if x != '' else 'N/A')


    # artist_end_date
    # death date of artist (9999 for still living) 
    ##      if null, change to '' to allow string filters
    #      if multiple artists keep primary artist
    art.artist_end_date = art.artist_end_date.fillna('')
    art['artist_end_date'] = art['artist_end_date'].map(lambda x: x.split(separator, 1)[0])
    art['artist_end_date'] = art['artist_end_date'].str.strip()
    # filter down to year only, remove invalid values, keep negative sign. 
    regexp = r'(-?\d+)'
    art['artist_end_date'] = art['artist_end_date'].map(lambda x: re.findall(regexp, x)[0] if x != '' else 'N/A')

    # artist_ulan_url
    # ULAN URL for the artist     
    ##      if null, change to '' and keep only primary artist url
    ##      change to bool if artist url exists
    ##      change column name to 'has_artist_url'
    art.artist_ulan_url = art.artist_ulan_url.fillna('').map(lambda x: x.split(separator, 1)[0])
    art.artist_ulan_url = np.where(art['artist_ulan_url'].str.contains('http'), True, False)
    art.rename(columns={'artist_ulan_url':'has_artist_url'}, inplace=True)

    # artist gender
    # Gender of the artist.  Original data only contains designations for females
    ##      if null, change to 'N/A'
    ##      keep gender only for primary artist
    ##      if not N/A or Female, then Male
    ##      if id'd as N/A but there is an URL for the artist, change to male (in testing 99.99% of blank genders with url present were actually male)
    art.artist_gender = art.artist_gender.fillna('N/A')
    art['artist_gender'] = art['artist_gender'].map(lambda x: x.split(separator, 1)[0]).map(lambda x: 'Male' if x == '' else x)
    art['artist_gender'] = np.where((art['artist_gender'] == 'N/A') & (art['has_artist_url'] == True), 'Male', art['artist_gender'])

    return art
