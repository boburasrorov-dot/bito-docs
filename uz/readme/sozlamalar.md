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

# Sozlamalar

<details>

<summary>Sozlamalar bo'limi </summary>

Sozlamalar bo‘limi tizimning barcha asosiy parametrlarini boshqarish va moslashtirish imkonini beradi. Ushbu bo‘lim orqali foydalanuvchi tizim funksiyalarini yoqish yoki o‘chirish, turli modullar bo‘yicha sozlamalarni o‘zgartirish hamda biznes jarayonlarga mos konfiguratsiya qilish imkoniyatiga ega bo‘ladi. Bu bo‘lim tizimni moslashuvchan boshqarish va optimallashtirish uchun muhim hisoblanadi.

Chap menyudan **Sozlamalar** bo‘limiga kiriladi. Ushbu bo‘limga kirilganda umumiy sozlamalar oynasi ochiladi.

<figure><img src="../.gitbook/assets/image (510).png" alt=""><figcaption></figcaption></figure>

Sozlamalar oynasi bir nechta asosiy qismlardan iborat:

Yuqori qismda tablar (bo‘limlar) joylashgan bo‘lib, ular orqali turli yo‘nalishdagi sozlamalarga o‘tish mumkin. Masalan:

* **Sozlamalar** – umumiy tizim sozlamalari
* **CRM** – mijozlar bilan ishlashga oid sozlamalar
* **Ombor** – ombor va mahsulotlarga oid sozlamalar
* **Tashkilotlar** – kompaniya va filial sozlamalari
* **Foydalanuvchi sozlamalari** – foydalanuvchi bilan bog‘liq parametrlar
* **Obuna / Bitoverse** – qo‘shimcha xizmat va modullar

Agar foydalanuvchi ma’lum bir yo‘nalish (masalan, ombor) bo‘yicha sozlamalarni ko‘rmoqchi bo‘lsa, yuqoridagi tegishli tabni tanlaydi va tizim avtomatik ravishda shu bo‘lim sozlamalariga o‘tadi.

<figure><img src="../.gitbook/assets/image (512).png" alt=""><figcaption></figcaption></figure>

Chap tomonda sozlamalar ro‘yxati joylashgan bo‘lib, unda barcha mavjud sozlamalar kategoriyalar kesimida ko‘rsatiladi.

Chap menyudagi asosiy sozlamalar:

* **Umumiy** – tizimning asosiy funksional sozlamalari
* **To‘lov usuli** – to‘lov turlarini boshqarish
* **Chek** – чек va chop etish sozlamalari
* **Bot habarlari** – bot orqali yuboriladigan xabarlar sozlamasi
* **SMS sozlamasi** – SMS yuborish parametrlarini sozlash
* **Marketing SMS sozlamasi** – marketing xabarlarini boshqarish
* **Etiketka** – mahsulot etiketkalari sozlamalari
* **Sodiqlik kartasi** – bonus va sodiqlik tizimi sozlamalari
* **Qurilma** – qurilmalar bilan ishlash sozlamalari
* **Qurilma xavfsizlik** – qurilma xavfsizlik parametrlari
* **Ochiq cheklar** – ochiq cheklarni boshqarish
* **Savdo sozlamalari** – savdo jarayoniga oid sozlamalar
* **Tarozi sozlamalari** – tarozi integratsiyasi sozlamalari
* **Distribusiya sozlamalari** – distribusiya jarayonlari sozlamalari
* **Moliya sozlamalari** – moliyaviy parametrlar
* **Quti turlari** – mahsulotlar uchun qadoqlash (quti) turlarini yaratish va boshqarish imkonini beradi
* **Cashback** – mijozlar uchun cashback (qaytim bonus) tizimini sozlash va boshqarish
* **Mijoz eslatmalari** – mijozlar bilan ishlash jarayonida eslatma va bildirishnomalarni sozlash
* **Onlayn to‘lov sozlamalari** – onlayn to‘lov tizimlari va ularning parametrlarini sozlash
* **Chop etish shablonlari** – чек va boshqa hujjatlar uchun chop etish shablonlarini sozlash

CRM bo‘limiga oid sozlamalar:

* **Faollik indekslari** – mijozlar yoki agentlar faoliyatini baholash mezonlarini sozlash

Ombor bo‘limiga oid sozlamalar:

* **O‘lchov birliklari** – mahsulotlar uchun o‘lchov birliklarini yaratish va boshqarish
* **Attributlar** – mahsulot atributlarini (xususiyatlarini) sozlash

Tashkilotlar bo‘limiga oid sozlamalar:

* **Tashkilotlar** – kompaniya va filiallar ma’lumotlarini boshqarish
* **Qarzdorlik limiti** – mijozlar uchun maksimal qarz limitini belgilash
* **Qarzdorlik sanasi** – qarzdorlik muddati va to‘lov sanalarini sozlash

Foydalanuvchi sozlamalari:

* **Foydalanuvchi sozlamalari** – foydalanuvchilarga oid individual sozlamalar va parametrlar

Obuna va tizim modullari:

* **Obuna** – tizim obunasi va tarif rejalarini boshqarish
* **Bitoverse** – qo‘shimcha xizmatlar va platforma integratsiyalarini boshqarish

Foydalanuvchi chap tomondagi istalgan sozlama ustiga bosganda, shu sozlamaga tegishli oyna o‘ng tomonda ochiladi va u yerda parametrlarni o‘zgartirish mumkin bo‘ladi.

O‘ng tomonda tanlangan sozlamaga mos parametrlar ko‘rsatiladi. Bu yerda odatda funksiyalarni yoqish/o‘chirish (toggle), qiymatlarni kiritish yoki qo‘shimcha sozlashlar amalga oshiriladi.

<figure><img src="../.gitbook/assets/image (513).png" alt=""><figcaption></figcaption></figure>

Ushbu bo‘limning asosiy xususiyati shundaki, barcha tizim sozlamalari yagona joyda jamlangan va modullar kesimida boshqariladi. Bu esa foydalanuvchiga tizimni o‘z biznes jarayonlariga moslashtirish, funksiyalarni nazorat qilish va ishlash samaradorligini oshirish imkonini beradi.



</details>

<details>

<summary>Umumiy </summary>

Ushbu bo‘lim orqali tizimdagi barcha modullar va ularning ichki funksiyalarini boshqarish (yoqish/o‘chirish) mumkin. Bu orqali foydalanuvchi o‘z biznes jarayoniga mos bo‘lmagan bo‘limlarni o‘chirib, interfeysni soddalashtirishi mumkin.

**Modul darajasida boshqaruv**

* **Modulni o‘chirish** – tanlangan modul (masalan, Distributsiya) to‘liq tizimdan yashiriladi

<figure><img src="../.gitbook/assets/image (514).png" alt=""><figcaption></figcaption></figure>

* **Modulni yoqish** – modul yana qayta tiklanadi va barcha funksiyalari bilan ko‘rinadi

<figure><img src="../.gitbook/assets/image (515).png" alt=""><figcaption></figcaption></figure>

**Modul ichidagi oynalarni boshqarish**

* **Oynalarni o‘chirish** – modul ichidagi alohida funksiyalar (masalan, ko‘chirish sabablari, ichki ko‘chirishlar) ko‘rinmaydi

<figure><img src="../.gitbook/assets/image (517).png" alt=""><figcaption></figcaption></figure>

* **Oynalarni yoqish** – o‘sha funksiyalar qayta aktiv holatga keladi

<figure><img src="../.gitbook/assets/image (518).png" alt=""><figcaption></figcaption></figure>



#### Umumiy sozlamalar (asosiy parametrlar)

