# rasagula/views.py

from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np

# Fungsi untuk halaman utama
def index(request):
    return render(request, 'index.html', {})

# Fungsi untuk halaman deteksi
def deteksi(request):
    return render(request, 'dashboard/deteksi.html', {})

# Fungsi untuk memproses hasil deteksi
def result(request):
    if request.method == 'POST':  # Hanya menerima request POST
        try:
            # Load model dan scaler dari file .pkl
            with open('model-knn.pkl', 'rb') as model_file:
                saved_objects = pickle.load(model_file)
                model = saved_objects['model']
                scaler = saved_objects['scaler']
        except FileNotFoundError:
            return HttpResponse("Model tidak ditemukan. Pastikan file 'model-knn.pkl' tersedia.")
        except KeyError:
            return HttpResponse("File model tidak valid. Pastikan model dan scaler tersimpan dengan benar.")

        # Ambil nilai input dari form POST
        try:
            val1 = float(request.POST.get('n1', 0))  # Nilai 1
            val2 = float(request.POST.get('n2', 0))  # Nilai 2
            val3 = float(request.POST.get('n3', 0))  # Nilai 3
            val4 = float(request.POST.get('n4', 0))  # Nilai 4
            val5 = float(request.POST.get('n5', 0))  # Nilai 5
            val6 = float(request.POST.get('n6', 0))  # Nilai 6
            val7 = float(request.POST.get('n7', 0))  # Nilai 7
            val8 = float(request.POST.get('n8', 0))  # Nilai 8
        except ValueError:
            return HttpResponse("Input tidak valid. Pastikan semua nilai adalah angka.")

        # Buat array input baru
        input_data = np.array([[val1, val2, val3, val4, val5, val6, val7, val8]])

        # Normalisasi input baru menggunakan scaler
        try:
            input_normalized = scaler.transform(input_data)
        except Exception as e:
            return HttpResponse(f"Terjadi error saat normalisasi input: {e}")

        # Prediksi hasil menggunakan model KNN
        try:
            pred = model.predict(input_normalized)
        except Exception as e:
            return HttpResponse(f"Terjadi error saat prediksi: {e}")

        # Interpretasi hasil prediksi
        result = 'true' if pred[0] == 1 else 'false'

        # Kirim hasil prediksi dan nilai input ke template
        return render(request, 'dashboard/deteksi.html', {
            'result': result,
            'val1': val1,
            'val2': val2,
            'val3': val3,
            'val4': val4,
            'val5': val5,
            'val6': val6,
            'val7': val7,
            'val8': val8
        })

    # Tampilkan pesan jika metode request tidak valid
    return HttpResponse("Metode request tidak valid.")
