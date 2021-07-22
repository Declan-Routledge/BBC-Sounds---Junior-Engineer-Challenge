import csv
# Requires user to input a row of data at a time. Updates the CSV file of an appended row
def Add(id, album_title, artist, year_released): 
    with open('rms_albums.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([id,album_title,artist,year_released])
    pass
#Reads the CSV file and checks both UUID and Artist column for a match and returns the albums that correspond to the users input
def Get(id):
    albums = []
    with open('rms_albums.csv', 'r', newline='') as readOpen:
        for row in csv.reader(readOpen):
            if (row[0] == id) or row[2] ==id:
                albums.append(row[1])
    return albums
#Requires User to input UUID, with csv column field they want to change and the value to change it to.
def Update(id,headerToUpdate,updateValue):
    #check for 
    if headerToUpdate == "album title":
        headerToUpdate = 1
    elif headerToUpdate == "artist":
        headerToUpdate = 2
    elif headerToUpdate == "year released":
        headerToUpdate = 3
    else:
        raise ValueError("Select a field desired to be updated this corresponds with the id choosen. \n Options include between album title, artist, or year released.")
    with open('rms_albums.csv', 'r', newline='') as readOpen:
        data= list(csv.reader(readOpen))
    with open('rms_albums.csv', 'w', newline='') as writeOpen:
        writer = csv.writer(writeOpen)
        for row in data:
            if row[0] != id:
                writer.writerow(row)
            elif(row[0] == id):
                row[headerToUpdate] = updateValue
                writer.writerow(row)
    pass

def Delete(id):
    with open('rms_albums.csv', 'r', newline='') as readOpen:
        data= list(csv.reader(readOpen))
    with open('rms_albums.csv', 'w', newline='') as writeOpen:
        writer = csv.writer(writeOpen)
        for row in data:
            if row[0] != id:
                writer.writerow(row)
    pass
        