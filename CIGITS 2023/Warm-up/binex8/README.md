# binex8

Download [here](files/binex_8)

## Solve

Diberikan sebuah file dari hasil compile, selanjutnya kita analysis menggunakan `Ghidra`

Terdapat pada 3 function berbeda di global

![solve1](images/solve1.png)

Pada function main terdapat variable input dengan size 16 byte

![solve2](images/solve2.png)

Kemudian pada function win1 dan win2 terdapat keterangan berikut

![solve3](images/solve3.png)

![solve4](images/solve4.png)

Sesuai dengan chall kita membutuhkan address dari `"/bin/sh"` kemudian melakukan overwrite kepada argument yang ada pada `win2`

Disini saya menggunakan `gdb-pwndbg` untuk menemukan `"/bin/sh"` dengan command `vmmap`

![solve5](images/solve5.png)

Dapat terlihat start dan size dari program dengan begitu kita bisa menggunakan command `find` seperti ini `find 0x400000, +0x1000, "/bin/sh"`

![solve6](images/solve6.png)

Karena hanya dibutuhkan first argument pada win2 kita bisa menggunakan rdi sesuai keterangan [architecture](http://6.s081.scripts.mit.edu/sp18/x86-64-architecture-guide.html)

Karena file merupakan 64-bit, kita memperlukan 8 byte sehingga `16 + 8 = 24`

![solve7](images/solve7.png)

Berikut adalah script yang digunakan 

![solve8](images/solve8.png)

Jalankan script

![flag](images/flag.png)

```
flag{ba24fb25598667fc1574bacf31d1172b}
```