from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from chat_app.models import Chat

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ChatView(View):
    def get(self, request):
        chats = Chat.objects.all().order_by('-createdAt')
        data = [
            {
                "id": chat.id,
                "name": chat.name,
                "message": chat.message,
                "createdAt": chat.createdAt.isoformat(),
            }
            for chat in chats
        ]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            body = json.loads(request.body)

            chat = Chat.objects.create(
                name=body.get("name"),
                message=body.get("message"),
            )

            return JsonResponse(
                {
                    "id": chat.id,
                    "name": chat.name,
                    "message": chat.message,
                    "createdAt": chat.createdAt.isoformat(),
                },
                status=201
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)