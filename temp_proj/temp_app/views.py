from django.shortcuts import render
from django.http import HttpResponse



def info_view(request):
    context = {
        'name': 'გიორგი',
        'surname': 'გელაშვილი',
        'age': 18,
        'height': 180
    }
    return render(request, 'info.html', context)

def hobbies_view(request):
    context = {
        'hobbies': ['reading', 'coding', 'gaming'],
        'grade': 12
    }
    return render(request, 'hobbies.html', context)

