# Production

<details open>

<summary>Production</summary>

The **Production module** enables management of the product manufacturing process, raw material consumption, and automated acceptance of finished goods to the warehouse. Through this module, production orders are created, and warehouse movements are automatically executed based on them. This module is used to control the production process, calculate costs, and efficiently utilize resources.

Access Production → **Production** section and click the **"Create"** button to initiate a new production process.

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

When creating a production order, the following main fields are filled in:

* **Code** – unique identifier for the production document
* **Responsible person**\* – employee responsible for the process
* **Currency**\* – accounting currency (UZS and others)
* **Materials write-off warehouse**\* – warehouse from which raw materials are taken
* **Products receiving warehouse**\* – warehouse where finished goods are received
* **Materials write-off date**\* – raw material expense date
* **Warehouse receipt date**\* – finished goods receipt date
* **Recipe** – pre-created recipe
* **Quantity** – volume of product to be manufactured
* **Status** – process status (New, In Progress, Completed)
* **Note** – additional information

In the production window, the following sections are automatically formed based on the recipe:

#### **Raw Materials**

This section displays the products required for production.

* Product name
* Quantity in warehouse
* Quantity to be consumed
* Alternative products
* Expiration date
* Total cost

#### **Finished Goods**

Reflects the resulting products and records receipt to the warehouse.

#### **Additional Expenses**

Production-related expenses are added and affect the total cost.

System operation logic:

* When a recipe is selected, raw materials are automatically calculated
* When production is completed:
  * Raw materials are written off from the warehouse
  * Finished goods are received to the warehouse
  * Expenses are added to the product cost

</details>