# dashboard/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
import pickle

# Halaman deteksi
@login_required  # Dekorator untuk memastikan hanya pengguna yang login dapat mengakses halaman ini
def deteksi(request):
    # Menampilkan halaman deteksi dengan username pengguna
    return render(request, 'dashboard/deteksi.html', {'username': request.user.username})

# Halaman Pola Makan
@login_required
def pola_makan(request):
    # Menampilkan halaman pola makan dengan username pengguna
    return render(request, 'dashboard/pola-makan.html', {'username': request.user.username})

# Fungsi untuk hasil deteksi
@login_required
def result(request):
    # Path ke model KNN yang sudah disimpan
    model_path = os.path.join(os.path.dirname(__file__), 'model-knn.pkl')

    # Memastikan file model tersedia
    if not os.path.exists(model_path):
        return render(request, 'dashboard/deteksi.html', {
            'error': "Model tidak ditemukan. Pastikan file model-knn.pkl tersedia.",
            'username': request.user.username
        })

    # Load model dari file pickle
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Mendapatkan nilai input dari request
    try:
        val1 = float(request.GET.get('n1', 0))
        val2 = float(request.GET.get('n2', 0))
        val3 = float(request.GET.get('n3', 0))
        val4 = float(request.GET.get('n4', 0))
        val5 = float(request.GET.get('n5', 0))
        val6 = float(request.GET.get('n6', 0))
        val7 = float(request.GET.get('n7', 0))
        val8 = float(request.GET.get('n8', 0))
    except ValueError:
        # Jika input tidak valid, kembalikan pesan error ke template
        return render(request, 'dashboard/deteksi.html', {
            'error': "Input tidak valid. Pastikan semua nilai adalah angka.",
            'username': request.user.username
        })

    # Melakukan prediksi dengan model KNN
    try:
        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    except Exception as e:
        return render(request, 'dashboard/deteksi.html', {
            'error': f"Terjadi kesalahan saat prediksi: {e}",
            'username': request.user.username
        })

    # Menentukan hasil prediksi: 'true' jika 1, 'false' jika 0
    result = 'true' if pred[0] == 1 else 'false'

    # Mengembalikan hasil prediksi ke template
    return render(request, 'dashboard/deteksi.html', {
        'result': result,
        'username': request.user.username,
        'val1': val1,
        'val2': val2,
        'val3': val3,
        'val4': val4,
        'val5': val5,
        'val6': val6,
        'val7': val7,
        'val8': val8
    })

# Fungsi logout
from django.contrib.auth import logout
@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)  # Logout pengguna
        return redirect('login')  # Arahkan ke halaman login
    else:
        return redirect('home')  # Jika tidak login, arahkan ke halaman utama
