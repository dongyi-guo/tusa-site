# TUSA Club Admin Goal Testing Read-Aloud Report

This report tests functionalities of the new TUSA website's C&S part with the club admin account Club President Lookwhatwecando Withaform.

- The club page is at: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/
- The account page is at: https://tusa-dev.its.utas.edu.au/my/members/clubpresident-tfc/

## Executive Summary

Most governance and workflow goals are reachable through the club page under `Club Admin`, `Manage`, `Club Deals`, and `Resources + Forms`. The strongest paths are the Gravity Forms-style workflows: Event Management, Reaffiliation, Bank Signatories, Club Deals, Grant Application, and Grant Claim all expose clear final submit buttons.

The weakest paths are Store Manager and Club Docs. Store Manager shows the account is not enabled for selling, which blocks or hides product/merch creation and makes the Eventin event route unstable. Club Docs is worse from a user.

oint of view: the docs guide says a document library and upload controls should exist, but the live `Club Docs` tab renders only the site header and no document UI for this account.

Upload controls are present on Bank Signatories, Club Deals, Reaffiliation, Grant Claim, Grant Application, avatar, cover photo, and CSV import. I could not complete an actual file attach through automation, so server-side upload completion remains a manual verification item.

## Goal Map

```text
club-admin-goals
|-- sell-event-tickets
|   |-- profile/store-management/club-events - Eventin route for drafting ticketed events; currently unstable/hangs in automation.
|   `-- club/resources+forms/event-management - event application/risk form that references the drafted event; final strike is Submit.
|-- sell-merch
|   `-- profile/store-management/products - product/merch list loads, but selling is disabled and product create/edit controls are not exposed.
|-- event-application
|   `-- club/resources+forms/event-management - mega-form for event, risk, stall, liquor, and grant needs; final strike is Submit.
|-- reaffiliation
|   `-- club/resources+forms/reaffiliation - annual affiliation form with uploads, committee, membership, and declaration; final strike is Submit Application.
|-- change-logo-photos
|   |-- club/manage/photo - club avatar/logo upload; final strike follows Select your file and crop/save.
|   |-- club/manage/cover-photo - club banner upload; final strike follows Select your file and crop/save.
|   `-- club/resources+forms/reaffiliation - keep/change logo and banner choices also exist in annual reaffiliation.
|-- bank-signatories
|   `-- club/club-admin/bank-signatories - bank signatory change form with SGM minutes upload; final strike is Submit Request.
|-- club-deals
|   |-- club/club-deals/add-a-deal - create public/member-only deal with featured image; final strike is Create a Deal.
|   `-- club/club-deals/edit-deals - update or delete existing deals; final strike is Submit.
|-- form-status
|   `-- profile/workflow/status - status table with form type, submitter, current step, and status; detail links open individual submissions.
|-- memberships
|   |-- club/club-admin/membership-rules-and-tags - tag/rule setup; final strike is Save membership rules.
|   |-- club/club-admin/stats-csv-export - membership stats and full CSV download.
|   |-- club/club-admin/csv-import - member import flow with tag selection and CSV dropzone.
|   `-- club/manage/members - member list and role/removal actions.
|-- club-docs
|   `-- club/club-documents - expected upload library is blank for this account; no final strike available.
|-- grants
|   |-- club/resources+forms/grants/grant-application-form - standalone grant application; final strike is Submit.
|   `-- club/resources+forms/grants/grant-claims - reimbursement/claim form with receipts upload; final strike is Submit.
`-- uploads
    |-- bank, deals, reaffiliation, grants, avatar, cover, csv-import - controls present.
    `-- club-documents - upload controls missing.
