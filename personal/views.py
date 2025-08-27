from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Post
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/polls_detail.html', {
            'question': question,
            'error_message': "You didn't select a valid choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls_result', args=(question.id,)))


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'polls/register.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def blog_view(request):
    # Filter posts with post_type='blog' to show only blog posts
    blog_posts = Post.objects.filter(post_type='blog').order_by('-date')
    return render(request, 'personal/blog.html', {'posts': blog_posts})


def index_view(request):
    return render(request, 'personal/index.html')


def cv_view(request):
    return render(request, 'personal/cv.html')


# POLL VIEWS
def polls_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/polls_list.html', {'questions': questions})


def poll_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/polls_detail.html', {'question': question})


def poll_results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/polls_result.html', {'question': question})
