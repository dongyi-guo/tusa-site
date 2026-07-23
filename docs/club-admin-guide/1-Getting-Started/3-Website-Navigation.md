# Website Navigation



This guide will help you navigate the TUSA website and find what you need. As a club admin, it is important for you to be familar with **three** pages:

1. Your account page
2. Your club page
3. Your club's store manager

We will also cover important tabs in these pages.

---

## Your Account Page

Each account will have its own profile page, you can access it by:

- Clicking the avatar on the top right corner, or
- Visiting`https://tusa-dev.its.utas.edu.au/my/members/{your-username}/`
  - Replace `{your-username}` with your account's username.

Your account profile page will greet you with:

- Your avatar/photo

- Your name

- Your member type badge (Student, Club Admin, Club President, etc.)

**We encourage members to keep their profile name and avatar accurate**. This information is used to verify identity when accessing deals and other member benefits.

### Account Page Tabs

The account page will also greet you with a tab bar, including tabs below:

| Tab                  | What’s Here                     | URL Pattern                              |
| -------------------- | ------------------------------- | ---------------------------------------- |
| **Store Management** | Store manager                   | `/store-manager/`                        |
| **My Deals**         | Available deals from your clubs | `/my/members/{username}/deals/`          |
| **Clubs**            | Clubs and invitations           | `/my/members/{username}/groups/`         |
| **Account**          | Account settings                | `/my/members/{username}/settings/`       |
| **Notifications**    | Notifications                   | `/my/members/{username}/notifications/`  |
| **My Orders**        | Order management                | `/my/members/{username}/shop/`           |
| **Profile**          | Account profile                 | `/my/members/{username}`                 |
| **Events**           | Available events                | `/my/members/{username}/etn-main/`       |
| **Workflow**         | Workflow inbox                  | `/my/members/{username}/workflow-inbox/` |

---

## Your Club Page

If you are the member of a club, you will be able to access the club's page by: 

- **From your profile page,** clicking the **Clubs** tab, then select the club
- Visiting `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-handle}/`
  - Replace the `{club-handle}` with your club's handle

### Club Page Tabs

*All "URL Pattern" follows `https://tusa-dev.its.utas.edu.au/clubs/clubs-index` .*

| Tab                   | What’s Here                         | URL Pattern                     | Who Can See  |
| --------------------- | ----------------------------------- | ------------------------------- | ------------ |
| **Feed**              | Posts and newsfeeds                 | `/{club-handle}`                | Public       |
| **Photos**            | Photos                              | `/{club-handle}/photos`         | Public       |
| **Albums**            | Albums                              | `/{club-handle}/albums`         | Public       |
| **Club Admin**        | Admin area (Tags, Bank Signatories) | `/{club-handle}/rules`          | Admin only   |
| **Manage**            | Club settings                       | `/{club-handle}/admin`          | Admin only   |
| **Our Store**         | Club store                          | `/{club-handle}/our-store`      | Public       |
| **Club Deals**        | Club deals                          | `/{club-handle}/deals`          | Members only |
| **Club Docs**         | Club documentations                 | `/{club-handle}/club-documents` | Admin only   |
| **Exec Committee**    | Committee members                   | `/{club-handle}/exec`           | Public       |
| **Resources + Forms** | Resources for club operations       | `/{club-handle}/resources`      | Admin only   |

### Important Tabs

There are some tabs here worth extra noting:

#### Club Docs (Admins Only)

**URL:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-handle}/club-documents/`

The Club Docs tab is where the club admins manage official club documents. It has two sub-tabs:

| Section              | What’s Here                               |
| -------------------- | ----------------------------------------- |
| **Document Library** | View all uploaded club documents          |
| **Add a Doc**        | Upload new documents to your club library |

##### What should I add here?

It should include the essential files for your club's operation:

- Club constitution

- Meeting minutes

- Policies and procedures

- Financial records

- Other documents required for compliance

Documents uploaded here can be referenced in grant applications and other forms.

#### Club Deals (Members only)

**URL:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-handle}/deals/`

This tab contains **three** sub-tabs:

| Section           | What’s Here                                        |
| ----------------- | -------------------------------------------------- |
| **Current Deals** | View all active deals                              |
| **Add a Deal**    | Create a new deal (via Gravity Form)               |
| **Edit Deals**    | Modify or remove existing deals (via Gravity Form) |

For **members**, it will only show all available deals from the club, for **admins**, they will be able to add and modify deals.

#### Resources + Forms Tab (Admins Only)

**URL:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-handle}/resources/`

The Resources + Forms tab is where club admins access forms, applications, and compliance documents that are essential for club operations. This tab contains **five** sub-tabs:

| Section                      | What’s Here                                    |
| ---------------------------- | ---------------------------------------------- |
| **How to**                   | Assistant documentation for club admin.        |
| **Club Resources and Forms** | A searchable collection of forms and documents |
| **Reaffiliation**            | The form for annual reaffiliation              |
| **Event Management**         | Event management panel                         |
| **Grants**                   | Grant application panel                        |

For the **Event Management**, there are **five** views:

| Section                 | What’s Here                                     |
| ----------------------- | ----------------------------------------------- |
| **New Application**     | Start a new event/risk/stall/liquor application |
| **Ongoing/Completed**   | View status of submitted applications           |
| **Medical Disclosures** | Medical forms submitted by attendees            |
| **Liability Waivers**   | Signed waivers for events                       |
| **Parental Consent**    | Consent forms for under-18 attendees            |

Here you can:

- Submit event applications for approval

- Track application status

- Access compliance documents submitted by attendees

**Note:** You only see entries for your club’s applications and forms, not any other clubs.

For the **Grants**, there are **four** views:

| Section                    | What’s Here                                     |
| -------------------------- | ----------------------------------------------- |
| **How Grants Work**        | Information about the grant system              |
| **Grants Applied For**     | Your club’s grant applications and their status |
| **Grant Application Form** | Apply for a new grant                           |
| **Grant Claims**           | Claim funds for approved grants                 |

After grants submission, the funds will be processed on club's previously approved bank account.

**Important:** Grant application approval **DOES NOT MEAN** receiving money. You must submit a Grant Claim to receive funds (except startup grants).

---

## Store Manager (Admin Only)

**URL:** `https://tusa-dev.its.utas.edu.au/store-manager/`

Store manager is where you manage your club’s store, including products, orders, and many other settings.

You can access the store manager via the URL above, or you can access it through **Your Account Page > Store Management** tab.

### Why not in Club Page?

For each admin account, **We only allow ONE store of the administrated clubs can be accessed.** 

If you’re an admin for multiple clubs (so you have access to several different club groups), you still only have store access for ONE of them. If Store Manager was in the club group, clicking it might take you to a different club’s store, this may cause confusions and severe issues between your administrated clubs.

### So which is my store?

When you open Store Manager, check the **welcome bar at the top**. It shows which store you’re currently managing. Make sure it’s the right one before making changes.

### What If I want to change my store?

**Contact TUSA admin,** we will:

- Ask to be **demoted from Organizer** in the club group whose store you currently access

- Ask to be **promoted to Organizer** in the club group whose store you need

You may need to be demoted to regular member first, then re-promote, as getting promoted to a new store requires losing access to the old one.

### What if I need to manage multiple stores?

**Use different login profiles** for each club admin role:

- One login for Club A admin duties

- A different login for Club B admin duties

This avoids access conflicts and keeps things clear, zero confusion about which store you’re managing.

---

*Keep your profile updated for the best experience across the TUSA platform.*