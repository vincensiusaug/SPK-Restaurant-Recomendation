def Connectdb(database):
    import sqlite3
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return cursor

def ColoumAverage(cursor, field):
    import math
    data = []
    for row in cursor.execute("SELECT * FROM raw"):
        data.append(row[field]**2)
    normal = sum(data)
    normal = math.sqrt(normal)
    return normal
    
def maxkolom(ColIndex, data):
    temp=[]
    for row in data:
        temp.append(row[ColIndex])
    return max(temp)

def minkolom(ColIndex, data):
    temp=[]
    for row in data:
        temp.append(row[ColIndex])
    return min(temp)

def dbarray(cursor, data):
    for row in cursor.execute("SELECT * FROM Input"):
        data.append([row[0], row[1], row[2], row[3], row[4]])
    return data