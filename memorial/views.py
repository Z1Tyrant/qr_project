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
        
        # Imprimir información de depuración sobre el memorial creado
        print(f"Memorial creado: {memorial}")
        
        # Generar la URL del código QR y actualizar el modelo
        qr_code_url = generate_qr_code(memorial)
        memorial.qr_code_url = qr_code_url
        memorial.save()

        # Redirigir a la página de visualización del memorial
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