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

def lodge_complaint(request):
    complaints_dict = {"Driving without DL":500,"Not Wearing seat Belt":100,"Wrong parking":100,"Jumping Traffic Signals":100,
                  "Drunken Driving":500,"Triple Riding":100,"No Entry Violation":100,"Rider without Helmet":100,"Pillion Without Helmet":100,"Over Speeding":100}
    reg_num = request.POST.get('regnum')
    date = request.POST.get('date')
    place = request.POST.get('place')
    time = request.POST.get('time')
    violation = request.POST.get('cars')

    connection = db.get_connection()
    cursor = connection.cursor()
    
    query


