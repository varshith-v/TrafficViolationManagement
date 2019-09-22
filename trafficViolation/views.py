from django.shortcuts import render
import trafficViolation.database as db

# Create your views here.
def index(request):
    return render(request,'main.html')

def aboutus(request):
    return render(request,'aboutus.html')

def service(request):
    return render(request,'service.html')

def user_login(request):
    return render(request,'user_login.html')

def official_login(request):
    return render(request,'official_login.html')

def dlRegister(request):
    phNo = request.POST.get('phNo')
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    address = request.POST.get('address')
    categories_list = request.POST.getlist('category')
    categories = ','.join(categories_list)
    connection = db.get_connection()
    cursor = connection.cursor()

    cursor.execute('select DrivingLicenceNumber from drivinglicence order by id DESC limit 1')
    last_record = cursor.fetchone()

    dl_no = 'KA09 '+str(int(last_record[0][5:])+1)

    query = "Insert into drivinglicence(`DrivingLicenceNumber`, `Name`, `DateOfBirth`, `Address`, `PhoneNumber`, `Categories`) values(%s,%s,%s,%s,%s,%s)"
    values = (dl_no, name, dob, address, phNo, categories)

    cursor.execute(query,values)
    connection.commit()
    cursor.close()
    connection.close()
    return render(request,'result.html',{'result':'1 record successfully inserted'})