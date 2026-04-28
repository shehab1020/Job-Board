from django.http import JsonResponse


def handler404(request, exception):
    message = "path not found"
    response = JsonResponse(data={"msg":message})
    response.status_code = 404
    return response