# binex1

Download [file](files/binex_1)

## Solve

Diberikan sebuah file dari hasil compile, selanjutnya kita analysis menggunakan `Ghidra`

Pada function main, terdapat sebuah fungsi strcmp yang gunanya untuk melakukan compare string dan apabila string yang dibandingkan adalah benar maka flag akan muncul

![solve1](images/solve1.png)

Kita bisa menginputkan string tersebut `Th1s_is_mY_P@55w0rd` atau menggunakan payload seperti ini

![solve2](images/solve2.png)

Jalankan script

![flag](images/flag.png)

```
flag{now_you_can_use_ida}
```