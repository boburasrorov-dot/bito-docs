---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
---

# Tex karta

<details open>

<summary>Tex karta yaratish</summary>

Tex karta bo‘limi ishlab chiqarish bosqichlarini ketma-ketlik asosida bog‘lash va to‘liq ishlab chiqarish jarayonini shakllantirish uchun ishlatiladi. Bu yerda bosqichlar o‘zaro ulanadi va mahsulot qanday tartibda ishlab chiqarilishi aniqlanadi.

Ishlab chiqarish → **Tex karta** bo‘limiga kiriladi va yangi tex karta yaratiladi.

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

Tex karta yaratishda quyidagi maydonlar to‘ldiriladi:

* **Nomi**\* – tex karta nomi
* **Kodi** – tex karta identifikatori
* **Yuqori guruh** – kategoriyaga biriktirish
* **Izoh** – qo‘shimcha ma’lumot

<figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

Tex karta ichida bosqichlar ketma-ketligi kiritiladi:

* **Bosqich** – joriy bosqich tanlanadi
* **Keyingi bosqich** – undan keyin bajariladigan bosqich
* **Tarkib** – ushbu bosqichga tegishli tarkib (recipe)

Tizim ishlash logikasi:

* Bosqichlar avval **Bosqichlar bo‘limida** yaratiladi
* Tex kartada ushbu bosqichlar tanlanib, ketma-ketlikda bog‘lanadi
* Har bir bosqich keyingi bosqich bilan ulanib, to‘liq ishlab chiqarish zanjiri hosil qiladi
* Ushbu tex karta keyinchalik ishlab chiqarish jarayonida qo‘llaniladi

</details>
