# TUSA Tab Structure Report

This report investigates the website's structure of Club & Society segment for a role of a club admin. traversing through the TUSA Account Page and Club Main Page.

Scope: `Member Admin Page - TUSA` for `clubpresident-tfc`, and the club page `Lookwhatwecando Withaform`.

Note: Most member views and the club Feed were inspected through the logged-in Chrome session. The club Photos and Albums routes repeatedly stalled the Chrome page bridge when opened through the session; a non-session URL read showed those routes redirect to login when unauthenticated, so their logged-in body content is marked as not safely captured. Several club admin-style routes returned a "New Website Under Construction" page.

## Tree 

```text
member/clubpresident-tfc - Member/admin profile area for the club president account.
|-- Store Management - Dokan vendor/store dashboard with sales analytics and store operations.
|   |-- Dashboard - Shows store completion, selling-disabled warning, balance, sales metrics, and charts.
|   |-- Products - Product list/admin area with status filters and an empty product table.
|   |-- Club Events - Vendor event-management area; route entered but full content was not safely captured after SPA timeout.
|   |-- Orders - Store order-management area with all-orders and add-new-order routes.
|   |   `-- Add New Order - Route for manually creating a store order.
|   |-- Coupons - Store coupon-management area.
|   |-- Reports - Analytics section with product, revenue, order, variation, category, stock, and statement reports.
|   |-- Reviews - Store review-management area.
|   |-- Announcements (4) - Vendor announcements area showing four announcements in the menu count.
|   |-- Withdraw - Vendor withdrawal/payout area.
|   `-- Settings - Store configuration area.
|       |-- Store - Store profile/settings page.
|       |-- Payment - Payment-method setup page.
|       |-- Shipping - Shipping settings route.
|       |-- Social Profile - Social profile settings route.
|       `-- Store SEO - Store SEO settings route.
|-- My Deals - Lists all deals/perks attached to this user/club context.
|-- Clubs - Shows clubs associated with the user and group invitations.
|   |-- My Groups - Lists four clubs: Lookwhatwecando Withaform, Food Hub, Yet another test club, and Test Club.
|   `-- Invitations - Shows outstanding club invitations; currently none.
|-- Account - Account settings and privacy controls.
|   |-- Login Information - Lets the user update account email/password after entering current password.
|   |-- Notification Settings - Lets the user choose which events send email notifications.
|   |-- Privacy - Lets the user set visibility for profile, club admin, club personnel, and rep fields.
|   |-- Export Data - Lets the user request a zip export of created account data.
|   `-- Delete Account - Lets the user confirm irreversible account deletion.
|-- Notifications - Notification inbox.
|   |-- Unread - Shows unread notifications and notification-type filters; currently none.
|   `-- Read - Shows read/all notifications and notification-type filters; currently none.
|-- My Orders - WooCommerce customer account area.
|   |-- Orders - Shows purchase history; currently no orders.
|   |-- Track Orders - Lets the user track an order by order ID and billing email.
|   |-- Addresses - Shows billing and shipping address defaults.
|   |-- Payment Methods - Shows saved payment methods; currently none.
|   `-- Cart - Shows basket status; currently empty.
|-- Profile - Public and admin profile details for the account.
|   |-- View - Displays profile fields and club personnel role.
|   |-- Profile Photo - Lets the user upload/select/delete profile photo.
|   `-- Edit Profile - Blocked for club admins except during affiliation/reaffiliation.
|-- Events - Event list search/filter view; currently no events found.
`-- Workflow - Workflow inbox/report area; currently no pending tasks.

club/lookwhatwecando-withaform - Club group page and admin-facing club tabs.
|-- Feed - Group activity feed with post composer, search/filter controls, sorting, and existing activity/document post.
|-- Photos - Club media/photo view; route requires logged-in access and stalled during Chrome inspection.
|-- Albums - Club album view; route requires logged-in access and stalled during Chrome inspection.
|-- Club Admin - Route currently returns "New Website Under Construction".
|-- Manage - Route currently returns "New Website Under Construction".
|-- Our Store - Route currently returns "New Website Under Construction".
|-- Club Deals - Route currently returns "New Website Under Construction" via direct route read.
|-- Club Docs - Route currently returns "New Website Under Construction".
|-- Exec Committee - Route currently returns "New Website Under Construction".
`-- Resources + Forms - Route currently returns "New Website Under Construction".
```

## Detailed Path Notes

