### Accessing Membership Rules + Tags

You can manage your membership rules and tags via **a form under your club's page**:

**Path:** Your Club's Page > Club Admin > Membership Rules + Tags

**URL Pattern:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{your-club}/rules/`

**Who Can Access:**

- Club Presidents (organisers)
- Club Admins (group admins)
- TUSA Staff

---

### Setting Up Tags

With the form, you can configure up to **5 tag-expiry pairs** for your club:

| Field           | What It Does                                        |
| --------------- | --------------------------------------------------- |
| **Tag**         | Select the membership tag (e.g., “Chess Club 2026”) |
| **Expiry Date** | When this tag should expire (DD/MM/YYYY format)     |

#### Example: Annual Membership

Let's say Chess Club has a typical annual membership, and its renewal happens on December 31st:

| Tag             | Expiry     |
| --------------- | ---------- |
| Chess Club 2026 | 31/12/2026 |

This means:

- Members with this tag can access the club group
- On 1 January 2027, the tag automatically expires
- Members lose access unless renewal (with next year's tag assigned to their account) 

#### Example: Multi-Year Setup

Let's say Chess Club allows current members to subscribe for coming years:

| Tag             | Expiry     |
| --------------- | ---------- |
| Chess Club 2026 | 31/12/2026 |
| Chess Club 2027 | 31/12/2027 |
| Chess Club 2028 | 31/12/2028 |

This allows members to purchase future year memberships with each membership activating and expiring appropriately.

---

### Tag Expiry

In practice, we recommend all tags should have a maximum five-year expiry to maintain updated and proper access control for club admins.

#### Automatic Processing

A system runs every night at 12:05 AM that:

- **Checks** all clubs for expired tags
- **Removes** expired tags from your club settings
- **Updates** access rules automatically
- **Logs** the expiry for audit purposes
- **Notifies** TUSA admin of any expiries

#### Member Impact

When a member’s tag expires:

- They **lose access** to the private club group
- They **cannot see** member-only deals
- They **need to renew** their membership to regain access

#### You Don’t Need to Do Anything

Tag expiry is fully automatic. You don’t need to manually remove old tags or update settings when the year ends.

---

### Common Scenarios

You may step into scenarios below regularly:

#### Starting a New Year

At the start of a new membership year:

- Visit Membership Rules & Tags
  - Your Club's Page > Club Admin > Membership Rules + Tags
- Add the new year tag (e.g., “Your Club 2027”)
- Set expiry to end of that year (31/12/2027)
- Click Save

Old expired tags are automatically cleaned up.

#### Removing All Tags

If you need to remove all membership tags:

- Select “Remove Tag” for all 5 tag slots
- Click Save

This clears all tag requirements from your club.

#### Replacing an Expired Tag

If your current tag has expired, and you need to add a new one:

- Add the new year tag in slot 1
- Set “Remove Tag” for other slots (clears old settings)
- Click Save

---

### Best Practices

To maximum your business performance, we recommend some best practices while setting up your tags:

#### Naming Convention

Use a consistent naming format:

- `Your Club Name YYYY` (e.g., “Chess Club 2026”)
- This matches the membership tags created during affiliation

#### Expiry Dates

- Set expiry to **end of the membership period** (e.g., 31/12/2026)
- Tags expire at **11:59 PM** on the expiry date
- Processing runs at **12:05 AM** the next day

#### Planning Ahead

You can set up multiple years in advance so:

- Members can purchase early
- Tags activate immediately but expire on schedule
- Reduces admin work each year

---

### Understanding the Audit Log

Every tag change is logged for your club:

| What’s Logged    | Purpose                   |
| ---------------- | ------------------------- |
| Tag additions    | Track when rules were set |
| Tag expiries     | Automatic removal record  |
| Who made changes | Accountability            |
| Timestamps       | Timeline of changes       |

TUSA staff can access these logs if issues arise.

---

### Troubleshooting

There might be some tricky scenarios:

#### Members can’t access the group even tag's saved

**Check:**

- Is the tag correctly linked to your membership product?
- Did the member actually purchase the membership?
- Did the purchase go through successfully (not pending or refunded)?

If everything looks right and access still isn’t working, see [Reporting an Issue].

#### Members can still access even tag's expired

**This shouldn’t happen**, an automated daily process removes expired tags. If you notice this:

- Wait 24 hours (the system runs once daily)
- If still not fixed, see [Reporting an Issue]

#### I can’t see the Membership Rules tab

**Check:**

- Are you logged in as a club admin or president?
- Are you on your club’s dashboard (not the main TUSA dashboard)?
- Do you have organiser status in your club group?