```

## Detailed Read-Aloud Notes

### sell-event-tickets

Path attempted: `profile/Store Management/Club Events`

Primary URL:
https://tusa-dev.its.utas.edu.au/store-manager/eventin/vendor_event/#/events

Related safe setup:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/etn/

Final strike expected:
- On the Eventin draft flow: `Add New Event`, then save as draft. The help guide says not to publish directly.
- On the TUSA application flow: `Submit` on Event Management.

Read-aloud:
I started from the club admin mental model: to sell tickets, I expected the user first drafts an event in Store Manager, then files the event/risk application so TUSA can approve it. The docs confirm this: create draft event first, submit event application second, then TUSA approval publishes the event.

The live Store Manager event route was the confusing part. It opened at the right-looking Eventin vendor URL, but trying to read the page repeatedly hung the browser automation bridge. As a real user, this would feel like I had found the right door but the room was not responding. I resolved the navigation by cross-checking the help guide and the Club `Manage > Events` settings, which confirm that Club Events/Eventin is the intended route.

Status:
- Path found.
- Draft event creation not safely completable in this session because the Eventin route was unstable.
- This also blocks proving ticket sale setup from the admin side.

### sell-merch

Path attempted: `profile/Store Management/Products`

Primary URL:
https://tusa-dev.its.utas.edu.au/store-manager/new/#products

Final strike expected:
- `Add New Product`, then `Save Product` after entering product name, price, image, category, stock, and publish/draft status.

Read-aloud:
I expected merch to live under Store Manager because the club guide says products, memberships, and event tickets are all store items. The product list loaded and showed one draft product called `Membership product 2`, so the route is real.

The blocker appears immediately: `Error! Your account is not enabled for selling, please contact the admin`. There was no visible `Add New Product` action. Opening the existing draft product edit URL only rendered an `Edit Product Draft` shell with the same selling-disabled error, not a workable product form.

Status:
- Store/product path found.
- Merch creation is currently blocked for this account by seller enablement/payment/account state.
- Final strike could not be reached because the create/edit form is not exposed.

### event-application

Path: `club/Resources + Forms/Event Management`

URL:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/events/

Final strike:
- `Submit`
- Safer non-final action: `Save & Continue Later`

Read-aloud:
Once Store Manager became uncertain, I looked for the official application path. This page is much clearer. It is the combined event application, risk assessment, temporary stall, liquor permit, and grant application mega-form.

The form asks whether this is for a specific event or blanket risk assessment, then collects event partners, event committee/staff, consulted groups, selected event, ticket price, venue/location, event type, description, risk areas, additional risks, supporting documents, and a declaration. It also has `Add New Risk`, `Add Document`, `Submit`, and `Save & Continue Later`.

Status:
- Form is reachable and appears functional.
- It likely depends on the event draft existing first, because the form includes a `Select your event` style field.

### reaffiliation

Path: `club/Resources + Forms/Reaffiliation`

URL:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/affiliation/

Final strike:
- `Submit Application`
- Safer non-final action: `Save & Continue Later`

Read-aloud:
This was easy to locate after understanding the club `Resources + Forms` tab. The form is long but coherent: it looks like the annual club identity, governance, membership, assets, and declaration bundle.

The page includes affiliation year, affiliation type, acronym, keep/change logo, keep/change banner, short intro, club activities, membership type checkboxes, operating locations/categories, AGM agenda/minutes upload, financial report upload, asset list upload, social links, president and executive details, committee member repeaters, declaration checkboxes, applicant email, and signature.

Upload controls found:
- `#input_17_17` logo/icon, hidden until logo-change path is active.
- `#input_17_18` featured/banner image, hidden until banner-change path is active.
- `#input_17_6` AGM agenda and minutes.
- `#input_17_10` financial report.
- `#input_17_65` club assets list.
- `#input_17_30` membership list CSV.

Status:
- Path and final strike found.
- Upload controls are present.

### change-logo-photos

Paths:
- `club/Manage/Photo`
- `club/Manage/Cover Photo`
- Also partly in `club/Resources + Forms/Reaffiliation`

URLs:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-avatar/

https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-cover-image/

Final strike:
- Avatar/logo: `Select your file`, then the crop/save step that follows.
- Cover photo: `Select your file`, then the crop/save step that follows.

Read-aloud:
The front page images split into two separate admin tasks: the square logo/avatar and the wide cover/banner. I first expected this under `Club Admin`, but the actual controls live under `Manage`, which makes sense once I saw BuddyBoss-style group management.

The avatar page says to upload an image 700 x 700 or larger. The cover page says 1950 x 450 or larger. I stopped at the file picker because selecting a file here may immediately start upload/crop and potentially change the live club image.

Status:
- Both controls are present.
- I did not test actual media replacement because that would alter live visible club assets.

### bank-signatories

Path: `club/Club Admin/Bank Signatories`

URL:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/bank/

Final strike:
- `Submit Request`

Read-aloud:
This was where I expected it to be: governance-adjacent, under `Club Admin`. The page title is `Request to Change Bank Signatories`, and the explanatory text says this is for executives after an SGM elects new bank signatories.

Fields include applicant first/last/full name, email, position held, date of change, repeatable new signatory information via `Add Signatory`, SGM minutes upload, and signature. The upload prompt says accepted file types are pdf, doc, docx, and txt, max 10 MB.

Upload control found:
- `#input_41_8` / `input_8`, visible, SGM minutes upload.

Status:
- Path, upload control, and final strike found.

### club-deals

Paths:
- `club/Club Deals/Add a Deal`
- `club/Club Deals/Edit Deals`

URLs:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/deals/new-deal/

https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/deals/edit/

Final strikes:
- Add: `Create a Deal`
- Edit: `Submit`

