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

# Mahsulotlar

<details>

<summary>Mahsulotlar yaratish</summary>

Mahsulotlar bo‘limi orqali ombordagi barcha mahsulotlarni yaratish, tahrirlash va boshqarish jarayoni amalga oshiriladi. Bu bo‘lim mahsulotlar haqidagi asosiy ma’lumotlarni saqlash va ularni ombor, savdo hamda boshqa jarayonlar bilan bog‘lash uchun xizmat qiladi.

Foydalanuvchi chap menyudan **Ombor → Mahsulotlar** bo‘limiga kiradi va yangi mahsulot qo‘shish uchun **“Yaratish”** tugmasini bosadi.

<figure><img src="../../.gitbook/assets/image (371).png" alt=""><figcaption></figcaption></figure>

Mahsulot yaratishda quyidagi ma’lumotlar kiritiladi:

* **Nomi** — mahsulot nomi kiritiladi
* **Kategoriya** — mahsulot tegishli kategoriya tanlanadi
* **O‘lchov birligi** — mahsulot o‘lchov turi (dona, kg, litr va boshqalar)
* **Quti turi** — mahsulot qadoq turi tanlanadi
* **Qutidagi miqdori** — bitta qutidagi mahsulot soni
* **Quti shtrix-kodi** — quti uchun alohida shtrix-kod
* **SKU** — mahsulotning noyob identifikatsiya kodi
* **Shtrix-kod** — mahsulotning asosiy barkodi
* **Yetkazib beruvchi** — mahsulot yetkazib beruvchisi
* **Ombordagi o‘rni** — mahsulot joylashuvi (stellaj, sektor va boshqalar)
* **Izoh** — qo‘shimcha ma’lumot (ixtiyoriy)
* **Fayl yuklash** — mahsulotga tegishli fayl biriktirish

Inventarizatsiya sozlamalari:

* **Mahsulot / Yarim mahsulot / Xomashyo** — mahsulot turi belgilanadi qaysi biri tanlangan bo'lsa mahsulot shu hisoblanadi.&#x20;
* **Variant mahsulot** — variantli mahsulot sifatida ishlatish
* **Belgili mahsulot** — maxsus belgilash uchun
* **Yaroqlilik muddati** — amal qilish muddatini yuritish

<figure><img src="../../.gitbook/assets/image (373).png" alt=""><figcaption></figcaption></figure>

Mahsulot tarkibi (qo‘shimcha sozlamalar):

Bu bo‘limda mahsulotning ombor va savdo bilan bog‘liq parametrlarini sozlash mumkin:

* **Tashkilot** — mahsulot qaysi tashkilotlarga tegishli
* **Maksimal miqdori** — maksimal zaxira chegarasi
* **Normativ kun** —mahsulot tugaganda buyurtma berilsa shu mahsulot necha kunda keladi (analitika uchun)
* **Sariq chiziq** — ogohlantirish darajasi
* **Qizil chiziq** — kritik minimal daraja
* **Sotuvda mavjud** — mahsulotni sotuvga chiqarish
* **Chakana** — chakana savdo narxi
* **Ulgurji** — ulgurji narx
* **Boshqa narxlarni foydalanuvchi o'zi yaratib oladi**&#x20;

Ushbu bo‘lim orqali mahsulotlar to‘liq boshqariladi va ular keyingi jarayonlar (kirim, chiqim, inventarizatsiya, savdo) uchun asos bo‘lib xizmat qiladi.

</details>

<details>

<summary>Variant mahsulot yaratish</summary>

Agar mahsulot bir nechta variantlarda (masalan rang, o‘lcham va boshqalar) mavjud bo‘lsa, ularni alohida-alohida mahsulot sifatida emas, balki bitta mahsulot ichida variantlar orqali boshqarish mumkin.

Buning uchun mahsulot yaratish oynasida **“Variant mahsulot”** toggle switch yoqiladi. Ushbu funksiya yoqilganda tizimda qo‘shimcha **“Variant mahsulot”** oynasi ochiladi.

