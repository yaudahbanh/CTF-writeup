# binex6

Download [here](files/binex_6)

## Solve

Diberikan sebuah file dari hasil compile, selanjutnya kita analysis menggunakan `Ghidra`

Pada function main terdapat function lain bernama `vuln`

![solve1](images/solve1.png)

Pada function vuln terdapat sebuah variable dengan 32 byte, untuk sampai ke variable win kita perlu melakukan overflow

![solve2](images/solve2.png)

Karena file merupakan 64-bit, jadi kita perlu menambahkan 8 bytes `32 + 8 = 40`

![solve3](images/solve3.png)

Selanjutnya kita melakukan jump pada function win

Berikut adalah script yang digunakan

![solve4](images/solve4.png)

Jalankan script

![flag](images/flag.png)

```
flag{fc9e120ae248575a793aef8801a2d90a}
```