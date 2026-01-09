# from Model import Task

class TaskController:
    def __init__(self):
        self.daftar_task = []

    def tambah_task(self, judul, deskripsi=""):
        try:
            if not judul.strip():
                raise ValueError("Judul tidak boleh kosong!")

            task_baru = (judul, deskripsi)
            self.daftar_task.append(task_baru)
            return True, "✅ Task berhasil ditambahkan!"
        except ValueError as e:
            return False, f"❌ Error: {str(e)}"

    def get_semua_task(self):
        return self.daftar_task

    def get_task_by_status(self, status_cari):
        filtered = list(filter(
            lambda task: task.status == status_cari,
            self.daftar_task
        ))
        return filtered

    def hapus_task(self, nomor):
        try:
            idx = int(nomor) - 1
            if 0 <= idx < len(self.daftar_task):
                task_hapus = self.daftar_task.pop(idx)
                return True, f"✅ Task '{task_hapus.judul}' dihapus!"
            else:
                return False, "❌ Nomor task tidak valid!"
        except ValueError:
            return False, "❌ Input harus angka!"