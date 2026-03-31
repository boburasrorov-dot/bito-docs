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

# Customers

<details>

<summary>Customer database</summary>

When entering **CRM → Customers**, the system displays a list of all customers.

Through this section, you can manage the customer database, segment them, and control sales processes by customer.

<figure><img src="../../.gitbook/assets/image (318).png" alt=""><figcaption></figcaption></figure>

The customer list displays basic information for each customer, such as: name, phone number, category, first and last sale date, number of purchases, and average sales indicators.

<figure><img src="../../.gitbook/assets/image (324).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Categories</summary>

When entering **CRM → Categories**, the system displays a list of all created customer categories.

Through this section, you can divide customers into different categories. This makes working with customers more systematic and convenient.

For example, by dividing customers into wholesale, retail, or other types of groups, you can apply separate sales strategies for them.

<figure><img src="../../.gitbook/assets/image (319).png" alt=""><figcaption></figcaption></figure>

<div><figure><img src="../../.gitbook/assets/image (326).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (325).png" alt=""><figcaption></figcaption></figure></div>

To create a new category, click the Create button and enter the following information:

• **Name** — enter the category name. This is used to group customers.

• **Parent category** — if needed, you can link the category to another category (as a subcategory).

After the category is created, you can assign customers to this category.

</details>

<details>

<summary>Creating a customer</summary>

When clicking the Create button in CRM → Customers section, a new customer addition window opens.

Through this section, new customers are entered into the system and all information related to them is stored.

<figure><img src="../../.gitbook/assets/image (320).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (328).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (327).png" alt=""><figcaption></figcaption></figure>

When creating a customer, the following information is entered:

• **Image** — upload customer photo or logo.

• **Customer type** — select customer type (individual or legal entity).

• **Name** — enter customer name or organization name.

• **TIN** — if available, enter tax identification number.

• **Gender** — select customer gender (for individuals).

• **Responsible person** — assign the employee responsible for this customer.

• **Loyalty card** — enter or scan the loyalty card assigned to the customer.

• **Source** — specify where the customer came from (advertisement, referral, etc.).

• **Phone** — enter customer phone number. You can add multiple phones.

• **Category** — select which category the customer belongs to.

• **Location** — enter customer address or location (can be marked on map).

• **Supplier** — if the customer is a supplier, enable this option.

• **Upload file** — attach documents related to the customer.

• **Note** — write additional information or reminders.

• **Send notification** — enable or disable automatic notification sending to customer.

• **Status** — specify whether the customer is active or inactive.

Through the additional information section, you can enter more detailed information:

• **Last name** — customer's last name.\
• **Middle name** — customer's middle name.\
• **Date of birth** — customer's birth date.\
• **Address** — additional address information.\
• **Legal entity** — legal information if available.\
• **Telegram** — customer's Telegram account.\
• **Email** — customer's email address.

After all information is entered, it is saved and the customer is added to the system.

As a result, all customer information is stored in a unified system and the process of working with them becomes more convenient.

</details>

<details>

<summary>Customer window</summary>

**When clicking on a customer in CRM → Customers section**, their complete information opens.

Here you can see all information related to the customer: debt, sales, payments, and other history.

<figure><img src="../../.gitbook/assets/image (329).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (321).png" alt=""><figcaption></figcaption></figure>

### Mutual settlements report

In the mutual settlements report section, all monetary transactions with the customer are fully visible.

Here you can accurately track how much the customer owes you or how much payment they have made.

<figure><img src="../../.gitbook/assets/image (332).png" alt=""><figcaption></figcaption></figure>

**Table information**

• **Time** — when the operation was performed\
• **Action** — what happened (sale, payment, etc.)\
• **Note** — additional information\
• **Debit** — amount paid by the customer\
• **Credit** — amount of product or service sold to customer\
• **Balance** — remaining balance after each operation

**How it works**

• You sell product to customer → amount is **recorded in credit** (debt increases)\
• Customer makes payment → amount is **recorded in debit** (debt decreases)

Result:\
• **Balance** always shows the customer's current debt

**Example**

1. Sale of 1,000,000 soums made to customer\
   → Credit: 1,000,000\
   → Balance: 1,000,000 (customer is in debt)
2. Customer paid 400,000 soums\
   → Debit: 400,000\
   → Balance: 600,000

**Benefit**

• Keep accurate accounting with customer\
• Control debt\
• Check each operation by history

**Important**

Mutual settlements report is automatically generated:\
• When a sale is made\
• When payment is received\
• During returns or other financial transactions

### Balance

In the Balance section, the overall status of the customer's accounting with you is displayed.

Here you can see how much the customer owes you or how much money you received from them in advance.

<figure><img src="../../.gitbook/assets/image (333).png" alt=""><figcaption></figcaption></figure>

**Current balance**

• Current balance — customer's current accounting status

Balance is understood as follows:\
• If positive — customer is in debt to you\
• If negative — you are in debt to customer (there is advance payment)

**By organizations**

If you have multiple branches or stores:

