# Managing Membership Rules and Tags

As a club admin, you have full control of:

- When memberships expire
- What tags are applied to your members
- Who can purchase your products.

This guide covers both the group-level settings and product-level settings.

---

## Overview: Two Places to Manage Tags

You need to config your tags to manage:

- Membership Rules
- Products

Both work together to create your membership system, you can find the place to configure them as table below:

| Item | Location | What It Controls |
| ---- | ---- | ---- |
| **Membership Rules** | Your Club's Page > Club Admin > Membership rules and tags | Which tags grant access to your club group |
| **Products** | Product Settings (When creating or modifying products) | Which tags are applied on purchase, who can buy |

---

## What can Membership Tags do?

Membership tags can:

- **Grant access** to your club’s private members-only group
- **Control** who can see member-only content and deals
- **Expire** on dates you set, requiring members to renew
- **Restrict** who can purchase certain products

When someone purchases a membership from your club store, they receive a tag. That tag unlocks access to your club’s group and member benefits.

---

## Accessing Membership Rules

**Path:** Club Dashboard → Club Admin → Membership Rules + Tags

**URL Pattern:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{your-club}/rules/`

**Who Can Access:**

- Club Presidents (organisers)
- Club Admins (group admins)
- TUSA Staff

---

## How the Form Works

### Setting Up Tags

You can configure up to **5 tag-expiry pairs** for your club:

| Field           | What It Does                                        |
|-----------------|-----------------------------------------------------|
| **Tag**         | Select the membership tag (e.g., “Chess Club 2026”) |
| **Expiry Date** | When this tag should expire (DD/MM/YYYY format)     |

### Example: Annual Membership

For a typical annual membership:

| Tag             | Expiry     |
|-----------------|------------|
| Chess Club 2026 | 31/12/2026 |

This means:

- Members with this tag can access the club group
- On 1 January 2027, the tag automatically expires
- Members lose access until they renew

### Example: Multi-Year Setup

For clubs that want to set up multiple years in advance:

| Tag             | Expiry     |
|-----------------|------------|
| Chess Club 2026 | 31/12/2026 |
| Chess Club 2027 | 31/12/2027 |
| Chess Club 2028 | 31/12/2028 |

This allows members to purchase future year memberships now, with each expiring appropriately.

---

## What Happens When Tags Expire

### Automatic Processing

A system runs every night at 12:05 AM that:

- **Checks** all clubs for expired tags
- **Removes** expired tags from your club settings
- **Updates** access rules automatically
- **Logs** the expiry for audit purposes
- **Notifies** TUSA admin of any expiries

### Member Impact

When a member’s tag expires:

- They **lose access** to the private club group
- They **cannot see** member-only deals
- They **need to renew** their membership to regain access

### You Don’t Need to Do Anything

Tag expiry is fully automatic. You don’t need to manually remove old tags or update settings when the year ends.

---

## Common Scenarios

### Starting a New Year

At the start of a new membership year:

- Go to Membership Rules + Tags
- Add the new year tag (e.g., “Your Club 2027”)
- Set expiry to end of that year (31/12/2027)
- Click Save

Old expired tags are automatically cleaned up.

### Removing All Tags

If you need to remove all membership tags:

- Select “Remove Tag” for all 5 tag slots
- Click Save

This clears all tag requirements from your club.

### Replacing an Expired Tag

If your current tag has expired and you need to add a new one:

- Add the new year tag in slot 1
- Set “Remove Tag” for other slots (clears old settings)
- Click Save

---

## Best Practices

### Tag Naming Convention

Use a consistent naming format:

- `Your Club Name YYYY` (e.g., “Chess Club 2026”)
- This matches the membership tags created during affiliation

### Expiry Dates

- Set expiry to **end of the membership period** (e.g., 31/12/2026)
- Tags expire at **11:59 PM** on the expiry date
- Processing runs at **12:05 AM** the next day

### Planning Ahead

You can set up multiple years in advance:

- Members can purchase early
- Tags activate immediately but expire on schedule
- Reduces admin work each year

---

## Understanding the Audit Log

Every tag change is logged for your club:

| What’s Logged    | Purpose                   |
|------------------|---------------------------|
| Tag additions    | Track when rules were set |
| Tag expiries     | Automatic removal record  |
| Who made changes | Accountability            |
| Timestamps       | Timeline of changes       |

TUSA staff can access these logs if issues arise.

---

## Troubleshooting

### “I saved tags but members can’t access the group”

**Check:**

- Is the tag correctly linked to your membership product?
- Did the member actually purchase the membership?
- Did the purchase go through successfully (not pending or refunded)?

If everything looks right and access still isn’t working, see [Reporting an Issue].

### “Tags expired but members still have access”

**This shouldn’t happen** — an automated daily process removes expired tags. If you notice this:

- Wait 24 hours (the system runs once daily)
- If still not fixed, see [Reporting an Issue]

### “I can’t see the Membership Rules tab”

**Check:**

- Are you logged in as a club admin or president?
- Are you on your club’s dashboard (not the main TUSA dashboard)?
- Do you have organiser status in your club group?

---

## Part 2: Product Settings (When Creating Products)

When you create a **membership product** in your store, you get additional tag controls.

### Accessing Product Tag Settings

- Go to Store Manager → Products
- Create or edit a product
- Select the **Membership** category
- The membership settings section appears automatically

### Product Expiry: Auto-Retire Products

**Problem:** You don’t want to accidentally sell “2025 Membership” in 2026.

**Solution:** Set a product expiry date.

| Setting              | What It Does                                |
|----------------------|---------------------------------------------|
| **Expiration Date**  | When to stop selling this product           |
| **Action on Expiry** | Product goes to “Draft” (hidden from store) |

**Best Practice:** Set expiry to December 31 of the membership year. Adventure clubs might choose end of January to allow for summer trips.

### Apply Tags on Purchase

When someone buys this product, give them membership tags:

| Setting                    | Purpose                                 |
|----------------------------|-----------------------------------------|
| **Apply Tags on Purchase** | Tags given to ALL purchasers            |
| **Per-variation tags**     | Additional tags for specific variations |

#### Example: Multi-Year Membership

- Apply Tags: “Chess Club 2026”, “Chess Club 2027”
- Purchaser gets access for both years

### Restrict Who Can Purchase

Control who can see and buy your products:

#### Required Tags (Any)

User must have **at least one** of these tags to see the product.

| Use Case             | Required Tag                        |
|----------------------|-------------------------------------|
| Members-only renewal | “Your Club 2025” (existing members) |
| Students only        | “Student”                           |
| Current members only | Your club’s membership tag          |

**Example:** A “2026 Renewal” product that only 2025 members can see.

#### Excluded Tags (Not)

User must **NOT have** these tags to see the product.

| Use Case             | Excluded Tag                |
|----------------------|-----------------------------|
| Exclude juniors      | “Junior”                    |
| Exclude non-students | (use Required Tags instead) |

**Example – Adventure Club:** An event where insurance doesn’t cover under-18s:

- Excluded Tags: “Junior”
- Juniors cannot see or purchase tickets

### Product vs Variation Restrictions

You can set restrictions at two levels:

| Level               | Controls                        |
|---------------------|---------------------------------|
| **Product level**   | Entire product visibility       |
| **Variation level** | Individual variation visibility |

**Example – Student vs Non-Student Pricing:**

**Product:** “Chess Club 2026 Membership”

Apply Tags: “Chess Club 2026” (everyone gets this)

**Variation 1:** “Student – \$20”

Required Tags: “Student”

Only students see this option

**Variation 2:** “Non-Student – \$40”

Excluded Tags: “Student”

Only non-students see this option

Result: Each person sees only the price tier that applies to them.

---

## Common Membership Scenarios

### Scenario 1: Simple Annual Membership

#### Group Settings (Membership Rules + Tags)

- Tag: “Chess Club 2026”
- Expiry: 31/12/2026

#### Product Settings

- Category: Membership
- Expiry: 31/12/2026
- Apply Tags: “Chess Club 2026”
- No restrictions

**Result:** Anyone can buy, gets tag, tag expires end of year, product auto-retires.

### Scenario 2: Members-Only Renewal

#### Product Settings:

- Apply Tags: “Chess Club 2027”
- Required Tags: “Chess Club 2026”

**Result:** Only 2026 members can see and purchase the 2027 renewal.

### Scenario 3: Age-Restricted Event

#### Product Settings (Event Ticket)

- Excluded Tags: “Junior”

**Result:** Under-18s (Juniors) cannot see or purchase this ticket. Perfect for events where insurance or venue restrictions apply.

### Scenario 4: Student-Only Discount Variation

#### Product Level:

- Apply Tags: “Your Club 2026”

#### Variation 1 – Student \$30

- Required Tags: “Student”

#### Variation 2 – General \$50

- Excluded Tags: “Student”

**Result:** Students only see the \$30 option, non-students only see \$50.

---

## How Tags Flow Through the System

1. Member purchases product
2. Tags applied to member's account
3. Tags sync to email lists
4. Tags checked against Group Rules
5. If tag matches → Access granted to group
6. Member can see: deals, documents, news feed
7. Daily check on tag expiry
8. When expired → Tag removed → Access revoked

---

## Related Guides

[Club Identity Model](../8-understanding-your-club/2-understanding-club-identity-the-keystone-account-model.md) — How clubs work

[Creating Membership Products](./2-creating-membership-products.md) — Setting up the products that grant tags

[Reporting an Issue](../6-general/1-reporting-an-issue.md) — When something isn’t working

---

*Membership rules give you control over your club’s access. Set them up once per year and let the system handle the rest.*
