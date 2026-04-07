# Settings



### Settings Section

The Settings section allows you to manage and customize all key parameters of the system. Through this section, users can enable or disable system functions, modify settings across various modules, and configure them according to business processes. This section is crucial for flexible system management and optimization.

The **Settings** section is accessed from the left menu. When entering this section, the general settings window opens.

<figure><img src="../.gitbook/assets/image (510).png" alt=""><figcaption></figcaption></figure>

The settings window consists of several main parts:

Tabs (sections) are located at the top, through which you can navigate to different settings. For example:

* **Settings** – general system settings
* **CRM** – customer relationship management settings
* **Warehouse** – warehouse and product settings
* **Organizations** – company and branch settings
* **User settings** – user-related parameters
* **Subscription / Bitoverse** – additional services and modules

If the user wants to view settings for a specific area (e.g., warehouse), they select the corresponding tab at the top, and the system automatically navigates to that section's settings.

<figure><img src="../.gitbook/assets/image (512).png" alt=""><figcaption></figcaption></figure>

On the left side is a list of settings, displaying all available settings by category.

Main settings in the left menu:

* **General** – main functional settings of the system
* **Payment method** – managing payment types
* **Receipt** – receipt and printing settings
* **Bot messages** – configuring messages sent via bot
* **SMS settings** – setting up SMS sending parameters
* **Marketing SMS settings** – managing marketing messages
* **Labels** – product label settings
* **Loyalty card** – bonus and loyalty system settings
* **Device** – device management settings
* **Device security** – device security parameters
* **Open receipts** – managing open receipts
* **Sales settings** – sales process settings
* **Scale settings** – scale integration settings
* **Distribution settings** – distribution process settings
* **Finance settings** – financial parameters
* **Box types** – creating and managing packaging (box) types for products
* **Cashback** – setting up and managing cashback (return bonus) system for customers
* **Customer reminders** – setting up reminders and notifications when working with customers
* **Online payment settings** – setting up online payment systems and their parameters
* **Print templates** – configuring print templates for receipts and other documents

CRM section settings:

* **Activity indexes** – setting up criteria for evaluating customer or agent activity

Warehouse section settings:

* **Units of measurement** – creating and managing units of measurement for products
* **Attributes** – setting up product attributes (properties)

Organizations section settings:

* **Organizations** – managing company and branch information
* **Debt limit** – setting maximum debt limit for customers
* **Debt date** – setting up debt term and payment dates

User settings:

* **User settings** – individual settings and parameters for users

Subscription and system modules:

* **Subscription** – managing system subscription and pricing plans
* **Bitoverse** – managing additional services and platform integrations

When the user clicks on any setting in the left side, the window corresponding to that setting opens on the right side, where parameters can be modified.

On the right side, parameters corresponding to the selected setting are displayed. Here, functions are typically turned on/off (toggle), values are entered, or additional configurations are made.

<figure><img src="../.gitbook/assets/image (513).png" alt=""><figcaption></figcaption></figure>

The main feature of this section is that all system settings are consolidated in one place and managed by modules. This allows users to adapt the system to their business processes, control functions, and increase operational efficiency.





### General

Through this section, you can manage (enable/disable) all modules in the system and their internal functions. This allows users to disable sections that don't match their business processes and simplify the interface.

**Module-level management**

* **Disable module** – the selected module (e.g., Distribution) is completely hidden from the system

<figure><img src="../.gitbook/assets/image (514).png" alt=""><figcaption></figcaption></figure>

* **Enable module** – the module is restored and appears with all its functions

<figure><img src="../.gitbook/assets/image (515).png" alt=""><figcaption></figcaption></figure>

**Managing windows within modules**

* **Disable windows** – individual functions within the module (e.g., transfer reasons, internal transfers) become invisible

<figure><img src="../.gitbook/assets/image (517).png" alt=""><figcaption></figcaption></figure>

* **Enable windows** – those functions become active again

<figure><img src="../.gitbook/assets/image (518).png" alt=""><figcaption></figcaption></figure>

#### General settings (main parameters)

