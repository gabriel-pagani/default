from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import json
import os


def ferias(request):
    return render(request, 'app/ferias.html')


def data_ferias(request):
    json_path = os.path.join(settings.BASE_DIR, 'data.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        return JsonResponse({'error': 'Data not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
