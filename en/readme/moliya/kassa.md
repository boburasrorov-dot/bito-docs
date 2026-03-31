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

# Cash Register

<details>

<summary>Cash Register Window</summary>

The **Cash Register** section serves to manage all cash flows in the organization in a centralized manner. Through this section, you can create cash registers, maintain their balances, perform income and expense operations, and monitor all financial transactions in real time.

<figure><img src="../../.gitbook/assets/image (411).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>

#### Adding a Cash Register

To add a cash register to the system, press the **Add Cash Register** button and a special form will open. Through this form, basic parameters for the new cash register are set:

* **Cash Register Name** – used to identify the cash register (for example: Main Cash Register, Branch Cash Register)
* **Currency** – the monetary unit used in this cash register (som, dollar, and others). Each cash register operates in only one currency
* **Organization** – if there are multiple organizations in the system, specify which organization it belongs to
* **Responsible Person** – the employee responsible for the cash register

After all mandatory fields are filled in, press the **Save** button and the cash register becomes active in the system.

<div><figure><img src="../../.gitbook/assets/image (426).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (427).png" alt=""><figcaption></figcaption></figure></div>



#### Cash Register List and Balance

In the main part of the cash register window, all cash registers are displayed in card view. Each card provides quick information about the current status of the cash register:

* **Current Balance** – available funds at the current moment
* **Cash Register Name** – allows the user to quickly distinguish the cash register
* **Organization and Responsible Person** – shows who is responsible for this cash register

The following actions are available on each cash register:

* **Income** – record cash receipt to the cash register (for example: sales revenue, loan repayment)
* **Expense** – formalize cash withdrawal from the cash register (for example: expenses, payment to supplier)
* **Transfer** – transfer funds from one cash register to another (internal transfer)
* **More** – additional settings and actions (edit, delete, and others)

This approach allows the user to quickly assess the status of cash registers and perform operations quickly.

<figure><img src="../../.gitbook/assets/image (429).png" alt=""><figcaption></figcaption></figure>



#### Total Balances

The balances displayed at the top of the window are **not the sum of all cash registers**, but rather reflect **the distribution of funds within the selected cash register**. Through this block, the user can see exactly where and in what form the money in one cash register is being kept.

The following indicators are displayed:

* **Cash** – cash balance in the cash register
* **Terminal** – funds received through terminal
* **Currency (USD and others)** – funds in foreign currency
* **Electronic Payments (Click and others)** – amounts received through electronic payment systems

These values represent **the breakdown of funds within one cash register by source**.

For example, if the cash register has a total of **$1000**:

* $100 – received through terminal
* $100 – cash USD
* 9,000,000 som – cash som

The system displays these funds separately, but they all **constitute the total balance of one cash register**.

This way, the user can:

* understand **where (by channel)** the money is located
* and **in what form (by currency and payment type)** it is being kept

clearly and quickly.

<figure><img src="../../.gitbook/assets/image (431).png" alt=""><figcaption></figcaption></figure>

#### Transactions

The central part of the cash register section is the transactions table, which reflects all cash movements. Each operation is stored as a separate record and includes the following information:

* **Number** – unique identifier of the transaction
* **Date and Time** – the time when the operation was created and completed
* **Income / Expense** – whether money entered or left the cash register and the amount
* **Payment Method** – cash, terminal, electronic payment, and others
* **Status** – operation status (for example: completed)
* **Payment Type** – business context of the operation (sales, return, service, and others)
* **Cash Register** – which cash register the operation was performed in

At the bottom of the table:

* **Total Income and Expenses** – shows the overall calculation based on selected filters

This table serves as the main source for audit, control, and analysis.

<figure><img src="../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>



#### Transaction Details

When clicking on any entry in the transactions list, its detailed information opens in a separate window on the right side.

This window displays the following information:

* **Check Number** – operation number
* **Organization** – the organization to which the operation belongs
* **Device** – the device on which the operation was performed (if available)
* **Type** – operation type (for example: loan receipt, sale)
* **Created** – date and time when the operation was created
* **Cash Register** – which cash register it was performed in
* **Cashier** – the user who performed the operation
* **Payment Method** – cash, terminal, and others
* **Note** – additional information (if entered)
* **Start Date** – operation start time

At the bottom of the window:

* the **amount** of the operation (for example: 100,000 UZS)
* and its **status** (for example: Completed) are displayed

<figure><img src="../../.gitbook/assets/image (440).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Recording Income to Cash Register</summary>

Through the **Income** action, cash receipt to the cash register is recorded. This action is used to formalize sales revenues, loan repayments, or other financial income.

#### Recording Income

To record income, press the **Income** button on the cash register card and the income window opens on the right side.

The following information is entered in the window:

* **Cash Register** – the cash register receiving the money (usually already selected)
* **Invoice** – selected if the operation is related to a document
* **Payment Type** – the content of the operation (sales, return, and others)
* **Payment Method** – how the money was received (cash, terminal, card, and others)
* **Amount** – the amount of funds being received
* **Currency** – which currency the amount is in
* **Note** – optional field for entering additional information
* **File** – ability to attach a receipt or other document

