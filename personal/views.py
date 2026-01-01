from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Post
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, "personal/index.html")

@login_required
def vote(request, question_id):
    """
    Handle voting for a given poll question.

    Args:
        request (HttpRequest): The incoming HTTP request.
        question_id (int): The primary key of the Question being voted on.

    Returns:
        HttpResponse: Renders the poll detail page if no choice selected,
                      or redirects to the results page if successful.
    """
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
    """
    Handle user registration using a custom user creation form.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the registration page or redirects to login upon success.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'polls/register.html', {'form': form})


def post_detail(request, post_id):
    """
    Display a single blog post detail page.

    Args:
        request (HttpRequest): The incoming HTTP request.
        post_id (int): The primary key of the Post.

    Returns:
        HttpResponse: Renders the post detail template with the post context.
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'personal/post_detail.html', {'post': post})

def blog_view(request):
    """
    Display a list of blog posts ordered by date (newest first).

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the blog template with all blog posts.
    """
    blog_posts = Post.objects.filter(post_type='blog').order_by('-date')
    return render(request, 'personal/blog.html', {'posts': blog_posts})


def index_view(request):
    """
    Display the personal index (home) page.
    """
    return render(request, 'personal/index.html')


def cv_view(request):
    """
    Display the personal CV page.
    """
    return render(request, 'personal/cv.html')


# POLL VIEWS
def polls_list(request):
    """
    Display a list of all poll questions.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the poll list template with all questions.
    """
    questions = Question.objects.all()
    return render(request, 'polls/polls_list.html', {'questions': questions})


def poll_detail(request, question_id):
    """
    Display the detail page for a single poll question.

    Args:
        request (HttpRequest): The incoming HTTP request.
        question_id (int): The primary key of the Question.

    Returns:
        HttpResponse: Renders the poll detail template with the question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/polls_detail.html', {'question': question})


def poll_results(request, question_id):
    """
    Display the results for a single poll question.

    Args:
        request (HttpRequest): The incoming HTTP request.
        question_id (int): The primary key of the Question.

    Returns:
        HttpResponse: Renders the poll results template with the question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/polls_result.html', {'question': question})