* **Product tags** – allows adding special tags (labels) when creating products. If disabled, this function is not available
* **Receipt** – manages receipt printing function. If disabled, receipt settings also disappear and receipts cannot be printed
* **Product notes** – allows adding notes to products
* **Variant product** – allows creating product variants (e.g., color, size)
* **Composite product** – allows creating products consisting of multiple products (kits)
* **Location** – enables/disables working with locations within warehouse
* **Multiple units of measurement** – allows managing products in multiple units of measurement
* **Expiry date** – allows adding expiry dates to products
* **Box type** – allows managing products by box (packaging)
  * If **multiple units of measurement is enabled**, box type cannot be enabled
  * If **box type is enabled**, multiple units of measurement cannot be enabled
  * Reason: both functions partially cover the same task
* **Multi-warehouse** – allows working with multiple warehouses
  * If disabled → only one warehouse works
  * If multiple warehouses exist in the system → this setting cannot be disabled
*   **POS** – enable/disable Point of Sale function

    * If disabled → sales windows don't work

    <figure><img src="../.gitbook/assets/image (520).png" alt=""><figcaption></figcaption></figure>

* **Manage all modules** – scrolling down the page shows a list of all modules in the system
* **Disable modules** – disable and hide unnecessary modules from the system
* **Enable modules** – re-enable disabled modules and display them in the system

<div><figure><img src="../.gitbook/assets/image (521).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (522).png" alt=""><figcaption></figcaption></figure></div>





### Payment method

Through this section, you can create, edit, and manage all payment types used in the system. Active (enabled) payment methods are available for use in the sales process.

<figure><img src="../.gitbook/assets/image (523).png" alt=""><figcaption></figcaption></figure>

* **Name** – name of the payment method (e.g., Cash, Card, Click)
*   **Status** – indicates whether the payment method is active or inactive

    * If enabled → used in the system
    * If disabled → not visible in sales

**Adding a payment method:**

* **Add payment method** – opens window for creating a new payment type
* **Name** – name of the payment method
* **Quick key** – keyboard shortcut for quick selection of this payment type
* **Commission type** – commission type applied to the payment

<figure><img src="../.gitbook/assets/image (527).png" alt=""><figcaption></figcaption></figure>





### Receipt

Through this section, you can fully customize the appearance of receipts printed in the system. Here, texts, elements, and overall design of the receipt are managed.

**General information**

* **Organization** – specifies which organization the receipt is printed from
* **Receipt type** – receipt type (e.g., sales, purchase)
* **Receipt language** – language displayed on the receipt
* **Receipt header** – text appearing at the top of the receipt (e.g., "Thank you for shopping")
* **Auto-print receipt** – enables/disables automatic receipt printing at the end of sale
* **Apply to other organizations** – option to apply settings to multiple organizations

<figure><img src="../.gitbook/assets/image (528).png" alt=""><figcaption></figcaption></figure>

**Design and appearance**

* **Font style** – setting text appearance (bold, italic, underlined)
* **Logo** – uploading company logo or image to receipt

<figure><img src="../.gitbook/assets/image (529).png" alt=""><figcaption></figcaption></figure>

Scrolling down, you can manage which information appears on the receipt:

* **Enable/disable** elements via checkbox
*   For example:

    * Logo
    * Receipt header
    * Organization name
    * Transaction information
    * Product list
    * Total amount and others

    <figure><img src="../.gitbook/assets/image (530).png" alt=""><figcaption></figcaption></figure>

On the right side, a **real-time preview (sample)** of the receipt is shown:

* Changes made are immediately reflected
* You can preview how the receipt will print

<figure><img src="../.gitbook/assets/image (531).png" alt=""><figcaption></figcaption></figure>





### Bot messages

Through this section, you can configure the content and appearance of bot messages sent from the system (e.g., Report bot, Customer bot).

<figure><img src="../.gitbook/assets/image (532).png" alt=""><figcaption></figcaption></figure>

* **Select bot** – choose which bot the settings are for at the top (e.g., Report bot)
* **Select module** – specify which module the bot sends messages for (e.g., Sales, Manufacturing, and others)

<figure><img src="../.gitbook/assets/image (533).png" alt=""><figcaption></figcaption></figure>

In the lower section, checkboxes are used to select information that appears in the message:

* Number
* Code
* Responsible person
* Organization name
* Status
* Warehouses (source and destination)
* Date and time
* Currency
* Content and other information
* ...

Each element can be:

