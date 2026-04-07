# Sales

<details>

<summary>Sales module</summary>

The sales module allows viewing and managing all sales created in the system. To access the module, select the **Sales** section from the left menu and the **Sales** page opens.

On this page, the list of all sales created in the system is displayed in table format. The table shows basic information for each sale.

<figure><img src="../../.gitbook/assets/image (272).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (273).png" alt=""><figcaption></figcaption></figure>

The columns displayed in the table can be configured by the user. Users can select or modify table columns based on the information they need.

Typically, the following columns are displayed in the table:

* Date
* Customer
* Customer phone number
* Status
* Total quantity
* Total price
* Amount to be paid

Each row represents an individual sales document. Users can open a sales document by clicking on the sales row.

When a sales document is opened, the following information is displayed:

* Sales number
* Organization
* Warehouse
* Responsible person
* Customer
* Sales date
* Payment information
* Discounts
* Final amount

Additionally, at the bottom of the sales document, a list of products sold in this sale is shown in table format.

<figure><img src="../../.gitbook/assets/image (274).png" alt=""><figcaption></figcaption></figure>

When a sales document is opened, all basic information related to this sale is displayed. Here, detailed information about when and by whom the sale was created, which customer the sale was made to, and the sales amount is available.

In the sales document window, users can perform the following actions:

* **Create a return** from the sale
* **Copy** the sales document
* **Cancel** the sale
* **Download the sale in PDF or Excel format**
* **Print labels**
* Print sales receipt

A sales document typically displays the following information:

* Sales number
* Organization
* Warehouse
* Responsible person
* Customer
* Sales date
* Payment information
* Discounts
* Final amount

At the bottom of the sales document, a list of products sold in this sale is shown in table format. The table displays each product's name, unit of measurement, warehouse, quantity, price, discount, and total price.

<figure><img src="../../.gitbook/assets/image (275).png" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Creating a sale</summary>

Creating a new sales document in the system is done via the **Create** button. A sale can be created.

<figure><img src="../../.gitbook/assets/image (276).png" alt=""><figcaption></figcaption></figure>

Sales information is entered through several stages:

* Basic information
* Products
* Additional costs
* Payment

Each stage is designed to fill in a separate part of the sales document.<br>

#### **Basic information**

In this section, general information about the sale is entered.

<figure><img src="../../.gitbook/assets/image (277).png" alt=""><figcaption></figcaption></figure>

**Order -** If the sale is being made based on a previously created order, that order is selected.

**Contract-** If a contract has been signed with the customer, that contract is selected.

**Customer -** The customer to whom the product is being sold is selected; if the customer does not exist in the system, they are added via the "add" button.

<figure><img src="../../.gitbook/assets/image (279).png" alt=""><figcaption></figcaption></figure>

**Status -** Indicates which stage the sales process is in. The system has 3 types of statuses for sales:

* **New -** Indicates that the sale is not yet completed. At this stage, the sales document has been created, but the sale is not considered executed. Products in the warehouse do not decrease, but are considered **reserved** for this sale. Payment is also not considered received.
* **In Progress -** Indicates that the sale is not yet completed but is in the process of being executed. In this state as well, products are not removed from the warehouse, only **reserved** for the sale. Until payment is completed, the sale is not considered fully executed.
* **Completed -** Indicates that the sale has been fully executed. At this stage, products are **removed** from the warehouse, payment is considered **received**, and this sale is also **included in system reports**.

**Date -** The date and time the sale was executed.

**Delivery date -** The date the product is scheduled to be delivered to the customer.

**Delivery address -** The address where the product will be delivered.

**Responsible person -** The employee responsible for this sale.

**Intermediary -** If the sale was made through an intermediary, that intermediary is indicated.

**Currency -** Indicates in which currency the sale will be executed.

**Upload file -** The ability to attach additional documents or files related to the sale.

**Note -** A field for entering additional notes or reminders about the sale.



#### Entering products

Products being sold are entered in the **Products** stage of the sales document. Here, products to be added to the sale, their quantities, and prices are specified.

<figure><img src="../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

At the top of the section, the following settings are available:

**Price -** Select which price type the product price is taken from (for example: store price).&#x20;

**Warehouse -** Indicates which warehouse the product is being sold from. The available quantity of the product is shown based on the selected warehouse.



**Adding products**

Products can be added to the sale in several ways.