<figure><img src="../../.gitbook/assets/image (375).png" alt=""><figcaption></figcaption></figure>

Bu bo‘limda mahsulot variantlari quyidagicha kiritiladi:

* **Variant** — mahsulot varianti turi tanlanadi (masalan: rang, o‘lcham)
* **Attribut** — tanlangan variantga tegishli qiymatlar kiritiladi (masalan: oq, qora)

Variantlar kiritilgandan so‘ng **“Mahsulotlarni qo‘shish”** tugmasi bosiladi. Shundan keyin tizim avtomatik ravishda **“Mahsulot tarkibi”** bo‘limini shakllantiradi.

<figure><img src="../../.gitbook/assets/image (376).png" alt=""><figcaption></figcaption></figure>



Mahsulot tarkibi bo‘limida:

* har bir variant uchun alohida mahsulot (SKU) yaratiladi
* **SKU** — har bir variant uchun alohida kiritiladi yoki
* **Avtomatik yaratish** orqali tizim tomonidan generatsiya qilinadi

Natijada, kiritilgan atributlar soniga qarab mahsulotlar avtomatik ko‘payadi.

Masalan:\
Agar “Telefon” mahsuloti uchun **rang** varianti tanlanib, atribut sifatida **qizil** va **qora** kiritilsa, tizim avtomatik ravishda 2 ta mahsulot yaratadi:

* Telefon / qizil
* Telefon / qora

Bu yondashuv mahsulotlarni tizimli boshqarish, har bir variantni alohida hisobga olish va savdo jarayonlarini soddalashtirish imkonini beradi.

<figure><img src="../../.gitbook/assets/image (377).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (379).png" alt=""><figcaption></figcaption></figure>

Variantlar orqali mahsulot yaratish tizimda mahsulotlarni yanada strukturali va samarali boshqarishga imkon beradi.

Bu funksiyadan foydalanish orqali quyidagilarga erishiladi:

* **Mahsulotlarni tartibli boshqarish** — bir xil mahsulotning turli variantlari (rang, o‘lcham va boshqalar) bitta mahsulot ichida saqlanadi, tizim chalkash bo‘lib ketmaydi
* **Har bir variantni alohida nazorat qilish** — har bir variant uchun alohida SKU, narx va qoldiq yuritish mumkin
* **Ombor hisobini aniqlashtirish** — masalan, “qizil” va “qora” mahsulotlar alohida hisoblanadi, qaysi biri ko‘p yoki kamligi aniq ko‘rinadi
* **Savdo jarayonini soddalashtirish** — sotuv vaqtida aniq variant tanlanadi, xatoliklar kamayadi
* **Avtomatik mahsulot yaratish** — variant atributlari asosida tizim avtomatik bir nechta mahsulot hosil qiladi, qo‘lda yaratishga hojat qolmaydi
* **Moslashuvchanlik** — yangi variantlar qo‘shish yoki o‘zgartirish oson, tizimni kengaytirish qulay

Natijada, variantlar orqali mahsulot boshqaruvi yanada professional darajaga chiqadi va ombor hamda savdo jarayonlari ancha aniq va tez ishlaydi.

</details>

<details>

<summary>Begili mahsulot yaraitsh</summary>

Agar mahsulot yaratishda **“Belgili mahsulot”** toggle switch yoqilsa, ushbu mahsulot uchun har bir birlik alohida **unikal identifikatsiya (belgi)** bilan yuritiladi.

Bu funksiyada mahsulot oddiy miqdor bo‘yicha emas, balki **har bir dona kesimida** boshqariladi.

<figure><img src="../../.gitbook/assets/image (381).png" alt=""><figcaption></figcaption></figure>

Natijada tizimda quyidagilar amalga oshiriladi:

* har bir mahsulot uchun alohida **unikal kod (serial raqam, IMEI va boshqalar)** biriktiriladi
* mahsulot harakati (kirim, chiqim, inventarizatsiya, sotuv) aynan shu belgi orqali kuzatiladi
* bir xil mahsulotlar aralashib ketmaydi, har biri alohida nazorat qilinadi