• Separate balance is shown for each organization\
• You can see in which branch the customer has debt

**Total**

• Total (in base currency) — overall balance across all branches

This allows you to quickly see the overall accounting.

**Balance is automatically calculated:**

• When product is sold → balance increases (customer becomes debtor)\
• When customer makes payment → balance decreases\
• If there is a return → balance is recalculated

**Example**

1. Customer purchased product for 1,000,000 soums\
   → Balance: 1,000,000
2. Customer paid 300,000 soums\
   → Balance: 700,000
3. Paid another 700,000\
   → Balance: 0 (account closed)

**Additional features**

• Debt limit — you can set maximum debt for customer\
• Conversion — if there are different currencies, you can convert them

**Benefit**

• Control customer debt\
• Quickly see how much each customer owes\
• Simplify accounting

If balance is positive — customer is in debt to you\
If negative — you are in debt to customer

### Cashback

In the Cashback section, the accumulated bonus (cashback) for the customer and its history are displayed.

<figure><img src="../../.gitbook/assets/image (334).png" alt=""><figcaption></figcaption></figure>

These bonuses are usually calculated as money returned to the customer during the sales process.

• **Current balance** — cashback amount currently available to customer

This amount is a bonus that the customer can use on future purchases.

**Cashback history** - Here you can see all cashbacks given to the customer and their movement.

**In the table:**

• **Time** — date and time when cashback was given\
• **Action** — where the cashback came from (which sale or operation)\
• **Debit** — cashback amount used\
• **Credit** — cashback amount added

**How it works**

• When customer makes a sale — they are given cashback\
• This amount is automatically added to their cashback balance\
• On next purchase — cashback can be used

**Example**

• Customer made a purchase of 1,000,000 soums\
• 5% cashback was given → 50,000 soums\
• This amount goes to cashback balance

On next sale:\
• Customer can use these 50,000 soums

**Important**

For cashback to work:\
• Cashback settings must be enabled in the system\
• Percentage or rules must be set in Marketing → Cashback section

### Sales history

In the Sales history section, a list of all sales made with the customer is displayed.

Here you can see when, how much, and what kind of sales the customer made.

<figure><img src="../../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

**Table information**

• **№** — serial number\
• **Sale number** — unique ID assigned to each sale\
• **Sale type** — sale or returned sale\
• **Sale time** — date and time when sale was made\
• **Status** — sale status (completed or cancelled)\
• **Amount due** — unpaid amount for this sale\
• **Total returned** — if there was a return, the returned amount

**How it works**

• Each sale automatically goes into this list\
• If product is returned — it is shown separately as "returned"\
• Unpaid amounts are linked to the balance

**Example**

• Sale of 999,000 soums was made\
→ Amount due: 999,000

• If payment is made\
→ This amount decreases

• If there is a return\
→ Appears in "Total returned" column

**Benefit**

• View customer's purchase history\
• Check when which sale occurred\
• Control debt and returns

### Product sales

In the Product sales section, a list of all products purchased by the customer is displayed.

Here you can see which product the customer purchased, when, and through which sale.

<figure><img src="../../.gitbook/assets/image (335).png" alt=""><figcaption></figcaption></figure>

**Table information**

• **№** — serial number\
• **Customer** — customer who purchased the product\
• **Products** — name of sold product\
• **Category** — which category the product belongs to\
• **Unit of measurement** — product measurement (piece, liter, kilogram, etc.)\
• **Sale number** — which sale the product belongs to\
• **Status** — sale status (completed or cancelled)

**How it works**

• Products from each sale go into this list separately\
• If there are multiple products in one sale — each appears in a separate row\
• If sale is cancelled or returned — visible through status

**Example**

• Customer purchased "Apple juice"\
→ appears in list with product name and category

• If they also purchased another product\
→ it is also shown in a separate row

**Benefit**

• See what customer is buying more\
• Identify best-selling products\
• Analyze sales by product

### Invoice

In the Invoice section, a list of all invoices issued to the customer is displayed.

Here you can view official accounting for sales made to the customer.

<figure><img src="../../.gitbook/assets/image (337).png" alt=""><figcaption></figcaption></figure>

**Table information**

• **№** — serial number\
• **Number** — invoice number\
• **Date** — invoice creation date\
• **Organization** — which branch or store it was created in\
• **Type** —\
  — **Income** — money received from customer\
  — **Expense** — product or service provided to customer\
• **Amount due** — total amount on invoice\
• **Paid** — amount paid by customer

**How it works**

• An invoice is created for each sale\
• The invoice generates the customer's debt\
• When customer makes payment — "paid" amount increases

**Example**

• Sale of 999,000 soums was made\
→ Amount due: 999,000\
→ Paid: 0

• Customer made payment\
→ Paid: 999,000\
→ Debt is closed

**Types**

• **Income invoice** — payments received from customer\
• **Expense invoice** — products or services sold to customer

**Filter and export**

• Invoices can be filtered by date\
• Can be separated by organization (branch)\
• Data export option is available

**Benefit**

