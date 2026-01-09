# PARENT CLASS (INHERITANCE)
class BaseTask:
    """Parent class untuk inheritance"""

    # CONSTRUCTOR
    def __init__(self, judul):
        # ENCAPSULATION: Private attribute
        self.__judul = judul
        self.__tanggal = "2024-1-9"

    # GETTER dengan @property
    @property
    def judul(self):
        """Getter untuk mengakses private attribute"""
        return self.__judul

    @property
    def tanggal(self):
        return self.__tanggal

    # METHOD untuk POLYMORPHISM
    def get_info(self):
        """Method yang akan di-override di child class"""
        return f"Task: {self.__judul}"

# CHILD CLASS (INHERITANCE)
class Task(BaseTask):
    """
    Child class yang mewarisi BaseTask
    INHERITANCE
    """

    def __init__(self, judul, deskripsi=""):
        # Panggil constructor parent class (super())
        super().__init__(judul)

        # Tambah atribut baru di child class
        self.__deskripsi = deskripsi
        self.__status = "Belum selesai"
        self.__prioritas = "Medium"

    # GETTER DAN SETTER
    @property
    def deskripsi(self):
        return self.__deskripsi

    # SETTER dengan validasi
    @deskripsi.setter
    def deskripsi(self, value):
        self.__deskripsi = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        # VALIDASI INPUT dalam setter
        if value in ["Belum selesai", "Selesai", "Ditunda"]:
            self.__status = value
        else:
            raise ValueError("Status tidak valid!")

    @property
    def prioritas(self):
        return self.__prioritas

    @prioritas.setter
    def prioritas(self, value):
        if value in ["Low", "Medium", "High"]:
            self.__prioritas = value
        else:
            raise ValueError("Prioritas harus Low/Medium/High!")

    # POLYMORPHISM: METHOD OVERRIDING
    def get_info(self):
        """
        Override method dari BaseTask
        POLYMORPHISM - Pertemuan 12 hal 15
        """
        return f" {self.judul} | Status: {self.status} | Prioritas: {self.prioritas}"

    # OVERLOADING (Contoh sederhana)
    def update(self, status=None, prioritas=None):
        """
        Method overloading sederhana
        Bisa update status saja, prioritas saja, atau keduanya
        """
        if status:
            self.status = status
        if prioritas:
            self.prioritas = prioritas

        return "Task berhasil diupdate!"