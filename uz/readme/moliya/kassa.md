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

# Kassa

<details>

<summary>Kassa oynasi</summary>

**Kassa** bo‘limi tashkilotdagi barcha pul oqimlarini markazlashgan holda boshqarish uchun xizmat qiladi. Ushbu bo‘lim orqali kassalar yaratish, ularning balansini yuritish, kirim-chiqim operatsiyalarini amalga oshirish hamda barcha moliyaviy tranzaksiyalarni real vaqt rejimida kuzatish mumkin.

<figure><img src="../../.gitbook/assets/image (411).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>

#### Kassa qo‘shish

Kassani tizimga qo‘shish uchun **Kassa qo‘shish** tugmasi bosiladi va maxsus forma ochiladi. Ushbu forma orqali yangi kassa uchun asosiy parametrlar belgilanadi:

* **Kassa nomi** – kassani identifikatsiya qilish uchun ishlatiladi (masalan: Asosiy kassa, Filial kassasi)
* **Valyuta** – ushbu kassada ishlatiladigan pul birligi (so‘m, dollar va boshqalar). Har bir kassa faqat bitta valyutada ishlaydi
* **Tashkilot** – agar tizimda bir nechta tashkilot mavjud bo‘lsa, qaysi tashkilotga tegishli ekanligi belgilanadi
* **MJSh (mas’ul shaxs)** – kassaga javobgar bo‘lgan xodim

Barcha majburiy maydonlar to‘ldirilgandan so‘ng **Saqlash** tugmasi bosiladi va kassa tizimda aktiv holatga o‘tadi.

<div><figure><img src="../../.gitbook/assets/image (426).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (427).png" alt=""><figcaption></figcaption></figure></div>



#### Kassalar ro‘yxati va balans

Kassa oynasining asosiy qismida barcha kassalar kartochkalar ko‘rinishida joylashadi. Har bir kartochka kassaning joriy holati haqida tezkor ma’lumot beradi:

* **Joriy balans** – ayni vaqtdagi mavjud pul mablag‘i
* **Kassa nomi** – foydalanuvchiga kassani tez ajratib olish imkonini beradi
* **Tashkilot va mas’ul shaxs** – ushbu kassaga kim javobgar ekanligini ko‘rsatadi

Har bir kassa ustida quyidagi amallar mavjud:

* **Kirim** – kassaga pul tushumini kiritish (masalan: savdo tushumi, qarz qaytishi)
* **Chiqim** – kassadan pul chiqimini rasmiylashtirish (masalan: xarajatlar, yetkazib beruvchiga to‘lov)
* **Ko‘chirish** – mablag‘ni bir kassadan boshqasiga o‘tkazish (ichki transfer)
* **Ko‘proq** – qo‘shimcha sozlamalar va amallar (tahrirlash, o‘chirish va boshqalar)

Bu yondashuv foydalanuvchiga kassalar holatini tezkor baholash va amallarni tez bajarish imkonini beradi.

<figure><img src="../../.gitbook/assets/image (429).png" alt=""><figcaption></figcaption></figure>



#### Umumiy balanslar

Oynaning yuqori qismida ko‘rsatiladigan balanslar **barcha kassalar yig‘indisi emas**, balki **tanlangan kassa ichidagi mablag‘larning taqsimotini** aks ettiradi. Bu blok orqali foydalanuvchi aynan bitta kassadagi pulning qayerda va qanday ko‘rinishda saqlanayotganini ko‘rishi mumkin.

Quyidagi ko‘rsatkichlar chiqariladi:

* **Naqd** – kassadagi naqd pul qoldig‘i
* **Terminal** – terminal orqali tushgan mablag‘lar
* **Valyuta (USD va boshqalar)** – xorijiy valyutadagi mablag‘lar
* **Elektron to‘lovlar (Click va boshqalar)** – elektron to‘lov tizimlari orqali tushgan summalar

Ushbu qiymatlar **bir kassaning ichidagi mablag‘larning manbalar bo‘yicha bo‘linishini** bildiradi.

