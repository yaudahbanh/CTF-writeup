# CPNS

> ![chall.pcapng](file/ChallPcap.pcapng)

## Solve

Diberikan sebuah file pcap, langsung saja kita buka dengan Wireshark

![solve1](images/solve1.jpg)

Karena sesuai deskripsi soal yang berkaitan dengan ```HEAD``` maka saya langsung filter ke protokol HTTP dan kemudian melihat isi dari header requestnya

![solve2](images/solve2.jpg)

```
UNITY2023{5U8M1T_Y0UR_FL4G}
```