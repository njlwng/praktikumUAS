# Class untuk Presentation Layer

class TaskView:
    """Class untuk menangani semua tampilan ke user"""

    @staticmethod
    def tampilkan_menu():
        """Menampilkan menu utama program"""
        print("\n" + "=" * 50)
        print("📝 TO-DO LIST MANAGER")
        print("=" * 50)
        print("1. Tambah Task Baru")
        print("2. Lihat Semua Task")
        print("3. Filter Task (by Status)")
        print("4. Update Status Task")
        print("5. Hapus Task")
        print("6. Statistik")
        print("7. Keluar")
        print("=" * 50)

    @staticmethod
    def tampilkan_submenu_filter():
        """Menampilkan submenu untuk filter"""
        print("\n" + "-" * 30)
        print("🔍 FILTER TASK")
        print("-" * 30)
        print("1. Filter by Status")
        print("2. Filter by Prioritas")
        print("3. Kembali")
        print("-" * 30)

    @staticmethod
    def input_data(prompt, tipe="str", default=""):
        """
        Meminta input dari user dengan validasi

        Parameters:
        - prompt: Teks yang ditampilkan ke user
        - tipe: "str" atau "int" (tipe data yang diharapkan)
        - default: Nilai default jika user tidak input
        """
        try:
            if default:
                user_input = input(f"{prompt} [{default}]: ").strip()
            else:
                user_input = input(f"{prompt}: ").strip()

            # Jika user tidak input dan ada default, pakai default
            if not user_input and default:
                return default

            # Konversi tipe data
            if tipe == "int":
                return int(user_input)
            elif tipe == "float":
                return float(user_input)
            else:
                return user_input

        except ValueError:
            print("❌ Error: Input harus berupa angka!")
            return None

    @staticmethod
    def tampilkan_pesan(pesan, simbol="📢", garis=False):
        """
        Menampilkan pesan dengan format yang konsisten

        Parameters:
        - pesan: Pesan yang akan ditampilkan (bisa string atau list)
        - simbol: Simbol/emoji di depan pesan
        - garis: True untuk menampilkan garis pembatas
        """
        if garis:
            print("\n" + "-" * 40)

        if isinstance(pesan, list):
            for p in pesan:
                print(f"{simbol} {p}")
        else:
            print(f"{simbol} {pesan}")

        if garis:
            print("-" * 40)

    @staticmethod
    def tampilkan_tasks(tasks, judul="DAFTAR TASK"):
        """
        Menampilkan daftar task dalam bentuk tabel

        Parameters:
        - tasks: List of task objects atau dictionaries
        - judul: Judul tabel
        """
        if not tasks:
            print(f"\n📭 Tidak ada task.")
            return

        print(f"\n{'=' * 70}")
        print(f"{judul:^70}")
        print(f"{'=' * 70}")
        print(f"{'No':<4} {'Judul':<25} {'Status':<15} {'Prioritas':<12} {'Deskripsi':<15}")
        print(f"{'=' * 70}")

        for i, task in enumerate(tasks, 1):
            # Handle berbagai format task
            if isinstance(task, dict):
                # Jika task adalah dictionary
                judul_task = task.get('judul', 'Tidak ada judul')[:23]
                status = task.get('status', 'Belum selesai')
                prioritas = task.get('prioritas', 'Medium')
                deskripsi = task.get('deskripsi', '')[:13]
            else:
                # Jika task adalah object
                judul_task = getattr(task, 'judul', 'Tidak ada judul')[:23]
                status = getattr(task, 'status', 'Belum selesai')
                prioritas = getattr(task, 'prioritas', 'Medium')
                deskripsi = getattr(task, 'deskripsi', '')[:13]

            # Tentukan icon berdasarkan status
            status_icon = "✅" if status == "Selesai" else "⏳"

            # Tentukan icon berdasarkan prioritas
            prioritas_icon = {
                "High": "🔥",
                "Medium": "⚠️",
                "Low": "🔵"
            }.get(prioritas, "⚪")

            # Tampilkan dalam baris tabel
            print(f"{i:<4} {judul_task:<25} "
                  f"{status_icon} {status:<13} "
                  f"{prioritas_icon} {prioritas:<10} "
                  f"{deskripsi:<15}")

        print(f"{'=' * 70}")
        print(f"Total: {len(tasks)} task")

    @staticmethod
    def tampilkan_statistik(stats):
        """Menampilkan statistik dalam format yang rapi"""
        print("\n" + "=" * 40)
        print("📊 STATISTIK TASK")
        print("=" * 40)
        print(f"Total Task     : {stats.get('total', 0)}")
        print(f"Task Selesai   : {stats.get('selesai', 0)}")
        print(f"Task Berjalan  : {stats.get('total', 0) - stats.get('selesai', 0)}")
        print(f"Persentase     : {stats.get('persentase', 0):.1f}%")

        # Progress bar sederhana
        if stats.get('total', 0) > 0:
            persentase = stats.get('persentase', 0)
            filled = int(persentase / 5)  # Setiap 5% = 1 karakter
            progress_bar = "[" + "█" * filled + " " * (20 - filled) + "]"
            print(f"\nProgress       : {progress_bar} {persentase:.1f}%")

        print("=" * 40)

    @staticmethod
    def input_task():
        """Meminta input data task dari user"""
        print("\n" + "=" * 30)
        print("➕ INPUT DATA TASK")
        print("=" * 30)

        judul = input("Judul task: ").strip()
        if not judul:
            return None

        deskripsi = input("Deskripsi (opsional): ").strip()

        # Input status dengan pilihan
        print("\nPilihan Status:")
        print("1. Belum selesai (default)")
        print("2. Selesai")
        print("3. Ditunda")

        status_pilihan = input("Pilih status [1]: ").strip()
        status_map = {"1": "Belum selesai", "2": "Selesai", "3": "Ditunda"}
        status = status_map.get(status_pilihan, "Belum selesai")

        # Input prioritas
        print("\nPilihan Prioritas:")
        print("1. Low")
        print("2. Medium (default)")
        print("3. High")

        prioritas_pilihan = input("Pilih prioritas [2]: ").strip()
        prioritas_map = {"1": "Low", "2": "Medium", "3": "High"}
        prioritas = prioritas_map.get(prioritas_pilihan, "Medium")

        return {
            "judul": judul,
            "deskripsi": deskripsi,
            "status": status,
            "prioritas": prioritas
        }

    @staticmethod
    def konfirmasi_hapus(task_info):
        """Meminta konfirmasi penghapusan"""
        print(f"\n⚠️  KONFIRMASI PENGHAPUSAN")
        print(f"Task yang akan dihapus: {task_info}")
        konfirmasi = input("Yakin ingin menghapus? (y/n): ").strip().lower()
        return konfirmasi == 'y'


# ===== FUNGSI TEST =====
if __name__ == "__main__":
    # Test tampilan
    print("🔧 TEST VIEW.PY")

    view = TaskView()

    # Test menu
    view.tampilkan_menu()

    # Test pesan
    view.tampilkan_pesan("Ini adalah pesan test", simbol="🧪", garis=True)

    # Test tabel dengan data dummy
    tasks_dummy = [
        {"judul": "Belajar Python OOP", "status": "Belum selesai", "prioritas": "High", "deskripsi": "Untuk UAS"},
        {"judul": "Buat Presentasi", "status": "Selesai", "prioritas": "Medium", "deskripsi": "Video UAS"},
        {"judul": "Upload ke GitHub", "status": "Belum selesai", "prioritas": "Low", "deskripsi": "Repository"}
    ]

    view.tampilkan_tasks(tasks_dummy, "DATA DUMMY")

    # Test statistik
    stats_dummy = {"total": 10, "selesai": 4, "persentase": 40.0}
    view.tampilkan_statistik(stats_dummy)

    print("\n✅ View.py berfungsi dengan baik!")