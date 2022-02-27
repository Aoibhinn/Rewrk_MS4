# Table of Contents
- [Testing](#testing)
  * [Manual testing information](#manual-testing-information)
    + [Feature 1 Navigation Menu and Homepage](#feature-1-navigation-menu-and-homepage)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)

     

## Manual testing information
Testing was completed on the following browsers and device types

Device Number | Physical/Emulator | Device Name | Device Type | Browser | Version
------------ | ------------ | ------------- | ------------- | ------------- | -------------
1 | Emulator | iPadMini | Tablet | Chrome Emulator | 94.0 |
2 | Emulator | iPhone X | Mobile | Chrome Emulator | 94.0 |
3 | Emulator | iPhone 5/SE | Mobile | Chrome Emulator | 94.0 |

- Below are the test results for testing the website requirements against a range of browsers and devices
- For the purpose of the screenshots I used a Chrome emulator for desktop, tablet and mobile


### Feature 1 Navigation Menu and Homepage
#### User Stories Steps 1
1. Navigate to https://rewrk-ms4.herokuapp.com/, and click on the My Account link as a regular user
2. Login to the website with a valid username and password
4. Navigate to the "All Services"
4. Navigate to the "Book Service"
5. Navigate to the "Case Studies"
6. Navigate to the "My Bookings"
7. Click the Logout button at the top right of the site

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The homepage is displayed, Login and Register links in the top right of the site | [Desktop](readme/testing/home_logged_out_desktop.png)  | [Tablet](readme/testing/home_logged_out_tablet.png)  | [Mobile](readme/testing/home_logged_out_mobile.png)  | Passed  |
Step 2 | The homepage is displayed with a header logo(desktop), All Services, Book Services, Case Studies, My Bookings and logout. | [Desktop](readme/testing/home_logged_in_desktop.png) | [Tablet](readme/testing/home_logged_in_tablet.png)  | [Mobile](readme/testing/home_logged_in_mobile.png) | Passed  |
Step 3 | All Services includes Header Image, Info About Rewrk, and Available Services. | [Desktop](readme/testing/all_services_desktop.png) | [Tablet](readme/testing/all_services_tablet.png)  | [Mobile](readme/testing/all_services_mobile.png)  | Passed  |
Step 4 | Book Service inlcudes input fields on form | [Desktop](#)  | [Tablet](#) | [Mobile](#)  |  |
Step 5 | Case Study inlcudes recent case studies posted by Rewrk Admin | [Desktop](#)  | [Tablet](#)  | [Mobile](#) |  |
Step 6 | My Bookings inlcudes table with services booked by customer | [Desktop](#) | [Tablet](#)  | [Mobile](#) |  |
Step 7 | The user is logged out | [Desktop](#)  | [Tablet](#)  | [Mobile](#) | Passed |