* **Mahsulot belgilari** – mahsulot yaratishda maxsus belgilar (label) qo‘shish imkonini beradi. O‘chirilsa, bu funksiya mavjud bo‘lmaydi
* **Chek** – chek chiqarish funksiyasini boshqaradi. O‘chirilsa, chek sozlamalari ham yo‘qoladi va chek chiqarib bo‘lmaydi
* **Mahsulotlar uchun eslatma** – mahsulotlarga eslatma qo‘shish imkonini beradi
* **Variant mahsulot** – mahsulot variantlarini (masalan, rang, o‘lcham) yaratish imkonini beradi
* **Tarkibli mahsulot** – bir nechta mahsulotdan iborat mahsulot (komplekt) yaratish imkonini beradi
* **Joylashuv** – ombor ichida joylashuvlar (lokatsiyalar) bilan ishlashni yoqadi/o‘chiradi
* **Bir nechta o‘lchov birligi** – mahsulotni bir nechta o‘lchov birliklarida yuritish imkonini beradi
* **Yaroqlilik muddati** – mahsulotlarga amal qilish muddati (expiry date) qo‘shish imkonini beradi
* **Quti turi** – mahsulotni quti (upakovka) asosida yuritish imkonini beradi
  * Agar **bir nechta o‘lchov birligi yoqilgan bo‘lsa**, quti turini yoqib bo‘lmaydi
  * Agar **quti turi yoqilgan bo‘lsa**, bir nechta o‘lchov birligini yoqib bo‘lmaydi
  * Sababi: ikkala funksiya bir xil vazifani qisman qoplaydi
* **Multi ombor** – bir nechta ombor bilan ishlash imkonini beradi
  * O‘chirilsa → faqat bitta ombor ishlaydi
  * Agar tizimda bir nechta ombor mavjud bo‘lsa → bu sozlamani o‘chirib bo‘lmaydi
*   **POS** – savdo nuqtasi (Point of Sale) funksiyasini yoqish/o‘chirish

    * O‘chirilsa → savdo oynalari ishlamaydi

    <figure><img src="../.gitbook/assets/image (520).png" alt=""><figcaption></figcaption></figure>



* **Barcha modullarni boshqarish** – sahifani pastga scroll qilganda tizimdagi barcha modullar ro‘yxati chiqadi
* **Modullarni o‘chirish** – kerak bo‘lmagan modullarni o‘chirib, tizimdan yashirish mumkin
* **Modullarni yoqish** – o‘chirilgan modullarni qayta yoqib, tizimda ko‘rsatish mumkin

<div><figure><img src="../.gitbook/assets/image (521).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (522).png" alt=""><figcaption></figcaption></figure></div>

</details>

<details>

<summary>To'lov usuli</summary>

Ushbu bo‘lim orqali tizimda ishlatiladigan barcha to‘lov turlarini yaratish, tahrirlash va boshqarish mumkin. Faol (yoqilgan) to‘lov usullari savdo jarayonida foydalanish uchun mavjud bo‘ladi.

<figure><img src="../.gitbook/assets/image (523).png" alt=""><figcaption></figcaption></figure>



* **Nomi** – to‘lov usulining nomi (masalan: Naqd, Karta, Click)
*   **Holati** – to‘lov usulining aktiv yoki noaktiv ekanligini bildiradi

    * Yoqilgan bo‘lsa → tizimda foydalaniladi
    * O‘chirilgan bo‘lsa → savdoda ko‘rinmaydi



**To‘lov usuli qo'shish:**

* **To‘lov usulini qo‘shish** – yangi to‘lov turini yaratish oynasini ochadi
* **Nomi** – to‘lov usulining nomi
* **Tezkor klavish** – ushbu to‘lov turini tez tanlash uchun klaviatura tugmasi (shortcut)
* **Komissiya turi** – to‘lovda qo‘llaniladigan komissiya turi

<figure><img src="../.gitbook/assets/image (527).png" alt=""><figcaption></figcaption></figure>



</details>

<details>

<summary>Chek</summary>

Ushbu bo‘lim orqali tizimda chiqariladigan chek (receipt) ko‘rinishini to‘liq sozlash mumkin. Bu yerda chekdagi matnlar, elementlar va umumiy dizayn boshqariladi.

**Umumiy ma’lumotlar**

* **Tashkilot** – chek qaysi tashkilot nomidan chiqarilishini belgilaydi
* **Chek turi** – chek turi (masalan: savdo, xarid)
* **Chek tili** – chekda chiqadigan til
* **Chekning sarlavhasi** – chek yuqorisida chiqadigan matn (masalan: “Savdo uchun rahmat”)
* **Chekni avtomatik chiqarish** – savdo yakunida chek avtomatik chiqishini yoqadi/o‘chiradi
* **Boshqa tashkilotlarga ham qo‘llash** – sozlamani bir nechta tashkilotga qo‘llash imkoniyati

<figure><img src="../.gitbook/assets/image (528).png" alt=""><figcaption></figcaption></figure>

**Dizayn va ko‘rinish**

* **Font stili** – matn ko‘rinishini (qalin, kursiv, tagi chizilgan) sozlash
* **Logotip** – chekga kompaniya logotipini yuklash

<figure><img src="../.gitbook/assets/image (529).png" alt=""><figcaption></figcaption></figure>



Pastga scroll qilganda chekda qaysi ma’lumotlar chiqishini boshqarish mumkin:

* Checkbox orqali elementlarni **yoqish/o‘chirish**
*   Masalan:

    * Logotip
    * Chek sarlavhasi
    * Tashkilot nomi
    * Tranzaksiya ma’lumotlari
    * Mahsulotlar ro‘yxati
    * Jami summa va boshqalar

    <figure><img src="../.gitbook/assets/image (530).png" alt=""><figcaption></figcaption></figure>



O‘ng tomonda chekning **real vaqt preview (namuna)** ko‘rinishi beriladi:

* Kiritilgan o‘zgarishlar darhol aks etadi
* Chek qanday chiqishini oldindan ko‘rish mumkin

<figure><img src="../.gitbook/assets/image (531).png" alt=""><figcaption></figcaption></figure>



</details>

<details>

<summary>Bot habari</summary>

Ushbu bo‘lim orqali tizimdan yuboriladigan bot xabarlari (masalan, Hisobot bot, Customer bot) tarkibini va ko‘rinishini sozlash mumkin.

<figure><img src="../.gitbook/assets/image (532).png" alt=""><figcaption></figcaption></figure>

* **Bot tanlash** – yuqori qismda qaysi bot uchun sozlama qilinayotgani tanlanadi (masalan: Hisobot bot)
* **Modul tanlash** – bot qaysi modul bo‘yicha xabar yuborishini belgilaydi (masalan: Savdo, Ishlab chiqarish va boshqalar)

<figure><img src="../.gitbook/assets/image (533).png" alt=""><figcaption></figcaption></figure>



Pastki qismda checkboxlar orqali xabarda chiqadigan ma’lumotlar tanlanadi:

* Raqami
* Kodi
* Mas’ul shaxs
* Tashkilot nomi
* Holati
* Omborlar (chiqarish va joylashuv)
* Sana va vaqtlar
* Valyuta
* Tarkib va boshqa ma’lumotlar
* ...

Har bir elementni:

* **Yoqish** → xabarda ko‘rinadi
* **O‘chirish** → xabardan olib tashlanadi



**Vizual preview**

O‘ng tomonda tanlangan sozlamalar asosida:

* Xabar qanday ko‘rinishda yuborilishi
* Qaysi ma’lumotlar chiqishi

real vaqt rejimida ko‘rsatiladi.

<figure><img src="../.gitbook/assets/image (534).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>SMS sozlamasi</summary>

Ushbu bo‘lim orqali mijozlarga yuboriladigan SMS xabarlarni avtomatlashtirish va sozlash mumkin. Asosan qarzdorlik, bo‘lib to‘lash yoki boshqa eslatmalar uchun ishlatiladi.

* **Tashkilot** – SMS qaysi tashkilot nomidan yuborilishini belgilaydi
* **Turi** – SMS qaysi jarayon uchun yuborilishini tanlash:
  * Qarz
  * Bo‘lib to‘lash
* **Yoqish (toggle)** – ushbu SMS turini aktiv yoki noaktiv qilish
* **Boshqa tashkilotlarga ham qo‘llash** – sozlamani bir nechta tashkilotga tatbiq qilish
* **Tashkilotlar** – agar yuqoridagi sozlama yoqilsa, qaysi tashkilotlarga tegishli ekanligi tanlanadi

#### Shablon va integratsiya

