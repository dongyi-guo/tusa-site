# Finding Your Way Around: Profile and Group Navigation

[][1]

This guide helps you find things on the TUSA website. We’ll cover your profile tabs, club group tabs, and where to access specific features like deals.

------------------------------------------------------------------------

## Your Profile: Personal Hub[][2]

Your profile is your personal space on TUSA. Access it by clicking your avatar or going to your profile URL.

**URL Pattern:** `https://tusa-dev.its.utas.edu.au/my/members/{your-username}/`

### Profile Header[][3]

Your profile shows:

Your avatar/photo

Your display name

Your member type badge (Student, Club Admin, Club President, etc.)

**Important:** We encourage members to keep their profile name and avatar accurate. This information is used to verify identity when accessing deals and other member benefits.

### Profile Tabs[][4]

| Tab           | What’s Here                  | URL Pattern                         |
| ------------- | ---------------------------- | ----------------------------------- |
| **Activity**  | Your posts and activity feed | `/my/members/{username}/`           |
| **Profile**   | Your personal information    | `/my/members/{username}/profile/`   |
| **Groups**    | Clubs you belong to          | `/my/members/{username}/groups/`    |
| **Deals**     | Your personal deals list     | `/my/members/{username}/deals/`     |
| **Documents** | Your personal documents      | `/my/members/{username}/documents/` |
| **Settings**  | Account settings             | `/my/members/{username}/settings/`  |

------------------------------------------------------------------------

## Accessing Deals: Two Paths[][5]

There are two ways to access club deals. They show different information.

### Path 1: Your Profile Deals Tab (Recommended)[][6]

**URL:** `https://tusa-dev.its.utas.edu.au/my/members/{your-username}/deals/`

**Example:** `https://tusa-dev.its.utas.edu.au/my/members/a-lined-design/deals/`

| What You See                 | Description                          |
| ---------------------------- | ------------------------------------ |
| **Your avatar and name**     | Confirms your identity               |
| **Deals you’re entitled to** | Based on your club memberships       |
| **Full deal details**        | Discount codes, instructions         |
| **Verification**             | Shows YOU have access to these deals |

**Use this when:** You need to show a business that you’re entitled to a deal. Your name and photo appear, verifying you’re the member.

### Path 2: Via Club Group[][7]

**Navigation:** Profile Tab → Groups → Choose Your Club → Club Deals → Current Deals

**URL:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/deals/`

**Example:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/tusa/deals/`

| What You See                 | Description                   |
| ---------------------------- | ----------------------------- |
| **Club branding**            | Club name and logo            |
| **Available deals**          | All deals for this club       |
| **Deal details**             | Information about each deal   |
| **No personal verification** | Doesn’t show YOUR entitlement |

**Use this when:** You want to browse what deals a club offers, but don’t need to prove your membership.

### Which Path to Use?[][8]

| Situation                       | Best Path                                 |
| ------------------------------- | ----------------------------------------- |
| Showing ID at a business        | Profile Deals Tab (shows your name/photo) |
| Browsing available deals        | Either works                              |
| Checking if a deal exists       | Club Group path                           |
| Proving membership for discount | Profile Deals Tab                         |

------------------------------------------------------------------------

## Club Group Navigation[][9]

When you’re a member of a club, you can access the club group with its various tabs.

**URL Pattern:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/`

### How to Get to Your Club Group[][10]

**Method 1: From Your Profile**

Go to your profile

Click the **Groups** tab

Click on the club name

**Method 2: Direct URL**\
Navigate to: `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/`

**Method 3: From Clubs Directory**

Go to the Clubs page

Find and click your club

### Club Group Tabs[][11]

| Tab                   | What’s Here                                         | Who Can See           |
| --------------------- | --------------------------------------------------- | --------------------- |
| **Activity**          | Club news feed and posts                            | Members               |
| **Documents**         | Club documents (constitution, minutes)              | Members               |
| **Deals**             | Club deals and discounts (admins can also add/edit) | Members + Admins      |
| **Events**            | Club events                                         | Members (some public) |
| **Photos**            | Club photo albums                                   | Members               |
| **Club Docs**         | Document library and uploads                        | Admins only           |
| **Resources + Forms** | Event applications, compliance forms, grants        | Admins only           |
| **Manage**            | Member management, settings                         | Admins only           |

### Club Docs Tab (Admins Only)[][12]

The Club Docs tab is where club admins manage official club documents.

**URL:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/club-documents/`

| Section              | What’s Here                               |
| -------------------- | ----------------------------------------- |
| **Document Library** | View all uploaded club documents          |
| **Add a Doc**        | Upload new documents to your club library |

