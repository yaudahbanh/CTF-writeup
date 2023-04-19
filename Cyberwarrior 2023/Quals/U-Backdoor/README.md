# U-Backdoor

> Waduch! Kami lupa bagaimana cara mengeksekusi backdoor kami nih, bantu yah dek

![chall](images/chall.jpg)

## Solve

Diberikan website dengan tampilan seperti berikut

![proof1](images/proof1.jpg)

Rapikah dulu dengan php prettier agar bisa dibaca

![proof2](images/proof2.jpg)

Setelah di analisis ternyata kita perlu memasukan header contohnya seperti header User-Agent yang panjang value nya tidak lebih dari 15 char,
kemudian ada penambahan header U-BACKDOOR yang panjang value nya tidak lebih dari 17.
Ywdah lah yah kita gaskan seperti ini

![proof3](images/proof3.jpg)

Nah setelah gini berarti inject pointnya sudah dipastikan lewat header U-BACKDOOR, sisanya gimana cara memanfaatkan panjang value yang tidak boleh lebih dari 17 char?
Bener, pakek eval GET url nya

![proof4](images/proof4.jpg)

Langsung check response

![solve](images/solve.jpg)

```
uconnect{huft_membingungkan}
```