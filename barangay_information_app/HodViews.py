from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from barangay_information_app.models import Purok

from barangay_information_app.models import Officials

from barangay_information_app.models import CustomUser

from barangay_information_app.models import Household

from barangay_information_app.models import Staffs
from django.urls import reverse

from barangay_information_app.models import Reports

from barangay_information_app.models import Attendance


def admin_home(request):
    household_count=Household.objects.all().count()
    purok_count=Purok.objects.all().count()
    officials_count=Officials.objects.all().count()
    staff_count=Staffs.objects.all().count()

    purok_all=Purok.objects.all()
    purok_number_list=[]
    household_count_list=[]
    for purok in purok_all:
        households_count=Household.objects.filter(purok_id=purok.id).count()
        purok_number_list.append(purok.purok_number)
        household_count_list.append(households_count)

    return render(request, "hod_template/home_content.html",{"household_count":household_count,"purok_count":purok_count,"officials_count":officials_count,"staff_count":staff_count,"purok_number_list":purok_number_list,"household_count_list":household_count_list})

def add_official(request):
    return render(request, "hod_template/add_official_template.html")

def add_official_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        position = request.POST.get("position")
        contact_number = request.POST.get("contact_number")

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            official_model = Officials(last_name=last_name, first_name=first_name, middle_name=middle_name, suffix=suffix, age=age, gender=sex, position=position, contact_number=contact_number, profile_pic=profile_pic_url)
            official_model.save()
            messages.success(request, "Successfully Added Official")
            return HttpResponseRedirect("/add_official")
        except:
            messages.error(request, "Failed to Add Official")
            return HttpResponseRedirect("/add_official")


def add_purok(request):
    return render(request, "hod_template/add_purok_template.html")

def add_purok_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        purok_number = request.POST.get("purok_number")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")

        try:
            purok_model = Purok(purok_number=purok_number, last_name=last_name, first_name=first_name, middle_name=middle_name, suffix=suffix, age=age, gender=sex)
            purok_model.save()
            messages.success(request, "Successfully Added Purok")
            return HttpResponseRedirect("/add_purok")
        except:
            messages.error(request, "Failed to Add Purok")
            return HttpResponseRedirect("/add_purok")


def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Failed to Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))


def add_household(request):
    purok=Purok.objects.all()
    return render(request, "hod_template/add_household_template.html", {"purok":purok})

def add_household_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        purok_id = request.POST.get("purok")
        purok = Purok.objects.get(id=purok_id)
        place_of_birth = request.POST.get("place_of_birth")
        birthdate = request.POST.get("birthdate")
        civil_status = request.POST.get("civil_status")
        citizenship = request.POST.get("citizenship")
        occupation = request.POST.get("occupation")
        members_of_the_family = request.POST.get("members_of_the_family")

        try:
            household_model = Household(last_name=last_name, first_name=first_name, middle_name=middle_name, suffix=suffix, age=age, gender=sex, purok_id=purok, place_of_birth=place_of_birth, birthdate=birthdate, civil_status=civil_status, citizenship=citizenship, occupation=occupation, members_of_the_family=members_of_the_family)
            household_model.save()
            messages.success(request, "Successfully Added Household")
            return HttpResponseRedirect("/add_household")
        except:
            messages.error(request, "Failed to Add Household")
            return HttpResponseRedirect("/add_household")


def add_report(request):
    return render(request, "hod_template/add_report_template.html")

def add_report_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        complainant_full_name = request.POST.get("complainant_full_name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        civil_status = request.POST.get("civil_status")
        citizenship = request.POST.get("citizenship")
        occupation = request.POST.get("occupation")
        purok_number = request.POST.get("purok_number")
        address = request.POST.get("address")
        report_date = request.POST.get("report_date")
        report_message = request.POST.get("report_message")
        report_status = request.POST.get("report_status")
        defendant_full_name = request.POST.get("defendant_full_name")
        defendant_age = request.POST.get("defendant_age")
        defendant_sex = request.POST.get("defendant_sex")
        defendant_civil_status = request.POST.get("defendant_civil_status")
        defendant_citizenship = request.POST.get("defendant_citizenship")
        defendant_occupation = request.POST.get("defendant_occupation")
        defendant_purok_number = request.POST.get("defendant_purok_number")
        defendant_address = request.POST.get("defendant_address")

        try:
            report_model = Reports(complainant_full_name=complainant_full_name, age=age, gender=sex, civil_status=civil_status, citizenship=citizenship, occupation=occupation, purok_number=purok_number, address=address, report_date=report_date, report_message=report_message, report_status=report_status, defendant_full_name=defendant_full_name, defendant_age=defendant_age, defendant_gender=defendant_sex, defendant_civil_status=defendant_civil_status, defendant_citizenship=defendant_citizenship, defendant_occupation=defendant_occupation, defendant_purok_number=defendant_purok_number, defendant_address=defendant_address)
            report_model.save()
            messages.success(request, "Successfully Added Report")
            return HttpResponseRedirect("/add_report")
        except:
            messages.error(request, "Failed to Add Report")
            return HttpResponseRedirect("/add_report")


def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request, "hod_template/manage_staff_template.html", {"staffs":staffs})