* **Shablon** – yuboriladigan SMS matni (template) tanlanadi (integratsiya->xabarlardan yaratiladi)
* **Integratsiya** – SMS provayder yoki xizmat bilan ulanish (SMS orqali yuborish tanlanganda chiqadi)

<figure><img src="../.gitbook/assets/image (535).png" alt=""><figcaption></figcaption></figure>



* **Necha kun oldin xabar berish** – muddatdan oldin eslatma yuborish (masalan: 3 kun oldin)
* **Muddat o‘tgandan keyin necha kun xabar berish** – kechikkan holatda eslatma
* **Eslatish soati** – SMS yuboriladigan aniq vaqt
* **Necha kun oldin xabar berish** – muddatdan oldin eslatma yuborish (masalan: 3 kun oldin)
* **Muddat o‘tgandan keyin necha kun xabar berish** – kechikkan holatda eslatma
* **Eslatish soati** – SMS yuboriladigan aniq vaqt
* **SMS orqali yuborish** – SMS sifatida yuborish
* **Bot orqali yuborish** – Telegram yoki boshqa bot orqali yuborish

<figure><img src="../.gitbook/assets/image (536).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Marketing SMS sozlamasi</summary>

Ushbu bo‘lim orqali marketingga oid SMS xabarlarni sozlash mumkin. Asosan **kutilayotgan tovarlar (yetib kelgan mahsulotlar)** haqida mijozlarga avtomatik xabar yuborish uchun ishlatiladi.

<figure><img src="../.gitbook/assets/image (540).png" alt=""><figcaption></figcaption></figure>

* **Shablon** – yuboriladigan SMS matni (template) tanlanadi
* **SMS orqali yuborish** – xabarni SMS sifatida yuborish (tanlanganda integratsiya tanlash chiqadi)
* **Bot orqali yuborish** – xabarni bot (masalan, Telegram) orqali yubor



* Ushbu sozlama **faqat marketing maqsadlari uchun** ishlatiladi
* Ko‘pincha:
  * Kutilgan mahsulot kelganda
  * Yangi tovarlar kelib tushganda
  * Mijozni xabardor qilish kerak bo‘lgan holatlarda

ishlatiladi

</details>

<details>

<summary>Etiketka</summary>

Ushbu bo‘lim orqali mahsulotlar uchun etiketkalar (yorliqlar) yaratish va ularning dizaynini to‘liq sozlash mumkin.

**Etiketkalar ro‘yxati**

* Bu yerda yaratilgan barcha etiketkalar ko‘rinadi
* **Etiketka yaratish** tugmasi orqali yangi etiketka qo‘shiladi
*   Har bir etiketkani:

    * tahrirlash&#x20;
    * o‘chirish&#x20;

    mumkin

<figure><img src="../.gitbook/assets/image (541).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

Yangi etiketka yaratishda quyidagilar kiritiladi:

* **Nomi** – etiketka nomi
* **Uzunligi (mm)** – etiketka eni
* **Balandligi (mm)** – etiketka bo‘yi

Markaziy qismda esa etiketkaning **vizual dizayni** tuziladi.

<figure><img src="../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

#### Element qo‘shish

Etiketkaga elementlar qo‘shish uchun “+” tugmasi bosiladi va quyidagi variantlardan tanlanadi:

* **Matn** – oddiy yozuv (masalan: mahsulot nomi)
* **Rasm** – logo yoki boshqa rasm yuklash
* **Shtrix-kod** – mahsulot barkodi yoki ichki kod
* **Chiziq** – dizayn uchun ajratuvchi chiziq

Har bir element qo‘shilgach, etiketka ichida joylashtiriladi.

<figure><img src="../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

<div><figure><img src="../.gitbook/assets/image (546).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (547).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (548).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (549).png" alt=""><figcaption></figcaption></figure></div>

#### Dizaynni boshqarish

* Qo‘shilgan elementlar o‘ng tomonda ro‘yxat ko‘rinishida chiqadi
* Har bir elementni:
  * o‘chirish ❌
  * joylashuvini o‘zgartirish\
    mumkin
* Markazda etiketkaning real ko‘rinishi preview sifatida ko‘rsatiladi

<figure><img src="../.gitbook/assets/image (550).png" alt=""><figcaption></figcaption></figure>



</details>

<details>

<summary>Sodiqlik kartasi</summary>

Ushbu bo‘lim orqali mijozlar uchun **sodiqlik kartalari (loyalty cards)** ni yaratish va ularning dizaynini sozlash mumkin. Funksional jihatdan bu bo‘lim etiketka sozlamasiga o‘xshash ishlaydi.



* Bu yerda barcha yaratilgan kartalar ko‘rinadi
* **“Sodiqlik kartasi yaratish”** orqali yangi karta qo‘shiladi
*   Har bir kartani:

    * tahrirlash&#x20;
    * o‘chirish&#x20;

    mumkin

<figure><img src="../.gitbook/assets/image (551).png" alt=""><figcaption></figcaption></figure>

Yangi karta yaratishda quyidagi parametrlar kiritiladi:

* **Nomi** – karta nomi
* **Uzunligi (mm)** – karta eni
* **Balandligi (mm)** – karta bo‘yi

Markaziy qismda karta dizayni vizual tarzda tuziladi.

<figure><img src="../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

Kartaga element qo‘shish uchun “+” tugmasi orqali quyidagilar tanlanadi:

* **Matn** – mijoz ismi, karta nomi va boshqa yozuvlar
* **Rasm** – kompaniya logotipi yoki fon rasmi
* **Shtrix-kod** – karta identifikatori (barcode)
* **Chiziq** – dizayn elementlari uchun

<figure><img src="../.gitbook/assets/image (553).png" alt=""><figcaption></figcaption></figure>

* Qo‘shilgan elementlar kartada joylashtiriladi
* O‘ng tomonda elementlar ro‘yxati chiqadi
* Har bir elementni:
  * o‘chirish&#x20;
  * joylashuvini o‘zgartirish\
    mumkin
* Markaziy qismda karta qanday ko‘rinishi **real preview** sifatida ko‘rsatiladi

</details>

<details>

<summary>Qurilma</summary>

Ushbu bo‘lim orqali xodimlarning **mobil ilovaga kirishi uchun qurilmalar (device)** yaratiladi va boshqariladi.

**Qurilmalar ro‘yxati**

* Bu yerda yaratilgan barcha qurilmalar ko‘rinadi
* Har bir qurilma uchun:
  * nomi
  * holati (tasdiqlangan / bekor qilingan)\
    ko‘rsatiladi
* **“Qurilma qo‘shish”** orqali yangi qurilma yaratiladi

<figure><img src="../.gitbook/assets/image (554).png" alt=""><figcaption></figcaption></figure>

Yangi qurilma qo‘shishda:

* **Nomi** – qurilma nomi (masalan: telefon nomi yoki xodim nomi bilan)
* **Xodim almashishi** – kerak bo‘lsa qurilmani boshqa xodim ishlatishi uchun ruxsat

So‘ng **saqlash** orqali qurilma tizimga qo‘shiladi.

<figure><img src="../.gitbook/assets/image (555).png" alt=""><figcaption></figcaption></figure>

* Agar **“Qurilmalarni cheklash”** (Qurilma xavfsizlik sozlamasida) yoqilgan bo‘lsa:\
  → faqat shu yerda yaratilgan qurilmalar orqali tizimga kirish mumkin
* Agar qurilma yaratilmagan bo‘lsa:\
  → xodim mobil ilovaga kira olmaydi



1. Bitoda xodim yaratiladi
2. Shu bo‘limdan unga mos **qurilma yaratiladi**
3. Xodim mobil ilovada login qiladi
4. Tizimdan **yaratilgan qurilmani tanlaydi**
5. Shundan keyin tizimga kirish mumkin bo‘ladi

</details>

<details>

<summary>Qurilma xavfsizlik</summary>

Ushbu bo‘lim tizimga kirishni **qurilmalar orqali nazorat qilish va xavfsizlikni oshirish** uchun xizmat qiladi.

**Qurilmalarni cheklashni yoqish**

* Agar yoqilgan bo‘lsa:\
  → tizimga faqat **oldindan yaratilgan qurilmalar** orqali kirish mumkin
