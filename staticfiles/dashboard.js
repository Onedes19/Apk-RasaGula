/*-----------------------------------*\
  dahsboard.js
\*-----------------------------------*/

// Mendapatkan semua elemen menu di sidebar
const allSideMenu = document.querySelectorAll("#sidebar .side-menu.top li a");

// Menambahkan event listener ke setiap menu untuk memberikan efek "aktif"
allSideMenu.forEach((item) => {
  const li = item.parentElement; // Mendapatkan elemen induk (li)

  item.addEventListener("click", function () {
    // Menghapus kelas "active" dari semua menu
    allSideMenu.forEach((i) => {
      i.parentElement.classList.remove("active");
    });
    // Menambahkan kelas "active" ke menu yang diklik
    li.classList.add("active");
  });
});

// TOGGLE SIDEBAR
const menuBar = document.querySelector("#content nav .bx.bx-menu"); // Tombol untuk toggle sidebar
const sidebar = document.getElementById("sidebar"); // Elemen sidebar

menuBar.addEventListener("click", function () {
  sidebar.classList.toggle("hide"); // Menyembunyikan/menampilkan sidebar
});

// SEARCH BAR BEHAVIOR
const searchButton = document.querySelector(
  "#content nav form .form-input button"
); // Tombol pencarian
const searchButtonIcon = document.querySelector(
  "#content nav form .form-input button .bx"
); // Ikon di tombol pencarian
const searchForm = document.querySelector("#content nav form"); // Form pencarian

searchButton.addEventListener("click", function (e) {
  if (window.innerWidth < 576) {
    // Jika lebar layar lebih kecil dari 576px
    e.preventDefault(); // Mencegah pengiriman form
    searchForm.classList.toggle("show"); // Menampilkan atau menyembunyikan form
    if (searchForm.classList.contains("show")) {
      searchButtonIcon.classList.replace("bx-search", "bx-x"); // Ubah ikon ke "x"
    } else {
      searchButtonIcon.classList.replace("bx-x", "bx-search"); // Ubah ikon ke "search"
    }
  }
});

// PENGATURAN RESPONSIF SIDEBAR DAN FORM
if (window.innerWidth < 768) {
  sidebar.classList.add("hide"); // Sembunyikan sidebar jika lebar layar < 768px
} else if (window.innerWidth > 576) {
  searchButtonIcon.classList.replace("bx-x", "bx-search"); // Pastikan ikon pencarian adalah "search"
  searchForm.classList.remove("show"); // Sembunyikan form pencarian
}

// Ketika ukuran layar berubah
window.addEventListener("resize", function () {
  if (this.innerWidth > 576) {
    searchButtonIcon.classList.replace("bx-x", "bx-search"); // Pastikan ikon pencarian adalah "search"
    searchForm.classList.remove("show"); // Sembunyikan form pencarian
  }
});

// SWITCH MODE (DARK MODE)
const switchMode = document.getElementById("switch-mode"); // Tombol untuk dark mode

switchMode.addEventListener("change", function () {
  if (this.checked) {
    document.body.classList.add("dark"); // Aktifkan mode gelap
  } else {
    document.body.classList.remove("dark"); // Nonaktifkan mode gelap
  }
});
