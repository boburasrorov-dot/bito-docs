# Cash Register



### Cash Register Window

The **Cash Register** section serves to manage all cash flows in the organization in a centralized manner. Through this section, you can create cash registers, maintain their balance, perform income and expense operations, and track all financial transactions in real-time.

<figure><img src="../../.gitbook/assets/image (411).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>

#### Adding a Cash Register

To add a cash register to the system, click the **Add Cash Register** button and a special form opens. Through this form, basic parameters are set for the new cash register:

* **Cash Register Name** – used to identify the cash register (for example: Main Cash Register, Branch Cash Register)
* **Currency** – the monetary unit used in this cash register (som, dollar, etc.). Each cash register operates in only one currency
* **Organization** – if multiple organizations exist in the system, it is specified which organization it belongs to
* **Responsible Person** – the employee responsible for the cash register (this employee must not have another cash register assigned if it's not a different organization)

After all mandatory fields are filled in, click the **Save** button and the cash register becomes active in the system.

<div><figure><img src="../../.gitbook/assets/image (426).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (427).png" alt=""><figcaption></figcaption></figure></div>



#### Cash Register List and Balance

In the main part of the cash register window, all cash registers are displayed in card view. Each card provides quick information about the current state of the cash register:

* **Current Balance** – available funds at the present moment
* **Cash Register Name** – allows the user to quickly identify the cash register
* **Organization and Responsible Person** – shows who is responsible for this cash register

The following actions are available for each cash register:

* **Income** – enter cash receipts into the cash register (for example: sales revenue, debt repayment)
* **Expense** – formalize cash withdrawals from the cash register (for example: expenses, payment to supplier)
* **Transfer** – transfer funds from one cash register to another (internal transfer)
* **More** – additional settings and actions (edit, delete, etc.)

This approach allows the user to quickly assess the status of cash registers and perform actions quickly.

<figure><img src="../../.gitbook/assets/image (429).png" alt=""><figcaption></figcaption></figure>



#### Total Balances

The balances shown at the top of the window are **not the sum of all cash registers**, but rather reflect **the distribution of funds within the selected cash register**. Through this block, the user can see where and in what form the money in one specific cash register is kept.

The following indicators are displayed:

* **Cash** – cash balance in the cash register
* **Terminal** – funds received through the terminal
* **Currency (USD, etc.)** – funds in foreign currency
* **Electronic Payments (Click, etc.)** – amounts received through electronic payment systems

These values indicate **the breakdown of funds within one cash register by source**.

For example, if the cash register has a total of **$1000**:

* $100 – received through terminal
* $100 – cash USD
* 9,000,000 som – cash som

The system displays these funds separately, but they all **constitute the total balance of one cash register**.

Through this, the user can:

* understand **where (by channel)** the money is located
* and **in what form (by currency and payment type)** it is stored

clearly and quickly.

<figure><img src="../../.gitbook/assets/image (431).png" alt=""><figcaption></figcaption></figure>

#### Transactions

The central part of the cash register section is the transactions table where all cash movements are reflected. Each operation is stored as a separate record and includes the following information:

* **Number** – unique identifier of the transaction
* **Date and Time** – time when the operation was created and completed
* **Income / Expense** – whether cash entered or left the cash register and the amount
* **Payment Method** – cash, terminal, electronic payment, etc.
* **Status** – operation status (for example: completed)
* **Payment Type** – business context of the operation (sale, return, service, etc.)
* **Cash Register** – which cash register the operation was performed in

At the bottom of the table:

* **Total Income and Expenses** – overall calculation is shown based on selected filters

This table serves as the primary source for audit, control, and analysis.

<figure><img src="../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>



#### Transaction Details

When you click on any record in the transactions list, its detailed information opens in a separate window on the right side.

This window displays the following information:

* **Check Number** – operation number
* **Organization** – organization to which the operation belongs
* **Device** – device on which the operation was performed (if available)
* **Type** – operation type (for example: debt collection, sale)
* **Created** – date and time the operation was created
* **Cash Register** – which cash register it was performed in
* **Cashier** – user who performed the operation
* **Payment Method** – cash, terminal, etc.
* **Note** – additional information (if entered)
* **Start Date** – operation start time

At the bottom of the window:

* the operation **amount** (for example: 100,000 UZS)
* and its **status** (for example: Completed) are displayed

<figure><img src="../../.gitbook/assets/image (440).png" alt=""><figcaption></figcaption></figure>





### Making Income Entry to Cash Register

Through the **Income** action, cash receipts are entered into the cash register. This action is used to formalize sales revenue, debt repayment, or other financial income.

#### Making Income Entry

To make an income entry, click the **Income** button on the cash register card and the income window opens on the right side.

The following information is entered in the window:

* **Cash Register** – the cash register receiving the funds (usually already selected)
* **Invoice** – selected if the operation is associated with a document
* **Payment Type** – operation content (sale, return, etc.)
* **Payment Method** – how the money was received (cash, terminal, card, etc.)
* **Amount** – amount of funds being received
* **Currency** – which currency the amount is in
* **Note** – optional field for entering additional information
* **File** – option to attach a receipt or other document

<figure><img src="../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (439).png" alt=""><figcaption></figcaption></figure>

#### Saving

Based on the entered information, the following actions are performed:

* **Save** – saves the information
* **Save and Close** – saves and closes the window
* **Cancel** – cancels the action

#### Result

After the income is saved:

* the cash register balance increases
* the balance block above (cash, terminal, etc.) is updated accordingly
* a new record appears in the transactions table
* the operation status becomes **Completed**





### Making Expense from Cash Register

Through the **Expense** action, cash withdrawal from the cash register is formalized. This action is used to record expenses, payments to suppliers, or other financial expenditures in the system.

#### Making Expense

To make an expense, click the **Expense** button on the cash register card and the expense window opens on the right side.

The following information is entered in the window:

* **Cash Register** – the cash register from which funds are withdrawn (usually already selected)
* **Invoice** – selected if the operation is associated with a document
* **Payment Type** – operation content (for example: expense, payment, etc.)
* **Payment Method** – indicates how the money is withdrawn (cash, terminal, etc.)
* **Amount** – amount of funds being withdrawn
* **Currency** – which currency the amount is in
* **Note** – optional field for entering additional information
* **File** – option to attach a receipt or document

<figure><img src="../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (441).png" alt=""><figcaption></figcaption></figure>







### Transfer in Cash Register

Through the transfer action, funds from one cash register can be transferred to another. This function works **when 2 or more cash registers exist** in the system and is used to manage internal cash movements.

<figure><img src="../../.gitbook/assets/image (435).png" alt=""><figcaption></figcaption></figure>



#### Making Transfer

To perform a transfer, click the **Transfer** button on the cash register card and a special form opens on the right side.

The following information is entered in the window:

* **Cash Register** – the sending (source) cash register
* **Receiving Cash Register** – the cash register to which funds are transferred
* **Payment Method** – how the money is being transferred (cash, terminal, etc.)
* **Amount** – amount of funds being transferred
* **Currency** – monetary unit
* **Note** – additional information (optional)
* **File** – option to attach a document if needed

<figure><img src="../../.gitbook/assets/image (443).png" alt=""><figcaption></figcaption></figure>

#### Process

The transfer action works in two stages:

* **Sending (In Progress)**
  * After the transfer is saved, the operation changes to **In Progress** status
  * The money is counted as an expense from the sending cash register
  * In the receiving cash register, this operation appears as a **pending** document

<div><figure><img src="../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/image (446).png" alt=""><figcaption></figcaption></figure>

* **Receiving (Completed)**
  * After the operation is confirmed by the receiving cash register
  * The money enters the receiving cash register as income
  * The operation status in both cash registers becomes **Completed**





### Exchange in Cash Register

In the cash register section, through the exchange action, funds can be converted **by currency** or **by payment method**. These actions are used for internal management and proper distribution of cash in the cash register.

<figure><img src="../../.gitbook/assets/image (436).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (437).png" alt=""><figcaption></figcaption></figure>

### Exchange (Money)

Through this action, funds in the cash register can be transferred from one currency to another.

#### Making Exchange

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

Through this action, funds can be transferred from one payment type to another (currency does not change).

#### Making Exchange

Performed through **More → Exchange (Payment Method)**.

The following information is entered:

* **Cash Register** – the cash register where the operation is performed
* **Currency** – currency of the funds

**Expense:**

* **Amount** – outgoing amount
* **Payment Method** – channel from which money is withdrawn

**Income:**

* **Amount** – incoming amount
* **Payment Method** – channel to which money is transferred
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

