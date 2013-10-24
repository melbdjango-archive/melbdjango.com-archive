
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Idea, Vote
from .forms import IdeaForm, CommentForm

def idea_list(request):
    '''List all the Ideas!'''
    return render(request, 'hacks/idea_list.html', {
        'object_list': Idea.objects.all(),
    })

@login_required
def idea_add(request):
    '''Create a new Idea'''
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.owner = request.user
            idea.save()
            return redirect(idea)

    else:
        form = IdeaForm()

    return render(request, 'hacks/idea_form.html', {
        'form': form,
    })
    
def idea_detail(request, idea_id):
    '''Review an Idea'''
    idea = get_object_or_404(Idea, pk=idea_id)

    return render(request, 'hacks/idea_detail.html', {
        'object': idea,
    })

@require_POST
def idea_vote(request, idea_id, direction):
    '''Cast a vote'''
    idea = get_object_or_404(Idea, pk=idea_id)

    with transaction.commit_manually():
        try:
            vote = Vote.objects.create(user=request.user, idea=idea, value=direction)
        except IntegrityError:
            messages.warning(request, 'You can only vote once on each idea.')
            transaction.rollback()
        else:
            messages.success(request, 'You %s voted %s!' % (vote.get_value_display(), idea))
            transaction.commit()

    return redirect(idea)

def idea_comment(request, idea_id):
    '''Post a comment on an Idea'''
    idea = get_object_or_404(Idea, pk=idea_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.idea = idea
            comment.user = request.user
            comment.save()
            return redirect(idea)

    else:
        form = CommentForm()

    return render(request, 'hacks/idea_comment.html', {
        'object': idea,
        'form': form,
    })