### member/Store Management

This tab redirects to `/my/store-manager/?path=/analytics/Overview` and loads a Dokan vendor dashboard. The visible side menu contains Dashboard, Products, Club Events, Orders, Coupons, Reports, Reviews, Announcements (4), Withdraw, and Settings. Orders has sub-routes for All Orders and Add New Order. Reports has Products, Revenue, Orders, Variations, Categories, Stock, and Statement. Settings has Store, Payment, Shipping, Social Profile, and Store SEO.

The Dashboard view shows a selling-status warning: the account is not enabled for selling and the user should contact the admin. It also shows profile completion at 85 percent, prompting the user to add a payment method for the remaining progress. The analytics view shows Balance `$0.00`, date range set to month-to-date May 1-30, 2026 compared with May 1-30, 2025, and all performance metrics at zero: total sales, marketplace commission, net sales, orders, products sold, total earning, marketplace discount, store discount, and variations sold. Charts for Net sales and Orders show no data for the selected date range.

The Products view shows product status filters: All, Published, Pending Review, Draft, Rejected, In stock, and Out of stock, all with count zero. The product table headers are Products, Type, Stock, Status, Price, Earning, Views, and Actions, but no product rows are present. The other Dokan subviews are present in the navigation, but after Products the SPA repeatedly timed out during route switching, so their body contents were not safely captured.

### member/My Deals

The My Deals tab lists deal/perk cards associated with the user or club context. Visible deal headings included "Lookwhatwecando Withaform Member Perk - 15% Off at Teros", "please work", "test 7", "another bloody test", "Obar - 25% off food and drinks", "Featured Image, yeah! And bonus plants for plant lovers", and "Test Club's Beery Deal".

The Teros deal includes a full deal description, redemption instructions, and conditions: 15 percent off eligible full-priced products, in-store redemption, membership ID required, and sale/promotional items excluded. Users appear to be able to browse/read deal detail content from this tab; no editing controls were visible from this view.

### member/Clubs/My Groups

This view lists the clubs associated with the account. It includes sorting controls for Recently Active, Most Members, Newly Created, and Alphabetical, plus a type filter. The captured list shows 4 clubs: Lookwhatwecando Withaform, Food Hub, Yet another test club, and Test Club.

The user can browse their clubs and open the listed club pages. No create/edit controls were visible here.

### member/Clubs/Invitations

This sub-tab is the group invitation inbox. It displays the message "You have no outstanding group invites." No action buttons or invite rows were visible.

### member/Account/Login Information

This view lets the user update login credentials. It contains fields for current password, account email, new password, and repeated new password, plus a "Save Changes" action. The page notes that password fields should be left blank for no password change and includes a lost-password link near the current password field.

### member/Account/Notification Settings

This view controls email notification preferences. It presents a preferences/subscriptions table with email toggles for mentions, replies to post comments, password changes, activity feed replies, social group details changes, group promotions, group invitations, membership requests, accepted/rejected group requests, and new posts in subscribed groups. The primary action is "Save Changes".

### member/Account/Privacy

This view controls profile visibility. It contains visibility selectors for profile detail fields such as first name, last name, nickname, pronouns, UTAS student status, TUSA involvement, campus, personal bio, and junior status. It also includes club admin personal details, club personnel fields, and rep fields, each with visibility choices such as Public, All Members, and Only Me. The primary action is "Save Changes".

### member/Account/Export Data

This view explains that the user can request a copy of all data they have created on the platform. The flow sends an email verification request, then requires site admin review; if approved, a zip file is generated and emailed. The action is "Request Data Export".

### member/Account/Delete Account

This view warns that deleting the account will delete all created content and is completely irreversible. The user must tick "I understand the consequences" before using the "Delete Account" action.

### member/Notifications/Unread

This view is an unread-notification inbox. It includes filters for View All, New mentions, New activity comments, New activity posts, New followers, Group invitations and requests, Group promotions, Group details changed, and Password changed. The current state says there are no unread notifications.

### member/Notifications/Read

This view is the read/all-notification inbox with the same notification-type filters. The current state says there are no notifications.

### member/My Orders/Orders

This WooCommerce account sub-tab shows purchase history. It currently reports "No order has been made yet" and provides a "Browse products" action.

### member/My Orders/Track Orders

This sub-tab lets the user track an order. It asks for Order ID and Billing email, then provides a "Track" action. The page explains that the order ID should come from the receipt or confirmation email.