* **Enabled** → appears in message
* **Disabled** → removed from message

**Visual preview**

On the right side, based on selected settings:

* How the message will be sent
* What information will appear

is displayed in real-time.

<figure><img src="../.gitbook/assets/image (534).png" alt=""><figcaption></figcaption></figure>





### SMS settings

Through this section, you can automate and configure SMS messages sent to customers. Mainly used for debt, installment, or other reminders.

* **Organization** – specifies which organization the SMS is sent from
* **Type** – select which process the SMS is sent for:
  * Debt
  * Installment
* **Enable (toggle)** – activate or deactivate this SMS type
* **Apply to other organizations** – apply settings to multiple organizations
* **Organizations** – if the above setting is enabled, select which organizations it applies to

#### Template and integration

* **Template** – select the SMS text (template) to be sent (created from integration->messages)
* **Integration** – connection with SMS provider or service (appears when SMS sending is selected)

<figure><img src="../.gitbook/assets/image (535).png" alt=""><figcaption></figcaption></figure>

* **Days before notification** – send reminder before deadline (e.g., 3 days before)
* **Days after deadline notification** – reminder for overdue cases
* **Notification time** – exact time SMS is sent
* **Days before notification** – send reminder before deadline (e.g., 3 days before)
* **Days after deadline notification** – reminder for overdue cases
* **Notification time** – exact time SMS is sent
* **Send via SMS** – send as SMS
* **Send via bot** – send via Telegram or other bot

<figure><img src="../.gitbook/assets/image (536).png" alt=""><figcaption></figcaption></figure>





### Marketing SMS settings

Through this section, you can configure SMS messages for marketing purposes. Mainly used for automatically notifying customers about **expected goods (arrived products)**.

<figure><img src="../.gitbook/assets/image (540).png" alt=""><figcaption></figcaption></figure>

* **Template** – select the SMS text (template) to be sent
* **Send via SMS** – send message as SMS (integration selection appears when selected)
* **Send via bot** – send message via bot (e.g., Telegram)

* This setting is used **only for marketing purposes**
* Often used:
  * When expected product arrives
  * When new goods are received
  * When customer needs to be notified





### Labels

Through this section, you can create labels (tags) for products and fully customize their design.

**Labels list**

* All created labels are displayed here
* **Create label** button adds a new label
*   Each label can be:

    * edited
    * deleted

<figure><img src="../.gitbook/assets/image (541).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

When creating a new label, the following is entered:

* **Name** – label name
* **Length (mm)** – label width
* **Height (mm)** – label height

In the central section, the **visual design** of the label is created.

<figure><img src="../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

#### Adding elements

To add elements to the label, press the "+" button and select from the following options:

* **Text** – plain text (e.g., product name)
* **Image** – upload logo or other image
* **Barcode** – product barcode or internal code
* **Line** – separator line for design

Once each element is added, it is placed within the label.

<figure><img src="../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

<div><figure><img src="../.gitbook/assets/image (546).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (547).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (548).png" alt=""><figcaption></figcaption></figure> <figure><img src="../.gitbook/assets/image (549).png" alt=""><figcaption></figcaption></figure></div>

#### Design management

* Added elements appear as a list on the right side
* Each element can be:
  * deleted ❌
  * repositioned
* In the center, the actual appearance of the label is shown as a preview

<figure><img src="../.gitbook/assets/image (550).png" alt=""><figcaption></figcaption></figure>





### Loyalty card

Through this section, you can create **loyalty cards** for customers and customize their design. Functionally, this section works similarly to the label settings.

* All created cards are displayed here
* **"Create loyalty card"** adds a new card
*   Each card can be:

    * edited
    * deleted

<figure><img src="../.gitbook/assets/image (551).png" alt=""><figcaption></figcaption></figure>

When creating a new card, the following parameters are entered:

* **Name** – card name
* **Length (mm)** – card width
* **Height (mm)** – card height

In the central section, the card design is created visually.

<figure><img src="../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

To add an element to the card, press the "+" button and select from the following:

* **Text** – customer name, card name, and other text
* **Image** – company logo or background image
* **Barcode** – card identifier (barcode)
* **Line** – design elements

<figure><img src="../.gitbook/assets/image (553).png" alt=""><figcaption></figcaption></figure>

