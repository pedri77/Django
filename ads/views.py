from django.shortcuts import render

from ads.models import Ad


def home(request):
    # 1) Obtener los anuncios de la base de datos que están en estado Publicado
    published_ads = Ad.objects.filter(status=Ad.PUBLISHED)
    ads_list = published_ads[:4]

    # 2) Pasar los anuncios a la plantilla para que ésta los muestre en HTML
    context = {'ads': ads_list}
    return render(request, 'ads/home.html', context)
