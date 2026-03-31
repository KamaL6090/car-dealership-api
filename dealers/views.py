from django.http import JsonResponse
from .models import Dealer

# GET ALL DEALERS + FILTER BY STATE
def get_dealers(request):
    state = request.GET.get('state')

    if state:
        dealers = Dealer.objects.filter(state=state).values()
    else:
        dealers = Dealer.objects.all().values()

    return JsonResponse(list(dealers), safe=False)


# GET DEALER BY ID
def get_dealer_by_id(request, id):
    try:
        dealer = Dealer.objects.get(id=id)
        data = {
            "id": dealer.id,
            "name": dealer.name,
            "state": dealer.state,
            "city": dealer.city
        }
        return JsonResponse(data)
    except Dealer.DoesNotExist:
        return JsonResponse({"error": "Dealer not found"}, status=404)