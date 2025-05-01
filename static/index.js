/*-----------------------------------*\
  index.js
\*-----------------------------------*/

"use strict";

/**
 * menambahkan event listener ke beberapa elemen
 */

/** Fungsi untuk menambahkan event listener ke beberapa elemen */
const addEventOnElements = function (elements, eventType, callback) {
  for (let i = 0, len = elements.length; i < len; i++) {
    elements[i].addEventListener(eventType, callback);
  }
};

/**
 * PRELOADER
 *
 * preloader akan terlihat sampai dokumen selesai dimuat
 */

/** PRELOADER: Menampilkan preloader hingga halaman selesai dimuat */
const preloader = document.querySelector("[data-preloader]");

window.addEventListener("load", function () {
  preloader.classList.add("loaded");
  document.body.classList.add("loaded");
});

/**
 * NAVBAR MOBILE
 *
 * menampilkan navbar mobile saat tombol menu diklik
 * dan menyembunyikan setelah tombol tutup menu atau overlay diklik
 */

/** NAVBAR MOBILE: Mengatur tampilan navbar di layar kecil */
const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNav = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
};

addEventOnElements(navTogglers, "click", toggleNav);

/**
 * HEADER & TOMBOL KEMBALI KE ATAS
 *
 * mengaktifkan header & tombol kembali ke atas ketika jendela digulir ke bawah 100px
 */

/** HEADER & TOMBOL KEMBALI KE ATAS: Aktivasi elemen saat scroll */
const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeElementOnScroll = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
};

window.addEventListener("scroll", activeElementOnScroll);

/**
 * SCROLL REVEAL
 */

/** SCROLL REVEAL: Animasi elemen saat scroll */
const revealElements = document.querySelectorAll("[data-reveal]");

const revealElementOnScroll = function () {
  for (let i = 0, len = revealElements.length; i < len; i++) {
    if (
      revealElements[i].getBoundingClientRect().top <
      window.innerHeight / 1.15
    ) {
      revealElements[i].classList.add("revealed");
    } else {
      revealElements[i].classList.remove("revealed");
    }
  }
};

window.addEventListener("scroll", revealElementOnScroll);

window.addEventListener("load", revealElementOnScroll);

/** Fungsi untuk mengganti istilah ke 'gejala' di konten */
document.getElementById("gejala-btn").addEventListener("click", () => {
  document.getElementById("gejala-btn").classList.add("active");
  document.getElementById("faktor-btn").classList.remove("active");
  document.getElementById("pencegahan-btn").classList.remove("active");
  let aboutChange = document.getElementById("about-change");
  let html = aboutChange.innerHTML;

  // Mengganti istilah tertentu
  html = html.replace(/faktor risiko|pencegahan/g, "gejala");
  html = html.replace(
    /Pola makan tidak sehat|Berolahraga/g,
    "Rasa haus yang berlebihan"
  );
  html = html.replace(
    /Obesitas atau berat badan berlebih|Menjaga berat badan ideal/g,
    "Sering buang air kecil"
  );
  html = html.replace("Riwayat keluarga", "Kelelahan yang berlebihan");
  html = html.replace("Manajemen stres", "Kelelahan yang berlebihan");
  html = html.replace(
    /Kurangnya aktivitas fisik|Cek kesehatan secara berkala/g,
    "Nafsu makan yang berlebihan"
  );

  aboutChange.innerHTML = html; // Perbarui konten HTML dengan perubahan
});

/** Fungsi untuk mengganti istilah ke 'faktor risiko' di konten */
document.getElementById("faktor-btn").addEventListener("click", () => {
  document.getElementById("gejala-btn").classList.remove("active");
  document.getElementById("faktor-btn").classList.add("active");
  document.getElementById("pencegahan-btn").classList.remove("active");

  let aboutChange = document.getElementById("about-change");
  let html = aboutChange.innerHTML;

  // Mengganti istilah tertentu
  html = html.replace(/gejala|pencegahan/g, "faktor risiko");
  html = html.replace(
    /Rasa haus yang berlebihan|Berolahraga/g,
    "Pola makan tidak sehat"
  );
  html = html.replace(
    /Sering buang air kecil|Menjaga berat badan ideal/g,
    "Obesitas atau berat badan berlebih"
  );
  html = html.replace("Kelelahan yang berlebihan", "Riwayat keluarga");
  html = html.replace("Manajemen stres", "Riwayat keluarga");
  html = html.replace(
    /Nafsu makan yang berlebihan|Cek kesehatan secara berkala/g,
    "Kurangnya aktivitas fisik"
  );

  aboutChange.innerHTML = html; // Perbarui konten HTML dengan perubahan
});

/** Fungsi untuk mengganti istilah ke 'pencegahan' di konten */
document.getElementById("pencegahan-btn").addEventListener("click", () => {
  document.getElementById("gejala-btn").classList.remove("active");
  document.getElementById("faktor-btn").classList.remove("active");
  document.getElementById("pencegahan-btn").classList.add("active");
  let aboutChange = document.getElementById("about-change");
  let html = aboutChange.innerHTML;

  // Mengganti istilah tertentu
  html = html.replace(/faktor risiko|gejala/g, "pencegahan");
  html = html.replace(
    /Pola makan tidak sehat|Rasa haus yang berlebihan/g,
    "Berolahraga"
  );
  html = html.replace(
    /Obesitas atau berat badan berlebih|Sering buang air kecil/g,
    "Menjaga berat badan ideal"
  );
  html = html.replace(
    /Riwayat keluarga|Kelelahan yang berlebihan/g,
    "Manajemen stres"
  );
  html = html.replace(
    /Kurangnya aktivitas fisik|Nafsu makan yang berlebihan/g,
    "Cek kesehatan secara berkala"
  );

  aboutChange.innerHTML = html; // Perbarui konten HTML dengan perubahan
});

// Memilih semua tombol dengan class 'btn-text title-lg'
var btn1 = document.getElementById("a-href1");

/** Menangani tampilan popup dan efek blur pada halaman */
btn1.addEventListener("click", function (event) {
  event.preventDefault(); // Mencegah aksi default dari link

  // Menampilkan popup container
  var popupContainer = document.getElementById("popupContainer1");
  popupContainer.style.display = "flex";

  // Memburamkan body
  document.body.classList.add("active_blur");
});

var btn2 = document.getElementById("a-href2");
btn2.addEventListener("click", function (event) {
  event.preventDefault(); // Mencegah aksi default dari link

  // Menampilkan popup container
  var popupContainer = document.getElementById("popupContainer2");
  popupContainer.style.display = "flex";

  // Memburamkan body
  document.body.classList.add("active_blur");
});

var btn3 = document.getElementById("a-href3");
btn3.addEventListener("click", function (event) {
  event.preventDefault(); // Mencegah aksi default dari link

  // Menampilkan popup container
  var popupContainer = document.getElementById("popupContainer3");
  popupContainer.style.display = "flex";

  // Memburamkan body
  document.body.classList.add("active_blur");
});

/** Fungsi untuk menutup popup dan menghapus efek blur */
function closePopup(id) {
  var popupContainer = document.getElementById("popupContainer" + id);
  popupContainer.style.display = "none";

  // Menghapus efek blur dari body
  document.body.classList.remove("active_blur");
}
