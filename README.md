<br>![Responsive Rewrk](readme/testing/am_i_responsive_img.png)

# Rewrk

Rewrk is a digital service provider where customers can come and view each of the services offered by Rewrk, developed for Milestone 4 as part of the Code Institute/UCD - Diploma in Software Development (E-commerce Applications)

There are two types of users, and I have set up accounts for both

An admin(administrator) user account has been set up with username/password of admin/Password1@
A regular(shopper) user account has been set up with username/password of Test13/Password1@

**View the live site [here](https://rewrk-ms4.herokuapp.com/)**
<br><br>
<br>

# Table of Contents
1. [Scope](https://github.com/Aoibhinn/Rewrk_MS4#scope)
   * [User Stories](https://github.com/Aoibhinn/Rewrk_MS4#user-stories)
   * [Wireframes](https://github.com/Aoibhinn/Rewrk_MS4#wireframes)
2. [Features](https://github.com/Aoibhinn/Rewrk_MS4#features)
3. [Database Schema](https://github.com/Aoibhinn/Rewrk_MS4#database-schema)
4. [Technologies Used](https://github.com/Aoibhinn/Rewrk_MS4#technologies-used)
5. [Testing](https://github.com/Aoibhinn/Rewrk_MS4#testing)
    * [Functionality testing](https://github.com/Aoibhinn/Rewrk_MS4#functionality-testing)
    * [Code Validation](https://github.com/Aoibhinn/Rewrk_MS4#code-validation)
    * [Compatibility testing](https://github.com/Aoibhinn/Rewrk_MS4#compatibility-testing)
    * [Performance testing](https://github.com/Aoibhinn/Rewrk_MS4#performance-testing)
    * [User stories testing](https://github.com/Aoibhinn/Rewrk_MS4#user-stories-testing)
6. [Deployment](https://github.com/Aoibhinn/Rewrk_MS4#deployment)
7. [Acknowledgments](https://github.com/Aoibhinn/Rewrk_MS4#acknowledgements)

# Overview

* This project is a website is for submission as milestone project 4 as part of the Code Institute - Diploma in Software * Development (Full stack) course.
* The website is deployed using Heroku pages at the following url: https://rewrk-ms4.herokuapp.com/
* The repository on GitHub that contains the website source code and assets is available at the following url:https://github.com/Aoibhinn/Rewrk_MS4
* The website was built with a responsive look and feel for desktop, tablet and mobile devices.


# Strategy 


# Structure


## Code Structure


#### Models

# Scope
## User Stories

The user stories for the regular user eg: "customer" (a potential or existing customer) are described as follows:

### User Stories feature 2 External Service Booking Form
* User Story 2.1: As a website visitor I would like to book a service with Rewrk without creating an account
* User Story 2.2: As a website visitor I would to be notified if I have not completed the form accurately and in full
* User Story 2.3: As a website visitor I would like to be notified that I have completed the form accurately and in full via a confirmation message
### User Stories feature 3 - Case Studies & Case Study Details
* User Story 3.1: As a website visitor/logged in user I would like to view all published articles from rewrk along with the date, number of comments, and likes each of the received.
* User Story 3.2: As a website visitor/logged in user I would like case studies to be paginated so it does not take the page a long time to load
* User Story 3.3: As a website visitor/logged in user I would like to view the contents of an individual case study along with it's comments, likes, date of publication.
### User Stories feature 4 - Comments & Likes for Case Study Details
* User Story 4.1: As a logged in user I would like to view the number of likes and comments under a case study
* User Story 4.2: As a logged in user I would like to be able to input a comment into the comment text box
* User Story 4.3: As a logged in user I would like to be able to submit my comment under a case study and receive confirmation that it has been successfully submitted
* User Story 4.4: As a logged in user I would like to be able to like a case study
* User Story 4.5: As an admin user I would like to be able to view all comments under case studies
* User Story 4.6: As a logged in user I would like to be able to view individual case study comments and approve comments to be publised
* User Story 4.7: As a logged in user I would like to be able to view my approved comment under a case study
* User Story 4.1: As a unlogged in user I should not be able to submit a comment to a case study
### User Stories feature 5 - My Bookings and Logged in Booking
* User Story 5.1: As a logged in user I would like to be able to view all of my bookings I've currently made with rewrk
* User Story 5.2: As a logged in user I would like to be able to book a service directly from my booking page
* User Story 5.3: As a logged in user I would like to be able to select a date and service I would like to book with rewrk
* User Story 5.4: As a logged in user I would like to receive a confirmation message the service has been successfully booked and view the service I just booked
* User Story 5.5: As a logged in user I would like to to be able to edit a service I have booked
* User Story 5.5: As a logged in user I would like to to be able to delete a service I have booked
### User Stories feature 6 - Services and Service Detail
* User Story 6.1: As a normal/logged in user I want to be able to view all service rewrk has available
* User Story 6.2: As a normal/logged in user I want to be able to view the details and price of an available service
* User Story 6.2: As a normal I want to be able to book a service without having to create an account with rewrk
* User Story 6.4: As a logged in user I want to be able to create a booking from a service and be redirected back to 'my bookings' tab


[Back to Table of Contents](https://github.com/Aoibhinn/Rewrk_MS4#table-of-contents)

## Skeleton
### Wireframes
I used Balsamiq to create the wireframes.
Wireframes were not created for the Service, ServiceDetail, Login  pages as the basic design is similar to other form styled pages.



## Surface
### Color Palette
The main colors used in this project:
* Font and Accent color: #4C6FBF blue
* Background color: Black #003060; navy

### Typography
Sans-Serif is used as the main font. I did not feel it necessary to change the default font type as Sans-Serif is an easy font to read and displays well throughout the site.

### Images
Images were sourced from canva.com

[Back to Table of Contents](https://github.com/Aoibhinn/Rewrk_MS4#table-of-contents)

# Features
## Existing Features
### Navigation Bar
   * Featured on all pages is a fully responsive navigation bar that has links to all pages (Home, All Services, Book Service and My Bookings).
   * If the user is not logged in then there are two additional links available available (Register and Login).
   * If the user is logged in then the Register, Login links no longer display. The user can now Logout or view their bookings.
   * A confirmation message displays when the user logs in.
<img src="media/images/logged_in.png">
<img src="media/images/logged_out.png">

### Footer
   * Featured on all pages is a fully responsive footer that has links to all pages (All Services, Book Service, Case studies and Profile).
   * If the user is logged in then a link to their profile will be available.
<img src="media/images/Screenshot 2021-11-29 at 23.18.32.png">
<img src="media/images/Screenshot 2021-11-29 at 23.18.24.png">

### Available Service section
   * On the home page the available services and an excerpt is displayed.
   * If the user clicks on a specific service they can view the full description of the service information. At the bottom of the service detail page is a link to the service booking page.
<img src="media/images/all_services_ui.png">
<img src="media/images/service_detail_ui.png">
  
### Booking form
* This page invites the user to submit their interest in booking a specific service.
* On submission of the form the user is provided with a confirmation message.
<img src="media/images/Screenshot 2021-11-29 at 23.22.46.png">

### Case Studies
* This page show cases previous project Rewrk have worked on and the customer success stories.
* A user can select individual case studies to read about projects.
<img src="media/images/case_study_view.png">

## Future features
* A Calendar on the create booking page for logged in users which shows which days are booked and which are available for booking.
* Cancel and edit bookings from profile
* Payment method 

# Database Schema
### User Profile model
* Django's user and admin model was utilised.

### Service App
<img src="media/images/service_model.png">

### Case Study App
<img src="media/images/case_study_app.png">

### Customer app for viewing booked services
<img src="media/images/customer_booking_app.png">

# Technologies Used:
### Programming Languages:
* CSS, HTML, Python, and Django.
### Database framework
* Postgres.
### Git
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
### Github
* GitHub was used to store the projects code after being pushed from Git.
### Bootstrap 5
* Bootstrap was used to for design and to make the website responsive.
### Balsamiq
* Balsamiq was used to create the wireframes during the design process.

[Back to Table of Contents](https://github.com/Aoibhinn/Rewrk_MS4#table-of-contents)

# Testing
## Functionality Testing
### Manual testing
* I used Google Chrome developer tools throughout the development process for testing and solving problems with style and display issues.
* I used Github Project and Issues to track tasks. After each task completion, I would fully test it before moving on to the next task.
* All links were tested multiple times during the development process and again once the project was completed to ensure that all pages were linked correctly.
* All Forms and form elements were tested to ensure that they work as they should, with user feedback on errors as well as user feedback on successful submission.


## Code Validation
**1. CSS Validation using <a href="https://jigsaw.w3.org/css-validator/#validate_by_input" target="_blank" rel="noopener">W3C CSS Validator Services</a>.**

No errors were found in the style.css
<img src="media/images/Screenshot 2021-11-28 at 11.38.40.png">


**2. <a href="http://pep8online.com/">PEP8</a> was used to test the Python code**

All Python files were tested with PEP8, with no errors found.
There were some pylint errors in gitpod regarding missing docstrings, these errors were fixed during development.


## Compatibility Testing
* The website was tested on Google Chrome, and apple cellphones.
* The website was viewed on a variety of device sizes such as Desktop, Iphone11, I also used the responsive function when inspecting the pages to view various sizes. 

[Back to Table of Contents](https://github.com/Aoibhinn/Rewrk_MS4#table-of-contents)

## User Stories testing
### As a customer/potential customer
1. I want to find information about the various services.
    * Users can do this on the home page, if they want more detailed information they can click on the service they are interested in and find more information.

    <img src="media/images/all_services_ui.png">
    <img src="media/images/service_detail_ui.png">

2. I want to read about past projects Rewrk have worked with.
    * Users can read about past projects to learn more about was Rewrk has successfully achieved for their past clients.
    <img src="media/images/case_study_view.png">
    <img src="media/images/case_study_detail.png">

3. I want to book one of Rewkrs services
    * Users can leave their details via Rewkrs service booking form for a member of the team to get back to them.
    <img src="media/images/book_service.png">

4. I want to register on the website
    * Users can register using the register link.
    <img src="media/images/register.png">

5. I was to view the services I have booked with Rewrk
    * Users can register an account on Rewrk and an admin member can add bookings to their profiles
    <img src="media/images/Screenshot 2021-11-29 at 23.28.45.png">


### As an Admin user:

1. I would like to be able to add draft services so that I can finish writing the content later.
    * The website owner can add a draft service which will not be published to the site until the status is changed to published.
    <img src="media/images/draft.png">

2. I would like to manage Rewrks case studies 
    * The admin panel allows the website owner to amend and update case studies.
    <img src="media/images/case_study.png">

3. I want to be able to add booked services to customer accounts
    * The admin panel allows admin users to add bookings to customer registered accounts
    <img src="media/images/Screenshot 2021-11-29 at 23.30.29.png">

[Back to Table of Contents](https://github.com/Aoibhinn/Rewrk_MS4#table-of-contents)


# Deployment
The project was deployed to GitHub Pages using the following steps, I used Gitpod as a development environment where I commited all changes to git version control system. I used the push command in Gitpod to save changes into GitHub.

### Deployment to Heroku
Before creating a Heroku app make sure your project has these two files:

* requirements.txt - You can create one by using <code>pip3 freeze --local > requirements.txt</code>
* Procfile - You can create one by using echo web: <code>python run.py > Procfile</code>

### Create application:

1. Navigate to Heroku's site <a href="https://id.heroku.com/login" target="_blank" rel="noopener">here</a>. (Note: Right click on link to open a new tab).
2. Register and/or Login as applicable.
3. Click on the new button in the top right and select "Create new app".
4. Enter the app name and region closest to you.
5. Click the create app button.

### Set environment variables:

1. Click on the settings tab and then click "Reveal config vars".
2. Config variables added throughout project:
(add image of variables)

### Setting up database in deployment

1. Temporarily add the <code>DATABASE_URL</code> to <code>settings.py</code>:

    <code>DATABASES = {
'default': dj_database_url.parse('your_postgres_database_url')
}</code>

2. Migrate the data from development to production version.

    * To migrate the database models in the project to the Postgres database you can use the following command:

    <code>python3 manage.py migrate</code>

3. You will then need a superuser for the Postgres database too. To create one you can use the following command:

    <code>python3 manage.py createsuperuser</code>

4. Remove the Postgres database URL from settings.py as this should not in any case be deployed to GitHub for security reasons.

5. To connect your Heroku app to be deployed from a Github repository, you can follow these steps:

    * Open the heroku app page on the deploy tab and select GitHub - Connect to GitHub.
    * Sign into GitHub if not already.
    * A prompt to find a Github repository to connect to will then be displayed.
    * Enter the repository name for the project and click search.
    * Once the repository has been found, click the connect button.

6. Once you have your GitHub repository connected, without leaving deploy tab:

    * Under Automatic deploys section, choose the branch you want to deploy from and then click the "Enable Automatic Deploys" button.
    * To deploy your app to Heroku click the "Deploy Branch" button.

[Back to Table of Contents](https://github.com/Aoibhinn/Rewrk_MS4#table-of-contents)

## Acknowledgements
* My mentor for support, advice and feedback.
* The students on Slack for peer review and comments.
* Code Institute Tutor support for help with coding issues.
* My family and friends for their support, feedback and testing.

[Back to Table of Contents](https://github.com/Aoibhinn/Rewrk_MS4#table-of-contents)


