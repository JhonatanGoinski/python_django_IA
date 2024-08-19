from django.shortcuts import render
from .models import Video
from django.http import HttpResponse
from .utils import Transcricao, gerar_resumo


# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        video = request.FILES.get('video')
        

        video_upload = Video(titulo=titulo, video=video)
        video_upload.save()

        transcricao = Transcricao(video_upload.video.path)
        trascript = transcricao.transcrever()

        video_upload.transcricao = trascript
        video_upload.resumo = gerar_resumo(trascript)
        video_upload.save()
        return HttpResponse('Deu certo')
