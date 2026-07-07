# Membership Products

Membership is not just a title for your club members, it is a symbol of belonging. Create a membership product to segue others into your club and become a member or unlock your members to exclusive events, and use memberships and the tag system to manage your member's privileges and the exclusive contents they could get.

- Membership product is a type of product managed via Store Manager, please make sure you’ve read [Your Products](./1-Your-Products.md) page for the basics
- On the TUSA website, memberships work through **tags.** When customer purchases your membership product:

  - Membership tag(s) upon your setting will be applied to customer's account automatically

  - All rules reflected by the tag will apply immediately
  
  - With the tag, the account will automatically gain access to your club’s private group, unlocking contents such as:
    - Deals
    - Documents
    - News feed
    - Member contents
  
  - When the tag expires, the customer's access will be revoked.

---

## What Do I Need?

There are **two** essential things you need to pay attention:

### Your Tags

**During your affiliation or reaffiliation, membership tags of your club will be created for you, as you cannot create new tags yourself.** Make sure they are present in your club's settings:

- Go to **Store Manager → Products → Add New Product**
- Select the **Membership** category
- Look at the **Apply Membership Tags on Purchase** dropdown
- You should see tags like “Your Club Name 2026”, “Your Club Name 2027”

**Don’t see any tags?** Contact TUSA – your tags may not have been created yet.

### Tag Expiry

Your club group needs to know which tags grant access and set a proper expiry on it:

- Go to **your club page**.
- Navigate to **Club Admin → Membership Rules + Tags**
- Set which tags to c (e.g., “Your Club 2026”)
- Set when tags expire (e.g., 31/12/2026)

---

## Steps For Your Membership Product

### Step 1: Create New Product

- Go to **Store Manager → Products**
- Click **Add New Product**

### Step 2: Enter Product Details

Fill in the product details with some best practices:

#### Product Name

- Clear and specific
- Include the year if relevant
- For example:
  - “Chess Club Membership 2026”
  - “Basketball Club Annual Membership”
  - “Gaming Society 2-Year Membership 2026-2027”

#### Price

- Your membership fee (e.g., `20` for \$20)
- Can be `0` for free memberships

#### Description

- What members get
- Duration of membership
- When it expires
- Any benefits included

An example description could be: 

> Join the Chess Club for 2026! Your membership includes:
>
> - Access to all club meetings and events
> - Member-only deals and discounts
> - Access to club documents and resources
> - Voting rights at AGM
>
> Membership valid until December 31, 2026.

### Step 3: Select the Membership Category

**This is critical!**

- Find the **Category** section
- Select **Membership** (or **Memberships**)

When you select this category, the membership settings section appears with tag options.

### Step 4: Set Product Expiry

You don’t want to accidentally sell “2025 Membership” in 2026. To set expiry for a product:

- Find **Membership Product Expiry** section
- Set **Expiration Date** to when you want to STOP selling this product
- The product automatically becomes a Draft (hidden) after this date

**Recommended:** Set to December 31 of the membership year. Adventure clubs might use end of January.

### Step 5: Apply Membership Tags

The tag gives your buyers the access to your club.

- Find **Apply Membership Tags on Purchase**
  Click the dropdown
- Select your club’s membership tag (e.g., “Your Club 2026”)

**For multi-year memberships:** Select multiple tags applicable.

Example: “Chess Club 2026” AND “Chess Club 2027”

### Step 6: Save and Publish

- Set status to **Published**
- Click **Save Product**
- Your membership product is now live!

---

## For Ticket Sales

Besides connecting your new members in, membership products can also be used to:

- Sell membership as an event ticket
  - The “Event + Membership” bundle deals
  - For example: the first event of the year usually includes membership
- Special events that require membership

### Setup

When creating an event ticket:

- Create your event as normal
- For the ticket type, set it up with regular price
- While ticket appears in the product section, edit the product by adding membership tags

**Or use the Membership Variations approach:**

- Create a “Bundle” product
- Include the event ticket
- Apply membership tags on purchase

---

## Student vs Non-Student Pricing

Many clubs have different prices for students and non-students, to achieve this, set product variations for the products you intend to have different price tags:

#### Step 1: Create Variable Product

- Set Product Type to **Variable Product**

#### Step 2: Add Price Attribute

- Add attribute named “Membership Type”
- Values: `Student | Non-Student`
- Check **Used for variations**
- Save Attributes