* Agar o‘chirilgan bo‘lsa:\
  → istalgan qurilmadan kirish mumkin (cheklovsiz)

**Webdan kirishni ham cheklash**

* Agar yoqilsa:\
  → qurilma cheklovi **faqat mobil emas, web (brauzer)** uchun ham amal qiladi
* Ya’ni, foydalanuvchi kompyuterdan ham faqat ruxsat etilgan qurilma orqali kira oladi

**Yangi qurilmalarni tasdiqlash**

* Agar yoqilgan bo‘lsa:\
  → yangi qurilmadan kirishga urinishda:
  * qurilma tizimga qo‘shiladi
  * lekin **admin tasdiqlamaguncha kirish bloklanadi**
* Agar o‘chirilgan bo‘lsa:\
  → yangi qurilmalar avtomatik ruxsat bilan kiradi (agar umumiy cheklov o‘chirilgan bo‘lsa)

**Ishlash logikasi**&#x20;

* **Qurilmalarni cheklash ON:**
  * faqat sozlamadagi qurilmalar ishlaydi
  * boshqa qurilma → kira olmaydi
* **Qurilmalarni cheklash OFF + Yangi qurilmani tasdiqlash ON:**
  * yangi qurilma kirishga urinadi
  * admin tasdiqlamaguncha → kirish bloklanadi

<figure><img src="../.gitbook/assets/image (557).png" alt=""><figcaption></figcaption></figure>

**IP manzillar ro‘yxati**

* Bu yerda ruxsat etilgan IP manzillar kiritiladi
* Agar yoqilgan bo‘lsa:\
  → faqat shu IP manzillardan tizimga kirish mumkin



</details>

<details>

<summary>Ochiq cheklar</summary>

Ushbu bo‘lim tizimdagi yakunlanmagan savdolarni (ochiq cheklarni) boshqarish uchun ishlatiladi. Bu yerda kassir tomonidan boshlangan, lekin hali yopilmagan savdolar saqlanadi va ularni keyinchalik davom ettirish yoki yakunlash mumkin.

Ochiq chek — bu mahsulotlar tanlangan, lekin savdo hali to‘liq tugallanmagan holat hisoblanadi.

<figure><img src="../.gitbook/assets/image (558).png" alt=""><figcaption></figcaption></figure>

* Ochiq cheklarni ro‘yxat ko‘rinishida ko‘rish
* Har bir chekni ochib davom ettirish
* Savdoni yakunlash (to‘lov qilish orqali)
* Keraksiz cheklarni o‘chirish

</details>

<details>

<summary>Savdo sozlamalari</summary>

Ushbu bo‘lim savdo jarayonining asosiy logikasini va cheklovlarini boshqarish uchun ishlatiladi. Bu yerda kassada ishlash tartibi, chegirmalar, qarz, cashback va boshqa muhim funksiyalar yoqiladi yoki o‘chiriladi.

<figure><img src="../.gitbook/assets/image (568).png" alt=""><figcaption></figcaption></figure>

#### Asosiy funksiyalar

* **Keshbek faolligi** → mijozlarga cashback berish funksiyasini yoqadi yoki o‘chiradi
* **Soliq faolligi** → savdoda soliq hisoblashni aktiv qiladi
* **Soliqni chegirmadan keyin hisoblash** → soliq avval emas, chegirmadan keyin hisoblanadi
* **Umumiy chegirmani mahsulotnikidan keyin hisoblash** → umumiy chegirma mahsulot chegirmalaridan keyin qo‘llanadi

<figure><img src="../.gitbook/assets/image (559).png" alt=""><figcaption></figcaption></figure>

#### Nazorat va tasdiqlash

* **Boshliq tomonidan tasdiqlangan chegirma** → katta chegirmalar faqat rahbar tasdig‘i bilan amalga oshiriladi
* **Qarz boshliq tomonidan tasdiqlanadi** → qarzga sotish uchun qo‘shimcha tasdiq talab qilinadi
* **Chegirmaga limit qo‘yish** → chegirmaga maksimal limit belgilash mumkin

<figure><img src="../.gitbook/assets/image (560).png" alt=""><figcaption></figcaption></figure>

#### Mahsulot va ko‘rsatish sozlamalari

* **Mahsulot yalpi og‘irligini ko‘rsatish**
* **Mahsulot sof og‘irligini ko‘rsatish** → mahsulot og‘irliklarini chek yoki interfeysda chiqarish

<figure><img src="../.gitbook/assets/image (561).png" alt=""><figcaption></figcaption></figure>

#### Savdo jarayoniga ta’sir qiluvchi sozlamalar

* **Eski sana bilan sotuv qilish** → oldingi sana bilan savdo qilishga ruxsat beradi
* **Buyurtmadan ko‘p sotish** → buyurtmadagi miqdordan ortiq sotishga ruxsat
* **Mijozni tanlash majburiy** → savdo qilishdan oldin mijozni tanlash talab qilinadi
* **Ochiq chekda mahsulotni band qilish** → ochiq chekda mahsulot zaxiradan band qilinadi

<figure><img src="../.gitbook/assets/image (562).png" alt=""><figcaption></figcaption></figure>



#### Qo‘shimcha savdo imkoniyatlari

* **Ko‘p valyutali chek** → bir nechta valyutada savdo qilish
* **Holatli sotuv** → savdoga statuslar biriktirish (masalan: yakunlangan)
* **Tezkor mahsulot yaratish** → savdo oynasidan chiqmasdan yangi mahsulot qo‘shish
* **Qolmagan tovarlarni sota olish** → stokda yo‘q mahsulotni sotishga ruxsat
* **Nol yoki manfiy narxlarni cheklash** → noto‘g‘ri narx bilan savdoni bloklash

<figure><img src="../.gitbook/assets/image (563).png" alt=""><figcaption></figcaption></figure>



#### To‘lov va qarz bilan ishlash

* **Qarzga sotish**→ mijozga qarzga savdo qilish
* **Bo‘lib to‘lash** → to‘lovni qismlarga bo‘lib olish imkoniyati

<figure><img src="../.gitbook/assets/image (564).png" alt=""><figcaption></figcaption></figure>



#### Cheklov va limitlar

* **Maksimal eski sana** → nechta kun oldingi sana bilan savdo qilish mumkinligini belgilaydi

<figure><img src="../.gitbook/assets/image (566).png" alt=""><figcaption></figcaption></figure>

* **Minimal va maksimal savdo miqdori** → savdoda miqdoriy cheklovlar o‘rnatiladi

<figure><img src="../.gitbook/assets/image (567).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Tarozi sozlamalari</summary>

Ushbu bo‘lim tarozi (elektron tarozi) bilan ishlash va **shtrix-kod orqali mahsulotni avtomatik aniqlash** jarayonini sozlash uchun ishlatiladi. Asosan og‘irlik bilan sotiladigan mahsulotlar (meva, sabzavot va h.k.) uchun muhim hisoblanadi.

<figure><img src="../.gitbook/assets/image (569).png" alt=""><figcaption></figcaption></figure>



Bu yerda tarozi bilan ishlashning asosiy parametrlari belgilanadi:

* **Tashkilot** → sozlama qaysi tashkilot uchun amal qilishini belgilaydi
* **Turi (Moslashtirilgan)** → tayyor yoki custom (moslashtirilgan) tarozi konfiguratsiyasini tanlash
* **Bo‘lim kodi** → tarozi shtrix-kodida mahsulot turini ajratish uchun ishlatiladi
* **Nuqtadan keyingi raqam** → og‘irlik nechta kasr son bilan olinishini belgilaydi\
  (masalan: 0.123 → 3 ta raqam)

#### Shtrix-kod strukturasini sozlash

Tarozi orqali keladigan shtrix-kod bir nechta qismlardan iborat bo‘ladi. Shu yerda u qanday tuzilishda bo‘lishi belgilanadi:

* **1-raqam** → bo‘lim kodi (tovar turi identifikatori)
* **2-raqam**→ qo‘shimcha identifikatsiya (yana bo‘lim yoki kategoriya)
* **3-raqam**→ mahsulot kodi (SKU)
* **4-raqam**→ nazorat raqami (tekshiruv uchun)
* **+ Qo‘shish**→ kerak bo‘lsa qo‘shimcha segmentlar qo‘shish mumkin\\



