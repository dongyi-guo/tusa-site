# Setting Up Shipping for Your Store

If you’re selling physical products (merchandise, not memberships or tickets), you need to set up shipping. This guide explains how store shipping works.

---

## Do I Need Shipping?

You will need to set up shipping for your physical products.

**No physical products? - Skip this Guide.**

| Product Type                           | Shipping Required?   |
|----------------------------------------|----------------------|
| Merchandise (t-shirts, stickers, etc.) | **Yes**              |
| Memberships                            | No – digital product |
| Event Tickets                          | No – digital product |

---

## How Shipping Zones Work

### The Basics

TUSA has set up **shipping zones** – geographic regions where shipping can be offered. You don’t create zones, but you set your **shipping rates** within them.

### Available Zones

| Zone               | Who It Covers                                       |
|--------------------|-----------------------------------------------------|
| **Sandy Bay Area** | Postcodes 7001-7007 (Sandy Bay campus area)         |
| **Rozelle**        | Postcodes 2035-2040 (Sydney campus area)            |
| **Tasmania**       | All of Tasmania                                     |
| **Australia**      | All of Australia                                    |
| **Everywhere**     | Rest of world (blocked – no international shipping) |

### Multiple Zone Matching

A customer can match **multiple zones**. For example, someone at Sandy Bay (postcode 7004) matches:

- Sandy Bay Area ✓
- Tasmania ✓
- Australia ✓

They see shipping options from **all matching zones** and choose what suits them.

---

## Setting Up Your Shipping Rates

### Step 1: Go to Shipping Settings

- Go to **Store Manager**
- Click **Settings**
- Click **Shipping** tab

### Step 2: Configure Australia Zone (Recommended)

This gives all Australian customers a shipping option.

- Find the **Australia** zone
- Click **Add Shipping Method**
- Select **Flat Rate**
- Enter your shipping cost (recommended: `15.50`)
- Save

**Result:** Every Australian customer can choose this shipping option.

### Step 3: Add Local Pickup (Optional)

If customers can collect from your club's room or campus:

- Find the **Tasmania** zone (or relevant zone)
- Click **Add Shipping Method**
- Select **Local Pickup**
- Add collection details (where, when)
- Save

**Result:** Tasmanian customers see both flat rate AND local pickup options.

---

## Recommended Setup for Most Clubs

For clubs selling merchandise occasionally:

| Zone      | Method       | Price   | Notes                            |
|-----------|--------------|---------|----------------------------------|
| Australia | Flat Rate    | \$15.50 | Covers postage anywhere in Aus   |
| Tasmania  | Local Pickup | Free    | Collection from campus/club room |

This simple setup works for most situations.

---

## What Customers See

When a customer checks out with a physical product:

- They enter their address
- System matches their address to zones
- They see available shipping options
- They choose one
- Shipping cost is added to their order

### Example – Sandy Bay customer

- Sees: Local Pickup (free), Flat Rate (\$15.50)
- Chooses: Local Pickup
- Pays: Product price only

### Example – Melbourne customer

- Sees: Flat Rate (\$15.50) only
- No local pickup option (too far)
- Pays: Product price + \$15.50

---

## Shipping Statuses

When you ship an order, you update the status:

| Status               | When to Use                         |
|----------------------|-------------------------------------|
| **Processing**       | You’re preparing the order          |
| **Ready for pickup** | Order ready for customer collection |
| **On the way**       | You’ve posted/shipped it            |
| **Picked up**        | Customer has collected it           |
| **Delivered**        | Customer has received it            |

### Updating Order Status

- Go to Store Manager → Orders
- Find the order
- Click to open it
- Change the status
- Customer gets notified of status changes

---

## Common Questions

### “Customer says they can’t check out”

Possible causes could be:

- You haven’t set up any shipping methods
- Customer is international (blocked)
- Product is physical but shipping not configured

**Fix:** Add at least Flat Rate to Australia zone.

### “Customer sees too many options”

This is normal! If they match multiple zones, they see all options. They choose what works for them.

### “Can we ship internationally?”

No. International shipping is blocked at the platform level.

### “What should I charge for shipping?”

#### Recommendations

**Small items** (stickers, badges): \$5-10

**Medium items** (t-shirts): \$12-15

**Large items** (hoodies): \$15-20

**Or use flat rate:** \$15.50 covers most things

Consider: Australia Post costs + packaging + your time

### “Can I offer free shipping?”

Yes! Set Flat Rate to \$0. Or only offer Local Pickup (which is usually free).

### “What if I only want local pickup?”

Only add Local Pickup method to Tasmania (or relevant) zone. Don’t add Flat Rate. Customers outside Tasmania won’t be able to order.

---

## Products That Don’t Need Shipping

These products skip shipping automatically:

**Memberships** – Digital products

**Event Tickets** – Digital products

**Downloads** – Digital products

You don’t need to do anything special – they just work.

---

## Troubleshooting

### “No shipping options available” Error

If customer sees this error message at checkout, the cause might be:

- No shipping methods configured at all
- Customer’s address doesn’t match any zone with methods
- Product is set as physical but no shipping for their location

**To Fix:**

- Add Flat Rate to Australia zone
- Save
- Request the customer to retry

### Orders Coming Through Without Shipping

This might happen if:

- Product is set as “Virtual” (no shipping needed)
- All items in cart are digital

**Check:** Edit your product → Is it marked as Virtual/Downloadable? If it’s physical, uncheck those options.

### Customer Charged Wrong Amount

**Check:**

- What zone did they match?
- What shipping method did they choose?
- Review order details in Store Manager → Orders

---

## Step-by-Step: First Time Setup

If you’ve never set up shipping before, do this:

- **Go to:** Store Manager → Settings → Shipping
- **Find:** Australia zone
- **Click:** Add Shipping Method
- **Select:** Flat Rate
- **Enter:** 15.50 (or your preferred amount)
- **Click:** Save

That’s it! All Australian customers can now order your physical products.

**Optional extra:**

- Find Tasmania zone
- Add Local Pickup
- Enter collection location
- Save
- Now Tasmanian customers can choose pickup instead.

---

## Related Guides

[Adding Products](./1-adding-products-to-your-club-store.md) – Creating products

[Creating Membership Products](./2-creating-membership-products.md) – These don’t need shipping

---

*Physical products need shipping. Digital products (memberships, tickets) don’t.*
