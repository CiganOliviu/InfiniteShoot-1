from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ImagesClient, PlatformPresentationImage


def gallery_view(request):
    template_name = "gallery/gallery_view.html"

    images_for_first_column = PlatformPresentationImage.objects.filter(column="First Column")
    images_for_second_column = PlatformPresentationImage.objects.filter(column="Second Column")
    images_for_third_column = PlatformPresentationImage.objects.filter(column="Third Column")
    images_for_fourth_column = PlatformPresentationImage.objects.filter(column="Fourth Column")

    context = {
        'images_for_first_column': images_for_first_column,
        'images_for_second_column': images_for_second_column,
        'images_for_third_column': images_for_third_column,
        'images_for_fourth_column': images_for_fourth_column,
    }

    return render(request, template_name, context)


@login_required
def personal_gallery_view(request):
    template_name = 'gallery/personal_gallery_view.html'

    images_first_column_client_query = ImagesClient.objects.filter(client=request.user, column="First Column")
    images_second_column_client_query = ImagesClient.objects.filter(client=request.user, column="Second Column")
    images_third_column_client_query = ImagesClient.objects.filter(client=request.user, column="Third Column")
    images_fourth_column_client_query = ImagesClient.objects.filter(client=request.user, column="Fourth Column")


    context = {
        'images_first_column_client_query': images_first_column_client_query,
        'images_second_column_client_query': images_second_column_client_query,
        'images_third_column_client_query': images_third_column_client_query,
        'images_fourth_column_client_query': images_fourth_column_client_query,
    }

    return render(request, template_name, context)

