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

# Ishlab chiqarish

<details open>

<summary>Ishlab chiqarish</summary>

**Ishlab chiqarish bo‘limi** mahsulotlarni ishlab chiqarish jarayonini boshqarish, xomashyoni sarflash va tayyor mahsulotni omborga qabul qilishni avtomatlashtirish imkonini beradi. Ushbu bo‘lim orqali ishlab chiqarish buyurtmalari yaratiladi va ular asosida ombordagi harakatlar avtomatik amalga oshiriladi. Bu bo‘lim ishlab chiqarish jarayonini nazorat qilish, tannarxni hisoblash va resurslardan samarali foydalanish uchun ishlatiladi.

Ishlab chiqarish → **Ishlab chiqarish** bo‘limiga kiriladi va **“Yaratish”** tugmasi orqali yangi ishlab chiqarish jarayoni yaratiladi.

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

Ishlab chiqarish yaratishda quyidagi asosiy maydonlar to‘ldiriladi:

* **Kod** – ishlab chiqarish hujjati uchun unikal identifikator
* **Mas’ul shaxs**\* – jarayonga javobgar xodim
* **Pul birligi**\* – hisob-kitob valyutasi (UZS va boshqalar)
* **Materiallarni hisobdan chiqarish ombori**\* – xomashyo olinadigan ombor
* **Mahsulotlar joylashadigan ombor**\* – tayyor mahsulot kiradigan ombor
* **Materiallarni hisobdan chiqarish sanasi**\* – xomashyo chiqim sanasi
* **Omborga kirish sanasi**\* – tayyor mahsulot kirim sanasi
* **Tarkib** – oldindan yaratilgan tarkib (recipe)
* **Miqdori** – ishlab chiqariladigan mahsulot hajmi
* **Holati** – jarayon holati (Yangi, Jarayonda, Yakunlangan)
* **Izoh** – qo‘shimcha ma’lumot

Ishlab chiqarish oynasida tarkib asosida quyidagi bo‘limlar avtomatik shakllanadi:

#### **Xomashyo**

Bu yerda ishlab chiqarish uchun kerakli mahsulotlar ko‘rsatiladi.

* Mahsulot nomi
* Ombordagi miqdori
* Sarflanadigan miqdor
* Alternativ mahsulotlar
* Yaroqlilik muddati
* Umumiy tannarx

#### **Tayyor mahsulot**

Natijada olinadigan mahsulotlar aks etadi va omborga kirim qilinadi.

#### **Qo‘shimcha xarajat**

Ishlab chiqarishga bog‘liq xarajatlar qo‘shiladi va umumiy tannarxga ta’sir qiladi.

Tizim ishlash logikasi:

* Tarkib tanlanganda xomashyo avtomatik hisoblanadi
* Ishlab chiqarish yakunlanganda:
  * Xomashyo ombordan chiqim qilinadi
  * Tayyor mahsulot omborga kirim qilinadi
  * Xarajatlar mahsulot tannarxiga qo‘shiladi

</details>
