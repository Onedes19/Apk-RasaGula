# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import CustomUser, EmailVerificationCode
import random

# Halaman autentikasi (login/daftar)
def auth_view(request):
    return render(request, 'accounts/auth.html')

# Fungsi untuk menghasilkan kode verifikasi secara acak
def generate_verification_code():
    return str(random.randint(100000, 999999))

# Fungsi pendaftaran pengguna baru
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validasi data input
        if not username or not email or not password:
            messages.error(request, "Semua kolom wajib diisi.")
            return redirect('auth')

        # Cek apakah username atau email sudah digunakan
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Nama pengguna sudah digunakan.")
            return redirect('auth')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email sudah terdaftar.")
            return redirect('auth')

        # Buat user baru dengan status tidak aktif
        user = CustomUser.objects.create_user(
            username=username, email=email, password=password, user_type='client')
        user.is_active = False
        user.save()

        # Buat dan simpan kode verifikasi
        code = generate_verification_code()
        EmailVerificationCode.objects.create(user=user, code=code)

        # Kirim email verifikasi
        email_subject = "Kode Verifikasi Akun - RasaGula"
        email_body = f"""
Halo {username},

Terima kasih telah mendaftar di aplikasi RasaGula.

Berikut adalah kode verifikasi akun Anda:
{code}

Jangan bagikan kode ini kepada siapa pun.
Kode ini hanya berlaku satu kali dan akan kadaluarsa setelah digunakan.

Salam hangat,  
Admin RasaGula
"""
        email_msg = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email='RasaGula Admin <rasagula27@gmail.com>',
            to=[email],
            headers={'Reply-To': 'rasagula27@gmail.com'}
        )
        email_msg.send(fail_silently=False)

        messages.success(request, "Pendaftaran berhasil. Silakan periksa email Anda untuk kode verifikasi.")
        return redirect('verify_email', user_id=user.id)

    return redirect('auth')

# Fungsi login
@csrf_exempt
def login_view(request):
    next_url = request.GET.get('next', 'dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Selamat datang, {username}!")
            return redirect(next_url)
        else:
            messages.error(request, "Nama pengguna atau kata sandi salah.")

    return render(request, 'accounts/auth.html', {'next': next_url})

# Fungsi dashboard untuk klien
def dashboard_view(request):
    if not request.user.is_authenticated or request.user.user_type != 'client':
        return redirect('login')

    return render(request, 'dashboard/deteksi.html', {'username': request.user.username})

# Fungsi verifikasi email
def verify_email_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    email_verified = False

    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            verification_code = EmailVerificationCode.objects.get(user=user, code=code)
            user.is_active = True
            user.save()
            verification_code.delete()
            login(request, user)
            email_verified = True
            messages.success(request, "Email berhasil diverifikasi. Selamat datang!")
            return redirect('dashboard')

        except EmailVerificationCode.DoesNotExist:
            messages.error(request, "Kode verifikasi tidak valid.")

    return render(request, 'accounts/verify_email.html', {'user': user, 'email_verified': email_verified})
