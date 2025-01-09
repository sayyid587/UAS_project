class Data:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def validate_nim(self):
        try:
            self.nim = int(self.nim)
            return True
        except (ValueError):
            return False

    def validate_nama(self):
        if self.nama.replace(" ", "").isalpha():
            return True
        return False