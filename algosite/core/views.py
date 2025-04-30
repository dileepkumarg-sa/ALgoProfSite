from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
COURSES = [
    {
        'id': 1,
        'title': 'Artificial Intelligence',
        'tagline': 'Learn core AI concepts including expert systems and neural networks.',
        'instructor': 'Dr. Jane Smith',
        'duration': '4 weeks',
        'level': 'Beginner',
        'description': 'This course covers AI fundamentals with practical labs.',
        'image': 'images/ai.jpg',
    },
    {
        'id': 2,
        'title': 'Machine Learning',
        'tagline': 'Dive into supervised and unsupervised learning.',
        'instructor': 'John Doe',
        'duration': '6 weeks',
        'level': 'Intermediate',
        'description': 'Explore ML techniques using Python and libraries like Scikit-learn.',
        'image': 'images/ml.jpg',
    },
    {
        'id': 3,
        'title': 'Algorithmic Trading',
        'tagline': 'Design and test automated trading systems.',
        'instructor': 'Jane Trader',
        'duration': '5 weeks',
        'level': 'Advanced',
        'description': 'Quantitative finance meets code: build live trading systems.',
        'image': 'images/trading.jpg',
    },
]
def home(request):
    return render(request, 'core/home.html')

def aboutus(request):
    return render(request, 'core/aboutus.html')

def services(request):
    return render(request, 'core/services.html')
def courses(request):
    return render(request, 'core/courses.html', {'courses': COURSES})

def course_detail(request, course_id):
    course = next((c for c in COURSES if c['id'] == course_id), None)
    if not course:
        return render(request, '404.html', status=404)
    return render(request, 'core/course_detail.html', {'course': course})

def team(request):
    return render(request, 'core/team.html')

def products(request):
    return render(request, 'core/products.html')

def contact(request):
    return render(request, 'core/contact.html')
def services(request):
    return render(request, 'core/services.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'core/profile.html')
