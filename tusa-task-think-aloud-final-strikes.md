# TUSA Goal Testing: Think-Aloud Notes And Final Strikes

Scope:
- Member/admin page: https://tusa-dev.its.utas.edu.au/my/members/clubpresident-tfc/
- Club page: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/

Safety rule followed:
- I stopped before any final submit, save, create, publish, delete, import, payment, media replacement, membership role change, or live upload action.
- The "final strike" below is the last action the real user would click after verifying the details.

## 1. List an event to sell tickets

Final-strike path:
- Draft event/tickets: https://tusa-dev.its.utas.edu.au/my/store-manager/eventin/vendor_event/#/events
- Event approval form: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/events/

Final strike:
- Expected draft event action: `Add New Event`, then save the event as draft.
- Approval action: `Submit` on the Event Management form.

Think-aloud:
I expected ticket sales to start from Store Manager, because events with tickets behave like sellable store/event objects. The help guide confirmed the intended sequence: create a draft event first, then submit the Event Application/Risk Assessment, then TUSA approval publishes the event.

The Eventin route looked like the right place but was unstable during testing. It repeatedly hung while being inspected, so I could confirm the route but not safely reach the event creation form. I then cross-checked the Event Management form, which clearly supports event approval and ticket-price details once a draft event exists.

Outcome:
- Path found.
- Ticketed event setup is not safely completable in this session because the Eventin route is unstable.

## 2. Create and sell their own merch

Final-strike path:
- https://tusa-dev.its.utas.edu.au/my/store-manager/new/#products

Final strike:
- Expected action: `Add New Product`, then `Save Product`.
- Actual final strike could not be reached because the account is not enabled for selling.

Think-aloud:
I went to Store Manager > Products because the club guide says merchandise, memberships, and tickets are managed through the club store. The products page loaded and showed one draft item, `Membership product 2`, so the products area exists.

The blocker appeared immediately: `Error! Your account is not enabled for selling, please contact the admin`. I tried opening the existing draft product edit route, but it only showed an edit shell and the same selling-disabled warning, with no usable product form.

Outcome:
- Product/merch path found.
- Merch creation and selling are blocked by seller/account enablement.

## 3. Complete an Event Application

Final-strike path:
- https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/events/

Final strike:
- `Submit`
- Safer pause action: `Save & Continue Later`

Think-aloud:
After the Eventin route became unreliable, this page was the clear official application route. It is labelled as the combined Event Application, Risk Assessment, Temporary Stall Application, Liquor Permit Application, and Grant Application form.

The form collects event/risk type, event partners, staff or committee involved, consulted groups, selected event, ticket prices, venue/location, event type, description, risk checkboxes, custom risks, supporting documents, and declaration details. The presence of `Add New Risk`, `Add Document`, `Submit`, and `Save & Continue Later` made the completion path clear.

Outcome:
- Form is reachable.
- Final strike found.
- It likely depends on having a draft event created first.

## 4. Complete annual reaffiliation

Final-strike path:
- https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/affiliation/

Final strike:
- `Submit Application`
- Safer pause action: `Save & Continue Later`

Think-aloud:
This was easy to locate once I understood that official club forms live under `Resources + Forms`, not the profile Workflow submission page. The reaffiliation form is long but logically grouped around identity, governance, membership, documents, committee details, and declaration.

It includes affiliation year/type, acronym, logo/banner choices, club intro, activities, membership types, operating locations, categories, AGM agenda/minutes upload, financial report upload, asset list upload, membership list upload, social links, president details, executive details, committee member rows, declaration, applicant email, and signature.

Outcome:
- Reaffiliation form reachable.
- Required upload fields and final strike found.

## 5. Change logo and front-page photos

Final-strike paths:
- Logo/avatar: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-avatar/
- Cover/banner: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-cover-image/
- Reaffiliation image choices: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/affiliation/

Final strike:
- Logo/avatar: `Select your file`, then crop/save on the next step.
- Cover/banner: `Select your file`, then crop/save on the next step.
- Reaffiliation: `Submit Application` if changing images through annual reaffiliation.

Think-aloud:
I first expected image controls under `Club Admin`, but the actual live-media controls are under `Manage`, which fits the BuddyBoss-style group management pattern. The square logo/avatar and wide cover/banner are separate subtabs.

I stopped at the file picker because selecting a file may immediately begin the live media upload/crop flow. The avatar page recommends 700 x 700 or larger; the cover page recommends 1950 x 450 or larger.

Outcome:
- Logo and cover upload controls found.
- I did not attach a file or change live images.

## 6. Complete a Change of Bank Signatories Form

Final-strike path:
- https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/bank/

Final strike:
- `Submit Request`

Think-aloud:
This was where I expected it: under `Club Admin`, beside membership rules and other governance tools. The page is titled `Request to Change Bank Signatories` and explains that executives use it after an SGM elects new signatories.

The form includes applicant name, email, position, date of change, repeatable new signatory rows via `Add Signatory`, SGM minutes upload, and signature. The SGM upload says accepted file types are pdf, doc, docx, and txt, max 10 MB.

Outcome:
- Form reachable.
- Upload control and final strike found.

## 7. Set up Club Deals

Final-strike paths:
- Add a deal: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/deals/new-deal/
- Edit deals: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/deals/edit/

Final strike:
- Add a deal: `Create a Deal`
- Edit a deal: `Submit`

Think-aloud:
This area was one of the easiest to navigate. The Club Deals tab separates `Current Deals`, `Add a Deal`, and `Edit Deals`, which matched the user goal almost exactly.

The add form asks for deal title, featured image upload, category, public content, and members-only content. Edit Deals lets the admin pick an existing deal, update the title/content/category/image, and optionally delete it.

Outcome:
- Add and edit paths reachable.
- Featured image upload and final strikes found.

