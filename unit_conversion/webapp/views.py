from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse


def convert_temperature(request):
    from_unit = request.GET.get('from_unit')
    to_unit = request.GET.get('to_unit')
    value = float(request.GET.get('value'))
    print(from_unit, to_unit, value)
    if from_unit == 'C' and to_unit == 'F':
        converted_value = (value * 9/5) + 32
    elif from_unit == 'F' and to_unit == 'C':
        converted_value = (value - 32) * 5/9  
    else:
        return HttpResponse("incorrect params")
    response = {
        'input' : str(value) +' '+from_unit,
        'output': str(round(converted_value,2)) +' '+to_unit
    }
    return JsonResponse(response)

def convert_weight(request):
    from_unit = request.GET.get('from_unit')
    to_unit = request.GET.get('to_unit')
    value = float(request.GET.get('value'))
    print(from_unit, to_unit, value)
    if from_unit == 'kg' and to_unit == 'lb':
        converted_value = value * 2.20462
    elif from_unit == 'lb' and to_unit == 'kg':
        converted_value = value * 0.453592
    else:
        return HttpResponse("incorrect params")
    response = {
        'input' : str(value) +' '+from_unit,
        'output': str(round(converted_value,2)) +' '+to_unit
    }
    return JsonResponse(response)

def convert_length(request):
    from_unit = request.GET.get('from_unit')
    to_unit = request.GET.get('to_unit')
    value = float(request.GET.get('value'))
    if from_unit == 'm' and to_unit == 'ft':
        converted_value = value * 3.281
    elif from_unit == 'ft' and to_unit == 'm':
        converted_value = value * 0.3048
    else:
        return HttpResponse('incorrect params')
    response = {
        'input' : str(value) +' '+from_unit,
        'output': str(round(converted_value,2)) +' '+to_unit
    }

    return JsonResponse(response)