def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request, "hod_template/edit_staff_template.html", {"staff":staff, "id":staff_id})

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")

        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()
            messages.success(request, "Successfully Edited Staff")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id":staff_id}))
        except:
            messages.error(request, "Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id":staff_id}))


def manage_household(request):
    household = Household.objects.all()
    return render(request, "hod_template/manage_household_template.html", {"household":household})


def edit_household(request, household_id):
    household = Household.objects.get(id=household_id)
    purok = Purok.objects.all()
    return render(request, "hod_template/edit_household_template.html", {"household":household, "purok":purok, "id":household_id})

def edit_household_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        household_id = request.POST.get("household_id")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        purok_id = request.POST.get("purok")
        purok = Purok.objects.get(id=purok_id)
        place_of_birth = request.POST.get("place_of_birth")
        birthdate = request.POST.get("birthdate")
        civil_status = request.POST.get("civil_status")
        citizenship = request.POST.get("citizenship")
        occupation = request.POST.get("occupation")
        family_unit = request.POST.get("family_unit")

        try:
            household = Household.objects.get(id=household_id)
            household.last_name = last_name
            household.first_name = first_name
            household.middle_name = middle_name
            household.suffix = suffix
            household.age = age
            household.sex = sex
            household.purok_id = purok
            household.place_of_birth = place_of_birth
            household.birthdate = birthdate
            household.civil_status = civil_status
            household.citizenship = citizenship
            household.occupation = occupation
            household.family_unit = family_unit
            household.save()
            messages.success(request, "Successfully Edited Household")
            return HttpResponseRedirect(reverse("edit_household", kwargs={"household_id":household_id}))
        except:
            messages.error(request, "Failed to Edit Household")
            return HttpResponseRedirect(reverse("edit_household", kwargs={"household_id":household_id}))


def manage_purok(request):
    purok = Purok.objects.all()
    return render(request, "hod_template/manage_purok_template.html", {"purok":purok})


def edit_purok(request, purok_id):
    purok = Purok.objects.get(id=purok_id)
    return render(request, "hod_template/edit_purok_template.html", {"purok":purok, "id":purok_id})

def edit_purok_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        purok_id = request.POST.get("purok_id")
        purok_number = request.POST.get("purok_number")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")

        try:
            purok = Purok.objects.get(id=purok_id)
            purok.purok_number = purok_number
            purok.last_name = last_name
            purok.first_name = first_name
            purok.middle_name = middle_name
            purok.suffix = suffix
            purok.age = age
            purok.sex = sex
            purok.save()
            messages.success(request, "Successfully Edited Purok")
            return HttpResponseRedirect(reverse("edit_purok", kwargs={"purok_id":purok_id}))
        except:
            messages.error(request, "Failed to Edit Purok")
            return HttpResponseRedirect(reverse("edit_purok", kwargs={"purok_id":purok_id}))


def manage_official(request):
    official = Officials.objects.all()
    return render(request, "hod_template/manage_official_template.html", {"official":official})


def edit_official(request, official_id):
    official = Officials.objects.get(id=official_id)
    return render(request, "hod_template/edit_official_template.html", {"official":official, "id":official_id})

def edit_official_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        official_id = request.POST.get("official_id")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        position = request.POST.get("position")
        contact_number = request.POST.get("contact_number")

        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            official = Officials.objects.get(id=official_id)
            official.last_name = last_name
            official.first_name = first_name
            official.middle_name = middle_name
            official.suffix = suffix
            official.age = age
            official.sex = sex
            official.position = position
            official.contact_number = contact_number
            if profile_pic_url != None:
                official.profile_pic = profile_pic_url
            official.save()
            messages.success(request, "Successfully Edited Official")
            return HttpResponseRedirect(reverse("edit_official", kwargs={"official_id":official_id}))
        except:
            messages.error(request, "Failed to Edit Official")
            return HttpResponseRedirect(reverse("edit_official", kwargs={"official_id":official_id}))