Tarozida mahsulot tortilganda:

* shtrix-kod generatsiya qilinadi
* unda:
  * mahsulot kodi
  * og‘irlik
  * boshqa segmentlar bo‘ladi
* tizim shu sozlamalar orqali:\
  → mahsulotni avtomatik topadi\
  → og‘irligini hisoblab narx chiqaradi

</details>

<details>

<summary>Distributsiya sozlamalari</summary>

Ushbu bo‘lim distribustiya (tarqatish) jarayonlarida ishlatiladigan **buyurtma turini belgilash** uchun xizmat qiladi. Ya’ni tizimda yaratiladigan buyurtmalar qaysi turga kirishini shu yerda sozlash mumkin.

<figure><img src="../.gitbook/assets/image (570).png" alt=""><figcaption></figcaption></figure>

Bu sahifada faqat bitta asosiy parametr mavjud:

* **Buyurtma turi** → distribustiya jarayonida ishlatiladigan buyurtma turini tanlaysiz\
  \- Sotuv  \
  \- Sotuv Buyurtma&#x20;

Qaysi biri tanlangan bo'lsa usha buyurtmalar shunga tushadi.

</details>

<details>

<summary>Moliya sozlamalari</summary>

Ushbu bo‘lim tizimda moliyaviy jarayonlarni boshqarish, ya’ni valyuta ishlashi va kassa (pul oqimi) bilan bog‘liq operatsiyalarni sozlash uchun xizmat qiladi.

<figure><img src="../.gitbook/assets/image (573).png" alt=""><figcaption></figcaption></figure>

* **Ko‘p valyutadan foydalanish** – tizimda bir nechta valyutada ishlash imkonini yoqadi
* **Asosiy valyutaga konvertatsiya qilish** – boshqa valyutalarda kiritilgan summalarni avtomatik asosiy valyutaga o‘giradi
* **Xizmat turi tannarxi** – xizmatlar tannarxini hisoblash usuli
  * _Fiksal_ – doimiy qiymat
  * _Narxlangan_ – mahsulot yoki xizmat narxiga bog‘liq hisoblanadi

<figure><img src="../.gitbook/assets/image (571).png" alt=""><figcaption></figcaption></figure>



* **Tashkilot** – qaysi tashkilot uchun kassa sozlanayotganini tanlaysiz
* **Kassa sessiyasini faollashtirish** – kassani sessiya asosida ishlashini yoqadi
* **Qurilmaga bog‘lash** – kassa sessiyasini ma’lum qurilmaga biriktiradi
* **Faqat ochiq qurilmada ishlash** – faqat ruxsat berilgan qurilmalarda ishlashga cheklaydi
* **IP manzilni cheklash** – faqat ma’lum IP orqali ishlashga ruxsat beradi
* **Farq limiti haqida ogohlantirish** – kassadagi pul farqi bo‘lsa ogohlantiradi
* **Avtomatik chiqish** – ma’lum vaqtdan keyin tizimdan avtomatik chiqadi
* **Kunlik sessiya limiti** – kun davomida sessiya uchun limit o‘rnatadi
* **Avtomatik xarajat** – xarajatlarni avtomatik hisobga olishni yoqadi
* **Avtomatik yopish vaqti** – kassa sessiyasi avtomatik yopiladigan vaqt

<figure><img src="../.gitbook/assets/image (572).png" alt=""><figcaption></figcaption></figure>

Moliya sozlamalari tizimdagi pul oqimlarini to‘g‘ri boshqarish, xatoliklarni kamaytirish va xavfsizlikni ta’minlash uchun juda muhim. Bu sozlamalar orqali siz valyuta operatsiyalarini nazorat qilasiz, kassa intizomini o‘rnatasiz va moliyaviy jarayonlarni avtomatlashtirasiz.

</details>

<details>

<summary>Quti turlari </summary>

Ushbu bo‘lim tizimda mahsulotlar uchun ishlatiladigan qadoqlash (quti) turlarini yaratish va boshqarish uchun xizmat qiladi. Ya’ni mahsulotlar qanday birlikda (quti, rulon va h.k.) hisoblanishini shu yerda sozlaysiz.

<figure><img src="../.gitbook/assets/image (574).png" alt=""><figcaption></figcaption></figure>

"Yaratish" tugmasini bosish orqali yaratish oynasi ochiladi va ma'lumotlar to'ldiriladi va saqlanadi

#### Asosiy ma’lumolar

* **Nomi** – quti turining to‘liq nomi (masalan: QUTI, RULON)
* **Qisqa nomi** – qisqartirilgan nomi (tezkor ko‘rish va ishlatish uchun)
* **Kodi** – quti turiga biriktirilgan unikal identifikator
* **Faolligi** – ushbu quti turini aktiv yoki noaktiv qilish

<figure><img src="../.gitbook/assets/image (575).png" alt=""><figcaption></figcaption></figure>

Quti turlari mahsulotlarni to‘g‘ri birliklarda yuritish, ombor va savdo jarayonlarini aniq hisoblash uchun muhim. Bu orqali siz bir xil mahsulotni turli qadoqlarda (masalan dona, quti, rulon) boshqarishingiz va tizimda tartibli ishlashni ta’minlaysiz.

</details>

<details>

<summary>Cashback</summary>

Ushbu bo‘lim mijozlar uchun cashback (qaytim bonus) tizimini sozlash va boshqarish imkonini beradi. Cashback orqali mijozlarga xarid qilgandan keyin ma’lum foiz yoki summa qaytariladi.

**Asosiy ma’lumotlar**

* **Tashkilot** – cashback qo‘llaniladigan tashkilot
* **Boshqa tashkilotlarga ham qo‘llash** – bir nechta tashkilotlarga bir xil cashback sozlamasini qo‘llash
* **Turi** – cashback hisoblash usuli (3 xil tur mavjud)
* **Faolligi** – cashback sozlamasini yoqish yoki o‘chirish
* **Cashback** – qaytariladigan qiymat (foiz yoki summa)
* **Pul birligi** – cashback foiz (%) yoki aniq pul miqdorida berilishini tanlash

Cashback turlari

**1. Umumiy savdoga**\
Barcha savdolarga bir xil cashback qo‘llanadi. Har bir xariddan belgilangan foiz yoki summa qaytariladi.

<figure><img src="../.gitbook/assets/image (577).png" alt=""><figcaption></figcaption></figure>

**2. Savdo miqdoriga qarab**\
Cashback xarid summasiga bog‘liq bo‘ladi. Masalan, ma’lum summadan oshsa – ko‘proq cashback beriladi.

* **Savdo miqdori** – chegara summa
* Shu summaga qarab cashback foizi yoki qiymati belgilanadi

<figure><img src="../.gitbook/assets/image (576).png" alt=""><figcaption></figcaption></figure>

**3. Mahsulot bo‘yicha**\
Cashback aniq mahsulot yoki kategoriyaga bog‘lanadi.

* **Tanlash** – barcha kategoriya / kategoriya / mahsulot
* Tanlangan obyektga mos cashback belgilanadi

<figure><img src="../.gitbook/assets/image (578).png" alt=""><figcaption></figcaption></figure>



</details>

<details>

<summary>Mijoz eslatmalari</summary>

Ushbu bo‘lim mijozlarga avtomatik eslatmalar yuborish vaqtini sozlash uchun ishlatiladi. Bu orqali tizim mijozlarga ma’lum vaqtdan keyin yoki oldin eslatma berishi mumkin.

* **Mijoz eslatmalari (minut)** – eslatma yuboriladigan vaqt oralig‘i (daqiqalarda)
  * bu yerda kiritilgan qiymatga qarab tizim mijozga eslatma yuboradi
  * masalan: 10 minut qo‘yilsa, belgilangan hodisadan 10 minut oldin yoki keyin eslatma beriladi

<figure><img src="../.gitbook/assets/image (607).png" alt=""><figcaption></figcaption></figure>

