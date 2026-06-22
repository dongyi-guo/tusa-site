# Refunding Customers

This guide covers how to refund a customer when something goes wrong with an order — a faulty product, a cancelled event, a member changing their mind, anything that needs money to flow back.

You handle refunds entirely through your **Store Manager dashboard**. You don’t need to log in anywhere else, and you don’t need access to Stripe — your dashboard does the talking to Stripe behind the scenes when you click refund.

---

## How Refunds Work Here

The customer paid through Stripe when they checked out. That money lands in your club’s Stripe balance and **pays out to your club’s bank account within the day** — it doesn’t sit in escrow. When you process a refund, the money goes back to the customer from your Stripe balance, and your balance drops by that amount.

The whole flow:

- You click **Request Refund** on the order in your dashboard
- You enter the quantity, refund amount, and a reason
- You confirm in the popup
- Stripe sends the money back to the customer’s card automatically (5–10 business days for them to see it)
- Your order updates to **Refunded** (full) or stays **Completed** (partial)
- Your Stripe balance reflects the refund

You **never log into Stripe directly**. Clubs don’t have Stripe dashboard access — your Store Manager dashboard talks to Stripe behind the scenes, and that’s the only tool you need.

> **Important:** because Stripe pays out to you within the day, refunds come from your *current* Stripe balance — not from a holding account. If you’ve already withdrawn the money or spent it on club costs, refunding may push your balance negative. See [Where the refund money comes from](#where-the-refund-money-comes-from) below.

---

## Before You Refund

Pause and think:

| Question | Why it matters |
|----|----|
| **Is this within your refund policy?** | Some things you’ve sold (e.g., event tickets close to the date, custom merch) might have a no-refund rule. Check what you’ve told members. |
| **Has the order been fulfilled?** | Refunding a posted order is fine — but the customer still has the item. Decide if you want it back first. |
| **Is the order from your store?** | Check the welcome bar at the top of the dashboard — it shows which store you’re managing. Make sure the order is yours. |
| **Should you refund the full amount or part?** | Partial refunds are common (e.g., shipping refunded but item kept). |
| **Have you talked to the customer?** | A refund without a “we’ve sorted it” message can feel cold. Always include a note. |

If you’re not sure whether to refund, contact `clubs@tusa.utas.edu.au` for guidance before processing.

---

## Full Refund

Use this when the customer is getting all their money back.

### Step-by-step

- Open the **Store Manager dashboard** → **Orders**
- Find the order and click it to open the order details
- Click the **Request Refund** button
- **Quantity:** how many of each item you’re refunding (for a full refund, all of them)
- **Refund amount:** the full order total
- **Reason for refund:** a short note for your records (e.g., “Event cancelled — refunded all attendees”)
- Click **Submit Refund Request**
- Confirm in the popup

The order status changes to **Refunded** and the customer is emailed a refund confirmation. Because Stripe Connect is set up, the refund processes through to Stripe automatically — you don’t need to wait for TUSA to approve it.

> **One refund per order at a time.** If you’ve already submitted a refund request that’s still processing, you have to wait for it to clear before you can submit another one on the same order. If something’s gone wrong with a stuck request, contact `clubs@tusa.utas.edu.au`.

---

## Partial Refund

Use this when you’re returning some of the money but not all — refunding shipping but keeping the item, refunding one item from a multi-item order, applying a goodwill discount after the fact.

### Step-by-step

- Open the **Store Manager dashboard** → **Orders**
- Find the order and click it to open the order details
- Click the **Request Refund** button
- **Quantity:** how many of each item you’re refunding (often just one if multi-item)
- **Refund amount:** the partial amount (e.g., if the total was \$50 and you’re refunding \$10 for damaged packaging, type 10)
- **Reason for refund:** a short note for your records
- Click **Submit Refund Request**
- Confirm in the popup

After a partial refund, the order status stays **Completed** (it’s only marked Refunded when the *entire* order is refunded). The order details show what was refunded and the original total alongside.

---

## Where the Refund Money Comes From

This is the most important thing to understand about refunds — and it’s where most clubs get caught out.

### Stripe pays out within the day

When a customer pays your club, Stripe **pays that money out to your club’s bank account within the day** (on a daily payout cycle — it isn’t held in a Stripe account for you to withdraw later).

That means: by the time you process a refund a few days later, the money for that original sale is probably already in your club’s bank account, not your Stripe balance.

### The refund still has to come from somewhere

When you click Request Refund, Stripe sends the customer’s money back **from your Stripe balance**. If your Stripe balance is at \$0 (because everything’s already been paid out), Stripe runs your balance into the negative.

You can think of it as: **Stripe is now lending you the money to refund the customer**, and you’ll need to settle up.

### Clubs can’t see their Stripe balance directly

Clubs don’t have access to the Stripe dashboard, so you can’t check your balance yourself before processing a refund. **TUSA is your source of truth on this.** If you’re about to process anything bigger than a small refund — or if you’re processing several refunds at once — email `clubs@tusa.utas.edu.au` first and TUSA will let you know where your balance is sitting.

### How a negative balance gets cleared

If a refund pushes your balance below \$0, it gets resolved one of two ways:

| Option | How it works |
|----|----|
| **The next sales clear it** | When new orders come in, Stripe applies the incoming money to clear the negative balance first before paying out the rest to your club’s account. So if your balance is -\$50 and a new \$30 sale comes in, your balance becomes -\$20 and nothing pays out to you. The next sale of \$20+ clears it. |
| **Top up the balance** | TUSA can help arrange a top-up if your sales volume isn’t going to clear the balance soon enough. This is the path for end-of-semester refunds when you’re not running events. |

You’ll need TUSA’s help with the top-up route — clubs can’t do this themselves.

### Practical implications for clubs

- **Don’t spend the money the day it lands.** Keep enough in your account to cover potential refunds for at least a few weeks after each event/sale.
- **Track your refund obligations.** If you know an event is shaky and might be cancelled, don’t withdraw the ticket money to spend it before the event runs.
- **Larger refunds need bigger thinking.** Refunding 30 attendees from a \$20-each event = \$600 going back. Talk to TUSA *before* you process — they’ll know if your Stripe balance can cover it and what your options are if not.
- **Loop TUSA in early.** `clubs@tusa.utas.edu.au` is the right contact for any refund situation that feels uncertain.

---

## What Happens to Memberships, Tickets, and Tags

When the customer paid, the system applied tags to them — for events, that’s how member-tier pricing works; for memberships, that’s how their access flag is set. When you refund the order, the **money** goes back, but **the member’s tags and access don’t change on their own.** Updating them is part of managing your members, so you do it yourself after the refund — don’t assume it’s been pulled.

### What this means in practice

| Order type | What’s certain | What you should do |
|----|----|----|
| **Event ticket** | The money refunds correctly. A refund doesn’t remove the ticket-tier tag for you. | After refunding, check the member’s profile or tag list. If the ticket-tier tag is still applied and shouldn’t be, **remove it yourself** — as club president or admin you manage your own members’ tags. |
| **Membership** | The money refunds correctly. The member’s access tag may or may not be removed automatically depending on how their membership was set up. | After refunding a membership, check the member’s profile to confirm their tag/access reflects what you intended. If they’re still showing as a member, **remove the membership tag / take them off your member list yourself.** |
| **Physical product (merch)** | Just the money goes back. No tags to worry about. | Decide separately whether to ask for the item back. |
| **Hire equipment** | Hire orders are handled by TUSA, not by clubs. | Email `clubs@tusa.utas.edu.au` if a hire refund is needed. |

> **Always verify after a refund.** Don’t trust that a tag has been removed automatically — open the member’s profile and check. If the access hasn’t been pulled, **remove it yourself** — club presidents and admins manage their own members’ tags.

---

## Refund Timing

Once you click refund, here’s what the customer experiences:

| Time | What they see |
|----|----|
| **Immediately** | Refund confirmation email from your store |
| **Same day** | The refund shows as “pending” in their bank account or card statement |
| **5–10 business days** | The money is actually back on their card |

Stripe controls the timing of when banks process the refund — there’s nothing you (or even TUSA) can do to speed this up. If a customer asks why it’s taking so long, tell them the standard 5–10 business days and offer to check the refund status in your dashboard if they’re worried.

---

## Common Situations

### “Customer wants a refund the day after the event”

Most clubs have a no-refund rule for events that have already happened. Check what your event listing said about refunds. If your policy doesn’t allow it, gently decline. If you’re feeling generous, you can — but note that this sets an expectation for future events.

### “Customer says product was damaged on arrival”

- Ask for a photo
- Decide whether to refund, replace, or offer a discount
- If refunding: full refund + don’t ask for the item back if it’s unusable
- Add a note documenting what happened in case you need to claim through your insurance later

### “Customer was charged twice”

- Check the orders list — are there two orders with the same items?
- If yes, refund the duplicate (full refund, reason: “Duplicate order — accidental double-checkout”)
- If only one order shows but the customer’s bank shows two charges, it’s a payment processing issue — contact `clubs@tusa.utas.edu.au` and TUSA will check Stripe directly

### “Customer wants their membership refunded mid-year”

- Most clubs operate “no refund on memberships once the year starts” — check what your membership product page says
- If you decide to refund: full refund, the member loses access automatically
- If you want to refund the unused portion (e.g., they joined last month and want a partial back): partial refund. Their membership stays active — you’ll need to manually remove them from your member list afterwards if you want to actually end their membership

### “Customer ordered the wrong item, wants to swap”

Two ways:

- **Refund + new order:** Full refund the original, ask them to place a new order for the correct item. Cleanest for accounting.
- **Edit the order:** Change the line items in the order and adjust the total — only works if the price difference goes one way (charging extra) or the customer is okay with a small leftover credit. Refund-and-reorder is usually simpler.

### “I refunded the wrong order!”

- Refunds can’t be un-refunded. The money is on its way back to the customer. You’ll need to:
- Contact the customer and explain
- Ask them to place a new order for the same items
- Apologise — this happens, customers are usually understanding

---

## When You Can’t Refund

| Situation | What to do |
|----|----|
| **Refund button doesn’t appear or won’t submit** | The order might already be fully refunded, an existing refund request might still be pending, or the payment status might be wrong. Check the order status first. If you genuinely need to refund and can’t, contact `clubs@tusa.utas.edu.au`. |
| **Order is from a long time ago** | Stripe has time limits on how far back refunds can be processed. If the dashboard refund won’t go through and the order is old, contact `clubs@tusa.utas.edu.au` — TUSA can help work out an alternative way to settle with the customer. |
| **Customer’s card was cancelled or expired** | The refund typically still goes through to their bank — banks handle redirecting refunds to closed accounts. The customer might need to follow up with their bank, but the money does usually reach them. |
| **Customer is asking for a refund but it’s outside your policy** | You’re not obliged to refund. Politely explain your policy and what they signed up for. If you do refund anyway as a goodwill gesture, add a clear order note so future you understands why. |
| **Customer paid by bank transfer or cash** | This is rare on the website. If it happens, don’t use the refund button — talk to `clubs@tusa.utas.edu.au` for the right way to record it. |

---

## Disputes and Chargebacks

A **dispute** (also called a **chargeback**) is when a customer skips asking you for a refund and instead tells their bank “this charge was wrong, take it back.” The bank takes the money out of your Stripe account immediately.

If this happens:

- You’ll get notified that a dispute has been raised
- **There’s a deadline to respond** — usually a week or two, shown in the dispute notification. Miss it and the customer wins by default.
- Contact `clubs@tusa.utas.edu.au` immediately — TUSA helps respond to disputes because they involve Stripe directly
- Gather evidence: order details, communication with the customer, proof of delivery, screenshots

Disputes are stressful — they’re rare for clubs but they can happen. The single biggest thing you can do to prevent them is **respond to refund requests quickly**. A customer who’s been ignored for two weeks is more likely to dispute than one who got a friendly “we’ll sort this today.”

---

## Quick Reference

### Refund flow at a glance

1. Customer asks for refund
2. Check your policy + the order
3. For anything bigger than a small refund: email TUSA first
4. Store Manager → Orders → open the order → Request Refund
5. Enter quantity, amount, reason → Submit Refund Request → confirm
6. Customer auto-emailed, money on the way back (5-10 days)
7. Verify any tags / access have actually been removed

### Where everything is

| For… | Go to |
|----|----|
| Refunding an order | Store Manager → Orders → open the order → Request Refund |
| Checking past refunds | Store Manager → Orders → filter by status “Refunded” |
| Checking your Stripe balance | Email `clubs@tusa.utas.edu.au` — clubs don’t have direct access |
| Customer asking when their refund will arrive | Tell them 5–10 business days from when you processed it |
| Verifying member access was actually removed | Open the member’s profile after the refund, check tags |
| Help with a stuck refund or balance question | Email `clubs@tusa.utas.edu.au` |
| A dispute notification | Email `clubs@tusa.utas.edu.au` immediately — don’t wait |

---

## Need Help?[](#need-help)

**Email:** `clubs@tusa.utas.edu.au`

**In Person:** Visit the TUSA office

**Online:** Use the contact form on the website

---

## Related Guides[](#related-guides)

[Managing Orders](./5-managing-orders.md) — order statuses, fulfilment, day-to-day order management

[Stripe & Payments](../1-getting-started/1-stripe-&-payments.md) — how TUSA manages your club’s Stripe connection

[Managing Members](../7-managing-your-club/2-managing-club-members.md) — what happens to members when you refund their membership
