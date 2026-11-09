from django.shortcuts import render
from django.http import JsonResponse
from .models import TutorProfile

def index_page(request):
    return render(request, 'index.html')

def tutors_api(request):
    subject_filter = request.GET.get('subject', '')
    if subject_filter:
        tutors = TutorProfile.objects.filter(subjects__title__icontains=subject_filter)
    else:
        tutors = TutorProfile.objects.all()
        
    data = []
    for t in tutors:
        # Збираємо всі назви предметів репетитора в один список
        subjects_list = [sub.title for sub in t.subjects.all()]
        
        data.append({
            'name': f"{t.user.first_name} {t.user.last_name}",
            'education': t.education,
            'experience': t.experience,
            'bio': t.bio,
            'price': float(t.price_per_hour),
            'subjects': subjects_list  # Передаємо предмети на фронтенд
        })
        
    return JsonResponse(data, safe=False)
