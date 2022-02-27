# Table of Contents
- [Testing](#testing)
  * [Manual testing information](#manual-testing-information)
    + [Feature 1 Navigation Menu and Homepage](#feature-1-navigation-menu-and-homepage)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)
    + [Feature 2 External Service Booking Form](#feature-2-external-service-booking-form)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)
    + [Feature 3 Case Studies & Case Study Details](#feature-3-case-studies-&-case-study-details)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)
    + [Feature 4 Comments & Likes for Case Study Details](#feature-4-comments-&-likes-for-case-study-details)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)
    + [Feature 5 My Bookings and Logged in Booking](#feature-5-my-bookings-and-logged-in-booking)
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
Step 4 | External Book Service inlcudes input fields on form | [Desktop](readme/testing/external_booking_form_desktop.png)  | [Tablet](readme/testing/external_booking_form_tablet.png) | [Mobile](readme/testing/external_booking_form_mobile.png)  | Passed |
Step 5 | Case Study inlcudes recent case studies posted by Rewrk Admin | [Desktop](readme/testing/case_studies_desktop.png)  | [Tablet](readme/testing/case_studies_tablet.png)  | [Mobile](readme/testing/case_studies_mobile.png) | Passed |
Step 6 | My Bookings inlcudes table with services booked by customer | [Desktop](readme/testing/booked_services_desktop.png) | [Tablet](readme/testing/booked_services_tablet.png)  | [Mobile](readme/testing/booked_services_mobile.png) | Passed |
Step 7 | The user is logged out | [Desktop](readme/testing/logout_desktop.png)  | [Tablet](readme/testing/logout_tablet.png)  | [Mobile](readme/testing/logout_mobile.png) | Passed |


### Feature 2 External Service Booking Form
#### User Stories Steps 1
1. Navigate to https://rewrk-ms4.herokuapp.com/service_booking/booking/
2. Complete fields but leave telephone blank
3. Complete fields but leave try to input a 'letter' instead of a number
4. Complete all fields
5. Click Submit


#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The external service booking form is displayed | [Desktop](readme/testing/external_booking_form_desktop.png)  | [Tablet](readme/testing/external_booking_form_tablet.png)  | [Mobile](readme/testing/external_booking_form_mobile.png)  |Passed |
Step 2 | A notification appears asking user to 'Fill in this field' | [Desktop](readme/testing/external_booking_form_unfilled_fields_desktop.png)  | [Tablet](readme/testing/external_booking_form_unfilled_fields_tablet.png)  | [Mobile](readme/testing/external_booking_form_unfilled_fields_mobile.png)  | Passed  |
Step 3 | The user is able to complete all fields with their details | [Desktop](readme/testing/external_booking_form_filled_fields_desktop.png)  | [Tablet](readme/testing/external_booking_form_filled_fields_tablet.png)  | [Mobile](readme/testing/external_booking_form_filled_fields_mobile.png)  | Passed |
Step 4 | A success message appears confirming 'A member of our team will be in touch with you shortly! | [Desktop](readme/testing/external_booking_form_success_message_desktop.png)  | [Tablet](readme/testing/external_booking_form_success_message_tablet.png)  | [Mobile](readme/testing/external_booking_form_success_message_mobile.png)  | Passed |

### Feature 3 Case Studies & Case Study Details
#### User Stories Steps 1
1. Navigate to https://rewrk-ms4.herokuapp.com/case_study/
2. Scroll down the case study page
3. Select first case study 

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The case study page is displayed with header text and published case studies | [Desktop](readme/testing/case_study_desktop.png)  | [Tablet](readme/testing/case_study_tablet.png)  | [Mobile](readme/testing/case_study_mobile.png)  | Passed |
Step 2 | The case study page is pagniated and will display a next button when posts exceeds 6 | [Desktop](readme/testing/paginate_case_study_desktop.png)  | [Tablet](readme/testing/paginate_case_study_tablet.png)  | [Mobile](readme/testing/paginate_case_study_mobile.png)  | Passed |
Step 3 | User is redirected to case study detail page to view title, time, author, content, comments, postcomment and like functionality | [Desktop](readme/testing/case_study_detail_desktop.png)  | [Tablet](readme/testing/case_study_detail_tablet.png)  | [Mobile](readme/testing/case_study_detail_mobile.png)  | Passed |

### Feature 4 Comments & Likes for Case Study Details
#### User Stories Steps 1
1. Navigate to https://rewrk-ms4.herokuapp.com/case_study/national-trust/ and as a logged in user scroll down the case study detail pag to view comments and likes
2. Input text into 'Leave Comment Field'
3. Select the 'submit' button
4. Select the 'like' button under case study
5. As an admin neviagte to https://rewrk-ms4.herokuapp.com/admin/case_study/comment/
6. As an admin select test comment
7. Navigate to https://rewrk-ms4.herokuapp.com/case_study/national-trust/
8. Log out and navigate to https://rewrk-ms4.herokuapp.com/case_study/national-trust/ 

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The user is able to view comments, like and leave a comment under the case study | [Desktop](readme/testing/comments_likes_desktop.png)  | [Tablet](readme/testing/comments_likes_tablet.png)  | [Mobile](readme/testing/comments_likes_mobile.png)  | Passed |
Step 2 | The user is able to input a comment in the 'Leave a Comment' form | [Desktop](readme/testing/input_comment_desktop.png)  | [Tablet](readme/testing/input_comment_tablet.png)  | [Mobile](readme/testing/input_comment_mobile.png)  | Passed |
Step 3 | A success message is displayed notifying the user their comment is awaiting approval | [Desktop](readme/testing/comment_awaiting_approval_desktop.png)  | [Tablet](readme/testing/comments_likes_tablet.png)  | [Mobile](readme/testing/comments_likes_mobile.png)  | Passed |
Step 4 | The heart icon is filled and the counter is changed to 1 | [Desktop](readme/testing/like_case_study_desktop.png)  | [Tablet](readme/testing/like_case_study_tablet.png)  | [Mobile](readme/testing/like_case_study_mobile.png)  | Passed |
Step 5 | Admin can view comments | [Desktop](readme/testing/admin_comments.png) |   |   | Passed |
Step 6 | User is able to view approved comment | [Desktop](readme/testing/approved_comment_desktop.png)  | [Tablet](readme/testing/approved_comment_tablet.png)  | [Mobile](readme/testing/approved_comment_mobile.png)  | Passed |
Step 7 | 'Leave a Comment' form is not available for logged out users  | [Desktop](readme/testing/logged_out_comment_form_desktop.png)  | [Tablet](readme/testing/logged_out_comment_form_tablet.png)  | [Mobile](readme/testing/logged_out_comment_form_mobile.png)  | Passed |


### Feature 5 My Bookings and Logged in Booking
#### User Stories Steps 1
1. As a logged in user navigate to https://rewrk-ms4.herokuapp.com/customer/ no bookings
2. Select 'Click here to book a new service'
3. Select a 'Booking Date' and 'Service'
4. Select 'submit'
5. Select 'edit'
6. From the calender dropdown chose a new date and select 'Update'
7. Select 'delete'
8. Select 'delete booking'


#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | User is presented with booking table and message notifying them they have no bookings | [Desktop](readme/testing/my_bookings_desktop.png)  | [Tablet](readme/testing/my_bookings_tablet.png)  | [Mobile](readme/testing/my_bookings_mobile.png)  | Passed |
Step 2 | User is redirected to a create booking page | [Desktop](readme/testing/create_booking_desktop.png)  | [Tablet](readme/testing/my_bookings_tablet.png)  | [Mobile](readme/testing/my_bookings_mobile.png)  | Passed |
Step 3 | User can select date and service from the date and dropdown box | [Desktop](readme/testing/complete_create_booking_desktop.png)  | [Tablet](readme/testing/complete_create_booking_tablet.png)  | [Mobile](readme/testing/complete_create_booking_mobile.png)  | Passed |
Step 4 | The selected service and date are displayed in the table along with a success message | [Desktop](readme/testing/success_booked_service_desktop.png)  | [Tablet](readme/testing/success_booked_service_tablet.png)  | [Mobile](readme/testing/success_booked_service_mobile.png)  | Passed |
Step 5 | User is redirected to the 'edit booking' page | [Desktop](readme/testing/edit_booking_desktop.png)  | [Tablet](readme/testing/edit_booking_tablet.png)  | [Mobile](readme/testing/edit_booking_mobile.png)  | Passed |
Step 6 | Updated booking with new date is displayed | [Desktop](readme/testing/successfully_updated_desktop.png)  | [Tablet](readme/testing/successfully_updated_tablet.png)  | [Mobile](readme/testing/successfully_updated_mobile.png)  | Passed |
Step 7 | User is redirected to delete booking page with confirmation message | [Desktop](readme/testing/delete_booking_desktop.png)  | [Tablet](readme/testing/delete_booking_tablet.png)  | [Mobile](readme/testing/delete_booking_mobile.png)  | Passed |
Step 8 | User is redirected back to booked services and services is deleted | [Desktop](readme/testing/deleted_booking_desktop.png)  | [Tablet](readme/testing/deleted_booking_tablet.png)  | [Mobile](readme/testing/deleted_booking_mobile.png)  | Passed |


## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
templates/services.html | 0 errors and 0 contrast errors| [Results](#) 
templates/service.html | 0 errors and 0 contrast errors| [Results](#)  
templates/post_detail.html | 0 errors and 0 contrast errors| [Results](#)  
templates/edit_booking.html | 0 errors and 0 contrast errors| [Results](#)
templates/delete_booking.html | 0 errors and 0 contrast errors| [Results](#)
templates/create_booking.html | 0 errors and 0 contrast errors| [Results](#)  
templates/case_study.html | 0 errors and 0 contrast errors| [Results](#) 
templates/booking.html | 0 errors and 0 contrast errors| [Results](#)     
templates/booked_services.html | 0 errors and 0 contrast errors| [Results](#)  
templates/base.html | 0 errors and 0 contrast errors| [Results](#)  
templates/account/login.html | 0 errors and 0 contrast errors| [Results](#)
templates/account/logout.html | 0 errors and 0 contrast errors| [Results](#)
templates/account/signup.html | 0 errors and 0 contrast errors| [Results](#) 
<br>


