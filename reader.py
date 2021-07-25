import csv
#importing a standard python library, to read Comma seperated value file.

#Opening a read only copy of the csv file and saving it to a List.
with open('rms_albums.csv', 'r', newline='') as readOpen:
        csvData= list(csv.reader(readOpen))

#Using a append method to add a full row of data to the csvData List. 
def Add(id, album_title, artist, year_released): 
        if(yearChecker(year_released)):
            raise ValueError ("Enter a valid possible non-negative year.")
        if(idChecker(id)):
           raise ValueError ("Enter a valid  UUID for examples of such go to: https://www.uuidtools.com/v4")
        csvData.append([id,album_title,artist,year_released])
        return csvData

#Takes either a UUID or artist name and searches both fields for matches and 
# saves their corresponding albums to a new list. 
def Get(id):
    albums = []
    for row in csvData:
        if (row[0] == id) or (row[2] ==id):
            albums.append(row[1])
    return albums

#Requires User to input UUID, with csv column field they desire change in and the value to change it to.
def Update(id,headerToUpdate,updateValue):
    #check for correct field input and assigns corresponding column order
    if (idChecker(id)):
        raise ValueError ("Enter a valid  UUID for examples of such go to: https://www.uuidtools.com/v4")
    if headerToUpdate == "album title":
        headerToUpdate = 1
    elif headerToUpdate == "artist":
        headerToUpdate = 2
    elif headerToUpdate == "year released":
        headerToUpdate = 3
        if(yearChecker(updateValue)):
            raise ValueError ("Enter a valid possible non-negative year.")
    else:
        raise ValueError("Select a field desired to be updated this corresponds with the id choosen. \n Options include between album title, artist, or year released.")
#Compares Id column and updates value if equal to id provided
    for row in csvData:
        if(row[0] == id):
            row[headerToUpdate] = updateValue
    return csvData

# Takes UUID and searches that column for matches and deletes the row if equal.
def Delete(id):
    if(idChecker(id)):
           raise ValueError ("Enter a valid  UUID for examples of such go to: https://www.uuidtools.com/v4")
    for row in csvData:
        if row[0] == id:
            csvData.remove(row)
    return csvData

def idChecker(id):
    if (type (id) != str):
        return True
    elif (len(id) != 36):
        return True
    return False

def yearChecker(year):
    if (type (year) == str):
        if (int(year) < 0 or (int(year))>3500):
            return True
        elif (int(year) > 0 and (int(year))<3500):
             return False
    elif (type (year) == int):
        if ( year<0 or year>3500):
            return True
        else:
            return False
    else:
        return True
    

         

