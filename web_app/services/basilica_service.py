
from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()



BASILICA_API_KEY= os.getenv('BASILICA_API_KEY', default='la macate')

def basilica_api_client():
    connection = Connection(BASILICA_API_KEY)
    print(type(connection)) #> <class 'basilica.Connection'>
    return connection