Masalan, kassada umumiy **1000$** mavjud bo‘lsa:

* 100$ – terminal orqali tushgan
* 100$ – naqd USD
* 9 000 000 so‘m – naqd so‘m

Tizim ushbu mablag‘larni alohida ko‘rsatadi, lekin ularning barchasi **bitta kassaning umumiy balansini tashkil qiladi**.

Shu orqali foydalanuvchi:

* pulning **qayerda (kanal bo‘yicha)** turganini
* va **qanday ko‘rinishda (valyuta va to‘lov turi bo‘yicha)** saqlanayotganini

aniq va tez tushunishi mumkin.

<figure><img src="../../.gitbook/assets/image (431).png" alt=""><figcaption></figcaption></figure>

#### Tranzaksiyalar

Kassa bo‘limining markaziy qismi – bu barcha pul harakatlari aks ettiriladigan tranzaksiyalar jadvali hisoblanadi. Har bir operatsiya alohida yozuv sifatida saqlanadi va quyidagi ma’lumotlarni o‘z ichiga oladi:

* **Raqami** – tranzaksiyaning noyob identifikatori
* **Sana va vaqt** – operatsiya yaratilgan va yakunlangan vaqt
* **Kirim / Chiqim** – pulning kassaga kirgani yoki chiqgani va summasi
* **To‘lov usuli** – naqd, terminal, elektron to‘lov va boshqalar
* **Holati** – operatsiya holati (masalan: bajarildi)
* **To‘lov turi** – operatsiyaning biznes konteksti (savdo, qaytarish, xizmat va boshqalar)
* **Kassa** – operatsiya qaysi kassada amalga oshirilgani

Jadval pastki qismida:

* **Jami kirim va chiqimlar** – tanlangan filtrlar asosida umumiy hisob-kitob ko‘rsatiladi

Bu jadval audit, nazorat va tahlil uchun asosiy manba hisoblanadi.

<figure><img src="../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>



#### Tranzaksiya tafsilotlari

Tranzaksiyalar ro‘yxatidagi istalgan yozuv ustiga bosilganda, uning batafsil ma’lumotlari o‘ng tomonda alohida oynada ochiladi.

Bu oynada quyidagi ma’lumotlar ko‘rsatiladi:

* **Check raqami** – operatsiya raqami
* **Tashkilot** – operatsiya tegishli tashkilot
* **Qurilma** – operatsiya amalga oshirilgan qurilma (agar mavjud bo‘lsa)
* **Turi** – operatsiya turi (masalan: qarz olish, savdo)
* **Yaratildi** – operatsiya yaratilgan sana va vaqt
* **Kassa** – qaysi kassada amalga oshirilgani
* **Kassir** – operatsiyani bajargan foydalanuvchi
* **To‘lov usuli** – naqd, terminal va boshqalar
* **Izoh** – qo‘shimcha ma’lumot (agar kiritilgan bo‘lsa)
* **Boshlanish sanasi** – operatsiya boshlanish vaqti

Oynaning pastki qismida:

* operatsiyaning **summasi** (masalan: 100 000 UZS)
* va uning **holati** (masalan: Yakunlangan) ko‘rsatiladi

<figure><img src="../../.gitbook/assets/image (440).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Kassaga kirim qilish</summary>

**Kirim** amali orqali kassaga pul tushumi kiritiladi. Ushbu amal savdo tushumlari, qarz qaytimi yoki boshqa moliyaviy kirimlarni rasmiylashtirish uchun ishlatiladi.

#### Kirim qilish

Kirim qilish uchun kassa kartasidagi **Kirim** tugmasi bosiladi va o‘ng tomonda kirim oynasi ochiladi.

Oynada quyidagi ma’lumotlar kiritiladi:

