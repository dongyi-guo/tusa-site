# Sell Memberships

This guide explains how to create products that give buyers membership to your club. When someone purchases a membership product, they automatically get access to your club’s private group.

**Before reading this:** Make sure you’ve read [Adding Products](./1-adding-products-to-your-club-store.md) for the basics.

---

## How Membership Products Work

After the customer purchases a membership product:

1. A membership tag will be applied to their account automatically. 
   - The tag will match your club's group rules.
2. The customer will gain access to your club group.
   - They can see: deals, documents, news feed, member content.
3. When the tag expires, the customer's access will be revoked.

---

## Before You Create a Membership Product

### 1. Your Tags Must Exist First

Membership tags are created when your club is affiliated/reaffirmed. You cannot create new tags yourself.

#### Check your available tags:

- Go to Store Manager → Products → Add New
- Select the **Membership** category
- Look at the **Apply Membership Tags on Purchase** dropdown
- You should see tags like “Your Club Name 2026”, “Your Club Name 2027”

**Don’t see any tags?** Contact TUSA – your tags may not have been created yet.

### 2. Your Group Rules Must Be Set

Your club group needs to know which tags grant access:

- Go to your Club Dashboard.
- Navigate to Club Admin → Membership Rules + Tags
- Set which tags grant access (e.g., “Your Club 2026”)
- Set when tags expire (e.g., 31/12/2026)

See [Membership Rules Guide] for full details.

---

## Creating a Membership Product – Step by Step

### Step 1: Create New Product

- Go to Store Manager → Products
- Click **Add New Product**

### Step 2: Enter Product Details

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
- For example:

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

## Creating Membership with Ticket Sales

You can also grant membership when someone buys an event ticket.

### When to Use This

- First event of the year includes membership
- Special events that require membership
- “Event + Membership” bundle deals

### How to Do It

When creating an event ticket:

- Create your event as normal
- For the ticket type, set it up with regular price
- In the product settings (if ticket appears as product), add membership tags

**Or use the Membership Variations approach:**

- Create a “Bundle” product
- Include the event ticket
- Apply membership tags on purchase

---

## Student vs Non-Student Pricing

Many clubs have different prices for students and non-students.

### Using Variations

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

You will need to apply your Membership Tags on the main product, such as “Your Club 2026”.

Both student and non-student purchasers get the same membership tag – they just pay different prices.

---

## Checklist: Complete Membership Product Setup

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

## Testing Your Membership Product

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



## Part 2: Membership Product Settings



When you create a **membership product** in your store, you get additional tag controls.

### Accessing Product Tag Settings



You can manage tags for each product:

- Go to Store Manager → Products
- Create or edit a product
- Select the **Membership** category
- The membership settings section appears automatically

### Product Expiry: Auto-Retire Products



You don’t want to accidentally sell “2025 Membership” in 2026. To avoid this, set a product expiry date for the tag.

| Setting              | What It Does                                |
| -------------------- | ------------------------------------------- |
| **Expiration Date**  | When to stop selling this product           |
| **Action on Expiry** | Product goes to “Draft” (hidden from store) |

**Best Practice:** Set expiry to December 31 of the membership year. Adventure clubs might choose end of January to allow for summer trips.

### Tag Application / Membership Activation Upon Purchasing



When someone buys this product, give them membership tags:

| Setting                    | Purpose                                 |
| -------------------------- | --------------------------------------- |
| **Apply Tags on Purchase** | Tags given to ALL purchasers            |
| **Per-variation tags**     | Additional tags for specific variations |

#### Example: Multi-Year Membership



Your club can manage multi-year membership with multiple tags with respectively expiries:

- Apply Tags: “Chess Club 2026”, “Chess Club 2027”
- Purchaser gets access for both years

### Restrictions via Tags



Control who can see and buy your products:

#### Required Tags (Any)



User must have **at least one** of these tags to see the product.

| Use Case             | Required Tag                        |
| -------------------- | ----------------------------------- |
| Members-only renewal | “Your Club 2025” (existing members) |
| Students only        | “Student”                           |
| Current members only | Your club’s membership tag          |

