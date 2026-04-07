# Permissions

<details open>

<summary>Permissions</summary>

**The Permissions section** is used to manage employee capabilities in the system. Through this section, it is precisely defined which module each position or employee can access and which operations they can perform. This ensures system security and enables control over each user working within their scope of responsibilities.

<figure><img src="../../.gitbook/assets/image (471).png" alt=""><figcaption></figcaption></figure>

Navigate to **HR → Permissions** section and create a new permission (role/permission set) via the **"Create"** button.

All permissions are displayed in table format in this section.

**Table columns:**

* **Name** – permission (role) name

<figure><img src="../../.gitbook/assets/image (480).png" alt=""><figcaption></figcaption></figure>



When creating a new permission, permissions are configured across system modules. Each module is opened separately and operations within it are managed.

<div><figure><img src="../../.gitbook/assets/image (481).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (482).png" alt=""><figcaption></figcaption></figure></div>

The following main operations are available for each module:

* **Create** – add new data
* **View** – view data
* **Edit** – modify existing data
* **Delete** – delete data
* **Export** – download data

There are 3 states available for each operation:

* **Denied** – no permission at all
* **If responsible** – can only work with data assigned to them
* **Granted** – can work with all data

Additionally, there is a general toggle to completely enable or disable each module. If a module is disabled, all permissions within it are automatically revoked.

Permissions work **interdependently** with each other. For example, if a sales employee is granted permission only for the **Sales** section and **Warehouse** section permissions are restricted:

* they cannot view products
* they cannot view warehouse balances
* as a result, they cannot fully execute the sales process

Therefore, when configuring permissions, it is important to consider interdependencies between modules. Practically speaking:

* for sales to function, at least product and warehouse viewing permissions must be available
* incorrectly configured permissions can restrict system functionality

Through this section, it is possible to precisely manage who can do what in the system, standardize roles, and ensure high-level security.

</details>