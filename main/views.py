from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    context = None
    if request.method == 'POST':
        mensagemRetorno = 'E-mail enviado com sucesso!'

        destino = request.POST.get('destino')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        try:
            send_mail(assunto, mensagem, 'meuemail@email.com', [destino], fail_silently=False,)
        except:
            mensagemRetorno = 'Falha ao enviar e-mail'

        context = {
            'mensagem': mensagemRetorno,
        }

    return render(request, 'index.html', context=context)