**Example:** You can have a “2026 Renewal” product that only 2025 members can see.

#### Excluded Tags (Not)



User must **NOT have** these tags to see the product.

| Use Case             | Excluded Tag                |
| -------------------- | --------------------------- |
| Exclude juniors      | “Junior”                    |
| Exclude non-students | (use Required Tags instead) |

**Example:** There is an event where insurance doesn’t cover under-18s:

- Excluded Tags: “Junior”
- Juniors cannot see or purchase tickets

### Product vs Variation Restrictions



You can set restrictions at two levels:

| Level               | Controls                        |
| ------------------- | ------------------------------- |
| **Product level**   | Entire product visibility       |
| **Variation level** | Individual variation visibility |

#### Example – Student vs Non-Student Pricing:



Let's say Chess Club has their membership's price varies depending on whether buyer is a student.

**Product:** “Chess Club 2026 Membership”

- Apply Tags: “Chess Club 2026” (every member this year can see it)

**Variation 1:** “Student – $20”

- Required Tags: “Student”
- Only students see this option

**Variation 2:** “Non-Student – $40”

- Excluded Tags: “Student”
- Only non-students see this option

The settings above will ensure each person can only see the price tier that applies to them.

------

## Common Membership Scenarios



### Scenario 1: Simple Annual Membership



Assume:

- Your club's membership renews every year
- Everyone can purchase current year's membership
- Everyone who does not renew will lose their membership automatically
- Current year's membership product will disappear automatically when it's no longer eligible (this year has passed)

Let's say it's the Chess Club again, the **Group Settings (Membership Rules + Tags)** should be:

- Tag: “Chess Club 2026”
- Expiry: 31/12/2026

And the **Product Settings** should be:

- Category: Membership
- Expiry: 31/12/2026
- Apply Tags: “Chess Club 2026”
- No restrictions

Now anyone can buy, gets tag, tag expires end of year, product auto-retires.

### Scenario 2: Members-Only Renewal



#### Product Settings



Let's say Chess Club only wants 2026 members can see and purchase the 2027 membership product right now (renewal).

- Apply Tags: “Chess Club 2027”
- Required Tags: “Chess Club 2026”

### Scenario 3: Age-Restricted Event



If an event cannot accommodate underage customers due to reasons such as insurance:

- Excluded Tags: “Junior”

**Result:** Under-18s (Juniors) cannot see or purchase this ticket. Perfect for events where insurance or venue restrictions apply.

### Scenario 4: Student-Only Discount Variation



**Product:**

- Apply your product tags, such as: “Your Club 2026”

**Variation 1 – Student $30**

- Required Tags: “Student”

**Variation 2 – General $50**

- Excluded Tags: “Student”

This will make student members only see the $30 option, and non-students only see $50.



## Frequently Asked Questions

### Can I create my own tags?

No. Tags are created by TUSA during affiliation/reaffiliation. Contact TUSA if you need new tags.

### What happens when membership expires?

- The tag is automatically removed (daily at 12:05 AM after expiry date)
- Member loses access to the club group
- They need to purchase new membership to regain access

### Can someone buy membership twice?

Yes, but they’ll just get the same tag again. It won’t hurt anything, but consider whether you want to prevent this with Required Tags (exclude people who already have the tag).

### How do I offer family/group memberships?

This is complex – contact TUSA for advice. One option is to manually apply tags to additional family members.

### My membership product expired – what now?

- Create a new membership product for the new year
- Set up with new year’s tags
- Update your group rules if needed
- The old product stays hidden (as Draft)

---

## Related Guides

[Adding Products](./1-adding-products-to-your-club-store.md) – Basic product creation

[Membership Rules](./4-managing-membership-rules-and-tags.md) – Setting up group access rules

[Shipping Setup](./3-setting-up-shipping-for-your-store.md) – Required for physical products (not memberships)

---

*Membership products are digital – no shipping required. The tag is the product!*

