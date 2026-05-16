from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .firebase_config import get_firebase_db
from firebase_admin import exceptions


def ma_vue(request):
    return render(request, 'menu.html', {})


def details_view(request, category_name):
    context = {
        'category_name': category_name,
        'title': category_name.capitalize()
    }
    return render(request, 'details.html', context)


@csrf_exempt
def add_order_to_firebase(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            db = get_firebase_db()

            # Utilisation de la méthode pour Firebase Realtime Database
            new_order_ref = db.child('orders').push(data)

            return JsonResponse({'success': True, 'order_id': new_order_ref.key})
        
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        
        except exceptions.FirebaseError as e:
            # Gérer les erreurs spécifiques à Firebase
            print(f"Firebase Error: {str(e)}")
            return JsonResponse({'success': False, 'error': f'Firebase Error: {str(e)}'}, status=500)
        
        except Exception as e:
            # Gérer les erreurs inattendues
            print(f"An unexpected error occurred: {e}")
            error_str = str(e)
            if "database" in error_str.lower() and "does not exist" in error_str.lower():
                return JsonResponse({'success': False, 'error': 'Firestore database not set up. Please enable Firestore in your Firebase project at https://console.cloud.google.com/datastore/setup?project=bssfood-7eeec'}, status=500)
            return JsonResponse({'success': False, 'error': 'An unexpected error occurred'}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)