Jarayon qanday ishlaydi:

Inventarizatsiya, kirim yoki sotuv jarayonida:

* tizim mahsulot miqdorini emas, balki **har bir dona uchun alohida belgi kiritishni talab qiladi**
* foydalanuvchi har bir mahsulot uchun unik kodlarni qo‘lda kiritadi yoki yuklaydi
* tizim ushbu belgilarni saqlab, keyingi operatsiyalarda aynan shu mahsulotni aniqlaydi



Inventorizatsiyada:

<figure><img src="../../.gitbook/assets/image (380).png" alt=""><figcaption></figcaption></figure>



Savdoda:

<figure><img src="../../.gitbook/assets/image (383).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (385).png" alt=""><figcaption></figcaption></figure>

Masalan:\
Agar “iPhone” mahsuloti belgili mahsulot sifatida yaratilsa, omborga 10 dona kirim qilinayotganda har bir iPhone uchun alohida IMEI raqam kiritiladi. Keyinchalik sotuv yoki chiqimda aynan qaysi IMEI sotilgani tizimda aniq ko‘rinadi.

Foydasi:

* qimmat va muhim mahsulotlarni aniq nazorat qilish
* yo‘qotish va chalkashliklarning oldini olish
* kafolat va servis jarayonlarini oson yuritish
* har bir mahsulot tarixini (kimdan kelgan, qachon sotilgan) kuzatish

Ushbu funksional odatda **texnika do‘konlari, elektronika savdosi va serial raqam bilan ishlanadigan mahsulotlar** uchun qo‘llaniladi.

</details>

<details>

<summary>Yaroqlilik muddati mavjud mahsulot yaratish</summary>

<figure><img src="../../.gitbook/assets/image (387).png" alt=""><figcaption></figcaption></figure>

Agar mahsulot yaratishda **“Yaroqlilik muddati”** toggle switch yoqilsa, ushbu mahsulot uchun amal qilish muddati (expiry date) bilan ishlash yoqiladi.

Bu degani mahsulot oddiy miqdor bo‘yicha emas, balki **yaroqlilik muddati kesimida** boshqariladi.

Ushbu funksional asosan oziq-ovqat, dori-darmon va tez buziladigan mahsulotlar uchun qo‘llaniladi.

Jarayon qanday ishlaydi:

* **Xarid (kirim) jarayonida**\
  mahsulot omborga qabul qilinayotganda har bir mahsulot uchun **yaroqlilik muddati kiritiladi**
* **Omborda saqlashda**\
  mahsulotlar yaroqlilik muddati bo‘yicha alohida partiyalarda saqlanadi
* **Savdo jarayonida**\
  mahsulot sotilayotganda foydalanuvchi **qaysi yaroqlilik muddatiga ega mahsulotni** sotayotganini tanlaydi

<figure><img src="../../.gitbook/assets/image (388).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (389).png" alt=""><figcaption></figcaption></figure>

Natijada tizimda quyidagilar ta’minlanadi:

* mahsulotlar muddati bo‘yicha aniq nazorat qilinadi
* muddati yaqinlashgan mahsulotlarni kuzatish imkoniyati paydo bo‘ladi
* eskirgan yoki muddati o‘tgan mahsulotlar bilan ishlashda xatoliklar kamayadi
* FIFO (oldin kelgan — oldin sotiladi) tamoyilini qo‘llash osonlashadi

Masalan:\
Agar “Kefir” mahsuloti uchun yaroqlilik muddati yoqilgan bo‘lsa, omborga kirim qilinayotganda har bir partiya uchun sana kiritiladi (masalan: 23.03.2026). Savdo vaqtida esa aynan shu sana bo‘yicha mahsulot tanlab sotiladi.

Bu esa mahsulot sifatini nazorat qilish va yo‘qotishlarni kamaytirishda muhim rol o‘ynaydi.







</details>

