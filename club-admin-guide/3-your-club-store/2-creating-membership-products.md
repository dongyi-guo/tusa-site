# Creating Membership Products

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

## Excluding Certain Users

Some products shouldn’t be available to everyone.

### Excluding Juniors

You may have some products that under-18s can’t purchase (insurance, legal requirements).

**In your product's settings:**

- Excluded Tags: “Junior”

**Result:** Anyone with the “Junior” tag cannot see this product.

### Common Exclusions

| Exclude These         | Use Excluded Tag                    |
|-----------------------|-------------------------------------|
| Under-18s             | “Junior”                            |
| Non-students          | Use Required Tags “Student” instead |
| Specific member types | The relevant tag                    |

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
|---------------------|-------------------------------------------------|
| Tag not applied     | Is the tag selected in product settings?        |
| Can’t access group  | Are group rules set in Membership Rules + Tags? |
| Product not visible | Is category set? Is it Published?               |
| Wrong people see it | Check Required/Excluded tags                    |

---

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