* Added elements are placed on the card
* A list of elements appears on the right side
* Each element can be:
  * deleted
  * repositioned
* In the center, how the card looks is shown as a **real preview**





### Device

Through this section, **devices** are created and managed for employees to access the mobile application.

**Device list**

* All created devices are displayed here
* For each device:
  * name
  * status (confirmed / canceled)\
    is shown
* **"Add device"** creates a new device

<figure><img src="../.gitbook/assets/image (554).png" alt=""><figcaption></figcaption></figure>

When adding a new device:

* **Name** – device name (e.g., phone name or employee name)
* **Employee replacement** – allow the device to be used by another employee if needed

Then **save** to add the device to the system.

<figure><img src="../.gitbook/assets/image (555).png" alt=""><figcaption></figcaption></figure>

* If **"Restrict devices"** is enabled (in Device security settings):\
  → only devices created here can access the system
* If no device is created:\
  → employee cannot log into the mobile app

1. Employee is created in BITO
2. From this section, a **device is created** for them
3. Employee logs into the mobile app
4. Selects the **created device** from the system
5. Only then can they access the system





### Device security

This section serves to **control access to the system through devices and enhance security**.

**Enable device restriction**

* If enabled:\
  → only **pre-created devices** can access the system
* If disabled:\
  → any device can access (unrestricted)

**Restrict web access as well**

* If enabled:\
  → device restriction applies **not only to mobile but also to web (browser)**
* Meaning, users can only access from a computer through an authorized device

**Confirm new devices**

* If enabled:\
  → when attempting to log in from a new device:
  * device is added to the system
  * but **access is blocked until admin approval**
* If disabled:\
  → new devices are automatically allowed (if general restriction is disabled)

**Working logic**

* **Restrict devices ON:**
  * only devices in settings work
  * other devices → cannot access
* **Restrict devices OFF + Confirm new device ON:**
  * new device attempts to access
  * access is blocked until admin approves

<figure><img src="../.gitbook/assets/image (557).png" alt=""><figcaption></figcaption></figure>

**IP address list**

* Allowed IP addresses are entered here
* If enabled:\
  → only these IP addresses can access the system





### Open receipts

This section is used to manage incomplete sales (open receipts) in the system. Here, sales started by the cashier but not yet closed are saved, and they can be continued or completed later.

An open receipt is a state where products are selected but the sale is not yet fully completed.

<figure><img src="../.gitbook/assets/image (558).png" alt=""><figcaption></figcaption></figure>

* View open receipts in list form
* Open and continue each receipt
* Complete the sale (by making payment)
* Delete unnecessary receipts





### Sales settings

This section is used to manage the main logic and restrictions of the sales process. Here, cashier workflow, discounts, debt, cashback, and other important functions are enabled or disabled.

<figure><img src="../.gitbook/assets/image (568).png" alt=""><figcaption></figcaption></figure>

#### Main functions

* **Cashback activity** → enables or disables giving cashback to customers
* **Tax activity** → activates tax calculation in sales
* **Calculate tax after discount** → tax is calculated after discount, not before
* **Calculate general discount after product discount** → general discount is applied after product discounts

<figure><img src="../.gitbook/assets/image (559).png" alt=""><figcaption></figcaption></figure>

#### Control and approval

* **Manager-approved discount** → large discounts are only made with manager approval
* **Debt approved by manager** → additional approval required for credit sales
* **Set discount limit** → set maximum limit for discounts

<figure><img src="../.gitbook/assets/image (560).png" alt=""><figcaption></figcaption></figure>

#### Product and display settings

* **Show product gross weight**
* **Show product net weight** → display product weights on receipt or interface

<figure><img src="../.gitbook/assets/image (561).png" alt=""><figcaption></figcaption></figure>

#### Settings affecting sales process

* **Sales with old date** → allow sales with previous date
* **Sell more than order** → allow selling more than the order quantity
* **Customer selection mandatory** → require selecting customer before making sale
* **Reserve product in open receipt** → product is reserved from stock in open receipt

<figure><img src="../.gitbook/assets/image (562).png" alt=""><figcaption></figcaption></figure>

#### Additional sales capabilities

