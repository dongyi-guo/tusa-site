# Creating Membership Products

[][1]

This guide explains how to create products that give buyers membership to your club. When someone purchases a membership product, they automatically get access to your club’s private group.

**Before reading this:** Make sure you’ve read [Adding Products] for the basics.

------------------------------------------------------------------------

## How Membership Products Work[][2]

    Customer purchases membership product
            ↓
    Membership tag automatically applied to their account
            ↓
    Tag matches your club's group rules
            ↓
    Customer gains access to your club group
            ↓
    Can see: deals, documents, news feed, member content
            ↓
    When tag expires → access is revoked

------------------------------------------------------------------------

## Before You Create a Membership Product[][3]

### 1. Your Tags Must Exist First[][4]

Membership tags are created when your club is affiliated/reaffirmed. You cannot create new tags yourself.

**Check your available tags:**

Go to Store Manager → Products → Add New

Select the **Membership** category

Look at the **Apply Membership Tags on Purchase** dropdown

You should see tags like “Your Club Name 2026”, “Your Club Name 2027”

**Don’t see any tags?** Contact TUSA – your tags may not have been created yet.

### 2. Your Group Rules Must Be Set[][5]

Your club group needs to know which tags grant access:

Go to your Club Dashboard

Navigate to Club Admin → Membership Rules + Tags

Set which tags grant access (e.g., “Your Club 2026”)

Set when tags expire (e.g., 31/12/2026)

See [Membership Rules Guide] for full details.

------------------------------------------------------------------------

## Creating a Membership Product – Step by Step[][6]

### Step 1: Create New Product[][7]

Go to Store Manager → Products

Click **Add New Product**

### Step 2: Enter Product Details[][8]

**Product Name:**

Clear and specific

Include the year if relevant

Examples:

– “Chess Club Membership 2026”\
– “Basketball Club Annual Membership”\
– “Gaming Society 2-Year Membership 2026-2027”

**Price:**

Your membership fee (e.g., `20` for \$20)

Can be `0` for free memberships

**Description:**

What members get

Duration of membership

When it expires

Any benefits included

Example:

    Join the Chess Club for 2026!Your membership includes:
    Access to all club meetings and events
    Member-only deals and discounts
    Access to club documents and resources
    Voting rights at AGMMembership valid until December 31, 2026.

### Step 3: Select the Membership Category[][9]

**This is critical!**

Find the **Category** section

Select **Membership** (or **Memberships**)

When you select this category, the membership settings section appears with tag options.

### Step 4: Set Product Expiry[][10]

**Why this matters:** You don’t want to accidentally sell “2025 Membership” in 2026.

Find **Membership Product Expiry** section

Set **Expiration Date** to when you want to STOP selling this product

The product automatically becomes a Draft (hidden) after this date

**Recommended:** Set to December 31 of the membership year. Adventure clubs might use end of January.

### Step 5: Apply Membership Tags[][11]

This is what actually gives buyers access to your club.

Find **Apply Membership Tags on Purchase**

Click the dropdown

Select your club’s membership tag (e.g., “Your Club 2026”)

**For multi-year memberships:** Select multiple tags

Example: “Chess Club 2026” AND “Chess Club 2027”

### Step 6: Save and Publish[][12]

Set status to **Published**

Click **Save Product**

Your membership product is now live!

------------------------------------------------------------------------

## Creating Membership with Ticket Sales[][13]

You can also grant membership when someone buys an event ticket.

### When to Use This[][14]

First event of the year includes membership

Special events that require membership

“Event + Membership” bundle deals

### How to Do It[][15]

When creating an event ticket:

Create your event as normal

For the ticket type, set it up with regular price

In the product settings (if ticket appears as product), add membership tags

**Or use the Membership Variations approach:**

Create a “Bundle” product

Include the event ticket

Apply membership tags on purchase

------------------------------------------------------------------------

## Student vs Non-Student Pricing[][16]

Many clubs have different prices for students and non-students.

### Using Variations[][17]

**Step 1: Create Variable Product**

Set Product Type to **Variable Product**

**Step 2: Add Price Attribute**

Add attribute named “Membership Type”