Read-aloud:
This was one of the more user-friendly areas. The top-level Club Deals tab separates current deals, new deal, and edit deals. I did not have to infer much.

Add a Deal asks for deal title, featured image upload, category, public content, and members-only content. Categories include Activities, Food + Drink, Health + Fitness, Retail, and Travel. Edit Deals lets the user pick an existing deal, update title/content/category/image, and optionally delete the deal.

Upload control found:
- `#input_14_14` / `input_14`, visible, Deal Featured Image, max 10 MB.

Status:
- Path, upload control, and final strike found.

### form-status

Path: `profile/Workflow/Workflow Status`

URL:
https://tusa-dev.its.utas.edu.au/my/workflow-status/

Final strike:
- None. This is a view/status page.

Read-aloud:
I first tried `Submit a Workflow Form`, but it showed `No workflow forms`. That was confusing because forms clearly exist elsewhere. The resolution is that club forms are embedded on club resource pages, while workflow status is the reporting/tracking area.

The status page is useful. It has filters for form type and status, and it shows date submitted, form name, submitter, current step, status, and details links.

Observed entries:
- ID 5206, Event Application/Risk/etc, submitted by Club President - Lookwhatwecando Withaform, Approved.
- ID 5197, Club Reaffiliation, submitted by Club President - Lookwhatwecando Withaform, Pending at Approve Application.
- ID 4368, Event Application/Risk/etc, submitted by Club President, Pending at Temporary Stall Application - Clubs Approval.

Example detail URLs:
https://tusa-dev.its.utas.edu.au/my/workflow-status/?page=gravityflow-inbox&view=entry&id=51&lid=5206

https://tusa-dev.its.utas.edu.au/my/workflow-status/?page=gravityflow-inbox&view=entry&id=17&lid=5197

Status:
- Status and submitter visibility confirmed.

### memberships

Paths:
- `club/Club Admin/Membership rules and tags`
- `club/Club Admin/Stats + CSV Export`
- `club/Club Admin/CSV Import`
- `club/Manage/Members`
- `club/Manage/Requests`

URLs:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/tags/

https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/csv/

https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/import/

https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/manage-members/

Final strikes:
- Membership rules: `Save membership rules`
- CSV export: `Download Full Member List (CSV)`
- CSV import: import/submit after selecting tags and CSV
- Member management: role/removal actions such as promote, demote, remove, kick/ban

Read-aloud:
I expected U18/current-student/associate rules to be under `Manage`, but the real rules area sits under `Club Admin`. `Manage > Members` is more about individual people and roles.

Membership rules exposes five tag/value/expiry blocks and a save button. Stats + CSV Export gives total members and breakdowns. It showed 7 total members, 3 current UTAS students, 0 junior members under 18, and no junior members requiring parental consent. CSV Import asks the user to choose membership tags first, then upload a member CSV with First Name, Last Name/Family Name, Email, and Student Number columns.

The live member list shows club admins and regular members, plus actions to demote, promote, remove, or kick/ban. I did not click those actions.

Upload control found:
- `#tusa-file-input`, hidden behind CSV dropzone text on CSV Import.

Status:
- Membership rules, member list, stats, export, and import path found.
- CSV import upload control exists but actual import was not executed.

### club-docs

Path: `club/Club Docs`

URL:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/club-documents/

Final strike:
- Expected from the guide: `Upload Document` / `Add New`, then `Save` or `Submit`.
- Actual live page: no available final strike.

Read-aloud:
This is the biggest mismatch between documentation and live UI. The club admin guide says the Club Documents tab should show a document library with upload/add controls, categories, expiry dates, uploader, upload date, and document management actions.

The live club-documents page for this account loaded only the site header/navigation and no document library content. No document table, no upload button, no file input, no category/expiry fields, and no final action appeared.

Status:
- Expected path found.
- Actual UI missing.
- This blocks managing docs uploads such as RSAs, Food Handling Certificates, Working With Vulnerable People cards, First Aid certificates, insurance, minutes, and governance files from the advertised document library.

### grants

Path: `club/Resources + Forms/Grants`

URL:
https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/grants/

Final strikes:
- Grant Application Form: `Submit`
- Grant Claims: `Submit`

Read-aloud:
At first the Grants page looked like explanatory text only because the top of the page focuses on how grants work. Scanning the page structure revealed the hidden-in-plain-sight sections: `How Grants Work`, `Grants Applied For`, `Grant Application Form`, and `Grant Claims`.

Grant Application Form is form `gform_19`. It asks which grant is being applied for, applicant details, club details, prerequisites, requested amount, application text, document selections/uploads, and acknowledgements. Grant Claim is form `gform_25`; it asks which approved grant is being claimed, reimbursement details, applicant details, summary/final budget info, and receipts/invoices. The claim dropdown currently showed no available approved grant results.

