from django.http import HttpResponse
from django.shortcuts import render

from ads.models import Ad


def home(request):
    # 1) Obtener los anuncios de la base de datos que están en estado Publicado
    published_ads = Ad.objects.filter(status=Ad.PUBLISHED).order_by('-last_modification')
    ads_list = published_ads[:4]

    # 2) Pasar los anuncios a la plantilla para que ésta los muestre en HTML
    context = {'ads': ads_list}
    return render(request, 'ads/home.html', context)


def ad_detail(request, ad_id):
    try:
        ad = Ad.objects.get(id=ad_id)
        context = {'ad': ad}
        return render(request, 'ads/ad_detail.html', context)
    except Ad.DoesNotExist:
        return HttpResponse('Ad not found', status=404)
