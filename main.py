import csv
import json
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home')
def home(request):
    return Response("Hello World")


@view_config(route_name='benford', renderer='json')
def benford(request):
    file = request.POST['csv'].file
    string = file.read().decode('utf-8')
    numbers = string.splitlines()
    count = len(numbers)
    is_brenford = True
    # first_digits = [x[0] for x in numbers]

    expected_frequency = [0.301, 0.176, 0.125,
                          0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
    actual_frequency = [0.0 for x in range(9)]
    for number in numbers:
        first_digit = int(number[0])
        actual_frequency[first_digit-1] += 1

    for i in range(9):
        actual_frequency[i] = actual_frequency[i]/count
        if (abs(actual_frequency[i]-expected_frequency[i]) > 0.02):
            is_brenford = False

    print(actual_frequency)
    response = {
        "is_brenford": is_brenford,
        "actual_frequency": actual_frequency,
        "expected_frequency": expected_frequency}

    return Response(json.dumps(response))


if __name__ == '__main__':
    with Configurator() as cnfg:
        cnfg.add_route('home', '/')
        cnfg.add_route('benford', '/benford')
        cnfg.scan()
        myApp = cnfg.make_wsgi_app()
    myServer = make_server('0.0.0.0', 8000, myApp)
    myServer.serve_forever()
