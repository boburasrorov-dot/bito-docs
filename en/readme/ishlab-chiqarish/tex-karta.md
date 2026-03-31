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

# Routing

<details open>

<summary>Creating a routing</summary>

The routing section is used to link production stages in sequence and form a complete production process. Here, stages are interconnected, and the order in which the product is manufactured is defined.

Navigate to Production → **Routing** section and create a new routing.

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

When creating a routing, the following fields are filled in:

* **Name**\* – routing name
* **Code** – routing identifier
* **Parent group** – category assignment
* **Note** – additional information

<figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

Within the routing, the sequence of stages is entered:

* **Stage** – current stage is selected
* **Next stage** – stage to be executed next
* **Recipe** – recipe associated with this stage

System operation logic:

* Stages are first created in the **Stages section**
* In the routing, these stages are selected and linked in sequence
* Each stage is connected to the next stage, forming a complete production chain
* This routing is subsequently applied in the production process

</details>