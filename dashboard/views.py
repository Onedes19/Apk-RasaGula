# dashboard/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import pickle
import numpy as np
import pandas as pd
import os

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
    # Path file model
    model_path = os.path.join(os.path.dirname(__file__), 'model-knn.pkl')

    # Periksa apakah file model tersedia
    if not os.path.exists(model_path):
        return render(request, 'dashboard/deteksi.html', {
            'error': "Model tidak ditemukan. Pastikan file 'model-knn.pkl' tersedia.",
            'username': request.user.username
        })

    # Load model dan scaler dari file pickle
    try:
        with open(model_path, 'rb') as model_file:
            saved_objects = pickle.load(model_file)
            model = saved_objects['model']
            scaler = saved_objects['scaler']
    except KeyError:
        return render(request, 'dashboard/deteksi.html', {
            'error': "File model tidak valid. Pastikan model dan scaler tersimpan dengan benar.",
            'username': request.user.username
        })

    # Ambil nilai input dari URL (GET)
    try:
        val1 = float(request.GET.get('n1', 0))  # Jumlah Kehamilan
        val2 = float(request.GET.get('n2', 0))  # Gula Darah
        val3 = float(request.GET.get('n3', 0))  # Tekanan Darah
        val4 = float(request.GET.get('n4', 0))  # Lingkar Perut
        val5 = float(request.GET.get('n5', 0))  # Insulin
        val6 = float(request.GET.get('n6', 0))  # IMT
        val7 = float(request.GET.get('n7', 0))  # Riwayat Keluarga
        val8 = float(request.GET.get('n8', 0))  # Usia
    except ValueError:
        return render(request, 'dashboard/deteksi.html', {
            'error': "Input tidak valid. Pastikan semua nilai adalah angka.",
            'username': request.user.username
        })

    # Kolom sesuai saat training model (gunakan kapital dan spasi!)
    kolom = ['Jumlah Kehamilan', 'Gula Darah', 'Tekanan Darah', 'Lingkar Perut',
             'Insulin', 'IMT', 'Riwayat Keluarga', 'Usia']
    
    # Buat DataFrame input
    input_df = pd.DataFrame([[val1, val2, val3, val4, val5, val6, val7, val8]], columns=kolom)

    # Lakukan prediksi dan normalisasi
    try:
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)[0][1]
        probability_percent = int(round(probability * 100))

    except Exception as e:
        return render(request, 'dashboard/deteksi.html', {
            'error': f"Terjadi kesalahan saat memproses prediksi: {e}",
            'username': request.user.username
        })

    result = 'true' if prediction[0] == 1 else 'false'

    return render(request, 'dashboard/deteksi.html', {
        'result': result,
        'probability': probability_percent,
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
