# Log sebuah website

> Cari sebuah perbedaan dari 2 log tersebut Format Flag : uconnect{\w+}

![chall](images/chall.png)

[logA](files/accesslog-A.txt), [logB](files/accesslog-B.txt)

## Solve

Diberikan dua buah log file, sesuai deskripsi mencari perbedaan oleh karena itu saya langsung menggunakan command ```diff``` untuk melihat perbedaan dari kedua file

![diff](images/diff.png)

Setelah itu saya buka di dalam notepad

![result](images/result.png)

Sepertinya sudah ada titik terang, namun kita perlu rapikan

![solve](images/solve.png)

```
uconnect{C0MmanD_L1n3_fuN_C0oyY_y4_k4N?}
```