def manage_report(request):
    report = Reports.objects.all()
    return render(request, "hod_template/manage_report_template.html", {"report":report})


def edit_report(request, report_id):
    report = Reports.objects.get(id=report_id)
    return render(request, "hod_template/edit_report_template.html", {"report":report, "id":report_id})

def edit_report_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        report_id = request.POST.get("report_id")
        complainant_full_name = request.POST.get("complainant_full_name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        civil_status = request.POST.get("civil_status")
        citizenship = request.POST.get("citizenship")
        occupation = request.POST.get("occupation")
        purok_number = request.POST.get("purok_number")
        address = request.POST.get("address")
        report_date = request.POST.get("report_date")
        report_message = request.POST.get("report_message")
        report_status = request.POST.get("report_status")
        defendant_full_name = request.POST.get("defendant_full_name")
        defendant_age = request.POST.get("defendant_age")
        defendant_sex = request.POST.get("defendant_sex")
        defendant_civil_status = request.POST.get("defendant_civil_status")
        defendant_citizenship = request.POST.get("defendant_citizenship")
        defendant_occupation = request.POST.get("defendant_occupation")
        defendant_purok_number = request.POST.get("defendant_purok_number")
        defendant_address = request.POST.get("defendant_address")

        try:
            report = Reports.objects.get(id=report_id)
            report.complainant_full_name = complainant_full_name
            report.age = age
            report.sex = sex
            report.civil_status = civil_status
            report.citizenship = citizenship
            report.occupation = occupation
            report.purok_number = purok_number
            report.address = address
            report.report_date = report_date
            report.report_message = report_message
            report.report_status = report_status
            report.defendant_full_name = defendant_full_name
            report.defendant_age = defendant_age
            report.defendant_sex = defendant_sex
            report.defendant_civil_status = defendant_civil_status
            report.defendant_citizenship = defendant_citizenship
            report.defendant_occupation = defendant_occupation
            report.defendant_purok_number = defendant_purok_number
            report.defendant_address = defendant_address
            report.save()
            messages.success(request, "Successfully Edited Report")
            return HttpResponseRedirect(reverse("edit_report", kwargs={"report_id":report_id}))
        except:
            messages.error(request, "Failed to Edit Report")
            return HttpResponseRedirect(reverse("edit_report", kwargs={"report_id":report_id}))


def staff_take_attendance(request):
    return render(request, "staff_template/staff_take_attendance.html")

def staff_take_attendance_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        position = request.POST.get("position")
        contact_number = request.POST.get("contact_number")

        try:
            attendance_model = Attendance(last_name=last_name, first_name=first_name, middle_name=middle_name, suffix=suffix, age=age, gender=sex,  position=position, contact_number=contact_number)
            attendance_model.save()
            messages.success(request, "Successfully Attendance Added")
            return HttpResponseRedirect("/staff_take_attendance")
        except:
            messages.error(request, "Failed to Add Attendance")
            return HttpResponseRedirect("/staff_take_attendance")



def view_attendance(request):
    attendance = Attendance.objects.all()
    return render(request, "staff_template/view_attendance_template.html", {"attendance":attendance})


def edit_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    return render(request, "staff_template/edit_attendance_template.html", {"attendance":attendance, "id":attendance_id})

def edit_attendance_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        attendance_id = request.POST.get("attendance_id")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        suffix = request.POST.get("suffix")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        position = request.POST.get("position")
        contact_number = request.POST.get("contact_number")

        try:
            attendance = Attendance.objects.get(id=attendance_id)
            attendance.last_name = last_name
            attendance.first_name = first_name
            attendance.middle_name = middle_name
            attendance.suffix = suffix
            attendance.age = age
            attendance.sex = sex
            attendance.position = position
            attendance.contact_number = contact_number
            messages.success(request, "Successfully Edited Report")
            return HttpResponseRedirect(reverse("edit_attendance", kwargs={"report_id":attendance_id}))
        except:
            messages.error(request, "Failed to Edit Attendance")
            return HttpResponseRedirect(reverse("edit_attendance", kwargs={"attendance_id":attendance_id}))


def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"hod_template/admin_profile.html",{"user":user})

def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            # if password!=None and password!="":
            #     customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))