## 8. See status of submitted forms and who submitted

Final-strike path:
- https://tusa-dev.its.utas.edu.au/my/workflow-status/

Final strike:
- None. This is a view/details workflow status page.

Think-aloud:
I initially tried `Submit a Workflow Form`, but it showed `No workflow forms`, which was misleading. The actual forms live on the club Resources pages, while profile Workflow is mainly for tracking.

The Workflow Status page is useful because it shows form type, date submitted, submitter, current step, status, and links to detail views. I confirmed existing rows for Event Application/Risk and Club Reaffiliation, including submitter names and pending/approved states.

Observed detail examples:
- Approved Event Application: https://tusa-dev.its.utas.edu.au/my/workflow-status/?page=gravityflow-inbox&view=entry&id=51&lid=5206
- Pending Reaffiliation: https://tusa-dev.its.utas.edu.au/my/workflow-status/?page=gravityflow-inbox&view=entry&id=17&lid=5197

Outcome:
- Status and submitter visibility confirmed.

## 9. Manage memberships, U18/current student/associate rules, and membership list

Final-strike paths:
- Membership rules: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/tags/
- Stats and CSV export: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/csv/
- CSV import: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/import/
- Member list/actions: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/manage-members/
- Membership requests: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/membership-requests/

Final strike:
- Membership rules: `Save membership rules`
- CSV export: `Download Full Member List (CSV)`
- CSV import: import/submit after selecting membership tags and CSV file.
- Member actions: promote, demote, remove, or kick/ban links.

Think-aloud:
I expected this to be under `Manage`, but rules and exports are actually under `Club Admin`. `Manage > Members` is for individual member actions, while `Club Admin > Membership rules and tags` controls the rules/tags side.

The stats page showed 7 total members, 3 current UTAS students, 0 junior members under 18, and no junior members requiring parental consent. CSV Import asks for membership tag selection first, then a CSV with First Name, Last Name/Family Name, Email, and Student Number.

Outcome:
- Rules, stats, export, import, member list, and membership request paths found.
- No role/removal/import action was executed.

## 10. Manage club docs uploads

Final-strike path:
- Expected page: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/club-documents/

Final strike:
- Expected from guide: `Upload Document` or `Add New`, then `Save` or `Submit`.
- Actual live page: no final strike available.

Think-aloud:
This was the clearest mismatch between the guide and the live UI. The club guide says the Club Documents tab should provide a document library for files like RSAs, Food Handling Certificates, Working With Vulnerable People cards, First Aid certificates, insurance, minutes, and governance documents.

The live `Club Docs` page loaded only the header/navigation for this account. I found no document table, no upload button, no file input, no category/expiry fields, and no save/submit action.

Outcome:
- Expected route found.
- Actual document upload UI missing or not rendering for this account.
- This blocks the club document upload goal.

## 11. Submit a grant application or grant reimbursement/claim

Final-strike path:
- https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/grants/

Final strike:
- Grant Application Form: `Submit`
- Grant Claims/reimbursement: `Submit`

Think-aloud:
At first, Grants looked like a guidance page only. Reading the page structure more carefully showed tab-like sections for `How Grants Work`, `Grants Applied For`, `Grant Application Form`, and `Grant Claims`.

The Grant Application form asks which grant is being applied for, applicant/club details, prerequisites, requested amount, supporting information, documents, and acknowledgements. The Grant Claim form is for reimbursement after approval and asks which grant is being claimed, claim details, final budget/summary information, and receipts/invoices.

One important note: the Grant Claim dropdown showed no available approved grant results during testing, which may be correct if there is no approved grant ready to claim.

Outcome:
- Grant application and grant claim paths found.
- Final strikes found.
- Claim readiness may depend on having an approved grant.

## 12. Make sure uploads are working

Final-strike paths and upload controls:
- Bank Signatories: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/bank/
  - Upload: SGM Minutes, `#input_41_8`
  - Final strike: `Submit Request`
- Add Club Deal: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/deals/new-deal/
  - Upload: Deal Featured Image, `#input_14_14`
  - Final strike: `Create a Deal`
- Reaffiliation: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/affiliation/
  - Uploads: logo `#input_17_17`, banner `#input_17_18`, AGM minutes `#input_17_6`, financial report `#input_17_10`, assets `#input_17_65`, membership CSV `#input_17_30`
  - Final strike: `Submit Application`
- Grants: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/resources/grants/
  - Uploads: Grant Application supporting documents, Grant Claim receipts/invoices `#input_25_18`
  - Final strike: `Submit`
- Avatar: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-avatar/
  - Upload: BuddyBoss avatar picker
  - Final strike: `Select your file`, then crop/save
- Cover: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/admin/group-cover-image/
  - Upload: BuddyBoss cover picker
  - Final strike: `Select your file`, then crop/save
- CSV Import: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/rules/import/
  - Upload: hidden CSV dropzone input `#tusa-file-input`
  - Final strike: import/submit after tag and CSV selection
- Club Docs: https://tusa-dev.its.utas.edu.au/clubs/clubs-index/lookwhatwecando-withaform/club-documents/
  - Upload: not found
  - Final strike: not available

Think-aloud:
I could verify that upload controls exist across most forms, and I stopped before any live submission. For avatar and cover, I stopped before selecting a file because that could immediately alter live club media.

The Chrome automation wrapper available in this session does not expose a real file-selection method, so I could not prove server-side upload completion. It also does not expose browser `File`/`DataTransfer` constructors inside page evaluation, so synthetic file attachment was not possible either. That means the correct next manual test is to attach small safe files at each upload point and stop before the final strike buttons listed above.

Outcome:
- Upload controls found for all major forms except Club Docs.
- Actual file attachment/upload completion still needs manual verification.

