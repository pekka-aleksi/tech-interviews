from django.template.response import TemplateResponse
from rest_framework.decorators import api_view

from collections import deque

from sympy.parsing.sympy_parser import parse_expr

last_10_things_in_memory = deque(maxlen=30)


def domath(payload):

    try:
        resp = {val: "{}".format(parse_expr(val)) for k, val in payload.items()}
        return resp
    except Exception as e:
        print(e)
        return {}



@api_view(['GET', 'POST'])
def index(request):

    if request.method == 'POST':
        W = domath(request.POST)
        last_10_things_in_memory.append(W)

    return TemplateResponse(request, 'index.html', {'stuff': list(last_10_things_in_memory)[::-1]})
