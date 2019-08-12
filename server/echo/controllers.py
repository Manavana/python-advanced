from protocol import make_response


def get_echo(request):
    # из объекта запроса извлекаются данные
    data = request.get('data')
    # возвращаем объект запроса, основанные на его данных: запрос, код ответа сервера, данные
    return make_response(request, 200, data)