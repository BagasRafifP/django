from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse(
        """
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bagas | Tech Student</title>

<script src="https://cdn.tailwindcss.com"></script>

</head>

<body class="bg-slate-950 text-white scroll-smooth overflow-x-hidden">

<!-- Background decoration -->
<div class="fixed inset-0 -z-10 overflow-hidden">

<div class="absolute top-20 left-20 w-72 h-72 bg-sky-500/10 rounded-full blur-3xl"></div>

<div class="absolute bottom-20 right-20 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl"></div>

<div class="absolute top-1/2 left-1/2 w-[500px] h-[500px] bg-sky-400/5 rounded-full blur-3xl -translate-x-1/2 -translate-y-1/2"></div>

</div>


<!-- Navbar -->
<nav class="fixed top-0 w-full bg-slate-900/80 backdrop-blur border-b border-slate-800 z-50">

<div class="max-w-6xl mx-auto flex justify-between items-center p-4">

<h1 class="text-sky-400 font-bold text-xl tracking-wide">
Bagas.dev
</h1>

<div class="space-x-6 text-sm hidden md:block">

<a href="#about" class="hover:text-sky-400 transition">
About
</a>

<a href="#skills" class="hover:text-sky-400 transition">
Skills
</a>

<a href="#projects" class="hover:text-sky-400 transition">
Projects
</a>

<a href="/gallery" class="hover:text-sky-400 transition">
Gallery
</a>

<a href="#contact" class="hover:text-sky-400 transition">
Contact
</a>

</div>

</div>

</nav>


<!-- Hero -->
<section class="min-h-screen flex flex-col justify-center items-center text-center px-6 relative">

<!-- tempelan -->
<div class="absolute top-40 left-10 w-24 h-24 border border-sky-400/20 rotate-12 rounded-2xl"></div>

<div class="absolute bottom-32 right-10 w-16 h-16 border border-cyan-400/20 -rotate-12 rounded-full"></div>

<img src="static/bagas.jpeg"
class="w-44 h-44 rounded-full border-4 border-sky-400 shadow-[0_0_40px_rgba(56,189,248,0.6)] mb-6 object-cover">

<h1 class="text-5xl md:text-6xl font-bold text-sky-400">
Bagas
</h1>

<p class="mt-4 text-slate-300 max-w-xl leading-relaxed">
Pelajar yang suka teknologi, Arduino, web development,
dan bikin project aneh tapi keren.
</p>

<!-- tags -->
<div class="flex gap-3 mt-6 flex-wrap justify-center">

<span class="px-4 py-2 bg-slate-800 rounded-full text-sm border border-slate-700">
⚡ Tech Enthusiast
</span>

<span class="px-4 py-2 bg-slate-800 rounded-full text-sm border border-slate-700">
💻 Web Dev
</span>

<span class="px-4 py-2 bg-slate-800 rounded-full text-sm border border-slate-700">
🔧 Arduino
</span>

</div>

<div class="mt-8 flex gap-4 flex-wrap justify-center">

<a href="#projects"
class="px-6 py-3 bg-sky-400 text-black rounded-full hover:bg-cyan-300 transition font-semibold">
Lihat Project
</a>

<a href="https://instagram.com"
target="_blank"
class="px-6 py-3 border border-sky-400 rounded-full hover:bg-sky-400 hover:text-black transition">
Instagram
</a>

</div>

</section>


<!-- About -->
<section id="about" class="py-24 px-6 text-center bg-slate-900/40 backdrop-blur">

<h2 class="text-3xl font-bold text-sky-400 mb-6">
Tentang Saya
</h2>

<p class="max-w-2xl mx-auto text-slate-300 leading-relaxed">
Saya pelajar yang suka eksperimen teknologi seperti Arduino,
web development, dan berbagai project kreatif lainnya.
Saya suka bikin sesuatu yang random tapi kadang malah kepake 😭
</p>

</section>


<!-- Skills -->
<section id="skills" class="py-24 px-6 text-center relative">

<h2 class="text-3xl font-bold text-sky-400 mb-12">
Skill
</h2>

<div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">

<div class="bg-slate-900/70 backdrop-blur border border-slate-800 p-8 rounded-2xl hover:-translate-y-2 hover:border-sky-400 transition duration-300 shadow-xl">

<div class="text-4xl mb-4">💻</div>

<h3 class="text-xl font-semibold">
HTML & CSS
</h3>

<p class="text-slate-400 text-sm mt-2">
UI modern dan responsif
</p>

</div>

<div class="bg-slate-900/70 backdrop-blur border border-slate-800 p-8 rounded-2xl hover:-translate-y-2 hover:border-sky-400 transition duration-300 shadow-xl">

<div class="text-4xl mb-4">🔧</div>

<h3 class="text-xl font-semibold">
Arduino
</h3>

<p class="text-slate-400 text-sm mt-2">
Hardware + coding
</p>

</div>

<div class="bg-slate-900/70 backdrop-blur border border-slate-800 p-8 rounded-2xl hover:-translate-y-2 hover:border-sky-400 transition duration-300 shadow-xl">

<div class="text-4xl mb-4">🐍</div>

<h3 class="text-xl font-semibold">
Python
</h3>

<p class="text-slate-400 text-sm mt-2">
Automation & backend
</p>

</div>

</div>

</section>


<!-- Projects -->
<section id="projects"
class="py-24 px-6 bg-slate-900/40 backdrop-blur text-center relative">

<h2 class="text-3xl font-bold text-sky-400 mb-12">
Project
</h2>

<div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">

<div class="bg-slate-800/70 border border-slate-700 p-6 rounded-2xl hover:scale-105 hover:border-sky-400 transition duration-300 shadow-xl">

<div class="text-4xl mb-4">📟</div>

<h3 class="text-lg font-bold">
Arduino LCD System
</h3>

<p class="text-sm text-slate-400 mt-2">
Project LCD running text dengan tombol kontrol.
</p>

<button class="mt-4 px-4 py-2 bg-sky-400 text-black rounded-lg font-semibold hover:bg-cyan-300 transition">
Detail
</button>

</div>

<div class="bg-slate-800/70 border border-slate-700 p-6 rounded-2xl hover:scale-105 hover:border-sky-400 transition duration-300 shadow-xl">

<div class="text-4xl mb-4">🌐</div>

<h3 class="text-lg font-bold">
Python Web Server
</h3>

<p class="text-sm text-slate-400 mt-2">
Web sederhana menggunakan Flask.
</p>

<button class="mt-4 px-4 py-2 bg-sky-400 text-black rounded-lg font-semibold hover:bg-cyan-300 transition">
Detail
</button>

</div>

<div class="bg-slate-800/70 border border-slate-700 p-6 rounded-2xl hover:scale-105 hover:border-sky-400 transition duration-300 shadow-xl">

<div class="text-4xl mb-4">🎮</div>

<h3 class="text-lg font-bold">
Game Prototype
</h3>

<p class="text-sm text-slate-400 mt-2">
Eksperimen membuat game kecil.
</p>

<button class="mt-4 px-4 py-2 bg-sky-400 text-black rounded-lg font-semibold hover:bg-cyan-300 transition">
Detail
</button>

</div>

</div>

</section>


<!-- Gallery -->
<section id="gallery" class="py-24 px-6 relative overflow-hidden">

<div class="absolute top-10 left-10 w-32 h-32 bg-sky-400/10 blur-3xl rounded-full"></div>

<div class="absolute bottom-10 right-10 w-40 h-40 bg-cyan-400/10 blur-3xl rounded-full"></div>

<h2 class="text-3xl font-bold text-sky-400 mb-12 text-center">
Gallery
</h2>

<p class="text-center text-slate-400 mb-12">
Foto project, setup, random tech stuff,
karena manusia modern memang wajib punya galeri biar keliatan sibuk 😮‍💨
</p>

<div class="grid md:grid-cols-3 gap-6 max-w-6xl mx-auto">

<!-- FOTO 1 -->
<div class="group relative overflow-hidden rounded-2xl border border-slate-800 bg-slate-900">

<img src="static/gallery1.jpg"
class="w-full h-72 object-cover group-hover:scale-110 transition duration-500">

<div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>

<div class="absolute bottom-4 left-4">
<h3 class="font-bold text-lg">Project Setup</h3>
<p class="text-sm text-slate-300">
Tambahkan deskripsi foto
</p>
</div>

</div>

<!-- FOTO 2 -->
<div class="group relative overflow-hidden rounded-2xl border border-slate-800 bg-slate-900">

<img src="static/gallery2.jpg"
class="w-full h-72 object-cover group-hover:scale-110 transition duration-500">

<div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>

<div class="absolute bottom-4 left-4">
<h3 class="font-bold text-lg">Coding Night</h3>
<p class="text-sm text-slate-300">
Tambahkan deskripsi foto
</p>
</div>

</div>

<!-- FOTO 3 -->
<div class="group relative overflow-hidden rounded-2xl border border-slate-800 bg-slate-900">

<img src="static/gallery3.jpg"
class="w-full h-72 object-cover group-hover:scale-110 transition duration-500">

<div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>

<div class="absolute bottom-4 left-4">
<h3 class="font-bold text-lg">Random Build</h3>
<p class="text-sm text-slate-300">
Tambahkan deskripsi foto
</p>
</div>

</div>

</div>

</section>


<!-- Contact -->
<section id="contact" class="py-24 px-6 text-center bg-slate-900/40">

<h2 class="text-3xl font-bold text-sky-400 mb-6">
Kontak
</h2>

<div class="flex justify-center gap-6 flex-wrap">

<a href="mailto:bagasrp1098@email.com"
class="px-6 py-3 bg-sky-400 text-black rounded-full font-semibold hover:bg-cyan-300 transition">
Email
</a>

<a href="https://www.instagram.com/bagas_rafif_pratama/"
target="_blank"
class="px-6 py-3 border border-sky-400 rounded-full hover:bg-sky-400 hover:text-black transition">
Instagram
</a>

<a href="https://github.com/BagasRafifP"
target="_blank"
class="px-6 py-3 border border-sky-400 rounded-full hover:bg-sky-400 hover:text-black transition">
GitHub
</a>

</div>

</section>


<!-- Footer -->
<footer class="py-8 text-center text-slate-500 text-sm border-t border-slate-800">

© 2026 Bagas.dev

</footer>

</body>
</html>
    """,
        content_type='text/html',
    )

