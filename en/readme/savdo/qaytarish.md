# Return

<details>

<summary>Return reasons</summary>

In the sales return process, **Return reasons** are used to indicate why a product was returned. These reasons are created in the system in advance and are selected when formalizing the return document.

<figure><img src="../../.gitbook/assets/image (292).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (293).png" alt=""><figcaption></figcaption></figure>

Users can view return reasons, add new reasons, or edit existing ones through the **Sales → Return reasons** page.

When creating a new reason, the following information is entered:

**Name** – the name of the return reason.\
**Code** – identification code for the reason (optional).\
**Return type** – indicates the condition of the returned product.\
**Comment** – field for entering additional information about the reason.\
**Active** – specifies whether the reason is active or inactive.

#### Return type

<figure><img src="../../.gitbook/assets/image (294).png" alt=""><figcaption></figcaption></figure>

Depending on the return type, it is determined in what condition the product will be received in the warehouse.

If **Valid** is selected – the returned product is **received in the warehouse as a valid product** and can be resold later.

If **Invalid** is selected – the returned product is **received in the selected warehouse as an invalid product**. Such products are usually not resold and are accounted for separately.

This way, the system **automatically accounts for the valid or invalid status of returned products**.

</details>

<details>

<summary>Returning created sales</summary>

#### Returning a sale (from within the sales document)

Returning a sale can be done by clicking the **"Return"** button from within the sales document. In this method, the return document is created based on the selected sale, and the sales data is automatically transferred to the return window.

<figure><img src="../../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (288).png" alt=""><figcaption></figcaption></figure>

The return process consists of several stages.

**1. Basic information**

At this stage, the basic information of the return document is displayed and some fields are filled in.

**Sale** – which sales document the return is being made for.\
**Customer** – the customer to whom the sale was made.\
**Time** – the date and time the return is being made.\
**Responsible person** – the employee responsible for the return operation.\
**Warehouse** – indicates which warehouse the returned products will be received in.\
**Currency** – shows in which currency the return calculations will be made.\
**Reason** – the return reason is selected. This field is mandatory. Reasons are created in advance in the **sales return reasons** section.

Additionally, there is an option to **upload a file** and add a **note** if needed.

**2. Products**

This section shows the list of products sold in the sale.

The user can:

* remove products that will not be returned from the list
* enter the **quantity** for products being returned

Based on this data, the system automatically calculates the total amount for the products.

**3. Additional costs**

If there are additional costs in the return process, they are entered in this section. These costs may affect the return amount.

**4. Payment**

The payment section shows the financial calculations for the return.

The following information is reflected here:

**Amount to be paid** – the total amount for the return.\
**Discount to be withheld** – the amount of discount to be withheld in the return.\
**Total discount** – the total discount amount.\
**Cashback to be returned** – the cashback that can be returned to the customer.\
**Debt** – if the customer has a debt.\
**Cashback used** – the amount of cashback used at the time of sale.\
**Tax to be withheld** – the amount of tax to be withheld in the return.\
**Total tax** – the total tax amount.\
**Total additional price** – the amount of additional costs.\
**Amount to be returned** – the final amount that should be returned to the customer.\
**Paid** – the amount returned to the customer.

If money needs to be returned to the customer, the **return method** is selected in the payment section and the amount to be returned is entered. After the data is entered, the return document is saved.



#### Returning a sale (Creating a return from the Sales module)

The second method of returning a sale is **creating a new return document through the "Return" page in the Sales module**.

<figure><img src="../../.gitbook/assets/image (289).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (291).png" alt=""><figcaption></figcaption></figure>

In this window, all completed returns can be viewed.

The user can enter the **Sales → Return** section from the left menu and create a new return document. In this method, the return process also has **the same form and data fields as in the first method**. That is, the return document consists of the following sections:

* **Basic information**
* **Products**
* **Additional costs**
* **Payment**

The information entered in these sections and the workflow are the same as the process of creating a return from within the sales document.

In this method, the return can be done in two ways.

<figure><img src="../../.gitbook/assets/image (290).png" alt=""><figcaption></figcaption></figure>

**1. Return based on a sale**

The user selects the required sale from the **Sale** field in the return window. After the sale is selected, the system automatically retrieves data related to that sale, including:

* customer
* warehouse
* products
* prices and amounts

Then the user enters the quantity of products being returned, selects the return reason, and enters additional information if needed.

**2. Return without selecting a sale**

In this method, the user can create a return document **without selecting a sales document**. In this case, products are **entered manually in the Products section**.

The user selects the required product from those available in the warehouse and enters the quantity being returned. In this process, the system considers the product as **returned to the warehouse**.

This method is usually used in the following cases:

* when the sales document is not available in the system
* when a product is returned to the warehouse for another reason
* in inventory or technical return situations

After the data is entered, the return document is saved and the products are reflected in the system as returned to the warehouse.

</details>