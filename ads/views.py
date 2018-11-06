from django.shortcuts import render

from ads.models import Ad


def home(request):
    # 1) Obtener los anuncios de la base de datos que están en estado Publicado
    ads_list = Ad.objects.filter(status=Ad.PUBLISHED)

    # 2) Pasar los anuncios a la plantilla para que ésta los muestre en HTML
    context = {'ads': ads_list}
    return render(request, 'ads/home.html', context)
