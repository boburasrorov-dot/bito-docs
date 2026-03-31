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

# Ruxsatlar

<details open>

<summary>Ruxsatlar</summary>

**Ruxsatlar bo‘limi** xodimlarning tizimdagi imkoniyatlarini boshqarish uchun xizmat qiladi. Ushbu bo‘lim orqali har bir lavozim yoki xodim uchun qaysi modulga kirish mumkinligi va qaysi amallarni bajarish mumkinligi aniq belgilanadi. Bu esa tizim xavfsizligini ta’minlash va har bir foydalanuvchini o‘z vazifasi doirasida ishlashini nazorat qilish imkonini beradi.

<figure><img src="../../.gitbook/assets/image (471).png" alt=""><figcaption></figcaption></figure>

**HR → Ruxsatlar** bo‘limiga kiriladi va **“Yaratish”** tugmasi orqali yangi ruxsat (role/permission set) yaratiladi.

Ushbu bo‘limda barcha ruxsatlar jadval (table) ko‘rinishida aks etadi.

**Jadval ustunlari:**

* **Nomi** – ruxsat (role) nomi

<figure><img src="../../.gitbook/assets/image (480).png" alt=""><figcaption></figcaption></figure>



Yangi ruxsat yaratishda tizim modullari kesimida ruxsatlar sozlanadi. Har bir modul alohida ochilib, uning ichidagi amallar boshqariladi.

<div><figure><img src="../../.gitbook/assets/image (481).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (482).png" alt=""><figcaption></figcaption></figure></div>

Har bir modul uchun quyidagi asosiy amallar mavjud:

* **Yaratish** – yangi ma’lumot qo‘shish
* **Ko‘rish** – ma’lumotlarni ko‘rish
* **O‘zgartirish** – mavjud ma’lumotlarni tahrirlash
* **O‘chirish** – ma’lumotlarni o‘chirish
* **Eksport** – ma’lumotlarni yuklab olish

Har bir amal uchun 3 xil holat mavjud:

* **Rad etilgan** – umuman ruxsat yo‘q
* **Agar mas’ul bo‘lsa** – faqat o‘ziga tegishli ma’lumotlar bilan ishlay oladi
* **Ruxsat berilgan** – barcha ma’lumotlar bilan ishlay oladi

Shuningdek, har bir modulni to‘liq yoqish yoki o‘chirish uchun umumiy toggle mavjud. Agar modul o‘chirilsa, uning ichidagi barcha ruxsatlar avtomatik ravishda bekor qilinadi.

Ruxsatlar bir-biri bilan **o‘zaro bog‘liq** ishlaydi. Masalan, agar sotuvchi xodimga faqat **Savdo** bo‘limi uchun ruxsat berilib, **Ombor** bo‘limi ruxsatlari cheklansa:

* u mahsulotlarni ko‘ra olmaydi
* ombordagi qoldiqlarni ko‘ra olmaydi
* natijada savdo jarayonini to‘liq bajara olmaydi

Shu sababli, ruxsatlarni sozlashda modullar o‘rtasidagi bog‘liqlikni hisobga olish muhim. Amaliy jihatdan:

* savdo ishlashi uchun kamida mahsulot va ombor ko‘rish ruxsati bo‘lishi kerak
* noto‘g‘ri sozlangan ruxsatlar tizimda ishlashni cheklab qo‘yishi mumkin

Bu bo‘lim orqali tizimda kim nima qila olishini aniq boshqarish, rollarni standartlashtirish va xavfsizlikni yuqori darajada ta’minlash mumkin.

</details>
