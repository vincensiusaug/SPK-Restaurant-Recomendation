import DBManager
import customer
cursor = DBManager.Connectdb("FlaskSite/static/database/data.db")
normal = []
berbobot = []
bobotAl = 0.1
bobotSk = 0.1
bobotDc = 0.1
bobotAcc = 0.2
bobotPrc = 0.2
bobotOa = 0.1
bobotOs = 0.2
data = []

user = customer.customer("ABC", False, True, False, -90, 23)

if user.smoking==False:
    bobotSk=0
    bobotPrc += 0.1

if user.alcohol==False:
    bobotAl=0
    bobotPrc+=0.1

if user.formal==False:
    bobotDc==0
    bobotPrc+=0.1

for row in cursor.execute("SELECT * FROM raw"):
    data.append(row)
for row in data:
    Id = row[0]
    Lat = row[1]
    Lon = row[2]
    Name = row[3]
    Al = row[4]
    Sk = row[5]
    Dc = row[6]
    Acc = row[7]
    Prc = row[8]
    Oa = row[9]
    Os = row[10]
    hasil = []
    recomendName = []
    recomendScore= []

    normal.append([Id, Lat, Lon, Name, Al/DBManager.ColoumAverage(cursor, 4), Sk/DBManager.ColoumAverage(cursor, 5), Dc/DBManager.ColoumAverage(cursor, 6), Acc/DBManager.ColoumAverage(cursor, 7), Prc/DBManager.ColoumAverage(cursor, 8), Oa/DBManager.ColoumAverage(cursor, 9), Os/DBManager.ColoumAverage(cursor, 10)])

for Id, Lat, Lon, Name, Al, Sk, Dc, Acc, Prc, Oa, Os in normal:
    berbobot.append([Id, Lat, Lon, Name, Al*bobotAl, Sk*bobotSk, Dc*bobotDc, Acc*bobotAcc, Prc*bobotPrc, Oa*bobotOa, Os*bobotOs])

for Id, Lat, Lon, Name, Al, Sk, Dc, Acc, Prc, Oa, Os in berbobot:
    hasil.append([round((Al+Sk+Dc+Acc+Prc+Oa)-Os,2), Id, Lat, Lon, Name])

def recommendation():
    a=1
    print("Solusi:")
    print("[Hasil perhitungan, Nomor sample]")
    for row in sorted(hasil, reverse=True): 
        print(row)
        recomendName.append(row[4])
        recomendScore.append(row[0])
        if a>=5:
            break
        else:
            a=a+1
    return recomendName, recomendScore