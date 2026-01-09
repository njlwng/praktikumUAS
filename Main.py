# main.py
print("🚀 Starting Program...")

# SIMPLE VIEW CLASS
class SimpleView:
    @staticmethod
    def tampilkan_menu():
        print("\n" + "=" * 40)
        print("📝 TO-DO LIST MANAGER")
        print("=" * 40)
        print("1. Tambah Task")
        print("2. Lihat Task")
        print("3. Hapus Task")
        print("4. Statistik")
        print("5. Keluar")
        print("=" * 40)

    @staticmethod
    def tampilkan_tasks(tasks):
        if not tasks:
            print("\n📭 Tidak ada task")
            return

        print("\n" + "=" * 50)
        print("DAFTAR TASK")
        print("=" * 50)

        for i, task in enumerate(tasks, 1):
            if isinstance(task, dict):
                print(f"{i}. {task.get('judul', 'No Title')} - {task.get('status', 'Belum selesai')}")
            else:
                print(f"{i}. {task}")

        print("=" * 50)

    @staticmethod
    def tampilkan_pesan(pesan):
        print(f"\n📢 {pesan}")


# ===== SIMPLE CONTROLLER (JIKA controller.py ERROR) =====
class SimpleController:
    def __init__(self):
        self.tasks = []
        print("✅ Controller siap")

    def tambah_task(self, judul, deskripsi=""):
        try:
            if not judul.strip():
                return False, "❌ Judul kosong"

            task = {
                "judul": judul,
                "deskripsi": deskripsi,
                "status": "Belum selesai"
            }
            self.tasks.append(task)
            return True, "✅ Berhasil ditambah"
        except:
            return False, "❌ Error"

    def get_semua_task(self):
        return self.tasks

    def hapus_task(self, nomor):
        try:
            idx = int(nomor) - 1
            if 0 <= idx < len(self.tasks):
                task = self.tasks.pop(idx)
                return True, f"✅ '{task['judul']}' dihapus"
            return False, "❌ Nomor salah"
        except:
            return False, "❌ Input angka"

    def hitung_statistik(self):
        total = len(self.tasks)
        selesai = len([t for t in self.tasks if t.get('status') == 'Selesai'])
        persentase = (selesai / total * 100) if total > 0 else 0
        return {"total": total, "selesai": selesai, "persentase": persentase}


# ===== PROGRAM UTAMA =====
def main():
    print("\n" + "=" * 50)
    print("       UAS BAHASA PEMROGRAMAN")
    print("       TO-DO LIST MANAGER")
    print("=" * 50)

    # Pakai controller dan view lokal (PASTI JALAN)
    controller = SimpleController()
    view = SimpleView()

    while True:
        view.tampilkan_menu()
        pilihan = input("Pilih (1-5): ").strip()

        if pilihan == "1":
            # TAMBAH TASK
            print("\n➕ TAMBAH TASK")
            judul = input("Judul: ").strip()

            if judul:
                deskripsi = input("Deskripsi (opsional): ").strip()
                sukses, pesan = controller.tambah_task(judul, deskripsi)
                view.tampilkan_pesan(pesan)
            else:
                view.tampilkan_pesan("❌ Judul wajib diisi")

        elif pilihan == "2":
            # LIHAT TASK
            tasks = controller.get_semua_task()
            view.tampilkan_tasks(tasks)

        elif pilihan == "3":
            # HAPUS TASK
            tasks = controller.get_semua_task()
            if not tasks:
                view.tampilkan_pesan("📭 Tidak ada task")
                continue

            view.tampilkan_tasks(tasks)
            nomor = input("Nomor task yang dihapus: ").strip()

            if nomor:
                sukses, pesan = controller.hapus_task(nomor)
                view.tampilkan_pesan(pesan)

        elif pilihan == "4":
            # STATISTIK
            stats = controller.hitung_statistik()
            print("\n📊 STATISTIK")
            print(f"Total Task   : {stats['total']}")
            print(f"Task Selesai : {stats['selesai']}")
            print(f"Persentase   : {stats['persentase']:.1f}%")

        elif pilihan == "5":
            # KELUAR
            print("\n" + "=" * 50)
            print("TERIMA KASIH! Program selesai.")
            print(f"Total task dibuat: {len(controller.tasks)}")
            print("=" * 50)
            break

        else:
            view.tampilkan_pesan("❌ Pilihan salah")

# JALANKAN
if __name__ == "__main__":
    main()