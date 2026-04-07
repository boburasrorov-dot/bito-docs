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

# Internal Transfers

<details>

<summary>Internal Transfer Requests</summary>

Through the Internal Transfer Requests section, you can create advance requests for transferring products between warehouses and control the process. This process helps systematically organize logistics and warehouse management.

To create an internal transfer request, the user goes to the **Warehouse → Internal Transfer Requests** section and creates a new document.

<figure><img src="../../.gitbook/assets/image (402).png" alt=""><figcaption></figcaption></figure>

The following information is entered:

* **Status** — document status (e.g.: New, Approved, etc.)
* **ITR Number** — document number
* **Transfer Type** — transfer direction (e.g.: between warehouses)
* **Time** — document creation date and time
* **Transfer Time** — planned transfer date
* **Sender Warehouse** — warehouse from which products are dispatched
* **Receiver Warehouse** — warehouse to which products go
* **Sender** — employee responsible for dispatch
* **Receiver** — receiving employee
* **Reason** — transfer reason (based on pre-created reasons)
* **Upload File** — attach document (optional)
* **Note** — additional comment (optional)

<figure><img src="../../.gitbook/assets/image (403).png" alt=""><figcaption></figcaption></figure>

Products to be transferred are added in the lower section:

* product is searched or selected
* quantity to be transferred is entered
* available quantity in warehouse is displayed

Advantages of this section:

* pre-planning the transfer process
* controlling movement between warehouses
* clearly defining employee responsibilities
* ability for subsequent reporting and analysis

For example:\
If a product is running out in one warehouse, an internal transfer request is first created to bring the product from another warehouse, and after approval, the actual transfer is carried out.



</details>

<details>

<summary>Internal Transfers</summary>

Through the Internal Transfers section, the actual process of transferring products between warehouses is carried out. This section allows transferring products from one warehouse to another based on internal transfer requests or independently.

To create an internal transfer, the user goes to the **Warehouse → Internal Transfers** section and clicks the "Create" button.

<figure><img src="../../.gitbook/assets/image (404).png" alt=""><figcaption></figcaption></figure>



The following information is entered:

* **Internal Transfer Request** — if a previously created request exists, it can be selected
* **Status** — document status (e.g.: New, Completed)
* **IT Number** — document number
* **Date** — document date
* **Transfer Type** — transfer direction (e.g.: inter-warehouse)
* **Transfer Time** — actual transfer time
* **Sender Warehouse** — warehouse from which products are dispatched
* **Receiver Warehouse** — warehouse to which products go
* **Sender** — employee responsible for dispatch
* **Receiver** — receiving employee
* **Reason** — transfer reason
* **Upload File** — attach document (optional)
* **Comment** — additional information (optional)

<figure><img src="../../.gitbook/assets/image (406).png" alt=""><figcaption></figcaption></figure>

Products are added in the lower section:

* product is selected or searched
* quantity to be transferred is entered
* available quantity in warehouse is displayed
* expiration date is also selected if necessary

<figure><img src="../../.gitbook/assets/image (405).png" alt=""><figcaption></figcaption></figure>

Additional features:

* **Import** — upload products via file
* **Quick Select** — quickly add products
* **Auto-fill** — automatically enter quantity based on available balance

If products need to be sent from "Main Warehouse" to "Store Warehouse," an internal transfer document is created, and after approval, the product is decreased from one warehouse and added to the other.

</details>