from pymongo import MongoClient
from dateutil import parser
import gridfs
from PIL import Image
from io import BytesIO

def get_database():
 
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://..."

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list'] 

def insert():
    # Get the database
    dbname = get_database()
    collection = dbname["store_items"] # [collection name]
    expiry_date = '2025-02-04T00:00:00.000Z'
    expiry = parser.parse(expiry_date)
    item_3 = {
    "item_name" : "Bagutte",
    "quantity" : 2,
    "ingredients" : "all-purpose flour",
    "expiry_date" : expiry
    }
    collection.insert_one(item_3)
    
def load():
    # Get the database
    dbname = get_database()
    collection = dbname["store_items"] # [collection name]
    items = collection.find(limit=5)
    # # using filter attribute
    # items = collection.find(filter={"quantity":5})
    print(type(items))
    print(items)
    ## Print out item info
    for idx, item in enumerate(items):
        print(f'{idx+1}\n \
              id: {item["_id"]}\n \
              item_name: {item["item_name"]},\n \
              quantity: {item["quantity"]}\n \
              ingredients: {item["ingredients"]}\n \
              expiry_date: {item["expiry_date"]}\n')
    
    

def insert_image():
    # Get the database
    dbname = get_database()
    fs = gridfs.GridFS(dbname,"images") # (database, collection name)
    file = "cat.jpg"
    with open(file, 'rb') as f:
        contents = f.read()
    
    fs.put(contents, filename="cat")
    
def load_image():
    # Get the database
    dbname = get_database()
    fs = gridfs.GridFS(dbname,"images") # (database, collection name)
    file = fs.find_one({'filename': 'cat'})
    ## Byte data
    data = file.read()
    ## Byte data have to change image
    stream = BytesIO(data)
    image = Image.open(stream).convert("RGBA")
    stream.close()
    image.save('out.png')
    