**What to upload here:**

Club constitution

Meeting minutes

Policies and procedures

Financial records

Any documents required for compliance

Documents uploaded here can be referenced in grant applications and other forms.

### Deals Tab (Members + Admins)[][13]

The Deals tab shows member deals. Admins have additional options to create and manage deals.

**URL:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/deals/`

**What Members See:**

Current Deals – browse available deals for this club

**What Admins See:**

| Section           | What’s Here                                        |
| ----------------- | -------------------------------------------------- |
| **Current Deals** | View all active deals                              |
| **Add a Deal**    | Create a new deal (via Gravity Form)               |
| **Edit Deals**    | Modify or remove existing deals (via Gravity Form) |

**Creating Deals:**

Click “Add a Deal” and complete the form

Set deal title, description, and redemption details

Choose which membership tags can see the full deal

Public users see teaser info; members see redemption codes

See [CLUB-DEALS.md] for technical documentation.

### Resources + Forms Tab (Admins Only)[][14]

The Resources + Forms tab is where club admins access forms, applications, and compliance documents.

**URL:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/resources/`

The first section contains a **Resource Library** – a searchable collection of forms and documents. When you click on a tile:

If the form needs to be filled in your club context, it will say so

Follow the instructions provided in each document/form

**Events Section:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/resources/events/`

| Section                 | What’s Here                                     |
| ----------------------- | ----------------------------------------------- |
| **New Application**     | Start a new event/risk/stall/liquor application |
| **Ongoing/Completed**   | View status of submitted applications           |
| **Medical Disclosures** | Medical forms submitted by attendees            |
| **Liability Waivers**   | Signed waivers for events                       |
| **Parental Consent**    | Consent forms for under-18 attendees            |

**This is where you:**

Submit event applications for approval

Track application status

Access compliance documents submitted by attendees

**Note:** You only see entries for YOUR club. The system automatically filters to show only your club’s applications and forms.

**Grants Section:** `https://tusa-dev.its.utas.edu.au/clubs/clubs-index/{club-slug}/resources/grants/`

| Section                    | What’s Here                                     |
| -------------------------- | ----------------------------------------------- |
| **How Grants Work**        | Information about the grant system              |
| **Grants Applied For**     | Your club’s grant applications and their status |
| **Grant Application Form** | Apply for a new grant                           |
| **Grant Claims**           | Claim funds for approved grants                 |

**Grant Claims Process:**

First, select the grant you were approved for

Then complete the claim form

Funds are processed after claim submission (requires approved bank details)

**Important:** Grant approval ≠ receiving money. You must submit a Grant Claim to receive funds (except startup grants).

See [Applying for Grants] for full details.

### Hidden Tabs (And Why)[][15]

Some tabs are intentionally hidden:

| Hidden Tab       | Why It’s Hidden                                              |
| ---------------- | ------------------------------------------------------------ |
| **Members**      | Privacy – members don’t need to see who else is in the club. We don’t use contact/chat features. |
| **Send Invites** | Wrong method for adding members. Use membership tags via product purchases instead. |

------------------------------------------------------------------------

## Club Store Navigation[][16]

The club store is the public-facing shop for each club.

**URL Pattern:** `https://tusa-dev.its.utas.edu.au/store/{club-slug}/`

### What’s in the Store[][17]

| Section            | What’s Here                       | Access               |
| ------------------ | --------------------------------- | -------------------- |
| **About**          | Club description, social links    | Public               |
| **Products**       | Merchandise, memberships, tickets | Public               |
| **Events**         | Event tickets for sale            | Public               |
| **Deals (Teaser)** | Preview of member deals           | Public (teaser only) |

### Store vs Group Deals[][18]

| Store Deals           | Group Deals        |
| --------------------- | ------------------ |
| Public teaser only    | Full details       |
| Shows what exists     | Shows how to use   |
| Encourages membership | Rewards membership |

------------------------------------------------------------------------

## Store Manager (Admin Only)[][19]

Store Manager is where you manage your club’s store – products, orders, settings.

**Access:** Profile → Store Manager tab

**URL:** `https://tusa-dev.its.utas.edu.au/my/store-manager/`

### Why Store Manager Isn’t in the Club Group[][20]

You might wonder: “Why do I access Store Manager through my profile, not through the club group?”

**The reason:** You can only have access to ONE store at a time.

If you’re an admin for multiple clubs (so you have access to several different club groups), you still only have store access for ONE of them. If Store Manager was in the club group, clicking it might take you to a different club’s store — confusing!