Mijoz eslatmalari funksiyasi mijozlar bilan aloqani yaxshilash, xizmatni unutib qo‘ymaslik va servis sifatini oshirish uchun muhim hisoblanadi. Bu sozlama ayniqsa xizmat ko‘rsatish, bron qilish yoki navbat tizimlarida samarali ishlaydi.

</details>

<details>

<summary>Onlayn to'lov sozlamalari</summary>

Ushbu bo‘lim tizimda onlayn to‘lovlarni (QR orqali to‘lov) sozlash va asosiy to‘lov provayderini tanlash uchun ishlatiladi. Bu orqali mijozlar QR-kod yordamida tez va qulay to‘lov amalga oshirishi mumkin.

**Asosiy QR-kod to‘lov usuli** – tizimda ishlatiladigan asosiy onlayn to‘lov xizmati

* masalan: Click yoki boshqa to‘lov tizimlari
* tanlangan xizmat orqali QR-kod generatsiya qilinadi va to‘lovlar qabul qilinadi

<figure><img src="../.gitbook/assets/image (608).png" alt=""><figcaption></figcaption></figure>

Onlayn to‘lov sozlamalari zamonaviy savdo jarayonida muhim rol o‘ynaydi. QR-kod orqali to‘lovni yoqish mijozlarga tezkor va kontaktsiz to‘lov imkonini beradi, bu esa xizmat tezligini oshiradi va mijozlar uchun qulaylik yaratadi.

</details>

<details>

<summary>Chop etish shablonlari</summary>

Ushbu bo‘lim tizimdagi hujjatlar (savdo, xarid, ombor va boshqalar) uchun chop etish (print), yuklab olish va yuborish shablonlarini sozlash imkonini beradi. Har bir bo‘lim uchun alohida shablon yuklab, tahrirlab va asosiy qilib belgilash mumkin.

<figure><img src="../.gitbook/assets/image (579).png" alt=""><figcaption></figcaption></figure>

#### Shablon yaratish

Ushbu oynada yangi chop etish shablonini yaratish va tizimga yuklash mumkin. Bu orqali hujjatlarni (chek, savdo hujjati va boshqalar) o‘zingizga mos formatda chiqarish imkoniyati yaratiladi.

* **Nomi** – yaratilayotgan shablon nomi
* **Shablon fayli (.xlsx)** – Excel formatdagi shablon faylini yuklash
* **Chek kengligi** – chek yoki hujjatning eni (printer formatiga moslash uchun)
* **Mahsulotlarni alfibo tartibida tartiblash** – mahsulotlar nomi bo‘yicha A-Z tartibda chiqadi
* **Mahsulotlarni kategoriyalar bo‘yicha tartiblash** – mahsulotlar kategoriya asosida guruhlanadi
* **Mahsulotlarni omborlar bo‘yicha tartiblash** – mahsulotlar ombor kesimida ajratib ko‘rsatiladi

<figure><img src="../.gitbook/assets/image (582).png" alt=""><figcaption></figcaption></figure>

#### Asosiy ma’lumotlar

* **Bo‘limlar (Barchasi / Savdo / Xarid / Ombor / Ishlab chiqarish)** – har bir jarayon uchun alohida shablonlarni boshqarish
* **Qidiruv (Qidirish)** – kerakli shablonni tez topish
* **Standart shablonni yuklash** – tizim tomonidan berilgan default shablonni yuklab olish
* **Asosiy shablonni yuklab olish** – hozir ishlatilayotgan asosiy shablonni yuklash
* **Shablonlar ro‘yxati** – mavjud barcha shablonlar (Excel yoki PDF formatda)
  * har bir shablonda yuklab olish va qo‘shimcha amallar mavjud
  * “Asosiy” belgisi – aynan shu shablon ishlatilayotganini bildiradi
* **+ Shablon yaratish** – yangi Excel shablon qo‘shish
* **+ PDF yaratish** – yangi PDF formatdagi shablon yaratish



<figure><img src="../.gitbook/assets/image (581).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/image (580).png" alt=""><figcaption></figcaption></figure>

Savdo (yoki boshqa hujjat) ichida quyidagi imkoniyatlar mavjud:

* **PDF sifatida saqlash** – hujjatni PDF formatda yuklab olish
* **Excel formatda yuklash** – hujjatni Excel ko‘rinishda yuklab olish
* **Telegram bot orqali yuborish** – hujjatni Telegram orqali mijozga yuborish

Chop etish shablonlari biznes hujjatlarini standartlashtirish va avtomatlashtirish uchun juda muhim. To‘g‘ri sozlangan shablonlar orqali hujjatlar bir xil formatda chiqariladi, bu esa professional ko‘rinish beradi va ish jarayonini tezlashtiradi.

</details>

<details>

<summary>Faollik indekslari</summary>

Bu bo‘lim mijozlarning faolligini baholash uchun ishlatiladi. Tizim har bir mijozni avtomatik ravishda **0 dan 100 gacha ball bilan hisoblaydi** va uning hozirgi holatini ko‘rsatadi — aktivmi, oddiymi yoki yo‘qolib borayaptimi.

Bu baholash 3 ta asosiy narsaga qaraydi:

* oxirgi qachon xarid qilgani
* nechta xarid qilgani
* qancha summa olib kelgani

Natijada siz mijozlarni oddiy ro‘yxat emas, balki **qiymati bo‘yicha boshqarishingiz mumkin**.

Quyidagi parametrlar orqali tizim qanday hisoblashini boshqarasiz:

* **Hisoblanish muddati (kun)** – mijoz faolligi qaysi davr bo‘yicha hisoblanishini belgilaydi (masalan: oxirgi 90 kun)
* **Oxirgi xarid vaqti (%)** – mijozning oxirgi xaridi qanchalik yangi ekanligi score ga qanchalik ta’sir qilishini belgilaydi
* **Xarid chastotasi (%)** – mijoz nechta xarid qilgani score ga qanchalik ta’sir qilishini belgilaydi
* **Xarid summasi (%)** – mijoz qancha pul olib kelgani score ga qanchalik ta’sir qilishini belgilaydi
* **Faollik indeksi oralig‘i** – mijozlarni score asosida segmentlarga ajratish uchun interval
* **Segment nomi** – har bir interval uchun nom (masalan: VIP, Oddiy, Yo‘qolayotgan)
* **Rang** – segmentni vizual ajratish uchun rang
* **Segment qo‘shish** – yangi interval qo‘shish imkoniyati

<figure><img src="../.gitbook/assets/image (583).png" alt=""><figcaption></figcaption></figure>

Tizim har bir mijozni 3 ta omil bo‘yicha baholaydi:

1. Agar mijoz yaqinda xarid qilgan bo‘lsa → yuqori ball
2. Agar ko‘p xarid qilgan bo‘lsa → yuqori ball
3. Agar ko‘p pul olib kelgan bo‘lsa → yuqori ball

Keyin bu uchta natija siz qo‘ygan foizlarga qarab birlashtiriladi va yakuniy ball chiqadi.

Masalan:

* yaqinda xarid qilgan → yaxshi
* lekin kam xarid qilgan → o‘rtacha
* o‘rtacha summa → o‘rtacha

Natijada mijoz “Standard” segmentga tushadi.

**Mijoz kartasi** – har bir mijoz uchun score va segment ko‘rinadi

<figure><img src="../.gitbook/assets/image (584).png" alt=""><figcaption></figcaption></figure>

Mijoz faollik indeksi biznesga mijozlarni chuqurroq tahlil qilish va ularni to‘g‘ri boshqarish imkonini beradi. Tizim avtomatik ravishda mijozlarning xarid xulqini baholab, ularni segmentlarga ajratadi va real holatini ko‘rsatadi.

</details>

<details>

<summary>O'lchov birliklari</summary>

Bu bo‘lim mahsulot va xizmatlar uchun ishlatiladigan o‘lchov birliklarini yaratish va boshqarish uchun mo‘ljallangan. Har bir mahsulot (masalan: dona, kg, litr) aynan shu yerda yaratilgan birlik orqali hisoblanadi.

<figure><img src="../.gitbook/assets/image (585).png" alt=""><figcaption></figcaption></figure>