* **Multi-currency receipt** → trade in multiple currencies
* **Sales with status** → attach statuses to sales (e.g., completed)
* **Quick product creation** → add new product without leaving sales window
* **Sell out-of-stock items** → allow selling products not in stock
* **Restrict zero or negative prices** → block sales with incorrect prices

<figure><img src="../.gitbook/assets/image (563).png" alt=""><figcaption></figcaption></figure>

#### Working with payment and debt

* **Credit sales** → sell to customers on credit
* **Installment payment** → allow receiving payment in installments

<figure><img src="../.gitbook/assets/image (564).png" alt=""><figcaption></figcaption></figure>

#### Restrictions and limits

* **Maximum old date** – specify how many days back sales can be dated

<figure><img src="../.gitbook/assets/image (566).png" alt=""><figcaption></figcaption></figure>

* **Minimum and maximum sale quantity** – set quantity restrictions in sales

<figure><img src="../.gitbook/assets/image (567).png" alt=""><figcaption></figcaption></figure>





### Scale settings

This section is used to configure working with scales (electronic scales) and **automatically identifying products via barcode**. It is mainly important for products sold by weight (fruits, vegetables, etc.).

<figure><img src="../.gitbook/assets/image (569).png" alt=""><figcaption></figcaption></figure>

Here, the main parameters for working with scales are set:

* **Organization** → specify which organization the setting applies to
* **Type (Custom)** → select ready-made or custom scale configuration
* **Department code** → used to differentiate product type in scale barcode
* **Decimal places** → specify how many decimal places weight is taken with\
  (e.g., 0.123 → 3 digits)

#### Configuring barcode structure

The barcode coming from the scale consists of several parts. Here, its structure is specified:

* **1st digit** → department code (product type identifier)
* **2nd digit** → additional identification (another department or category)
* **3rd digit** → product code (SKU)
* **4th digit** → check digit (for verification)
* **+ Add** → add additional segments if needed

When a product is weighed on the scale:

* barcode is generated
* it contains:
  * product code
  * weight
  * other segments
* the system through these settings:\
  → automatically finds the product\
  → calculates weight and determines price





### Distribution settings

This section is used to **specify the order type** used in distribution (distribution) processes. That is, here you can configure what type orders created in the system belong to.

<figure><img src="../.gitbook/assets/image (570).png" alt=""><figcaption></figcaption></figure>

This page has only one main parameter:

* **Order type** → select the order type used in the distribution process\
  \- Sales\
  \- Sales Order

Whichever is selected, those orders will go there.





### Finance settings

This section is used to manage financial processes in the system, that is, to configure currency operations and cash (cash flow) related operations.

<figure><img src="../.gitbook/assets/image (573).png" alt=""><figcaption></figcaption></figure>

* **Use multiple currencies** – enables working in multiple currencies in the system
* **Convert to base currency** – automatically converts amounts entered in other currencies to the base currency
* **Service type cost price** – method of calculating service cost price
  * _Fixed_ – constant value
  * _Priced_ – calculated based on product or service price

<figure><img src="../.gitbook/assets/image (571).png" alt=""><figcaption></figcaption></figure>

* **Organization** – select which organization the cash register is being configured for
* **Activate cash session** – enable cash register to work based on sessions
* **Link to device** – attach cash session to a specific device
* **Work only on open device** – restrict to working only on authorized devices
* **Restrict IP address** – allow working only from specific IP
* **Warn about balance difference** – notify if there is a cash balance discrepancy
* **Auto logout** – automatically log out of system after a certain time
* **Daily session limit** – set limit for session during the day
* **Auto expense** – enable automatic expense recording
* **Auto close time** – time when cash session automatically closes

<figure><img src="../.gitbook/assets/image (572).png" alt=""><figcaption></figcaption></figure>

Finance settings are very important for properly managing cash flows in the system, reducing errors, and ensuring security. Through these settings, you control currency operations, establish cash discipline, and automate financial processes.





### Box types

This section is used to create and manage packaging (box) types used for products in the system. That is, here you configure in what units (box, roll, etc.) products are counted.

<figure><img src="../.gitbook/assets/image (574).png" alt=""><figcaption></figcaption></figure>

Pressing the "Create" button opens the creation window where information is filled in and saved

#### Basic information

