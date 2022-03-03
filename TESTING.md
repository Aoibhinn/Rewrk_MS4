# Table of Contents
- [Testing](#testing)
  * [Manual testing information](#manual-testing-information)
    + [Feature 1 Navigation Menu and Homepage](#feature-1-navigation-menu-and-homepage)
      - [User Stories feature 1](#user-stories-feature-1)
      - [User Stories Steps 1](#user-stories-steps-1)
      - [User Story Testing Results 1](#user-story-testing-results-1)
    + [Feature 2 External Service Booking Form](#feature-2-external-service-booking-form)
      - [User Stories feature 2](#user-stories-feature-2)
      - [User Stories Steps 2](#user-stories-steps-2)
      - [User Story Testing Results 2](#user-story-testing-results-2)
    + [Feature 3 Case Studies & Case Study Details](#feature-3-case-studies-&-case-study-details)
      - [User Stories feature 3](#user-stories-feature-3)
      - [User Stories Steps 3](#user-stories-steps-3)
      - [User Story Testing Results 3](#user-story-testing-results-3)
    + [Feature 4 Comments & Likes for Case Study Details](#feature-4-comments-&-likes-for-case-study-details)
      - [User Stories feature 4](#user-stories-feature-4)
      - [User Stories Steps 4](#user-stories-steps-4)
      - [User Story Testing Results 4](#user-story-testing-results-4)
    + [Feature 5 My Bookings and Logged in Booking](#feature-5-my-bookings-and-logged-in-booking)
      - [User Stories feature 5](#user-stories-feature-5)
      - [User Stories Steps 5](#user-stories-steps-5)
      - [User Story Testing Results 5](#user-story-testing-results-5)
    + [Feature 6 Services and Service Detail](#feature-6-services-and-service-detail)
      - [User Stories feature 5](#user-stories-feature-5)
      - [User Stories Steps 5](#user-stories-steps-5)
      - [User Story Testing Results 5](#user-story-testing-results-5)

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

### User Stories feature 2
* User Story 2.1: As a website visitor I would like to book a service with Rewrk without creating an account
* User Story 2.2: As a website visitor I would to be notified if I have not completed the form accurately and in full
* User Story 2.3: As a website visitor I would like to be notified that I have completed the form accurately and in full via a confirmation message

#### User Stories Steps 2
1. Navigate to https://rewrk-ms4.herokuapp.com/service_booking/booking/
2. Complete fields but leave telephone blank
3. Complete fields but leave try to input a 'letter' instead of a number
4. Complete all fields
5. Click Submit

#### User Story Testing Results 2
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The external service booking form is displayed | [Desktop](readme/testing/external_booking_form_desktop.png)  | [Tablet](readme/testing/external_booking_form_tablet.png)  | [Mobile](readme/testing/external_booking_form_mobile.png)  |Passed |
Step 2 | A notification appears asking user to 'Fill in this field' | [Desktop](readme/testing/external_booking_form_unfilled_fields_desktop.png)  | [Tablet](readme/testing/external_booking_form_unfilled_fields_tablet.png)  | [Mobile](readme/testing/external_booking_form_unfilled_fields_mobile.png)  | Passed  |
Step 3 | The user is able to complete all fields with their details | [Desktop](readme/testing/external_booking_form_filled_fields_desktop.png)  | [Tablet](readme/testing/external_booking_form_filled_fields_tablet.png)  | [Mobile](readme/testing/external_booking_form_filled_fields_mobile.png)  | Passed |
Step 4 | A success message appears confirming 'A member of our team will be in touch with you shortly! | [Desktop](readme/testing/external_booking_form_success_message_desktop.png)  | [Tablet](readme/testing/external_booking_form_success_message_tablet.png)  | [Mobile](readme/testing/external_booking_form_success_message_mobile.png)  | Passed |

### Feature 3 Case Studies & Case Study Details

### User Stories feature 3
* User Story 3.1: As a website visitor/logged in user I would like to view all published articles from rewrk along with the date, number of comments, and likes each of the received.
* User Story 3.2: As a website visitor/logged in user I would like case studies to be paginated so it does not take the page a long time to load
* User Story 3.3: As a website visitor/logged in user I would like to view the contents of an individual case study along with it's comments, likes, date of publication.

#### User Stories Steps 3
1. Navigate to https://rewrk-ms4.herokuapp.com/case_study/
2. Scroll down the case study page
3. Select first case study 

#### User Story Testing Results 3
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The case study page is displayed with header text and published case studies | [Desktop](readme/testing/case_study_desktop.png)  | [Tablet](readme/testing/case_study_tablet.png)  | [Mobile](readme/testing/case_study_mobile.png)  | Passed |
Step 2 | The case study page is pagniated and will display a next button when posts exceeds 6 | [Desktop](readme/testing/paginate_case_study_desktop.png)  | [Tablet](readme/testing/paginate_case_study_tablet.png)  | [Mobile](readme/testing/paginate_case_study_mobile.png)  | Passed |
Step 3 | User is redirected to case study detail page to view title, time, author, content, comments, postcomment and like functionality | [Desktop](readme/testing/case_study_detail_desktop.png)  | [Tablet](readme/testing/case_study_detail_tablet.png)  | [Mobile](readme/testing/case_study_detail_mobile.png)  | Passed |

### Feature 4 Comments & Likes for Case Study Details

### User Stories feature 4
* User Story 4.1: As a logged in user I would like to view the number of likes and comments under a case study
* User Story 4.2: As a logged in user I would like to be able to input a comment into the comment text box
* User Story 4.3: As a logged in user I would like to be able to submit my comment under a case study and receive confirmation that it has been successfully submitted
* User Story 4.4: As a logged in user I would like to be able to like a case study
* User Story 4.5: As an admin user I would like to be able to view all comments under case studies
* User Story 4.6: As a logged in user I would like to be able to view individual case study comments and approve comments to be publised
* User Story 4.7: As a logged in user I would like to be able to view my approved comment under a case study
* User Story 4.1: As a unlogged in user I should not be able to submit a comment to a case study

#### User Stories Steps 4
1. Navigate to https://rewrk-ms4.herokuapp.com/national-trust/ and as a logged in user scroll down the case study detail pag to view comments and likes
2. Input text into 'Leave Comment Field'
3. Select the 'submit' button
4. Select the 'like' button under case study
5. As an admin neviagte to https://rewrk-ms4.herokuapp.com/admin/case_study/comment/
6. As an admin select test comment
7. Navigate to https://rewrk-ms4.herokuapp.com/national-trust/
8. Log out and navigate to https://rewrk-ms4.herokuapp.com/national-trust/

#### User Story Testing Results 4
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

### User Stories feature 5
* User Story 5.1: As a logged in user I would like to be able to view all of my bookings I've currently made with rewrk
* User Story 5.2: As a logged in user I would like to be able to book a service directly from my booking page
* User Story 5.3: As a logged in user I would like to be able to select a date and service I would like to book with rewrk
* User Story 5.4: As a logged in user I would like to receive a confirmation message the service has been successfully booked and view the service I just booked
* User Story 5.5: As a logged in user I would like to to be able to edit a service I have booked
* User Story 5.5: As a logged in user I would like to to be able to delete a service I have booked


#### User Stories Steps 5
1. As a logged in user navigate to https://rewrk-ms4.herokuapp.com/customer/ no bookings
2. Select 'Click here to book a new service'
3. Select a 'Booking Date' and 'Service'
4. Select 'submit'
5. Select 'edit'
6. From the calender dropdown chose a new date and select 'Update'
7. Select 'delete'
8. Select 'delete booking'

#### User Story Testing Results 5
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

### Feature 6 Services and Service Detail

### User Stories feature 6
* User Story 6.1: As a normal/logged in user I want to be able to view all service rewrk has available
* User Story 6.2: As a normal/logged in user I want to be able to view the details and price of an available service
* User Story 6.2: As a normal I want to be able to book a service without having to create an account with rewrk
* User Story 6.4: As a logged in user I want to be able to create a booking from a service and be redirected back to 'my bookings' tab

#### User Stories Steps 6
1. As a not logged in user navigate to https://rewrk-ms4.herokuapp.com and scroll down to 'Our Services'
2. As a not logged in user select the first service 'learn more' button
3. As a not logged in user select 'book now'
4. As a logged in user go to https://rewrk-ms4.herokuapp.com/marketing-workshops and click 'book now'

#### User Story Testing Results 6
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | User is presented with all available services | [Desktop](readme/testing/my_bookings_desktop.png)  | [Tablet](readme/testing/my_bookings_tablet.png)  | [Mobile](readme/testing/my_bookings_mobile.png)  | Passed |
Step 2 | User is presented with the details of the service including the price | [Desktop](readme/testing/service_detail_desktop.png)  | [Tablet](readme/testing/service_detail_tablet.png)  | [Mobile](readme/testing/service_detail_mobile.png)  | Passed |
Step 3 | User is redirected to the external service booking form | [Desktop](readme/testing/external_booking_form_desktop.png)  | [Tablet](readme/testing/external_booking_form_tablet.png)  | [Mobile](readme/testing/external_booking_form_mobile.png)  | Passed |
Step 4 | As a logged in user you are redirected to the 'create booking' form for logged in users | [Desktop](readme/testing/create_booking_desktop.png)  | [Tablet](readme/testing/create_booking_tablet.png)  | [Mobile](readme/testing/create_booking_mobile.png)  | Passed |



## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
templates/services.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_index.png) 
templates/service.html | 0 errors and 0 contrast errors| [Results](#)  
templates/edit_booking.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_edit_booking.png)
templates/delete_booking.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_delete_booking.png)
templates/create_booking.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_create_booking.png)  
templates/case_study.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_case_study.png) 
templates/booking.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_service_booking.png)     
templates/booked_services.html | 0 errors and 0 contrast errors| [Results](#)  
templates/account/login.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_login.png)
templates/account/signup.html | 0 errors and 0 contrast errors| [Results](readme/validation/w3_validation_signup.png) 
<br>

## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
static/style.css | Passed, No errors found | [Results](readme/validation/style_css_validated.png) 

