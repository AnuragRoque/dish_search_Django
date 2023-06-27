from django.shortcuts import render
from django.db.models import Q  # Add this line to import the Q object
from dish_search_app.models import Dish

# def search_dish(request):
#     query = request.GET.get('query', '')  # Get the search query from the request
#     dishes = Dish.objects.filter(
#         Q(id__icontains=query)
#     )  # Perform case-insensitive search by name or ID
#     dish_names = [dish.name for dish in dishes]  # Extract dish names from the query set
#     context = {'query': query, 'dishes': dish_names}
#     return render(request, 'search_dish.html', context)


def search_dish(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    dishes = Dish.objects.filter(name__icontains=query)  # Perform case-insensitive search by name
    context = {'query': query, 'dishes': dishes}
    return render(request, 'search_dish.html', context)