**1. Adding via search**\
The product name is entered in the product search field and the required product is selected from the list.

<figure><img src="../../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (282).png" alt=""><figcaption></figcaption></figure>

Via the **filter icon** next to the search field, additional filters are opened. These filters help sort products more precisely.

In the filter window, the following settings are available:

**Hide out-of-stock products**\
This setting controls whether to hide or show products that are not available in the warehouse.

* **Yes** — products that are out of stock in the warehouse are not shown in the list.
* **No** — all products, including out-of-stock products, are shown.

**Category**\
Allows filtering products by a specific category. This allows the user to see only products within the required category.



**2. Adding via quick select**\
When the **Quick Select** button is pressed, a product selection window opens. In this window, the product list is shown by category.

In this window, the following features are available:

* search for products
* view products by category
* select multiple products at once

After selecting a product, the **Save** button is pressed and the selected products are added to the sales document.

<figure><img src="../../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>





For each product added to the sale, entering its **quantity and price** is mandatory. If these fields are not filled in, the sales document cannot be finalized.

**Name -** Name of the product added to the sale.

**Unit of measurement -** The product's unit of measurement (for example: pieces, kg, liters).

**Warehouse -** Indicates which warehouse the product is being sold from. The warehouse can be selected here.

**Available quantity -** Shows the quantity of product available in the selected warehouse.

**Quantity -** The quantity of product being added to the sale. Filling this field is mandatory.

**Box quantity -** If the product is sold by boxes, the number of boxes can be entered.

**Expiration date -** The product's expiration date is shown (if available).

**Price type -** Select which price type the product price is taken from (for example: store price).

**Price -** The price per unit of the product. This field is also mandatory.

**Total price -** Automatically calculated by the system based on the entered quantity and price.

**Discount -** The amount of discount given on the product.

**Total discount -** The total amount with discount taken into account.

**Included tax -** The amount of tax calculated within the price.

**Added tax -** The amount of tax added to the product price.

**Total -** The final calculated amount for the product.

**Note -** A field for entering additional notes about the product.

<figure><img src="../../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>



#### Additional costs

During the sales process, there may be additional costs besides the product price. For example, **packaging, service fees, or other expenses**. These costs are entered into the sales document via **"Additional costs"**.

<figure><img src="../../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

In this section, the user can select a previously created additional cost type and add it to the sale. When an additional cost is added, it affects the sales amount and participates in calculating the final price.

The following columns are available in the table:

**Name -** Additional cost name (for example: packaging, delivery, etc.).

**Currency -** Indicates in which currency the cost will be entered.

**Price impact -** Shows how this cost affects the product price.

**Distribution method -** Indicates how the additional cost is distributed among products (for example: distribution by products).

**Recommended price -** The recommended additional cost value by the system.

**Maximum price -** The maximum additional cost amount that can be entered.

**Price -** The additional cost amount entered by the user.

After additional costs are entered, they are **added to the final sales amount** and reflected in the overall calculation.



#### Payment

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

In the **Payment** section of the sales document, payment information made by the customer is entered. Here it shows **which method the customer paid through** and **how much payment was made**.

At the top of the section, general calculation information for the sale is displayed:

**Sales** – total amount for the sale.\
**Included tax** – the amount of tax included in the price.\
**Added tax** – the amount of tax added to the product price.\
**Discount** – the total discount given for the sale.\
**Paid** – the amount paid by the customer.\
**Total additional cost** – the sum of additional costs.\
**Remaining** – the amount not yet paid.

At the bottom is the payments table, where the following information is entered:

**Payment method**\
The method through which the customer paid is selected. For example:

* Cash
* Card
* Terminal
* Bank transfer
* Credit
* Click
* Other payments entered in settings

**Amount**\
The amount paid through this payment method is entered.

**Currency**\
The currency in which the payment was made is selected (for example: som).

**Exchanged amount**\
If payment was made in another currency, the amount exchanged by the system is shown here.

If multiple payment methods are used for the sale, **an additional payment row can be added via the "+" button**. After payment information is entered, the sales document is **saved** and the sales process is finalized.



<figure><img src="../../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>

**1. View receipt (first button)**\
When this button is pressed, the **receipt view** for the sale opens. In this window, information such as sold products, their quantities, total amount, payment method, and change is displayed. The receipt can be **printed via printer** from this window.

