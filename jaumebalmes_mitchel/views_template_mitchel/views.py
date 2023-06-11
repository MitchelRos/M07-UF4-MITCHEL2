from django.shortcuts import get_object_or_404, redirect, render
from .form import ClasesForm
from .models import Clases


# Create your views here.
def home(request):
    return render(request, 'home.html')

# Listas de alumnos y profrsores para ejercicios anteriorer
students = [
    {'id': 1, 'name': 'Raul Rufo', 'desc': 'Maestría en Pelos Excéntricos'},
    {'id': 2, 'name': 'Herson', 'desc': 'Padre Esquizofrénico'},
    {'id': 3, 'name': 'Joan', 'desc': 'Mr. RAE y Biólogo'},
    {'id': 4, 'name': 'Mitchel', 'desc': '¿Bueno es él?'},
    {'id': 5, 'name': 'Kevin', 'desc': 'Se dice que le dieron su propia mesa en McDonald\'s'},
    {'id': 6, 'name': 'Barbara', 'desc': 'Sigue trabajando'},
]

profs = [
    {'id': 1, 'name': 'John Cena', 'clss': 'Gimnasio', 'age': '46'},
    {'id': 2, 'name': 'Chuck Norris', 'clss': 'Defensa Personal', 'age': 'Creador del universo'},
    {'id': 3, 'name': 'Barney Stinson', 'clss': 'Cómo vestirse elegante 101', 'age': '30'},
    {'id': 4, 'name': 'Michael Scott', 'clss': 'Negocios', 'age': '40'},
    {'id': 5, 'name': 'Sheldon Cooper', 'clss': 'Física', 'age': '30'},
    {'id': 6, 'name': 'Walter White', 'clss': 'Química', 'age': '50'},
    {'id': 7, 'name': 'Gandalf el Gris', 'clss': 'Magia', 'age': '?'},
    {'id': 8, 'name': 'Yoda', 'clss': 'La Fuerza', 'age': '+900'},
    {'id': 9, 'name': 'Drácula', 'clss': 'Vampirismo', 'age': 'mas años que mi vecina'},
]


# Lista y detalles de los alumnos
def Student(request):
    context = {'students': students}
    return render(request, 'student.html', context)

def student_info(request, student_id):
    # desde la lista global recojo info
    selected_student = None
    for student in students:
        if student['id'] == student_id:
            selected_student = student
            break

    context = {'student': selected_student, 'title': 'Student'}
    return render(request, 'detail-student.html', context)

# Lista y detalles de los profesores
def Teacher(request):
    context = {'profs': profs}
    return render(request, 'teacher.html', context)


def teacher_info(request, teacher_id):
    # Buscar el profesor seleccionado en la lista
    selected_teacher = None
    for teacher in profs:
        if teacher['id'] == teacher_id:
            selected_teacher = teacher
            break

    context = {'teacher': selected_teacher, 'title': 'Teacher'}
    return render(request, 'detail-teacher.html', context)

# Form de clases
def clases_form(request):
    form = ClasesForm()
    context = {'form':form}
    return render(request, 'form.html', context)

# ----------------------------------------------------------------------------
# ------------------------------- C - R - U - D ------------------------------
# ----------------------------------------------------------------------------

#-----------------R E A D-----------------
# Read all items
def list_clases(request):
    clases = Clases.objects.all()
    context = {'clases': clases}
    return render(request, 'clases.html', context)
# read 1 item
def clase_info(request, clase_id):
    clase = get_object_or_404(Clases, id=clase_id)
    return render(request, 'clase-info.html', {'clase': clase})

#----------------C R E A T E--------------
def add_clase(request):
    if request.method == 'POST':
        form = ClasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clases')
    else:
        form = ClasesForm()
    return render(request, 'clases_form.html', {'form': form})

#----------------U P D A T E--------------
def update_clase(request, clase_id):
    clase = get_object_or_404(Clases, id=clase_id)
    form = ClasesForm(request.POST or None, instance=clase)
    if form.is_valid():
        form.save()
        return redirect('list_clases')
    return render(request, 'clases_form-edit.html', {'form': form})

#----------------D E L E T E--------------
def delete_clase(request, clase_id):
    clase = get_object_or_404(Clases, id=clase_id)
    if request.method == 'POST':
        clase.delete()
        return redirect('list_clases')
    return render(request, 'clases_del-confirm.html', {'clase': clase})