Upload controls found:
- Grant Application has `Add Document` and `Select files` controls for supporting documents.
- Grant Claim has `Receipts and Invoices` upload control, button id `gform_browse_button_25_16`, file input `#input_25_18`.

Status:
- Grant application and reimbursement/claim paths found.
- Claim can be prepared, but the approved-grant selector had no selectable results at the time of testing.

## Upload Verification Notes

Controls found:
- Bank Signatories: `#input_41_8`, SGM Minutes, visible, pdf/doc/docx/txt, max 10 MB.
- Club Deals: `#input_14_14`, Deal Featured Image, visible, max 10 MB.
- Reaffiliation: logo `#input_17_17`, banner `#input_17_18`, AGM minutes `#input_17_6`, Financial Report `#input_17_10`, Club Assets `#input_17_65`, Membership List `#input_17_30`.
- Grant Application: `Add Document` and `Select files` controls for supporting documents.
- Grant Claim: `#input_25_18` behind `Receipts and Invoices` / `Select files`.
- Manage Photo: BuddyBoss avatar picker present.
- Manage Cover Photo: BuddyBoss cover picker present.
- CSV Import: `#tusa-file-input` behind the CSV dropzone.
- Club Docs: no upload controls present.

What I could not verify automatically:
- Actual OS-level file attachment and server upload completion. The Chrome automation wrapper available in this session supports clicking and reading fields, but not `setInputFiles`, and its page-evaluate context does not expose browser `File`/`DataTransfer` constructors. So the report verifies presence/reachability of upload controls, not completed uploads.

Manual final upload checks I recommend:
- Bank Signatories: upload a txt/pdf file, stop before `Submit Request`.
- Add a Deal: upload a small png/jpg, stop before `Create a Deal`.
- Reaffiliation: upload AGM minutes, financial report, asset list, and membership CSV, stop before `Submit Application`.
- Grants: upload supporting documents/receipts, stop before each `Submit`.
- Avatar/Cover: select file only if you are comfortable potentially changing live media, then verify crop/save.
- CSV Import: select a tag and CSV, stop before import/submit.
- Club Docs: confirm whether the blank page is a permissions/configuration bug.

## Blockers And Risks

1. Store Manager selling disabled

The account sees `Error! Your account is not enabled for selling, please contact the admin`. This blocks a club admin from creating/selling merch and likely complicates paid event/ticket setup.

2. Eventin route unstable

The Eventin route for club events appears to be the intended place to create draft ticketed events, but it repeatedly hung during automation inspection.

3. Club Docs blank

The live `Club Docs` page has no visible library or upload controls despite the documentation saying it should.

4. Workflow submission page says no forms

`/my/submit-a-workflow-form/` says `No workflow forms`, while club resource pages contain the actual forms. This can mislead users who assume workflow forms start from the profile Workflow tab.

5. Grant Claim depends on approved grants

The claim form is present, but the approved-grant dropdown showed no results. That is probably correct unless a grant is approved, but the user experience gives no next-step explanation in that field.

## Final Strike Index

| Goal | URL | Final strike |
| --- | --- | --- |
| Draft ticketed event | https://tusa-dev.its.utas.edu.au/my/store-manager/eventin/vendor_event/#/events | Expected `Add New Event` then save draft; route unstable |
| Event application/risk | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/events/ | `Submit` |
| Merch/product | https://tusa-dev.its.utas.edu.au/my/store-manager/new/#products | Expected `Add New Product` / `Save Product`; blocked by seller disabled state |
| Reaffiliation | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/affiliation/ | `Submit Application` |
| Logo/avatar | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-avatar/ | `Select your file`, then crop/save |
| Cover photo | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-cover-image/ | `Select your file`, then crop/save |
| Bank signatories | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/bank/ | `Submit Request` |
| Add club deal | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/deals/new-deal/ | `Create a Deal` |
| Edit club deal | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/deals/edit/ | `Submit` |
| Form status | https://tusa-dev.its.utas.edu.au/my/workflow-status/ | No final strike; view/details page |
| Membership rules | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/tags/ | `Save membership rules` |
| Membership CSV export | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/csv/ | `Download Full Member List (CSV)` |
| Membership CSV import | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/import/ | Import/submit after tag and CSV selection |
| Member list actions | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/manage-members/ | Promote/demote/remove/kick action links |
| Club Docs | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/club-documents/ | No live final strike; page blank |
| Grant application | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/grants/ | `Submit` on Grant Application Form |
| Grant claim | https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/grants/ | `Submit` on Grant Claims |
