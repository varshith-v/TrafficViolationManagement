from django.shortcuts import render
import mysql.connector as mysql

def vehicleRegPage(request):
    return render(request,'vehicle registration.html')

# Create your views here.
def registerVehicle(request):
    db = mysql.connect(
    host = "localhost",
    user = "remote",
    passwd = "tekSystems",
    database = "traffic"
    )
    cursor = db.cursor()

    query = "INSERT INTO vehicle (reg_no, owner, brand, model, date, address) VALUES (%s, %s, %s, %s, %s, %s)"

    owner = request.POST.get('owner')
    address = request.POST.get('address')
    brand = request.POST.get('brand')
    model = request.POST.get('model')
    date = request.POST.get('date')
    reg_no = request.POST.get('reg_no')
    values = (reg_no, owner, brand, model, date, address)

    cursor.execute(query, values)

    db.commit()

    print(cursor.rowcount,"record inserted")
    return render(request,'vehicle registration.html')