from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Memorial
from .utils import generate_qr_code

# Create your views here.
def create_memorial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Crear un nuevo memorial
        memorial = Memorial.objects.create(name=name, description=description)
        
        # Generar la URL del memorial
        memorial_url = request.build_absolute_uri(memorial.get_absolute_url())
        
        # Generar el código QR con el enlace al memorial
        qr_code_path = generate_qr_code(memorial_url)
        
        # Actualizar el modelo del memorial con la URL del código QR
        memorial.qr_code_url = qr_code_path
        memorial.save()

        return redirect('view_memorial', unique_id=memorial.unique_id)

    return render(request, 'create_memorial.html')

def view_memorial(request, unique_id):
    try:
        memorial = Memorial.objects.get(unique_id=unique_id)
        print("QR Code URL:", memorial.qr_code_url)
    except Memorial.DoesNotExist:
        # Manejar el caso en que no se encuentra el memorial
        return render(request, 'memorial_not_found.html')

    return render(request, 'view_memorial.html', {'memorial': memorial})