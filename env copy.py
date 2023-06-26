host = 'data.codeup.com'
username = 'pagel_2189'
password = 'RhMB57gTuvGNrIiZqljz8TrnycCx5R'

def get_db_url(db, username=username, host=host, password=password):
    """
    This function will:
    - take username, pswd, host credentials from imported env module
    - output a formatted connection_url to access mySQL db
    """
    return f'mysql+pymysql://{username }:{password}@{host}/{db}'