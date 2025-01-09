# UAS_project
Nama : Sayyid Sulthan Abyan <p>
Nim : 312410496 <p>
Kelas : TI.24.A.5 <p>
Mata kuliah : Bahasa pemrograman <p>

## Penjelasan Singkat
1. Kelas Data:
   - Metode __init__: Ini adalah metode konstruktor untuk kelas Data. Metode ini menginisialisasi atribut nim (Nomor Induk Mahasiswa) dan nama (nama mahasiswa).
   - Metode validate_nim: Metode ini memvalidasi apakah nim adalah sebuah integer. Jika konversi ke integer berhasil, maka akan mengembalikan True; jika tidak, mengembalikan False.
   - Metode validate_nama: Metode ini memeriksa apakah nama hanya mengandung karakter alfabet (mengizinkan spasi). Jika iya, maka akan mengembalikan True; jika tidak, mengembalikan False.
```python
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
```
2. Kelas View:
   - Metode display_table: Metode ini mencetak tabel yang terformat dari data mahasiswa. Metode ini menerima daftar objek Data sebagai masukan dan menampilkan setiap nim dan nama mahasiswa dalam format tabel yang terstruktur.
```python
          class View:
              def display_table(self, data):
                  print("\ndata mahasiswa")
                  print("+----+------------+-----------------------------+")
                  print("| No |    Nim     |             Nama            |")
                  print("+----+------------+-----------------------------+")
                  for i, value in enumerate(data, 1):
                      print(f"| {i:2} | {value.nim:<10} | {value.nama:<27} |")
                  print("+----+------------+-----------------------------+")
```            
3. Kelas Process:
   - Metode __init__: Konstruktor ini menginisialisasi daftar kosong data_list untuk menyimpan objek Data.
   - Metode add_data: Metode ini memvalidasi objek Data menggunakan metode validate_nim dan validate_nama. Jika kedua validasi berhasil, maka objek Data akan ditambahkan ke dalam data_list. Jika ada validasi yang gagal, maka akan mencetak pesan kesalahan.
   - Metode get_data_list: Metode ini mengembalikan data_list yang berisi semua objek Data yang valid.
```python
          class Process:
              def __init__(self):
                  self.data_list = []
          
              def add_data(self, data):
                  if data.validate_nim() and data.validate_nama():
                      self.data_list.append(data)
                  else:
                      print("Input tidak valid. Nim harus berupa angka dan Nama harus berupa huruf.")
          
              def get_data_list(self):
                  return self.data_list
```
4. main (jika __name__ == "__main__"):
   - Inisialisasi objek Process dan View: Membuat instance dari kelas Process dan View.
   - Loop input: Secara terus-menerus meminta pengguna untuk memasukkan nim dan nama sampai pengguna mengetik 'exit' untuk nim. Untuk setiap masukan, objek Data dibuat dan divalidasi. Jika valid, objek Data akan ditambahkan ke dalam data_list.
   - Tampilkan tabel: Setelah loop input selesai, metode display_table dari kelas View dipanggil untuk menampilkan daftar data mahasiswa yang valid.

```python
          if __name__ == "__main__":
              process = Process()
              view = View()
          
              while True:
                  input_nim = input("Masukkan Nim (atau 'exit' untuk keluar): ")
                  input_nama = input("Masukkan Nama : ")
                  if input_nim.lower() == 'exit':
                      break
                  data = Data(input_nim, input_nama)
                  process.add_data(data)
          
              view.display_table(process.get_data_list())
```


Output Program

![Gambar 1](https://github.com/user-attachments/assets/6e19e9e1-e9ef-4902-bf75-e7dbe5434929)


Link dekumentasi
https://youtu.be/xIKaRiRX7nA
