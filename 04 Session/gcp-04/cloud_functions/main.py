import functions_framework
import random

@functions_framework.http
def f_choose_physical_activity(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    random_activity = random.randint(0, 1)

    dict_activity = {0: 'sports', 1: 'fun'}
    random_number = random.randint(0, 3)
    activities = {'sports': ['futbol', 'running', 'surf', 'tenis'], 'fun': ['cine', 'restaurant', 'teatro', 'spa']}

    if request_json and 'activity' in request_json:
        return activities[request_json['activity']][random_number]
    elif request_args and 'activity' in request_args:
        return activities[request_args['activity']][random_number]
    else:
        return activities[dict_activity[random_activity]][random_number]