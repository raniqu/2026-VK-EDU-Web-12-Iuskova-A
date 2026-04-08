
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse

def get_questions():
    questions = []
    for i in range(1, 25):
        questions.append({
            'id': i,
            'title': f'Question title {i}',
            'text': f'This is the text for question {i}',
            'answers_count': i * 2,
            'tags': ['tag1', 'tag2', 'tag3'],
            'likes': i * 3,
        })
    return questions

def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def index(request):
    all_questions = get_questions()  
    page = paginate(all_questions, request, per_page=5)
    return render(request, 'questions/index.html', {'page': page})

def hot(request):
    return render(request, 'questions/hot.html')

def tag(request, tag_name):
    return render(request, 'questions/tag.html', {'tag_name': tag_name})

def question(request, question_id):
    return render(request, 'questions/question.html', {'question_id': question_id})

def ask(request):
    return HttpResponse("Страница создания вопроса (будет позже)")