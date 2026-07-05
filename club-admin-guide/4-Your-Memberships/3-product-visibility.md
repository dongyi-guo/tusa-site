# Product Visibility

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
| --------------------- | ----------------------------------- |
| Under-18s             | “Junior”                            |
| Non-students          | Use Required Tags “Student” instead |
| Specific member types | The relevant tag                    |

---

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

**Variation 1:** “Student – \$20”

- Required Tags: “Student”
- Only students see this option

**Variation 2:** “Non-Student – \$40”

- Excluded Tags: “Student”
- Only non-students see this option

The settings above will ensure each person can only see the price tier that applies to them.

---

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

**Variation 1 – Student \$30**

- Required Tags: “Student”

**Variation 2 – General \$50**

- Excluded Tags: “Student”

This will make student members only see the \$30 option, and non-students only see \$50.

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