<figure><img src="../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (439).png" alt=""><figcaption></figcaption></figure>

#### Saving

Based on the entered information, the following actions are performed:

* **Save** – saves the data
* **Save and Close** – saves and closes the window
* **Cancel** – cancels the action

#### Result

After the income is saved:

* the cash register balance increases
* the balance block above (cash, terminal, and others) is updated accordingly
* a new entry appears in the transactions table
* the operation status becomes **Completed**

</details>

<details>

<summary>Recording Expense from Cash Register</summary>

Through the **Expense** action, cash withdrawal from the cash register is formalized. This action is used to record expenses, payments to suppliers, or other financial expenses in the system.

#### Recording Expense

To record an expense, press the **Expense** button on the cash register card and the expense window opens on the right side.

The following information is entered in the window:

* **Cash Register** – the cash register from which money is being withdrawn (usually already selected)
* **Invoice** – selected if the operation is related to a document
* **Payment Type** – the content of the operation (for example: expense, payment, and others)
* **Payment Method** – indicates how the money is being withdrawn (cash, terminal, and others)
* **Amount** – the amount of funds being withdrawn
* **Currency** – which currency the amount is in
* **Note** – optional field for entering additional information
* **File** – ability to attach a receipt or document

<figure><img src="../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (441).png" alt=""><figcaption></figcaption></figure>



</details>

<details>

<summary>Transfer in Cash Register</summary>

Through the transfer action, you can transfer funds from one cash register to another. This function works **when there are 2 or more cash registers in the system** and is used to manage internal cash movements.

<figure><img src="../../.gitbook/assets/image (435).png" alt=""><figcaption></figcaption></figure>



#### Performing Transfer

To perform a transfer, press the **Transfer** button on the cash register card and a special form opens on the right side.

The following information is entered in the window:

* **Cash Register** – the cash register from which money is being withdrawn (sender)
* **Receiving Cash Register** – the cash register to which money is being transferred
* **Payment Method** – how the money is being transferred (cash, terminal, and others)
* **Amount** – the amount of funds being transferred
* **Currency** – monetary unit
* **Note** – additional information (optional)
* **File** – attach document if needed

<figure><img src="../../.gitbook/assets/image (443).png" alt=""><figcaption></figcaption></figure>

#### Process

The transfer action works in two stages:

* **Sending (In Progress)**
  * After the transfer is saved, the operation goes to **In Progress** status
  * Money is recorded as an expense from the sender cash register
  * In the receiving cash register, this operation appears as a **pending** document

<div><figure><img src="../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/image (446).png" alt=""><figcaption></figcaption></figure>

* **Receiving (Completed)**
  * After the operation is confirmed by the receiving cash register
  * Money is recorded as income to the receiving cash register
  * The operation status in both cash registers becomes **Completed**

</details>

<details>

<summary>Exchange in Cash Register</summary>

In the cash register section, through the exchange action, you can convert funds **by currency** or **by payment method**. These actions are used for internal management and proper distribution of cash in the cash register.

<figure><img src="../../.gitbook/assets/image (436).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (437).png" alt=""><figcaption></figcaption></figure>

### Exchange (Money)

Through this action, you can convert funds in the cash register from one currency to another currency.

#### Performing Exchange

Performed through **More → Exchange (Money)**.

The following information is entered:

* **Cash Register** – the cash register where the operation is performed
* **Payment Method** – through which channel the money is being exchanged

**Expense:**

* **Amount** – outgoing amount
* **Currency** – outgoing currency

**Income:**

* **Amount** – incoming amount
* **Currency** – incoming currency
* **Note** – additional information
* **File** – attach document (optional)

#### Process

* An **expense** is made in one currency
* An **income** is made in another currency

For example:\
$100 → 1,200,000 som

* $100 expense
* 1,200,000 som income

<figure><img src="../../.gitbook/assets/image (447).png" alt=""><figcaption></figcaption></figure>





### Exchange (Payment Method)

Through this action, you can transfer funds from one payment type to another (currency does not change).

#### Performing Exchange

Performed through **More → Exchange (Payment Method)**.

The following information is entered:

* **Cash Register** – the cash register where the operation is performed
* **Currency** – fund currency

**Expense:**

* **Amount** – outgoing amount
* **Payment Method** – channel from which money is being withdrawn

**Income:**

* **Amount** – incoming amount
* **Payment Method** – channel to which money is being received
* **Note** – additional information
* **File** – attach document (optional)

#### Process

* An **expense** is made from one payment method
* An **income** is made to another payment method

For example:\
100,000 som card → cash

* 100,000 som expense from card
* 100,000 som income to cash

<figure><img src="../../.gitbook/assets/image (438).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (448).png" alt=""><figcaption></figcaption></figure>

</details>