* **Name** – full name of box type (e.g., BOX, ROLL)
* **Short name** – abbreviated name (for quick viewing and use)
* **Code** – unique identifier attached to box type
* **Activity** – activate or deactivate this box type

<figure><img src="../.gitbook/assets/image (575).png" alt=""><figcaption></figcaption></figure>

Box types are important for managing products in correct units and accurate calculation in warehouse and sales processes. Through this, you can manage the same product in different packages (e.g., piece, box, roll) and ensure orderly system operation.





### Cashback

This section allows you to configure and manage the cashback (return bonus) system for customers. Through cashback, customers receive a certain percentage or amount back after making a purchase.

**Basic information**

* **Organization** – organization where cashback applies
* **Apply to other organizations** – apply the same cashback setting to multiple organizations
* **Type** – cashback calculation method (3 types available)
* **Activity** – enable or disable cashback setting
* **Cashback** – value to be returned (percentage or amount)
* **Currency unit** – select whether cashback is given as percentage (%) or exact amount

Cashback types

**1. For general sales**\
The same cashback applies to all sales. A specified percentage or amount is returned from each purchase.

<figure><img src="../.gitbook/assets/image (577).png" alt=""><figcaption></figcaption></figure>

**2. Based on sale amount**\
Cashback depends on purchase amount. For example, if it exceeds a certain amount – more cashback is given.

* **Sale amount** – threshold amount
* Cashback percentage or value is set based on this amount

<figure><img src="../.gitbook/assets/image (576).png" alt=""><figcaption></figcaption></figure>

**3. By product**\
Cashback is tied to a specific product or category.

* **Select** – all categories / category / product
* Appropriate cashback is set for the selected object

<figure><img src="../.gitbook/assets/image (578).png" alt=""><figcaption></figcaption></figure>





### Customer reminders

This section is used to configure the timing for sending automatic reminders to customers. Through this, the system can remind customers after or before a certain time.

* **Customer reminders (minutes)** – time interval (in minutes) when reminders are sent
  * based on the value entered here, the system sends reminders to customers
  * for example: if 10 minutes is set, a reminder is given 10 minutes before or after the specified event

<figure><img src="../.gitbook/assets/image (607).png" alt=""><figcaption></figcaption></figure>

The customer reminders function is important for improving communication with customers, not forgetting services, and increasing service quality. This setting works especially effectively in service provision, booking, or queuing systems.





### Online payment settings

This section is used to configure online payments (payment via QR) in the system and select the main payment provider. Through this, customers can make quick and convenient payments using QR codes.

**Main QR-code payment method** – main online payment service used in the system

* for example: Click or other payment systems
* QR code is generated and payments are accepted through the selected service

<figure><img src="../.gitbook/assets/image (608).png" alt=""><figcaption></figcaption></figure>

Online payment settings play an important role in modern sales processes. Enabling payment via QR code allows customers to make quick and contactless payments, which increases service speed and creates convenience for customers.





### Print templates

This section allows you to configure print, download, and send templates for documents (sales, purchase, warehouse, and others) in the system. For each section, separate templates can be uploaded, edited, and set as default.

<figure><img src="../.gitbook/assets/image (579).png" alt=""><figcaption></figcaption></figure>

#### Template creation

In this window, you can create and upload new print templates to the system. Through this, you can create the ability to output documents (receipts, sales documents, and others) in a format that suits you.

* **Name** – name of the template being created
* **Template file (.xlsx)** – upload template file in Excel format
* **Receipt width** – width of receipt or document (to adapt to printer format)
* **Sort products alphabetically** – products appear in A-Z order by name
* **Sort products by categories** – products are grouped by category
* **Sort products by warehouses** – products are shown separately by warehouse

<figure><img src="../.gitbook/assets/image (582).png" alt=""><figcaption></figcaption></figure>

#### Basic information

* **Sections (All / Sales / Purchase / Warehouse / Manufacturing)** – manage separate templates for each process
* **Search** – quickly find needed template
* **Download standard template** – download default template provided by system
* **Download main template** – download currently used main template
* **Templates list** – all available templates (in Excel or PDF format)
  * download and additional actions available for each template
  * "Main" indicator – shows that this template is being used
* **+ Create template** – add new Excel template
* **+ Create PDF** – create new PDF format template

<figure><img src="../.git