### Which Store Am I In?[][21]

When you open Store Manager, check the **welcome bar at the top**. It shows which store you’re currently managing. Make sure it’s the right one before making changes.

### Changing Store Access[][22]

If you need access to a different club’s store:

**Contact TUSA admin**

Ask to be **demoted from Organizer** in the club group whose store you currently access

Ask to be **promoted to Organizer** in the club group whose store you need

You may need to be demoted to regular member first, then re-promoted

**Remember:** You can only be vendor staff for one store at a time. Getting promoted to a new store requires losing access to the old one.

### Recommendation: Separate Profiles[][23]

If you’re involved with multiple clubs, we recommend using **different login profiles** for each club admin role:

One login for Club A admin duties

A different login for Club B admin duties

No confusion about which store you’re managing

This avoids access conflicts and keeps things clear.

------------------------------------------------------------------------

## Club Dashboard (Admin Only)[][24]

The Club Dashboard is within Store Manager – it’s where you manage products, orders, and club-specific settings.

**URL:** `https://tusa-dev.its.utas.edu.au/dashboard/`

Or navigate via: Profile → Store Manager → Dashboard

### Dashboard Tabs[][25]

| Tab                    | What’s Here                   |
| ---------------------- | ----------------------------- |
| **Dashboard Home**     | Overview and quick actions    |
| **Products**           | Manage store products         |
| **Orders**             | View and manage orders        |
| **Club Admin**         | Club-specific admin tools     |
| **Stats + CSV Export** | Member exports and statistics |
| **Settings**           | Store and profile settings    |

### Accessing Member Exports[][26]

**Path:** Club Dashboard → Club Admin → Stats + CSV Export

This is where you download member lists for reaffiliation and record-keeping.

------------------------------------------------------------------------

## Quick Reference: Common Tasks[][27]

### For Regular Members[][28]

| I want to…          | Go to…                        |
| ------------------- | ----------------------------- |
| See my deals        | Profile → Deals tab           |
| Find club documents | My club group → Documents tab |
| Check club events   | My club group → Events tab    |
| Update my profile   | Profile → Settings            |
| Join a club         | Club store → Buy membership   |

### For Club Admins[][29]

| I want to…         | Go to…                                      |
| ------------------ | ------------------------------------------- |
| Manage products    | Dashboard → Products                        |
| Export member list | Dashboard → Club Admin → Stats + CSV Export |
| Post announcement  | Club group → Activity (create post)         |
| Upload document    | Club group → Documents → Upload             |
| Create a deal      | Dashboard → Deals (or via group)            |

### For Club Presidents[][30]

| I want to…             | Go to…                        |
| ---------------------- | ----------------------------- |
| Complete reaffiliation | Dashboard → Reaffiliation tab |
| Manage store settings  | Dashboard → Settings          |
| Update committee       | Reaffiliation form (annual)   |
| View all club info     | Dashboard → Overview          |

------------------------------------------------------------------------

## URL Patterns Reference[][31]

### Profile URLs[][32]

    Base: /my/members/{username}/
    Activity: /my/members/{username}/
    Profile: /my/members/{username}/profile/
    Groups: /my/members/{username}/groups/
    Deals: /my/members/{username}/deals/

### Club Group URLs[][33]

    Base: /clubs/clubs-index/{club-slug}/
    Activity: /clubs/clubs-index/{club-slug}/
    Members: /clubs/clubs-index/{club-slug}/members/
    Documents: /clubs/clubs-index/{club-slug}/documents/
    Deals: /clubs/clubs-index/{club-slug}/deals/

### Club Store URLs[][34]

    Store: /store/{club-slug}/
    Products: /store/{club-slug}/section/products/

### Dashboard URLs[][35]

    Dashboard: /dashboard/
    Products: /dashboard/products/
    Orders: /dashboard/orders/
    Settings: /dashboard/settings/store/

------------------------------------------------------------------------

## Verifying Your Identity for Deals[][36]

When using a deal at a participating business, you may need to prove you’re a member.

### Best Practice[][37]

Go to your **Profile Deals tab** on your phone

Show the screen to the business

They can see:

– Your name\
– Your photo/avatar\
– The deal you’re claiming\
– Verification you’re entitled to it

### Why Profile Accuracy Matters[][38]

Businesses need to verify YOU are the member claiming the deal. Having an accurate:

Display name (your real name)

Profile photo (recognisable as you)

…makes verification quick and easy.

------------------------------------------------------------------------

*Keep your profile updated for the best experience across the TUSA platform.*