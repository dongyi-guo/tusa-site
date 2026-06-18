# New TUSA Site Workplace
This repository is for all my work on the new TUSA site, it includes the:

* Documentation overhaul from Sarah's previous work, including two set of guide files:
  * The Club Admin Guide
  * The Student Help Centre

* Blackbox Testing about the Club & Society Segments, this includes:
  * Checklists of tested items
  * Issue list(s)

## Documentation Overhaul

This section contains two folders: `club-admin-guide/` and `student-help-centre` .

For `club-admin-guide/` :

```
club-admin-guide/
├───1-getting-started
│       1-stripe-&-payments.md
│
├───2-starting-a-new-club
│       1-starting-a-new-club.md
│
├───3-your-club-store
│       1-adding-products-to-your-club-store.md
│       2-creating-membership-products.md
│       3-setting-up-shipping-for-your-store.md
│       4-managing-membership-rules-and-tags.md
│       5-managing-orders.md
│
├───4-events-&-activities
│       1-checking-in-event-attendees.md
│       2-creating-events.md
│       3-hiring-equipment-from-TUSA.md
│       4-submitting-event-applications.md
│
├───5-funding
│       1-applying-for-TUSA-grants.md
│
├───6-general
│       1-reporting-an-issue.md
│
├───7-managing-your-club
│       1-annual-club-reaffiliation.md
│       2-managing-club-members.md
│       3-managing-store-staff.md
│       4-uploading-and-managing-club-documents.md
│
└───8-understanding-your-club
        1-finding-your-way-around-profile-and-group-navigation.md
        2-understanding-club-identity-the-keystone-account-model.md
```

For `student-help-centre/` :

```
student-help-centre/
├───1-clubs-&societies
│       1-joining-clubs.md
│       2-starting-a-new-club.md
│
├───2-events
│       1-finding-and-attending-events.md
│       2-compliance-forms-for-event-attendees.md
│
└───3-volunteering
        1-food-hub-volunteering.md
```

Where the numbers for both tree structure identifies their order inside the list.

## Issue List for C&S Part

The Blackbox Testing of the Club & Society segment of the New TUSA Website should expose all functionalities that clubs expected to use our CRM for. This includes:

- [x] List an event to sell tickets.
  - [ ] Currently at Eventin an event cannot be published.
- [x] Create and sell their own merch.
  - [ ] The merch can be potentially sold, but no add-product button.
- [x] Complete an Event Application (to tell TUSA that they are running an event and acknowledge what risks are involved).
  - [x] Can be done without issues.
- [x] To complete a reaffiliation form annually.
  - [x] Can be done without issues.
- [x] Part of this is to change their logo and photos displayed at the front page of their club.
- [x] To complete a Change of Bank Signatories Form (to notify TUSA that the banks signatories are changing).
- [x] To set up Club Deals (i.e. what does club have to offer to entice students to join).
  - [ ] Adding a featuring photo to a deal seemingly not working
- [ ] See the status of their forms (once sent in + see who submitted).
  - [ ] Broken rn.
- [ ] Manage their memberships (rules for U18s, Current Students and Associates) + membership list.
- [x] Manage their club docs uploads (i.e. RSAs, Food Handling Certificates, Working With Vulnerable People Card uploads, First Aid Certs, etc.).
  - [x] The documentation has been tested without any issue.
- [ ] Submit a grant application form to claim reimbursement for expenses at an event or capital.
- [x] Make all required uploads.