* **Nom** – o‘lchov birligining to‘liq nomi (masalan: Kilogram, Dona, Litr)
* **Qisqa nom** – qisqartirilgan ko‘rinishi (masalan: kg, dona, l)
* **Kod** – tizim ichida ishlatiladigan unikal belgi (odatda qisqa nom bilan bir xil bo‘ladi)
* **Tur** – qaysi turdagi obyekt uchun ishlatilishini belgilaydi\
  – Mahsulot va xomashyo → ombor va savdoda ishlatiladi\
  – Xizmat → xizmatlar uchun ishlatiladi
* **Nuqtadan keyingi raqamlar soni** – o‘lchov qiymatida nechta kasr son ishlatilishini belgilaydi (masalan: 0 → butun son, 2 → 0.00 format)
* **Faolligi** – o‘lchov birligi aktiv yoki noaktiv ekanligini belgilaydi

<figure><img src="../.gitbook/assets/image (586).png" alt=""><figcaption></figcaption></figure>

* **Mahsulot yaratishda** – har bir mahsulotga o‘lchov birligi biriktiriladi
* **Savdo jarayonida** – mahsulot shu birlik bo‘yicha sotiladi (kg, dona va h.k.)
* **Ombor hisobida** – kirim-chiqim va qoldiq shu birlikda yuritiladi
* **Hisobotlarda** – mahsulot miqdorlari to‘g‘ri ko‘rinishda chiqadi

O‘lchov birliklari mahsulotlar bilan ishlashning asosiy bazasi hisoblanadi. To‘g‘ri sozlangan birliklar hisob-kitoblarni aniq qiladi va savdo hamda ombor jarayonlarida xatoliklarni oldini oladi.

</details>

<details>

<summary>Attributlar</summary>

Bu bo‘lim mahsulotlar uchun variantlar (variant mahsulotlar) yaratishda ishlatiladi. Ya’ni bitta mahsulotni turli xususiyatlar bilan sotish uchun atributlardan foydalaniladi (masalan: rang, razmer, hajm).

* **Atribut nomi** – mahsulot xususiyatining nomi (masalan: Rang, Razmer, Hajmi)
* **Qiymatlar** – atributga tegishli variantlar ro‘yxati (masalan: Qora, Oq, Qizil yoki 10, 11, 12)
* **Faolligi** – atribut aktiv yoki noaktiv ekanligini belgilaydi

<figure><img src="../.gitbook/assets/image (587).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (588).png" alt=""><figcaption></figcaption></figure>

* **Mahsulot yaratishda** – mahsulotga atribut qo‘shilib, variantlar yaratiladi (masalan: futbolka → S, M, L)
* **Variant mahsulotlar** – har bir atribut qiymati alohida SKU sifatida ishlashi mumkin
* **Savdo jarayoni** – mijoz kerakli variantni tanlaydi (rang, razmer va h.k.)
* **Ombor hisobi** – har bir variant alohida hisobda yuritiladi

Atributlar mahsulotlarni moslashuvchan boshqarish imkonini beradi. Ular orqali bitta mahsulotni turli variantlarda sotish, hisobini yuritish va mijozga qulay tanlov yaratish mumkin.

</details>

<details>

<summary>Tashkilotlar</summary>

Bu bo‘lim orqali tizimga yangi tashkilot (do‘kon, filial yoki biznes subyekt) qo‘shiladi. Har bir tashkilot alohida ishlaydi va o‘ziga tegishli omborlar, kassalar, xodimlar va narx sozlamalariga ega bo‘ladi.&#x20;

Tashkilot qo'shish uchun "Tashkilot qo'shish" tugmasiga bosiladi va 6 ta bosqichda ma'lumotlar to'ldiriladi.

1. **Asosiy ma’lumotlar**
   * **Nom** – tashkilot nomi (masalan: My do‘kon)
   * **Manzil** – tashkilot joylashgan manzil
   * **Qo‘shimcha** – qo‘shimcha izoh yoki ma’lumot
   * **Pul birligi** – tashkilotda ishlatiladigan valyuta (masalan: so‘m)
   * **Telefon raqami** – aloqa uchun telefon raqam
   * **Vaqt zonasi** – vaqt hisoblash uchun zona (timezone)
   * **Rasm yuklash** – tashkilot uchun logo yoki rasm

<figure><img src="../.gitbook/assets/image (589).png" alt=""><figcaption></figcaption></figure>

2. **Ko‘chirish (ma’lumot boshqa tashkilotlardan olish)**
   * **Tashkilot tanlash** – qaysi mavjud tashkilotdan ma’lumot ko‘chirish
   * **Mijozlar** – mijozlar bazasini ko‘chirish
   * **Mijoz kategoriyalari** – mijoz segmentlari
   * **Yetkazib beruvchilar** – supplierlar
   * **Yetkazib beruvchi kategoriyalari** – supplier kategoriyalari
   * **Mahsulotlar** – mahsulotlar ro‘yxati
   * **Materiallar** – xomashyo/materiallar
   * **Yarim tayyor mahsulotlar** – yarim ishlab chiqarilgan mahsulotlar
   * **Narxlar** – mahsulot narxlari
   * **Soliqlar** – soliq sozlamalari
   * **Chegirmalar** – chegirma turlari
   * **Bo‘limlar** – kompaniya bo‘limlari
   * **Lavozimlar** – ish rollari
   * **Xodimlar** – xodimlar ro‘yxati

<figure><img src="../.gitbook/assets/image (592).png" alt=""><figcaption></figcaption></figure>

3. Bu bosqichda tashkilotga ishlovchi xodimlar biriktiriladi va ularning tizimdagi roli (ruxsati) belgilanadi.
   * **Ismi** – xodimni tanlash yoki kiritish (mavjud userdan tanlanadi)
   * **Ruxsat** – xodimning tizimdagi roli\
     (masalan: hisobchi, kassir, admin va h.k.)
   * **Bo‘lim va lavozim** – xodim qaysi bo‘limda va qanday lavozimda ishlashi
   * **+ Xodim qo‘shish** – bir nechta xodimlarni qo‘shish imkoniyati

<figure><img src="../.gitbook/assets/image (597).png" alt=""><figcaption></figcaption></figure>

4. **Yaratilayotgan tashkilot uchun ombor yaratiladi**&#x20;
   * **Ombor nomi** – ombor nomi
   * **Ombor turi** – ombor turi (asosiy, ishlab chiqarish va h.k.)
   * **Mas’ul shaxs** – ombor uchun javobgar xodim
   * **Asosiy qilib belgilash** – default ombor sifatida belgilash

<figure><img src="../.gitbook/assets/image (591).png" alt=""><figcaption></figcaption></figure>

5. **Yaratilayotgan tashkilot uchun kassa yaratiladi**
   * **Kassa nomi** – kassa nomi
   * **Kassir** – mas’ul xodim
   * **Valyuta** – kassa ishlaydigan valyuta
   * **Balans o‘rnatish** – boshlang‘ich balans berish

<figure><img src="../.gitbook/assets/image (593).png" alt=""><figcaption></figcaption></figure>

6. **Yaratilgan tashkilotning mahsulotlarini narxlash**
   * **Do‘kondagi narx** – asosiy savdo narxi
   * **Sotib olish narxi** – kirim (cost price)
   * **Chakana** – retail narx
   * **Ulgurji** – wholesale narx

<figure><img src="../.gitbook/assets/image (594).png" alt=""><figcaption></figcaption></figure>

Tashkilot qo‘shish — tizimning asosiy strukturasi hisoblanadi. To‘g‘ri sozlangan tashkilot orqali barcha jarayonlar (savdo, ombor, moliya va CRM) tartibli va mustaqil ishlaydi.

</details>

<details>

<summary>Qarzdorlik limiti</summary>

Bu bo‘lim orqali har bir tashkilot uchun maksimal qarz (limit) miqdori belgilanadi. Ya’ni mijozlar yoki savdo jarayonida qancha miqdorgacha qarzdorlikka ruxsat berilishi shu yerda sozlanadi.

<figure><img src="../.gitbook/assets/image (598).png" alt=""><figcaption></figcaption></figure>

