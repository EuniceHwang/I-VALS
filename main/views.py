from django.shortcuts import render
from .models import Question, Type, Choice

def index(request):
    types = Type.objects.all()
    
    context = {
        'types': types,
    }
    
    return render(request, 'index.html', context=context)


def form(request):
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }
    
    return render(request, 'form.html', context)

def result(request):
    
    # 문항 수
    N = Question.objects.count()
    # 타입 갯수
    K = Type.objects.count()
    
    # 타입마다 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)
    
    for n in range(1, N+1):
        type_id = int(request.POST[f'question-{n}'][0])
        print(type_id)
        counter[type_id] += 1
    
    # 최고점 타입
    best_type_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_type = Type.objects.get(pk=best_type_id)
    best_type.count += 1
    best_type.save()
    
    context = {
        'type': best_type,
        'counter': counter
    }
    
    return render(request, 'result.html', context)