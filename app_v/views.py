from django.shortcuts import render
import mysql.connector as mysql

def vehicleRegPage(request):
    return render(request,'vehicle registration.html')

def loginPage(request):
    return render(request,'official_login.html')

# Create your views here.
def registerVehicle(request):
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "trafficViolation"
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

def authOfficer(request):
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "trafficviolation"
    )
    cursor = db.cursor()
    
    inputID = request.POST.get('id')
    inputPassword = request.POST.get('password')
    
    query = "SELECT * FROM official_login WHERE id = %s"
    
    values = (inputID,)
    cursor.execute(query,values)
    
    # if not cursor.rowcount:
    #     print('Invalid id')
    #     return render(request, 'official_login.html', {'fail': True})


    for row in cursor:
        if row[1] == inputPassword:
            return render(request,'loggedin.html')
        else:
            return render(request, 'official_login.html', {'fail': True})
        
    return render(request, 'official_login.html', {'fail': True})

def searchVehicle(request):
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "trafficViolation"
    )
    cursor = db.cursor()
    regNo = request.POST.get('reg_no')
    
    query = "SELECT * FROM vehicle WHERE reg_no = %s"
    
    values = (regNo,)
    cursor.execute(query,values)
    

    for row in cursor:
        return render(request, 'search.html',{'reg_no': row[0],'owner': row[1],'brand': row[2],'model': row[3],'date': row[4],'address': row[5]})
        
    return render(request, 'search.html', {'fail': True})


def authUser(request):
    db = mysql.connect(
    host = "localhost",
    user = "remote",
    passwd = "tekSystems",
    database = "traffic"
    )
    cursor = db.cursor()
    
    inputID = request.POST.get('id')
    inputPassword = request.POST.get('password')
    
    query = "SELECT * FROM user WHERE dl_number = %s"
    
    values = (inputID,)
    cursor.execute(query,values)
    
    # if not cursor.rowcount:
    #     print('Invalid id')
    #     return render(request, 'official_login.html', {'fail': True})


    for row in cursor:
        if row[3] == inputPassword:
            return render(request,'loggedin.html')
        else:
            return render(request, 'user_login.html', {'fail': True})
        
    return render(request, 'user_login.html', {'fail': True})



def searchDL(request):
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "trafficViolation"
    )
    cursor = db.cursor()
    dlNo = request.POST.get('dl_no')
    
    query = "SELECT * FROM drivinglicence WHERE drivinglicencenumber = %s"
    
    values = (dlNo,)
    cursor.execute(query,values)
    

    for row in cursor:
        return render(request, 'search.html',{'dlno': row[0],'name': row[1],'dob': row[2],'addr': row[3],'phone': row[4],'categ': row[5]})
        
    return render(request, 'search.html', {'fail': True})

def home(request):
    return render(request,'main.html')

def searchPage(request):
    return render(request,'search.html')

def dlRegPage(request):
    return render(request,'dlregister.html')

def userRegPage(request):
    return render(request,'user_reg.html')

def searchCompPage(request):
    return render(request,'searchComplaints.html')

def searchComplaints(request):
    return render(request,'searchComplaints.html')
    