Qarzdorlik limiti moliyaviy xavfni boshqarish uchun muhim sozlama bo‘lib, har bir tashkilot uchun qarz chegarasini nazorat qilish imkonini beradi.

</details>

<details>

<summary>Qarzdorlik sanasi</summary>

Bu bo‘lim orqali mijozning qarzdorlik muddati belgilanadi. Agar mijoz belgilangan muddat ichida qarzni to‘lamasa, u avtomatik ravishda **qora ro‘yxatga**  tushadi.

<figure><img src="../.gitbook/assets/image (599).png" alt=""><figcaption></figcaption></figure>

* **Muddat (son)** – qarzdorlik uchun ruxsat etilgan kunlar soni\
  (masalan: 30 kun)
* **Vaqt birligi** – muddatni kun, hafta yoki boshqa birlikda belgilash\
  (odatda: kun)
* **Saqlash** – kiritilgan muddatni tizimga saqlash

Qarzdorlik sanasi mijozlarning to‘lov intizomini nazorat qilish va risklarni kamaytirish uchun muhim sozlama bo‘lib, muddatdan o‘tgan qarzdorlarni avtomatik boshqarishga yordam beradi.

</details>

<details>

<summary>Foydalanuvchi sozlamalari</summary>

Bu bo‘lim orqali foydalanuvchi tizim interfeysini o‘ziga qulay qilib sozlashi mumkin. Ya’ni til, sana va vaqt formati, jadval ko‘rinishi, filtr ishlashi va bildirishnomalar kabi parametrlar shu yerda boshqariladi.

<figure><img src="../.gitbook/assets/image (600).png" alt=""><figcaption></figcaption></figure>

**Til va format sozlamalari**

* **Til** – tizim interfeysining tilini tanlash
* **Sana formati** – sananing ko‘rinish formatini belgilash (masalan: YYYY-MM-DD)
* **Vaqt formati** – vaqt ko‘rinishini tanlash (24 soat yoki boshqa format)
* **Vaqt tartibi** – vaqtni ko‘rsatish logikasi (boshlanish/tugash)
* **Raqam formati** – sonlar ko‘rinishini belgilash (masalan: 1,234.56 yoki 1 234,56)



**Ro‘yxat va jadval sozlamalari**

* **Qatorlar soni** – bir sahifada nechta yozuv ko‘rinishini belgilash
* **Saralash maydoni** – jadval qaysi ustun bo‘yicha saralanishini tanlash
* **Saralash tartibi** – o‘sish yoki kamayish bo‘yicha saralash
* **Qator o‘lchami** – jadval qatorlari balandligini sozlash
* **Matn o‘lchami** – jadval ichidagi yozuvlar o‘lchamini belgilash
* **Qator rangi** – jadval qatorlariga rang berish yoki bermaslik



**Boshlang‘ich modul**

* **Boshlang‘ich modul** – tizimga kirganda qaysi bo‘lim ochilishini tanlash
* **So‘nggi modulni davom ettirish** – oxirgi ishlatilgan bo‘limni qayta ochish

<figure><img src="../.gitbook/assets/image (601).png" alt=""><figcaption></figcaption></figure>

**Filtr sozlamalari**

* **Filtr ko‘rinishi** – filtrlar qanday ko‘rinishda ishlashini tanlash:
  * Statik (tugma orqali ochiladi)
  * Yig‘iladigan (dropdown ichida)
  * Ochiladigan (har biri alohida)
* **Sana oralig‘i** – default vaqt filtri (masalan: bu oy)



**Bildirishlar**

* **Desktop push** – brauzer orqali bildirishnomalarni yoqish/o‘chirish
* **Ovozli bildirish** – signal (sound) orqali ogohlantirish

Foydalanuvchi sozlamalari tizimni har bir user uchun individual moslash imkonini beradi va ish samaradorligini oshiradi, chunki har kim interfeysni o‘z ish uslubiga moslab oladi.

</details>

<details>

<summary>Obuna</summary>

Bu bo‘lim orqali foydalanuvchi tizimdan foydalanish uchun obuna (subscription) sotib oladi, foydalanuvchilar sonini belgilaydi va to‘lovni amalga oshiradi. Tizim avtomatik tarzda narxni hisoblab beradi va tanlangan tarif asosida xizmat muddatini ko‘rsatadi.

<figure><img src="../.gitbook/assets/image (602).png" alt=""><figcaption></figcaption></figure>

#### **Sozlamalar (nimalarni sozlash mumkin)**

**Litsenziyalar soni (foydalanuvchilar soni)**

* **Litsenziya narxi (oyiga)** – har bir foydalanuvchi uchun oylik narx (masalan: 100 000 UZS)
* **Foydalanuvchilar soni (- / +)** – nechta user uchun obuna olinayotganini tanlash
* **Jami narx** – tanlangan user soniga qarab avtomatik hisoblanadi

**Obuna muddati**

* **Obuna yoqish/o‘chirish** – subscription aktiv yoki noaktiv qilish
* **Muddat tanlash (1 oy / 3 oy / 6 oy / 12 oy)** – obuna davomiyligini tanlash
* **Bonus (tekin oylar)** – uzoq muddat tanlansa qo‘shimcha bepul oylar beriladi
* **Jami summa** – tanlangan muddat va user soniga qarab umumiy narx hisoblanadi

**Qo‘shimcha obuna (hisob-kitob paneli)**

* **Jami kun** – obuna qancha muddatga olinayotganini ko‘rsatadi
* **Foydalanuvchilar soni** – nechta user uchun hisoblanganini ko‘rsatadi
* **Narx** – umumiy summa (UZS)

<figure><img src="../.gitbook/assets/image (603).png" alt=""><figcaption></figcaption></figure>

* **To‘lov usullari:**
  * Bito Pay
  * Atmos
  * Visa
  * MasterCard
* **Shartlarga rozilik** – foydalanuvchi ommaviy oferta shartlariga rozilik bildiradi
* **Jami summa** – to‘lanadigan yakuniy summa ko‘rsatiladi

</details>

<details>

<summary>Bitoverse</summary>

Bitoverse — bu Bito tizimidan foydalanayotgan turli kompaniyalar o‘rtasida ma’lumot almashish imkonini beruvchi modul. Ushbu funksiya orqali bir kompaniya boshqa kompaniyaga ulanib, mahsulotlar, mijozlar yoki boshqa ma’lumotlarni tez va oson ulashishi mumkin.

Masalan:\
Kompaniya **A** (ulgurji savdo) va kompaniya **B** (chakana savdo) ikkalasi ham Bito ishlatadi. Kompaniya **B**, Bitoverse orqali kompaniya **A** ga ulanadi va kerakli ma’lumotlarni avtomatik tarzda olib ishlatadi.

<figure><img src="../.gitbook/assets/image (604).png" alt=""><figcaption></figcaption></figure>

#### **Akkount qo‘shish (ulanish yuborish)**

* **Foydalanuvchi nomi (username)** – ulanmoqchi bo‘lgan kompaniya akkauntini topish uchun username kiritiladi
* **Qidirish (search)** – kiritilgan username orqali tizimda mavjud akkauntni topish
* **So‘rov yuborish** – tanlangan akkauntga ulanish (request) yuboriladi





#### **Akkountlar (ulangan kompaniyalar)**

* **Akkountlar ro‘yxati** – siz ulangan yoki sizga ulangan kompaniyalar ro‘yxati
* **Tanlash** – qaysi kompaniya bilan ishlashni tanlash
* **Sozlash** – tanlangan kompaniya bilan qanday ma’lumot almashilishini boshqarish

<figure><img src="../.gitbook/assets/image (605).png" alt=""><figcaption></figcaption></figure>

#### **Kelgan so‘rovlar**

* **So‘rovlar ro‘yxati** – boshqa kompaniyalardan kelgan ulanish so‘rovlari
* **Qabul qilish** – ulanishni tasdiqlash
* **Rad etish** – so‘rovni bekor qilish

Bitoverse kompaniyalar o‘rtasida to‘g‘ridan-to‘g‘ri integratsiyani ta’minlab, ma’lumot almashishni avtomatlashtiradi va bizneslar o‘rtasidagi hamkorlikni ancha samarali qiladi.



</details>