• Conduct official accounting with customer\
• See exactly how much debt there is\
• Link payments and sales

### Payment history

In the Payment history section, a list of all payments made by the customer is displayed.

Here you can see when, how much, and by what method the customer made payments.

<figure><img src="../../.gitbook/assets/image (336).png" alt=""><figcaption></figcaption></figure>

**Table information**

• **№** — serial number\
• **Number** — payment document number\
• **Date** — payment date\
• **Created time** — time when payment was entered into system\
• **Completed date** — time when payment was confirmed\
• **Income** — amount paid by customer\
• **Expense** — expense amount if money was returned\
• **Payment method** — cash, card (Click, Payme, etc.)\
• **Status** — payment completed or cancelled\
• **Payment type** — what the payment relates to (for example: sale)\
• **Cashier** — employee who accepted the payment\
• **Note** — additional information

**How it works**

• When customer makes payment — a record is added here\
• Each payment automatically affects the balance\
• Payment is linked to sale or invoice

**Example**

• Customer paid 999,000 soums\
→ Income: 999,000\
→ Balance decreases

• Payment was made via Click\
→ Payment method: Click

### Reminders

The Reminders section is used to record important tasks and reminders related to the customer.

This allows you to schedule when to contact the customer, remind about debt, or plan meetings.

<figure><img src="../../.gitbook/assets/image (338).png" alt=""><figcaption></figcaption></figure>

**Main features**

• You can add reminders for customer\
• You can set date and time\
• You can specify responsible employee\
• You can write reminder text

**How it works**

• Reminder is created\
• Reminder appears at specified date and time\
• Employee performs necessary work with customer

**Reminder content**

• **Due date** — date and time when reminder should be completed\
• **Responsible person** — who should complete it\
• **Text (note)** — what needs to be done or reminder content

**Example**

• 17.03.2026, 16:00\
→ "Remind customer about debt"

• 20.03.2026, 10:00\
→ "Call about new product"

### Audit history

In the Audit history section, all change history related to the customer is stored.

Here you can see who, when, and what information was changed.

<figure><img src="../../.gitbook/assets/image (339).png" alt=""><figcaption></figcaption></figure>

**Main features**

• View all changes in customer information\
• Compare old and new values\
• Determine when and by whom the change was made

**How it works**

• Every time customer information is changed, the system records it\
• Changes are stored in history view\
• Each change shows old and new values

**Change content**

• **Change type** — which information changed (for example: address, phone, type)\
• **Old value** — information before change\
• **New value** — information after change\
• **Date and time** — when the change was made\
• **Status** — whether it was created or updated

**Example**

• Address was changed\
→ Old: not available\
→ New: Yunusabad, Tashkent

• Type was changed\
→ Old: none\
→ New: Individual

**Benefit**

• Control who changed what\
• Identify and check errors\
• Save information history

### Message history

In the Message history section, a list of all SMS or messages sent to the customer is displayed.

This allows you to control what messages were exchanged with the customer and whether they were delivered.

<figure><img src="../../.gitbook/assets/image (340).png" alt=""><figcaption></figcaption></figure>

**Table information**

• **№** — serial number\
• **Phone number** — customer number to which message was sent\
• **Recipient name** — customer name\
• **Content** — sent message text\
• **Status** — message status (sent, delivered, error)\
• **Created time** — date and time when message was sent\
• **Reason** — reason for sending message (for example: debt reminder, promotion, system message)

**How it works**

• Every SMS sent through the system is stored here\
• When message is sent, its status is recorded\
• If SMS platform (for example Eskiz) is connected, status is updated

**Example**

• "You have a debt of 150,000 soums"\
→ Status: Delivered

• "New product arrived"\
→ Status: Sent

**Benefit**

• Control messages sent to customer\
• Check which message was delivered\
• See effectiveness of marketing and reminders

</details>

<details>

<summary>Viewing customers on map</summary>

When entering the **CRM → View customers on map** section, all customers in the system are displayed on the map with their locations.

Through this section, you can view the geographical location of customers and analyze in which areas they are located.

The address entered when creating a customer is automatically marked on the map. Each customer is shown as a separate marker.

If there are multiple customers in one area, they are grouped and shown under one marker with a number.

<figure><img src="../../.gitbook/assets/image (341).png" alt=""><figcaption></figcaption></figure>

<div><figure><img src="../../.gitbook/assets/image (323).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (322).png" alt=""><figcaption></figcaption></figure></div>

**How it works**

• When creating a customer, their address is entered\
• The system marks this address on the map\
• All customers are visible on the general map\
• When clicking on a marker, customer information appears

**Main features**

• View customers on map\
• Analyze customers by region\
• Determine how many customers are in one location\
• Find needed customers through search and filter

**Example**

• There are 3 customers in Yunusabad area\
→ Appears as "3" on the map

• When clicking on marker\
→ Customer name and brief information appear

**Result**

• See exact location of customers\
• Simplify delivery and sales planning\
• Determine which area has more customers\
• Develop sales strategy by region

</details>