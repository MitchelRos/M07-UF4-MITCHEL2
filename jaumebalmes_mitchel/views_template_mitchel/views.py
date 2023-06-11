from django.shortcuts import render
from .form import ClasesForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Listas de alumnos y profrsores
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