### member/My Orders/Addresses

This sub-tab shows default checkout addresses. The billing address is present for Club President Lookwhatwecando Withaform and has an Edit link. The shipping address is not set and has an Add link.

### member/My Orders/Payment Methods

This sub-tab shows saved payment methods. It currently says "No saved methods found" and provides an "Add payment method" action.

### member/My Orders/Cart

This sub-tab shows cart state. It currently says the basket is empty and provides a "Return to shop" action.

### member/Profile/View

This sub-tab displays the account's profile details. Visible fields include First Name "Club President", Last Name "Lookwhatwecando Withaform", Nickname "ClubPresidentTFC", personal name, personal email, phone number, student number, current faculty/course, Australian address, current UTAS student status, and Club Personnel role "Club President".

### member/Profile/Profile Photo

This sub-tab manages the profile photo. It explains that the profile photo is used on the profile and throughout the site. It includes Upload, Take Photo, and Delete modes, a drop area, and a "Select your file" button. Guidance says best results require an image at least 700px by 700px.

### member/Profile/Edit Profile

This sub-tab is intentionally restricted. It says club admins and presidents may only change their profile during the affiliation and reaffiliation process, and instructs the user to contact `clubs@tusa.utas.edu.au` if details need to change.

### member/Events

This tab shows an Events List with a search field and category filter. Categories include Club Events, campus events, Food Hub, Hobart City, Inveresk, Online, Orientation, Post Graduate Students, Rozelle, Sandy Bay, Shut Up and Write, Training and Workshops, TUSA Events, and UTE. The current state says "No events found".

### member/Workflow

This view opens the Workflow Inbox. It includes links/sections for Back to Account, Workflow Status, Submit a Workflow Form, and Workflow Reports. The inbox table columns are ID, Form, Submitter, Step, and Submitted; the current state says "No Pending Tasks" and shows 0 to 0 of 0.

### club/Feed

The Feed tab is the primary group activity stream. The club header shows the name "Lookwhatwecando Withaform" and description "about the club here: Gingerbread, chupa chups, oat cake dessert, lollipop topping". The page includes a Club Admin button, a notification/bell control, and the main club tab bar.

The feed view includes a post composer with the prompt "Share something with the group..." and media/document/poll-style attachment icons. Below it are search/filter controls and a sorting control set to show new posts. The visible activity item says Club President Lookwhatwecando Withaform posted an update in the group around 7 months ago and includes a PDF attachment named "This-is-a-stand-in-document-for-Lookwhatercando-with-a-form-club.pdf" with size 401 kb. A Like action is available.

### club/Photos

The Photos tab is present in the logged-in club tab bar and points to `/photos/`. When opened through the logged-in Chrome session, this route repeatedly stalled the automation bridge before its body content could be captured. A non-session URL read redirects to the WordPress login page with "Please login to access this website", confirming that the route is protected. Treat this as a logged-in media/photo view whose actual loaded contents still need manual confirmation.

### club/Albums

The Albums tab is present in the logged-in club tab bar and points to `/albums/`. Like Photos, it stalled the logged-in automation route and redirects to login without session cookies. Treat this as a protected logged-in album view whose actual loaded contents still need manual confirmation.

### club/Club Admin

The Club Admin tab points to `/rules/`. A direct route read returned a "New Website Under Construction" page. No useful club-admin controls, form fields, or tables were exposed by that route.

### club/Manage

The Manage tab points to `/admin/`. A direct route read returned "New Website Under Construction". No management controls or secondary tabs were exposed by that route in the captured response.

### club/Our Store

The Our Store tab points to `/our-store/`. A direct route read returned "New Website Under Construction". No store product listing or club storefront controls were visible in the captured response.

### club/Club Deals

The Club Deals tab points to `/deals/`. A direct route read returned "New Website Under Construction". This differs from the member My Deals tab, which did show populated deal cards.

### club/Club Docs

The Club Docs tab points to `/club-documents/`. A direct route read returned "New Website Under Construction". The only document content captured in the club area was the PDF attachment visible on the Feed.

### club/Exec Committee

The Exec Committee tab points to `/exec/`. A direct route read returned "New Website Under Construction". No committee roster or editable executive-member controls were exposed in the captured response.

### club/Resources + Forms

The Resources + Forms tab points to `/resources/`. A direct route read returned "New Website Under Construction". No resources, forms, or submission controls were exposed in the captured response.

