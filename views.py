from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from .forms import SignUpForm, EventForm
from .models import Event, RSVP, Category

def signup_view(request):
    # same as earlier, + send activation mail via token...
    ...

def activate(request, uidb64, token):
    ...

def is_admin(u): return u.groups.filter(name='Admin').exists()
def is_organizer(u): return u.groups.filter(name='Organizer').exists()

@login_required
@user_passes_test(is_admin)
def admin_dash(request): ...

@login_required
@user_passes_test(is_organizer)
def org_dash(request): ...

@login_required
def part_dash(request):
    events = request.user.rsvp_events.all()
    ...

@login_required
@user_passes_test(is_organizer)
def event_create(request):
    ...
@login_required
def rsvp_event(request, event_id):
    ...

def event_list(request): ...
