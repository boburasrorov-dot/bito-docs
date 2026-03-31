---
description: Detailed analytical reports on product balances and warehouse movements.
---

# Warehouse

<details>

<summary>Product balance by organizations</summary>

<figure><img src="../../.gitbook/assets/image (249).png" alt=""><figcaption></figcaption></figure>

This report displays product balances by organizations. Through the report, you can see how much of each product is available in different organizations or branches. This report allows you to analyze product balances across warehouses or branches in one place.

<figure><img src="../../.gitbook/assets/image (261).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Image** — product image.

**Product** — product name.

**Unit of measure** — product unit of measure (for example: piece, kilogram, liter).

**Quantity** — total balance quantity of the product across all organizations.

**Organization names (for example: Jarvis, My company, My do'kon and others)** — product balance quantity in each organization or branch.

**Total** — at the end of the table, the total balance quantity for all products is shown.



**Business benefits**

Using this report, you can:

* view product balances by different branches or organizations
* quickly identify which products are available in which branch
* analyze product distribution among warehouses
* identify excess or shortage of products
* optimize logistics and warehouse management

</details>

<details>

<summary>Transfer report</summary>

<figure><img src="../../.gitbook/assets/image (250).png" alt=""><figcaption></figcaption></figure>

This report displays product transfer operations performed in the system. Through the report, you can see from which organization or warehouse products were transferred to where, the reason for transfer, quantity, and process status.

This report is used to monitor product movement between warehouses or within one organization.

<figure><img src="../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number of the transfer operation.

**Reason** — reason for product transfer.

**Number** — transfer document number.

**Code** — transfer operation code in the system.

**Date** — date and time when the transfer operation was created.

**Type** — transfer type. For example:

* Internal transfer
* Inter-company transfer

**Sender organization** — organization from which the product was sent.

**Recipient organization** — organization receiving the product.

**Sender warehouse** — warehouse from which the product was sent.

**Recipient warehouse** — warehouse receiving the product.

**Status** — status of the transfer operation. For example:

* In progress
* Completed

**Total quantity** — total quantity of products designated for transfer.

**Completed quantity** — quantity of products successfully transferred.

**Cancelled quantity** — quantity of cancelled products.

**In progress quantity** — quantity of products currently in progress.

**Product type count** — number of product types in the transfer document.

**Total cost** — total cost of products being transferred.



**Using this report, you can:**

* monitor product movement between warehouses
* see which products were sent from which organization to where
* track the status of transfer processes
* analyze reasons for product transfers
* efficiently organize logistics and warehouse management

</details>

<details>

<summary>View product range by time period</summary>

<figure><img src="../../.gitbook/assets/image (251).png" alt=""><figcaption></figcaption></figure>

This report displays the balance quantity of products by selected date and warehouse. Using the report, you can see how much of each product is available in the warehouse during a specific time period.

The report is generated only after **warehouse** and **date** are selected.

<figure><img src="../../.gitbook/assets/image (264).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Products** — product name.

**Unit of measure** — product unit of measure (for example: kg, piece, liter).

**Category** — category to which the product belongs.

**Quantity** — quantity of product available in warehouse as of the selected date.

**Reserved** — quantity of product reserved for other operations.

**Being transferred** — quantity of product in the process of being transferred to another warehouse or organization.

**Defective** — quantity of product marked as unfit for use.

**Total** — at the end of the table, the total quantity for all products is shown.



Using this report, you can:

* view warehouse balances as of a specific date
* determine in what quantities products are available
* monitor reserved products
* track products in transfer process
* analyze and plan warehouse inventory

</details>

<details>

<summary>Recommended product quantity</summary>

<figure><img src="../../.gitbook/assets/image (252).png" alt=""><figcaption></figcaption></figure>

This report recommends how much product should be purchased or added to inventory based on warehouse product balance and average daily sales. Using the report, you can determine for how many days the current inventory will last and how much product will be needed for future sales.

<figure><img src="../../.gitbook/assets/image (262).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Category** — category to which the product belongs.

**Product** — product name.

**Unit of measure** — product unit of measure (for example: kilogram, piece, liter).

**Quantity in warehouse** — product balance available in warehouse.

**Average daily sales** — average quantity of product sold per day.

**Sufficient for days** — shows for how many days the current inventory will last at the current sales rate.

**Recommended for 6 days** — recommended quantity to make product inventory sufficient for 6 days.

**Recommended for 10 days** — recommended quantity to make product inventory sufficient for 10 days.

**Recommended for 30 days** — recommended quantity to make product inventory sufficient for 30 days.

**Recommended until end of month** — recommended quantity to make product inventory sufficient until the end of the month.

**Total** — at the end of the table, the total quantity for all products is shown.



**Using this report, you can:**

* determine how long product inventory will last
* calculate how much product is needed for future sales
* prevent product shortages in the warehouse
* properly plan and purchase products
* efficiently manage warehouse inventory

</details>

<details>

<summary>Product receipt and issue</summary>

<figure><img src="../../.gitbook/assets/image (255).png" alt=""><figcaption></figcaption></figure>

This report displays product receipt and issue movements by selected date range and warehouse. Through the report, you can analyze in detail where products entered the warehouse from and through which operations they left the warehouse.

The report is generated after **date** and **warehouse** are selected.

<figure><img src="../../.gitbook/assets/image (263).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Products** — product name.

**Unit of measure** — product unit of measure (for example: kilogram, piece, liter).

**Category** — category to which the product belongs.

**Initial quantity** — quantity of product available in warehouse at the beginning of the selected period.



**Receipt section**

This section shows through which operations products entered the warehouse.

**Receipt** — quantity of product received into warehouse.

**Inventory** — quantity of product added during inventory process.

**Sales return** — quantity of product returned by customer.

**Internal transfer (receipt)** — product received through internal transfer from another warehouse.

**Inter-company transfer (receipt)** — product received through transfer from another organization.

**Manufactured** — quantity of product added to warehouse through production.



**Issue section**

This section shows through which operations products left the warehouse.

**Sales** — quantity of product sold.

**Purchase return** — quantity of product returned to supplier.

**Inventory (issue)** — quantity of product decreased during inventory process.

**Write-off** — quantity of product found defective and written off from records.

**Internal transfer (issue)** — product sent through internal transfer to another warehouse.

**Inter-company transfer (issue)** — product sent through transfer to another organization.



**Business benefits**

Using this report, you can:

* track product entry and exit movements in the warehouse
* see which operations affected product balances
* analyze warehouse movements in detail
* monitor inventory results
* efficiently organize product turnover and warehouse management

</details>

<details>

<summary>Product balance by warehouse</summary>

<figure><img src="../../.gitbook/assets/image (256).png" alt=""><figcaption></figcaption></figure>

This report displays product balances available in all warehouses belonging to the selected organization. Through the report, you can see how much of each product is in which warehouse.

<figure><img src="../../.gitbook/assets/image (265).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Image** — product image.

**Product** — product name.

**Country of manufacture** — country where the product was manufactured.

**Unit of measure** — product unit of measure (for example: kilogram, piece, liter).

**Total** — total quantity of product across all warehouses for the selected organization.

**Category** — category to which the product belongs.

**Warehouse names (for example: Main, For IP, Rulon sklad and others)** — quantity of product available in each warehouse.

**Total** — at the end of the table, the total balance for all products is shown.



Using this report, you can:

* view product balances across all warehouses belonging to the organization
* quickly identify which products are in which warehouse
* analyze product distribution among warehouses
* efficiently manage product inventory
* identify shortage or excess of products

</details>

<details>

<summary>Product balance by status</summary>

<figure><img src="../../.gitbook/assets/image (257).png" alt=""><figcaption></figcaption></figure>

This report displays warehouse product balances by various statuses. Through the report, you can see how much of the products are available in the warehouse, reserved, being transferred, or in defective condition.

This report is used to monitor the actual status of products in the warehouse and efficiently manage inventory.

<figure><img src="../../.gitbook/assets/image (266).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Products** — product name.

**Unit of measure** — product unit of measure (for example: kilogram, piece, liter).

**SKU** — unique identification code of the product in the system.

**Location in warehouse** — location of the product in the warehouse.

**Barcode** — product barcode number.

**Category** — category to which the product belongs.

**Total quantity** — total balance quantity of product in the warehouse.

**Quantity** — quantity of product currently available in the warehouse.

**Reserved** — quantity of product reserved for other operations.

When clicking on the reserved quantity, a list of invoices with reserved amounts for this product opens. The following information is displayed there:

* Name
* Reserved warehouse
* Quantity
* Created by
* Creation time

**Being transferred** — quantity of product in the process of being transferred to another warehouse or organization.

**Defective** — quantity of product marked as unfit for use.

**History** — ability to view product balance history.



**Filters**

The report can be filtered by the following parameters:

**Category** — display products by specific category.

**Warehouse** — display product balances by selected warehouse.

**Product type** — filter by product type.

**Warehouse balance** — filter by product balance status:

* **Yellow line** — product balance is approaching minimum level.
* **Red line** — product balance is critically low.
* **Out of stock** — product is out of stock in the warehouse.
* **Maximum quantity in warehouse** — product has reached maximum inventory quantity.
* **In stock** — product is available in the warehouse.



Using this report, you can:

* view the actual status of product inventory
* monitor reserved products
* track product movements between warehouses
* prevent inventory depletion
* organize warehouse management more efficiently

</details>

<details>

<summary>Product receipt</summary>

<figure><img src="../../.gitbook/assets/image (258).png" alt=""><figcaption></figcaption></figure>

This report provides information about products received into the warehouse through purchases. Through the report, you can see which product was received when, from which supplier, and to which warehouse.

This report is used to monitor products received in the warehouse, analyze work with suppliers, and monitor purchasing operations.

<figure><img src="../../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Products** — name of product received into warehouse.

**Unit of measure** — product unit of measure (for example: liter, kilogram, piece).

**Date** — date and time when product was received into warehouse.

**Number** — purchase document number. Clicking on this number allows opening the corresponding document.

**Supplier** — name of supplier who delivered the product.

**Warehouse** — warehouse where the product was received.

**Status** — current status of the document. For example:

* **Completed** — product was successfully received into warehouse.

**Receipt quantity** — quantity of product received into warehouse.

**Cost** — receipt cost of the product (purchase price).



Using this report, you can:

* monitor products received in the warehouse
* see how much product was received from which supplier
* analyze purchasing operations
* track receipt costs of products
* maintain warehouse records more accurately

</details>

<details>

<summary>Write-off report</summary>

<figure><img src="../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

This report provides information about products written off from the warehouse. Through the report, you can see which product was written off from which warehouse, for what reason, and in what quantity.

This report is used to monitor warehouse losses, track write-offs of defective or damaged products, and maintain accurate warehouse records.

<figure><img src="../../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

**The report table contains the following columns**

**№** — serial number in the table.

**Products** — name of written-off product.

**Warehouse** — name of warehouse from which product was written off.

**Reason** — shows why the product was written off. For example:

* spoiled
* damaged
* lost
* became defective

**Total quantity** — total quantity of written-off product.

**Total cost** — total cost of written-off products.



Using this report, you can:

* monitor warehouse losses
* monitor damaged or defective products
* analyze reasons for write-offs
* maintain warehouse records more accurately
* make decisions to reduce product losses

</details>