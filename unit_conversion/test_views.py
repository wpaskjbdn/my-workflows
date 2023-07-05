import pytest
from django.urls import reverse
from django.test import RequestFactory
from webapp.views import convert_temperature, convert_weight, convert_length
# from django.conf import settings
# import unit_conversion.settings
import os
import django
import json
# settings.configure(**vars(unit_conversion.settings))

os.environ.setdefault('DJANGO_SETTINGS_MODULE','unit_conversion.settings')
django.setup()

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def convert_temperature_url():
    return reverse('temperature_conversion')

@pytest.fixture
def convert_weight_url():
    return reverse('weight_conversion')

@pytest.fixture
def convert_length_url():
    return reverse('length_conversion')

@pytest.mark.parametrize('from_unit, to_unit, value, expected_output', [
    ('C', 'F', 0, '32.0 F'),
    ('F', 'C', 32, '0.0 C'),
    ('C', 'F', 100, '212.0 F'),
    ('F', 'C', -40, '-40.0 C'),
])
def test_convert_temperature(request_factory, convert_temperature_url, from_unit, to_unit, value, expected_output):
    request = request_factory.get(convert_temperature_url, {'from_unit': from_unit, 'to_unit': to_unit, 'value': value})
    response = convert_temperature(request)
    assert response.status_code == 200
    json_data = json.loads(response.content.decode('utf-8'))
    output = json_data['output']
    assert float(expected_output.split()[0]) == pytest.approx(float(expected_output.split()[0]), abs=0.01)
    assert output.split()[1] == expected_output.split()[1]

@pytest.mark.parametrize('from_unit, to_unit, value, expected_output', [
    ('kg', 'lb', 1, '2.20 lb'),
    ('lb', 'kg', 2.20462, '1.0 kg'),
    ('kg', 'lb', 10, '22.05 lb'),
    ('lb', 'kg', 22.0462, '10.0 kg'),
])
def test_convert_weight(request_factory, convert_weight_url, from_unit, to_unit, value, expected_output):
    request = request_factory.get(convert_weight_url, {'from_unit': from_unit, 'to_unit': to_unit, 'value': value})
    response = convert_weight(request)
    assert response.status_code == 200
    json_data = json.loads(response.content.decode('utf-8'))
    output = json_data['output']
    assert float(output.split()[0]) == pytest.approx(float(expected_output.split()[0]), abs=0.01)
    assert output.split()[1] == expected_output.split()[1]

@pytest.mark.parametrize('from_unit, to_unit, value, expected_output', [
    ('m', 'ft', 1, '3.28 ft'),
    ('ft', 'm', 3.281, '1.0 m'),
    # ('m', 'ft', 5, '16.40 ft'),
    ('ft', 'm', 16.40, '5.0 m'),
])
def test_convert_length(request_factory, convert_length_url, from_unit, to_unit, value, expected_output):
    request = request_factory.get(convert_length_url, {'from_unit': from_unit, 'to_unit': to_unit, 'value': value})
    response = convert_length(request)
    assert response.status_code == 200
    json_data = json.loads(response.content.decode('utf-8'))
    output = json_data['output']
    assert float(output.split()[0]) == pytest.approx(float(expected_output.split()[0]), abs=0.01)
    assert output.split()[1] == expected_output.split()[1]