* **Kassa** – pul tushadigan kassa (odatda tanlangan bo‘ladi)
* **Hisob faktura** – agar operatsiya hujjat bilan bog‘liq bo‘lsa tanlanadi
* **To‘lov turi** – operatsiya mazmuni (savdo, qaytarish va boshqalar)
* **To‘lov usuli** – pul qanday kelib tushgani (naqd, terminal, karta va boshqalar)
* **Summa** – kirim qilinayotgan mablag‘ miqdori
* **Valyuta** – summa qaysi valyutada ekanligi
* **Izoh** – qo‘shimcha ma’lumot kiritish uchun ixtiyoriy maydon
* **Fayl** – chek yoki boshqa hujjat biriktirish imkoniyati

<figure><img src="../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (439).png" alt=""><figcaption></figcaption></figure>

#### Saqlash

Kiritilgan ma’lumotlar asosida quyidagi amallar bajariladi:

* **Saqlash** – ma’lumotlarni saqlaydi
* **Saqlash va yopish** – saqlab oynani yopadi
* **Bekor qilish** – amalni bekor qiladi

#### Natija

Kirim saqlangandan so‘ng:

* kassa balansi oshadi
* yuqoridagi balans blokida (naqd, terminal va boshqalar) mos ravishda yangilanadi
* tranzaksiyalar jadvalida yangi yozuv paydo bo‘ladi
* operatsiya holati **Bajarildi** bo‘ladi

</details>

<details>

<summary>Kassadan chiqim qilish</summary>

**Chiqim** amali orqali kassadan pul chiqimi rasmiylashtiriladi. Ushbu amal xarajatlar, yetkazib beruvchilarga to‘lovlar yoki boshqa moliyaviy chiqimlarni tizimda qayd etish uchun ishlatiladi.

#### Chiqim qilish

Chiqim qilish uchun kassa kartasidagi **Chiqim** tugmasi bosiladi va o‘ng tomonda chiqim oynasi ochiladi.

Oynada quyidagi ma’lumotlar kiritiladi:

* **Kassa** – pul chiqayotgan kassa (odatda tanlangan bo‘ladi)
* **Hisob faktura** – agar operatsiya hujjat bilan bog‘liq bo‘lsa tanlanadi
* **To‘lov turi** – operatsiya mazmuni (masalan: xarajat, to‘lov va boshqalar)
* **To‘lov usuli** – pul qanday chiqayotganini bildiradi (naqd, terminal va boshqalar)
* **Summa** – chiqim qilinayotgan mablag‘ miqdori
* **Valyuta** – summa qaysi valyutada ekanligi
* **Izoh** – qo‘shimcha ma’lumot kiritish uchun ixtiyoriy maydon
* **Fayl** – chek yoki hujjat biriktirish imkoniyati

<figure><img src="../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (441).png" alt=""><figcaption></figcaption></figure>



</details>

<details>

<summary>Kassada ko'chirish</summary>

Ko‘chirish amali orqali bir kassadagi mablag‘ni boshqa kassaga o‘tkazish mumkin. Ushbu funksiya tizimda **2 yoki undan ortiq kassa mavjud bo‘lganda** ishlaydi va ichki pul harakatlarini boshqarish uchun qo‘llaniladi.

<figure><img src="../../.gitbook/assets/image (435).png" alt=""><figcaption></figcaption></figure>



#### Ko‘chirish qilish

Ko‘chirishni amalga oshirish uchun kassa kartasidagi **Ko‘chirish** tugmasi bosiladi va o‘ng tomonda maxsus forma ochiladi.

Oynada quyidagi ma’lumotlar kiritiladi:

* **Kassa** – pul chiqayotgan (yuboruvchi) kassa
* **Qabul qiluvchi kassa** – pul o‘tkaziladigan kassa
* **To‘lov usuli** – pul qanday ko‘chirilayotgani (naqd, terminal va boshqalar)
* **Summa** – o‘tkazilayotgan mablag‘ miqdori
* **Valyuta** – pul birligi
* **Izoh** – qo‘shimcha ma’lumot (ixtiyoriy)
* **Fayl** – kerak bo‘lsa hujjat biriktirish