from django.http import HttpResponse

def gallery(request):
    return HttpResponse(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Gallery</title>

            <script src="https://cdn.tailwindcss.com"></script>
        </head>

        <body class="bg-zinc-900 text-white p-10">

            <h1 class="text-4xl font-bold mb-6">
                🚗 Gallery Page
            </h1>

            <p class="text-zinc-400 mb-8">
                Ini adalah halaman gallery. Karena manusia ga bisa hidup tanpa upload foto mobil dan bilang "rawr spec".
            </p>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

                <div class="bg-zinc-800 rounded-2xl overflow-hidden shadow-lg">
                    <img 
                        src="https://images.unsplash.com/photo-1492144534655-ae79c964c9d7"
                        class="w-full h-52 object-cover"
                    >

                    <div class="p-4">
                        <h2 class="text-xl font-semibold">
                            JDM Car
                        </h2>
                    </div>
                </div>

                <div class="bg-zinc-800 rounded-2xl overflow-hidden shadow-lg">
                    <img 
                        src="https://images.unsplash.com/photo-1503376780353-7e6692767b70"
                        class="w-full h-52 object-cover"
                    >

                    <div class="p-4">
                        <h2 class="text-xl font-semibold">
                            Supercar
                        </h2>
                    </div>
                </div>

                <div class="bg-zinc-800 rounded-2xl overflow-hidden shadow-lg">
                    <img 
                        src="https://images.unsplash.com/photo-1511919884226-fd3cad34687c"
                        class="w-full h-52 object-cover"
                    >

                    <div class="p-4">
                        <h2 class="text-xl font-semibold">
                            Night Racing
                        </h2>
                    </div>
                </div>

            </div>

        </body>
        </html>
        """,
        content_type='text/html',
    )

def api_data(request):
    return JsonResponse(
        {
            'data': [
                {'id': 1, 'name': 'Sample Item 1', 'value': 100},
                {'id': 2, 'name': 'Sample Item 2', 'value': 200},
                {'id': 3, 'name': 'Sample Item 3', 'value': 300},
            ],
            'total': 3,
            'timestamp': '2024-01-01T00:00:00Z',
        }
    )
# testing