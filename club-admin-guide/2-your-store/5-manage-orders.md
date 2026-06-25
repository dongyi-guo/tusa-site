# Managing Orders

This guide covers viewing and managing orders for your club store.

---

## Accessing Orders

### Getting There

- Go to your **Profile**
- Click **Store Manager**
- Click **Dashboard**
- Click **Orders** tab

**Direct URL:** `https://tusa-dev.its.utas.edu.au/store-manager/new/#orders`

**Check If It's Your Store Before managing orders**, check the **Welcome Bar** at the top of the dashboard. It shows which store you’re managing. Make sure it’s your club’s store.

---

## Understanding Order Statuses

Orders move through different statuses as they’re processed. TUSA uses both standard WooCommerce statuses and some custom ones.

### Standard Statuses

An ongoing order (undrafted) can have seven standard statuses:

| Status              | What It Means                                             |
| ------------------- | --------------------------------------------------------- |
| **Pending Payment** | Order placed but payment not yet received                 |
| **Processing**      | Payment received, order ready to be fulfilled             |
| **Completed**       | Order fully fulfilled                                     |
| **Cancelled**       | Order cancelled (by you or customer)                      |
| **Refunded**        | Payment returned to customer                              |
| **Failed**          | Payment failed                                            |
| **On Hold**         | Waiting for something (payment verification, stock, etc.) |

### Custom Statuses

TUSA has added these custom statuses for specific scenarios:

| Status                 | What It Means                                      | When to Use                          |
| ---------------------- | -------------------------------------------------- | ------------------------------------ |
| **Ready for Pickup**   | Order prepared and waiting for customer collection | When order is packed and ready       |
| **Pickedup**           | Customer has collected their order                 | When customer collects in person     |
| **On the Way**         | Order dispatched for delivery                      | When you’ve posted/shipped the order |
| **Delivered**          | Order received by customer                         | When delivery confirmed              |
| **Returned from Hire** | Hire equipment returned                            | For TUSA Hire Store items            |

---

## Viewing Orders

### Order List

The Orders page shows all orders for your store with information below:

| Column      | What It Shows                        |
| ----------- | ------------------------------------ |
| **Order**   | Order number (click to view details) |
| **Date**    | When the order was placed            |
| **Status**  | Current order status                 |
| **Total**   | Order total amount                   |
| **Actions** | Quick action buttons                 |

### Filtering Orders

You can use the filter options to find specific orders:

- By status (Processing, Completed, etc.)
- By date range
- By customer name or email

### Order Details

Click an order number to see:

- Customer information
- Items ordered
- Payment details
- Shipping address (if applicable)
- Order notes

---

## Processing Orders

Depends on the type of orders and products/memberships, the order processing will also change accordingly.

### For Pickup Orders

- Order comes in as **Processing**
- Prepare the order
- Change status to **Ready for Pickup**
- Customer arrives → change to **Pickedup**

### For Shipped Orders

- Order comes in as **Processing**
- Pack and post the order
- Change status to **On the Way**
- Optionally add tracking info in order notes
- When delivered → change to **Delivered** (or let customer confirm)

### For Digital Products/Memberships

- Order comes in as **Processing**
- Membership tags applied automatically
- Change status to **Completed**

> [!TIP] Steps To Change the Status
>
> - Open the order
> - Find the **Status** dropdown
> - Select the new status
> - Click **Update**


Or use the **quick action button** if available from the orders list,

### Order Notes

It is always a good practice to add order notes, you can use order notes to:

- Record tracking numbers
- Note customer communication
- Log any issues or special requests

There are two types of notes:

- **Customer Notes:** Customer receives email notification
- **Private Notes:** Only visible to store admins

---

## Common Scenarios

### Customer Hasn’t Collected Their Order

- Check the order date
- Send a reminder (use customer’s email from order)
- If no response after reasonable time, contact TUSA for guidance

### Customer Wants to Cancel

- Check if order can be cancelled (not already shipped/collected)
- Change status to **Cancelled**
- Process refund if payment was taken

### Wrong Item or Quantity

- Add private note documenting the issue
- Contact customer to arrange resolution
- Update order or create new order as needed

### Partial Pickup

If customer only collects some items:

- Add a note specifying what was collected
- Keep status as **Processing** or **Ready for Pickup** until complete

---

## Membership Orders

Membership product orders work slightly differently:

- **Tags applied automatically** when order completes
- No physical fulfilment needed
- Order can usually go straight to **Completed**
- Check that member appears in your member list

If membership tags haven’t applied:

- Check the order status is Completed
- Verify the product has correct tag settings
- Contact TUSA support if issue persists

---

## Event Ticket Orders

For event ticket orders:

- Ticket is typically digital (PDF or email)
- No shipping required
- Order can usually go to **Completed** after payment
- Attendee should receive ticket/confirmation automatically

---

## Tips

### Check Orders Regularly

- Don’t let orders sit in Processing too long
- Customers expect timely responses

### Use Notes Generously

- Future you will thank past you
- Helpful if TUSA needs to assist

### Communicate With Customers**

- If there’s a delay, let them know
- Use the customer note feature to send updates

### Keep stock updated

- If products go out of stock, update your listings
- Prevents orders you can’t fulfil

---

## Need Help?

**Email:** <clubs@tusa.edu.au>

**Visit:** TUSA Clubs & Societies office

**Dashboard:** Use the feedback form for questions