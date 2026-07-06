from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator


# ------------------------
# Login View
# ------------------------
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("student_list")
    return render(request, "students/login.html", {"form": form})


# ------------------------
# Logout View
# ------------------------
def logout_view(request):
    logout(request)
    return redirect("login")


# ------------------------
# Student List
# ------------------------
@login_required
def student_list(request):
    search = request.GET.get("search")
    if search:
        student_list = Student.objects.filter(name__icontains=search)
    else:
        student_list = Student.objects.all()
    paginator = Paginator(student_list, 2)  # 2 students per page
    page_number = request.GET.get("page")
    students = paginator.get_page(page_number)
    return render(request, "students/student_list.html", {
        "students": students
    })


# ------------------------
# Add Student
# ------------------------
@login_required
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST["name"],
            roll_no=request.POST["roll_no"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            course=request.POST["course"],
        )
        return redirect("student_list")
    return render(request, "students/add_student.html")


# ------------------------
# Edit Student
# ------------------------
@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST["name"]
        student.roll_no = request.POST["roll_no"]
        student.email = request.POST["email"]
        student.phone = request.POST["phone"]
        student.course = request.POST["course"]
        student.save()
        return redirect("student_list")
    return render(request,"students/edit_student.html",{"student": student},)


# ------------------------
# Delete Student
# ------------------------
@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")




def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "students/register.html", {"form": form})


@login_required
def profile(request):
    return render (request , 'accounts/profile.html')


@login_required
def edit_profile(request):
    if request.method =="POST":
        user=request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        user.save()
        return redirect("profile")
    return render(request,'accounts/edit_profile.html')