**2. Change currency rate (second button)**\
If the sale is being made in another currency, this button allows **manually entering or changing the currency rate**.\
For example, in the system the dollar rate may be **12,000 som**, but for this particular customer the sale may be calculated at a **12,500 som rate**. In this case, a separate rate is entered for the sale via this button.

**3. Attach online payments (third button)**\
If **payment was made through online payment systems** for the sale, this button opens the corresponding payment window. Here you can select an existing online payment and **attach** it to this sales document.

**4. Create payment link (fourth button)**\
If the system is **integrated with other online payment services**, this button creates a **payment link** to send to the customer. The customer can make payment for the sale online through this link.

</details>

<details>

<summary>Setting plans</summary>

Sales plan setting — this is a function for setting sales targets for employees for a specific period (month). Through this section, a separate plan is set for each employee, and their fulfillment is subsequently monitored in the system.

<figure><img src="../../.gitbook/assets/image (606).png" alt=""><figcaption></figcaption></figure>

* From the top, **organization** and **month** are selected
* The **"SET PLAN"** button is pressed
* The table goes into active mode (editing opens)
* In each employee row, values are entered in the required fields:
  * amount
  * number of products
  * number of customers
  * number of sales
* The entered information is saved via the **"SAVE"** button



For each employee, the following fields are filled in:

* **Amount** – the total sales volume the employee must achieve
* **Number of products** – the quantity of products that must be sold
* **Number of customers** – the number of customers to be served
* **Number of sales** – the number of sales operations that must be completed

Through the sales plan setting function, the company sets clear goals, monitors employee activity, and has the opportunity to systematically increase sales results.

</details>

<details>

<summary>Sales dashboard</summary>

The sales dashboard displays **key indicators and analytical data** on sales activity on one page. Through this page, users can quickly monitor sales status and analyze key statistics. Data is typically formed **based on a selected date range**.

<figure><img src="../../.gitbook/assets/image (298).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (299).png" alt=""><figcaption></figcaption></figure>

**Key indicators**

At the top of the dashboard, key sales indicators are displayed in card format:

* **Sales amount** – total sales amount made during the selected period.
* **Gross revenue** – total revenue from sales.
* **Number of receipts** – number of sales operations completed.
* **Number of products** – total quantity of products sold.
* **Discount amount** – total amount of discounts given.
* **Average receipt price** – average amount per single sale.
* **Margin** – sales profit indicator in percentage.
* **Markup** – markup percentage applied to products.
* **Average number of products per receipt** – shows how many products are sold on average per receipt.

The percentages shown on the cards are calculated by **comparing current period indicators with the previous period**.



**Sales dynamics chart**

<figure><img src="../../.gitbook/assets/image (300).png" alt=""><figcaption></figcaption></figure>

On the dashboard, sales results are also displayed **in chart format**. Through the chart, you can observe how sales indicators changed during the selected period.

Two periods are compared in the chart:

* **Current period**
* **Previous period**

On the right side of the chart, you can select the indicator type. Users can change the chart by selecting one of the following:

* **Sales amount**
* **Gross revenue**
* **Discount amount**

Through this, users can analyze various sales indicators over time.

At the bottom of the sales dashboard, additional statistical information is displayed for deeper analysis of sales processes.

<figure><img src="../../.gitbook/assets/image (301).png" alt=""><figcaption></figcaption></figure>



**Best-selling products**

<figure><img src="../../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

In this section, a list of **best-selling products** for the selected period is displayed. For each product:

* product name
* how many times it was sold
* total share

is reflected. Also, the **Top** filter allows selecting how many products to display (for example, Top 5).



**Top purchasing customers**

<figure><img src="../../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

Here, a list of **top purchasing customers** within the selected period is displayed. For each customer, their **total purchase amount** is reflected. This information helps identify active customers and determine a strategy for working with them.



**Sales share by payment types**

<figure><img src="../../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

This diagram shows the **distribution of sales by payment methods**. The diagram typically reflects the following payment types:

* **Cash**
* **Via cashback**
* **Credit**

The share of each payment type in total sales is shown in percentages and amounts.



**Top selling employees**

<figure><img src="../../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

In this section, **most active employees** by sales volume are displayed. The following information is reflected in the table:

* employee name
* sales amount
* number of sales
* share in total sales

This information helps evaluate employee efficiency and analyze sales results.

</details>