import sqlite3
import datetime
import urllib.request
from app.config import Config



# Connect to the SQLite database
conn = sqlite3.connect('app//app.db')
cursor = conn.cursor()


#Print all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
# Fetch the ID and URL from the database
cursor.execute("SELECT id, url, title FROM entry")
data = cursor.fetchall()
print(cursor.fetchall())

# Iterate over the data and download files
for row in data:
    file_id = row[0]
    url = row[1]
    title = row[2]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_name = f"data\\{file_id} {title} {timestamp}.txt"
    # Download the file from the URL
    try:
        # Add in the user agent header to prevent 403 error
    #url = "https://www.yesbank.in/pdf/forexcardratesenglish_pdf"
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
        'AppleWebKit/537.11 (KHTML, like Gecko) '
        'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        
        request=urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        #print(response.text)
        data = response.read()
    #    print(type(data))
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
    except Exception as e:
        print(f"Error downloading file from {url}")
        print(e)
        continue
    # Append the last_updated_string field in the database with the timestamp in new line
    cursor.execute(f"SELECT last_updated_string FROM entry WHERE id={file_id}")
    last_updated_string = cursor.fetchone()[0]
    last_updated_string = f"{last_updated_string}\n{timestamp}"
    cursor.execute(f"UPDATE entry SET last_updated_string='{last_updated_string}' WHERE id={file_id}")
    
# Commit the changes and close the database connection
conn.commit()
conn.close()
