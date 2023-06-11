from django.shortcuts import render

# Create your views here.

def Student(request):
    student = [
        {'name': 'Raul Rufo', 'desc': 'Maestría en Pelos Excéntricos'},
        {'name': 'Herson', 'desc': 'Padre Esquizofrénico'},
        {'name': 'Joan', 'desc': 'Mr. RAE y Biólogo'},
        {'name': 'Mitchel', 'desc': '¿Bueno es él?'},
        {'name': 'Kevin', 'desc': 'Se dice que le dieron su propia mesa en McDonald\'s'},
        {'name': 'Barbara', 'desc': 'Sigue trabajando'},
    ]

    context = {'student': student}
    return render(request, 'student.html', context)

def Teacher(request):
    prof = [
        {'name': 'John Cena', 'clss': 'Gimnasio', 'age': '46'},
        {'name': 'Chuck Norris', 'clss': 'Defensa Personal', 'age': 'Creador del universo'},
        {'name': 'Barney Stinson', 'clss': 'Cómo vestirse elegante 101', 'age': '30'},
        {'name': 'Michael Scott', 'clss': 'Negocios', 'age': '40'},
        {'name': 'Sheldon Cooper', 'clss': 'Física', 'age': '30'},
        {'name': 'Walter White', 'clss': 'Química', 'age': '50'},
        {'name': 'Gandalf el Gris', 'clss': 'Magia', 'age': '?'},
        {'name': 'Yoda', 'clss': 'La Fuerza', 'age': '+900'},
        {'name': 'Drácula', 'clss': 'Vampirismo', 'age': 'mas años que mi vecina'},
    ]

    context = {'th': prof}
    return render(request, 'teacher.html', context)