<figure><img src="../../.gitbook/assets/image (443).png" alt=""><figcaption></figcaption></figure>

#### Jarayon

Ko‘chirish amali ikki bosqichda ishlaydi:

* **Yuborish (Jarayonda)**
  * Ko‘chirish saqlangandan so‘ng operatsiya **Jarayonda** holatiga o‘tadi
  * Pul yuboruvchi kassadan chiqim sifatida hisoblanadi
  * Qabul qiluvchi kassada esa ushbu operatsiya **kutilayotgan (pending)** hujjat sifatida ko‘rinadi

<div><figure><img src="../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/image (446).png" alt=""><figcaption></figcaption></figure>

* **Qabul qilish (Yakunlangan)**
  * Qabul qiluvchi kassa tomonidan operatsiya tasdiqlangandan so‘ng
  * Pul qabul qiluvchi kassaga kirim sifatida tushadi
  * Har ikkala kassada ham operatsiya holati **Yakunlangan** bo‘ladi

</details>

<details>

<summary>Kassada ayirboshlash</summary>

Kassa bo‘limida ayirboshlash amali orqali mablag‘larni **valyuta bo‘yicha** yoki **to‘lov usuli bo‘yicha** o‘zgartirish mumkin. Ushbu amallar kassadagi pulni ichki boshqarish va to‘g‘ri taqsimlash uchun ishlatiladi.

<figure><img src="../../.gitbook/assets/image (436).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (437).png" alt=""><figcaption></figcaption></figure>

### Ayirboshlash (Pulni)

Bu amal orqali kassadagi mablag‘ni bir valyutadan boshqa valyutaga o‘tkazish mumkin.

#### Ayirboshlash qilish

**Ko‘proq → Ayirboshlash (Pulni)** orqali amalga oshiriladi.

Quyidagi ma’lumotlar kiritiladi:

* **Kassa** – operatsiya amalga oshiriladigan kassa
* **To‘lov usuli** – pul qaysi kanal orqali ayirboshlanmoqda

**Chiqim:**

* **Summa** – chiqayotgan summa
* **Valyuta** – chiqayotgan valyuta

**Kirim:**

* **Summa** – kirayotgan summa
* **Valyuta** – kirayotgan valyuta
* **Izoh** – qo‘shimcha ma’lumot
* **Fayl** – hujjat biriktirish (ixtiyoriy)

#### Jarayon

* Bir valyutada **chiqim** qilinadi
* Boshqa valyutada **kirim** qilinadi

Masalan:\
100$ → 1 200 000 so‘m

* 100$ chiqim
* 1 200 000 so‘m kirim

<figure><img src="../../.gitbook/assets/image (447).png" alt=""><figcaption></figcaption></figure>





### Ayirboshlash (To‘lov usulini)

Bu amal orqali mablag‘ni bir to‘lov turidan boshqasiga o‘tkazish mumkin (valyuta o‘zgarmaydi).

#### Ayirboshlash qilish

**Ko‘proq → Ayirboshlash (To‘lov usulini)** orqali amalga oshiriladi.

Quyidagi ma’lumotlar kiritiladi:

* **Kassa** – operatsiya amalga oshiriladigan kassa
* **Valyuta** – mablag‘ valyutasi

**Chiqim:**

* **Summa** – chiqayotgan summa
* **To‘lov usuli** – pul chiqayotgan kanal

**Kirim:**

* **Summa** – kirayotgan summa
* **To‘lov usuli** – pul kirayotgan kanal
* **Izoh** – qo‘shimcha ma’lumot
* **Fayl** – hujjat biriktirish (ixtiyoriy)

#### Jarayon

* Bir to‘lov usulidan **chiqim** qilinadi
* Boshqa to‘lov usuliga **kirim** qilinadi

Masalan:\
100 000 so‘m karta → naqd

* 100 000 so‘m kartadan chiqim
* 100 000 so‘m naqdga kirim

<figure><img src="../../.gitbook/assets/image (438).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (448).png" alt=""><figcaption></figcaption></figure>

</details>