#### Step 3: Generate Variations

- Click **Generate Variations**
- Two variations are created

#### Step 4: Configure Each Variation

##### For Student Variation

- Price: \$20 (or your student rate)
- Required Tags (Any): “Student”
- After set, this variation will be only visible to students.

##### Non-Student Variation

- Price: \$40 (or your general rate)
- Excluded Tags: “Student”
- After set, this variation will be only visible to non-students.

#### Step 5: Set Parent Tags

- You will need to apply your Membership Tags on the main product, such as “Your Club 2026”.

Both student and non-student purchasers get the same membership tag – they just pay different prices.

---

## Members-Only Products

You can display a product that only existing members can buy.

### Example: Renewal Product

An example could be Membership Renewal, you want your club's 2025 members can purchase 2026 membership early but not anyone else. You could set a Membership Renewal Product that is Members-Only.

**In your product's settings:**

- Apply Tags: “Your Club 2026”
- Required Tags (Any): “Your Club 2025”

**Result:** Only people with the 2025 tag can see this product.

### Example: Member-Exclusive Merchandise

You may want special merchandise only sold to club members.

**In your product's settings:**

- Required Tags (Any): “Your Club 2026”

**Result:** Only current members can see and purchase.

---

## The Two Sides of Every Club[][2]

Every TUSA club has two sides that work together:

### 1. The Public-Facing Club Store

The store is your club’s **public face**. Anyone can see it.

| What’s Visible          | Description                                              |
| ----------------------- | -------------------------------------------------------- |
| **Club Profile**        | Your name, logo, description, social links               |
| **Events Archive**      | Past and upcoming event tickets                          |
| **Merchandise**         | Club merch for sale                                      |
| **Deals Teasers**       | Public preview of member deals (full details are hidden) |
| **Membership Products** | How people join your club                                |

**Key point:** When someone purchases a membership product from your store, they receive a **membership tag** — that tag is what unlocks the private side of your club.

### 2. The Private Members-Only Group

The group is your club’s **private community**. Only members who hold the membership tag can get in.

| What’s Private          | Description                        |
| ----------------------- | ---------------------------------- |
| **News Feed**           | Club announcements and discussions |
| **Member Directory**    | See who’s in your club             |
| **Club Documents**      | Constitutions, minutes, resources  |
| **Full Deal Details**   | Complete discount codes and offers |
| **Member Interactions** | Comments, posts, connections       |

**The membership tag is the key:** Buying membership in the store grants the tag, which unlocks the group.

---

## Excluding Certain Users

Some products shouldn’t be available to everyone.

### Excluding Juniors

You may have some products that under-18s can’t purchase (insurance, legal requirements).

**In your product's settings:**

- Excluded Tags: “Junior”

**Result:** Anyone with the “Junior” tag cannot see this product.

### Common Exclusions

| Exclude These         | Use Excluded Tag                    |
| --------------------- | ----------------------------------- |
| Under-18s             | “Junior”                            |
| Non-students          | Use Required Tags “Student” instead |
| Specific member types | The relevant tag                    |

---

## Checklist

Before your membership product is ready:

- **Product name** is clear and includes year
- **Category** is set to Membership
- **Price** is correct (can be \$0 for free)
- **Description** explains what members get
- **Product expiry** is set (so it auto-hides next year)
- **Membership tag** is selected under “Apply Tags”
- **Group rules** are set (in Club Dashboard \> Membership Rules)
- **Publish** your product

---

## Test It

### Before Going Live

- Ask a friend to test-purchase (or use a test account)
- Verify they receive the membership tag
- Verify they can access the club group
- Check deals and member content are visible to them

### If It’s Not Working

| Problem             | Check This                                      |
| ------------------- | ----------------------------------------------- |
| Tag not applied     | Is the tag selected in product settings?        |
| Can’t access group  | Are group rules set in Membership Rules + Tags? |
| Product not visible | Is category set? Is it Published?               |
| Wrong people see it | Check Required/Excluded tags                    |

---

## Related Guides

[Adding Products](./1-adding-products-to-your-club-store.md) – Basic product creation

[Membership Rules](./4-managing-membership-rules-and-tags.md) – Setting up group access rules

[Shipping Setup](./3-setting-up-shipping-for-your-store.md) – Required for physical products (not memberships)

---

*Membership products are digital – no shipping required. The tag is the product!*

