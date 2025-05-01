# dashboard/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np
from django.contrib.auth import logout

# Halaman deteksi
@login_required
def deteksi(request):
    return render(request, 'dashboard/deteksi.html', {'username': request.user.username})

# Halaman Pola Makan
@login_required
def pola_makan(request):
    return render(request, 'dashboard/pola-makan.html', {'username': request.user.username})

# Fungsi untuk hasil deteksi
@login_required
def result(request):
    # Load model dan scaler dari file .pkl
    try:
        with open('model-knn.pkl', 'rb') as model_file:
            saved_objects = pickle.load(model_file)
            model = saved_objects['model']
            scaler = saved_objects['scaler']
    except FileNotFoundError:
        return render(request, 'dashboard/deteksi.html', {
            'error': "Model tidak ditemukan. Pastikan file 'model-knn.pkl' tersedia.",
            'username': request.user.username
        })
    except KeyError:
        return render(request, 'dashboard/deteksi.html', {
            'error': "File 'model-knn.pkl' tidak valid. Pastikan model dan scaler tersimpan dengan benar.",
            'username': request.user.username
        })

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
        return render(request, 'dashboard/deteksi.html', {
            'error': "Input tidak valid. Pastikan semua nilai adalah angka.",
            'username': request.user.username
        })

    # Normalisasi input baru
    new_input = np.array([[val1, val2, val3, val4, val5, val6, val7, val8]])
    new_input_normalized = scaler.transform(new_input)

    # Melakukan prediksi dengan model KNN
    pred = model.predict(new_input_normalized)

    # Menentukan hasil prediksi
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
@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
