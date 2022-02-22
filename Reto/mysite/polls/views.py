from urllib import request
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.core.mail import send_mail

#no anda
#from celery import Celery
#from celery.schedules import crontab

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from .models import Choice, Question, User

#no anda
#app = Celery()
#mandar = False

def send_email(email):
    context = {'mail' : email}

    template = get_template('polls/correo.html')
    content = template.render(context)
    envio = EmailMultiAlternatives(
        'Un correo de prueba',
        'codigo facil',
        settings.EMAIL_HOST_USER,
        [email]
    )
    envio.attach_alternative(content, 'text/html')
    envio.send()

#@app.on_after_configure.connect
#def setup_periodic_tasks(sender, **kwargs):
#    sender.add_periodic_task(
#        10,
#        noPhoneSendMessage.s()
#       ,name='probar'
#       )

def noPhoneSendMessage():
    if(True):
        users = User.objects.filter(telefono="")
        for user in users:
            mail = user.email
            send_email(mail)
    
    

def mail_func(request):
    print(request.method)
    if request.method == 'POST':
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        if(mail):
            send_email(mail)
        elif(phone):
            noPhoneSendMessage()
            mandar = True

    return render(request, 'polls/mail.html',{})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

