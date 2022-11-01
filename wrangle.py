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

    
    art.drop(columns=[  'artist_prefix',
                        'object_id', 
                        'artist_display_name', 
                        'artist_display_bio',
                        'artist_suffix',
                        'object_date',
                        'object_end_date',
                        'dimensions',
                        'geography_type',
                        'city',
                        'state',
                        'county',
                        'region',
                        'subregion',
                        'locale',
                        'locus',
                        'excavation',
                        'river',
                        'rights_and_reproduction',
                        'link_resource',
                        'metadata_date',
                        'repository',
                        'tags_aat_url',
                        'tags_wikidata_url',
                        "reign",
                        "dynasty",
                        "period",
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

# 
def first_part_clean(   df,
                        consolidate_threshold=.01,
                        consolidate_list=["culture","gallery_number","object_name","credit_line","medium"],
                        group_to_decade=True,
                        dummy_columns = ['gallery_number','department','object_name',"culture","credit_line","medium"]
                    ):
    ''' 
    inputs: gonna need data frame, the rest can be left as default or modified as deemed necessary
    
    process:
            drops and object id, these are unique keys with no significance (using object number)
            cleans accessionyear, replacing nan with 0, and breaking strings into the first four (year)
                if group to decade is true, it'll floor the year and return the beginning decade number (1963 -> 1960)
            goes through gallery_number and fills nan with 0, encodes any strings to ints (starting at 1000), turns any low counts into 999
            fills object_name nan with Misc or classification if available
            fills title nan with Unknown
            turns portfolio into boolean (has or does not have)
            if consolidate list is not empyt:
                    it'll go through the list of features and turn any low values counts (threshold given) into "other") to help clean the data
            drop dynasty reign and period
            turns dummy list into dummy columns
    
    returns: modified dataframe
    '''

    ## ascension year, turning unknown into 0 so that they're not removed, may be able to impute with logical leaps/unknown value in doing so (case by case basis)
    df["accessionyear"] = df["accessionyear"].replace("NaN",0).fillna(0).astype("string").str[:4].astype(int)
    if group_to_decade:
        df["accessionyear"] = df["accessionyear"]//10*10

    # gallery number (name), placing na into none group for lack of better info. only 4 are string, remapping to encoded number
    df["gallery_number"] = df["gallery_number"].fillna(0)
    for i,each in enumerate(df[df["gallery_number"].fillna(0).astype(str).str.contains(r"[a-z]")]["gallery_number"].value_counts().index):
        #print(i,each)
        df["gallery_number"] = df["gallery_number"].replace({each:(1000+i)})
    df["gallery_number"]  = df["gallery_number"].astype(int)
    gal_count = df["gallery_number"].value_counts(normalize=True)
    idx = gal_count[gal_count.lt(consolidate_threshold)].index
    df.loc[df["gallery_number"].isin(idx), "gallery_number"] = 999
    

    ## replacing nan with misc category for object name
    df["object_name"] = np.where(df["object_name"].isna()==True,df["classification"],df["object_name"])
    df["object_name"] = df["object_name"].fillna("Misc")

    ## replacing nan with unknown for title name
    df["title"] = df["title"].fillna("Unknown")
    df.drop(columns="title",inplace=True)

    ## turning portfolio into boolean (all values seem to be individual, only 4 in target)
    df["portfolio"] = np.where(df.portfolio.isna(),False,True)

    #culture seems to be worth keeping at the moment

    ## consolidates low value counts
    if len(consolidate_list)>0:
        for each in consolidate_list:
            df[each] = df[each].fillna("Unknown")
            counts = df[each].value_counts(normalize=True)
            idx = counts[counts.lt(consolidate_threshold)].index
            df.loc[df[each].isin(idx), each] = 'Other'

    #get dummies for X subsets
    if len(dummy_columns)>0:
        temp_df = df.copy()
        df = pd.get_dummies(df, columns=dummy_columns, drop_first=False)
        ##adding columns back in for use in explore
        df = pd.concat([df,temp_df[dummy_columns]],axis=1)
    
    return df


def split_tvt_stratify(df, target):
    """
    takes in a dataframe, splits it into 60, 20, 20, 
    and seperates out the x variables and y (target) as new df/series
    """
    from sklearn.model_selection import train_test_split
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=0.2, random_state=123,stratify = df[target])

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=0.25, random_state=123,stratify = train_validate[target])

    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]

    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]

    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]

    print(f"df -> {df.shape}")
    print(f"train -> {train.shape}")
    print(f"validate -> {validate.shape}")
    print(f"test -> {test.shape}")

    return X_train, y_train, X_validate, y_validate, X_test, y_test, train, validate, test