Values: `Student | Non-Student`

Check **Used for variations**

Save Attributes

**Step 3: Generate Variations**

Click **Generate Variations**

Two variations are created

**Step 4: Configure Each Variation**

**Student Variation:**

Price: \$20 (or your student rate)

Required Tags (Any): “Student”

This variation only visible to students

**Non-Student Variation:**

Price: \$40 (or your general rate)

Excluded Tags: “Student”

This variation only visible to non-students

**Step 5: Set Parent Tags**

On the main product:

Apply Membership Tags: “Your Club 2026”

Both student and non-student purchasers get the same membership tag – they just pay different prices.

------------------------------------------------------------------------

## Members-Only Products[][18]

Want a product only existing members can buy?

### Renewal Product (Next Year)[][19]

**Use Case:** Only 2025 members can purchase 2026 membership early.

**Settings:**

Apply Tags: “Your Club 2026”

Required Tags (Any): “Your Club 2025”

**Result:** Only people with the 2025 tag can see this product.

### Member-Exclusive Merchandise[][20]

**Use Case:** Special merchandise only for club members.

**Settings:**

(Normal merchandise settings)

Required Tags (Any): “Your Club 2026”

**Result:** Only current members can see and purchase.

------------------------------------------------------------------------

## Excluding Certain Users[][21]

Some products shouldn’t be available to everyone.

### Excluding Juniors[][22]

**Use Case:** Under-18s can’t purchase (insurance, legal requirements)

**Settings:**

Excluded Tags: “Junior”

**Result:** Anyone with the “Junior” tag cannot see this product.

### Common Exclusions[][23]

| Exclude These         | Use Excluded Tag                    |
|-----------------------|-------------------------------------|
| Under-18s             | “Junior”                            |
| Non-students          | Use Required Tags “Student” instead |
| Specific member types | The relevant tag                    |

------------------------------------------------------------------------

## Checklist: Complete Membership Product Setup[][24]

Before your membership product is ready:

\[ \] **Product name** is clear and includes year

\[ \] **Category** is set to Membership

\[ \] **Price** is correct (can be \$0 for free)

\[ \] **Description** explains what members get

\[ \] **Product expiry** is set (so it auto-hides next year)

\[ \] **Membership tag** is selected under “Apply Tags”

\[ \] **Group rules** are set (in Club Dashboard \> Membership Rules)

\[ \] Product is **Published**

------------------------------------------------------------------------

## Testing Your Membership Product[][25]

### Before Going Live[][26]

Ask a friend to test-purchase (or use a test account)

Verify they receive the membership tag

Verify they can access the club group

Check deals and member content are visible to them

### If It’s Not Working[][27]

| Problem             | Check This                                      |
|---------------------|-------------------------------------------------|
| Tag not applied     | Is the tag selected in product settings?        |
| Can’t access group  | Are group rules set in Membership Rules + Tags? |
| Product not visible | Is category set? Is it Published?               |
| Wrong people see it | Check Required/Excluded tags                    |

------------------------------------------------------------------------

## Frequently Asked Questions[][28]

### Can I create my own tags?[][29]

No. Tags are created by TUSA during affiliation/reaffiliation. Contact TUSA if you need new tags.

### What happens when membership expires?[][30]

The tag is automatically removed (daily at 12:05 AM after expiry date)

Member loses access to the club group

They need to purchase new membership to regain access

### Can someone buy membership twice?[][31]

Yes, but they’ll just get the same tag again. It won’t hurt anything, but consider whether you want to prevent this with Required Tags (exclude people who already have the tag).

### How do I offer family/group memberships?[][32]

This is complex – contact TUSA for advice. One option is to manually apply tags to additional family members.

### My membership product expired – what now?[][33]

Create a new membership product for the new year

Set up with new year’s tags

Update your group rules if needed

The old product stays hidden (as Draft)

------------------------------------------------------------------------

## Related Guides[][34]

[Adding Products] – Basic product creation

[Membership Rules][Membership Rules Guide] – Setting up group access rules

[Shipping Setup] – Required for physical products (not memberships)

------------------------------------------------------------------------

*Membership products are digital – no shipping required. The tag is the product!*
