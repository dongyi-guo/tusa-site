# Membership Rules And Tags

Membership rules and tags are the tools for you as a club admin to grant full control of:

- When memberships expire
- What tags are applied to your members
- Who can purchase your products.

This guide will cover both the group-level settings and product-level settings. It is essential for you to configure your tags to manage:

- Membership Rules
- Membership Products

Both work together to create your membership system, you can find the place to make the configuration as table below:

| Item                    | Location                                                  | What It Controls                                |
| ----------------------- | --------------------------------------------------------- | ----------------------------------------------- |
| **Membership Rules**    | Your Club's Page > Club Admin > Membership rules and tags | Which tags grant access to your club group      |
| **Membership Products** | Product Settings (When creating or modifying products)    | Which tags are applied on purchase, who can buy |

---

## What Can Tags Do?

Membership tags can:

- **Grant access** to your club’s private members-only group
- **Control** who can see member-only content and deals
- **Expire** on dates you set, requiring members to renew
- **Restrict** who can purchase certain products

When someone purchases a membership from your club store, they receive a tag. That tag unlocks access to your club’s group and member benefits.

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

There are some scenarios that the membership system will always kick in helpful.

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

Let's say Chess Club only wants 2026 members can see and purchase the 2027 membership product right now (renewal).

In the product settings:

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

---

## Frequently Asked Questions (FAQs)

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
