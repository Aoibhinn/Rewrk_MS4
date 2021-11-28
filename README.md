# Rewrk

## Project 4 - Full Stack Toolkit
<img src="/workspace/Rewrk_MS4/media/images/home.png">

# Overview

Rewrk is a digital service provider where customers can come and view each of the services offered by Rewrk. Customers are able to read case studies about businesses who have utilised Rewrk’s services to ensure they are a credible provider. 

Site administrators have the ability to add, remove or update services and case studies to ensure the most up to date content is being presented to customers. Customers are able to create an account with Rewrk to view booked services and become part of a Rewrk community. 

This combined with an intuitive interface aims to deliver a smooth and enjoyable customer experience to maximise repeat visits to the site

The live site can be found <a href="https://rewrk-ms4.herokuapp.com/" target="_blank" rel="noopener">here</a>. (Note: Right click on link to open a new tab).

# Strategy 

During the pandemic a lot of local businesses were forced to close their doors for months. Prior to this many businesses did not have e-commerce websites or even social media accounts and when they were forced to close they were unable to reach any of their customers. 

Rewkrs aim is to provide these businesses with access to digital services at reasonable prices. Many web development companies charge high prices that can be out of reach to local, small businesses. Rewkrs aim is not only to create a digital presence for the business but also to educate business owners on how to continue to grow their business online long after working with Rewrk by creating a community that receives monthly emails from Rewrk. 

# Table of Contents


# UX
## Website owner business goals
* I want my visitors to be able to navigate my website intuitively and easily.
* I would like the website to be interesting for visitors.
* I would like to build and maintain relationships with potential and current visitors.
* I would like to manage the information about the various services.
* I would like to be able to add draft services so that I can finish writing the content later.
* I would like to manage customer case studies about past projects we have worked on
* I would like to be able to add draft case studies so that I can finish writing the content later.

## User Stories
### New user goals:
* I want to find information about the various services.
* I want to read information about past projects.
* I want to register on the website.
### Returning user goals:
* I would like to view the available services.
* I would like to be able to book a services.
* I would like to view the services I have registered for.
* I would like to be able to edit and delete services I have registered for.

[Back to Table of Contents]

## Wireframes
I used Balsamiq to create the wireframes.
Wireframes were not created for the Service, ServiceDetail, Login  pages as the basic design is similar to other form styled pages.

* Home page 
<img src="/workspace/Rewrk_MS4/media/images/All Services:Home.png" >

* service detail
<img src="/workspace/Rewrk_MS4/media/images/service_detail.png" >

* service booking
<img src="/workspace/Rewrk_MS4/media/images/service_booking.png" >

* login
<img src="/workspace/Rewrk_MS4/media/images/login.png" >

* create account
<img src="/workspace/Rewrk_MS4/media/images/create_an_account.png">

* Home page mobile view
<img src="/workspace/Rewrk_MS4/media/images/All_services_mobile.png">



[Back to Table of Contents]

## Design
### Colors
The main colors used in this project:
* Background color: #4C6FBF blue
* Font color: Black #003060; navy

### Fonts
Sans-Serif is used as the main font. I did not feel it necessary to change the default font type as Sans-Serif is an easy font to read and displays well throughout the site.

### Images
Images were sourced from canva.com


# Features
## Existing Features
### Navigation Bar
   * Featured on all pages is a fully responsive navigation bar that has links to all pages (Home, All Services, Book Service and Profile).
   * If the user is not logged in then there are three additional links available available (Register and Login).
   * If the user is logged in then the Register, Login links no longer display. The user can now Logout or view their Profile.
   * A confirmation message displays when the user logs in or logs out.
<img src="/workspace/Rewrk_MS4/media/images/logged_in.png">
<img src="/workspace/Rewrk_MS4/media/images/logged_out.png">


 
    
### Available Service section
   * On the home page the available services are displayed, with the price.
   * If the user clicks on a specific service they can view the full description of the service information. At the bottom of the service detail page is a link to the service booking page.
<img src="/workspace/Rewrk_MS4/media/images/all_services_ui.png">
<img src="/workspace/Rewrk_MS4/media/images/service_detail_ui.png">
  

### Booking form
* This page invites the user to submit their interest in booking a specific service.
* On submission of the form the user is provided with a confirmation message.
<img src="/workspace/Rewrk_MS4/media/images/book_service.png">

## Future features
* A Calendar on the create booking page for logged in users which shows which days are booked and which are available for booking.


# Database Schema
### User Profile model
* Django's user and admin model was utilised.

### Service app
<img src="/workspace/Rewrk_MS4/media/images/service_model.png">

# Technologies Used:
### Programming Languages:
* CSS, HTML, Python, and Django.
### Database framework
* Postgres.
### Git
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
### Github
* GitHub was used to store the projects code after being pushed from Git.
### Bootstrap 4
* Bootstrap was used to for design and to make the website responsive.
### Balsamiq
* Balsamiq was used to create the wireframes during the design process.


# Testing
## Functionality Testing
### Manual testing
* I used Google Chrome developer tools throughout the development process for testing and solving problems with style and display issues.
* I used Github Project and Issues to track tasks. After each task completion, I would fully test it before moving on to the next task.
* All links were tested multiple times during the development process and again once the project was completed to ensure that all pages were linked correctly.
* All Forms and form elements were tested to ensure that they work as they should, with user feedback on errors as well as user feedback on successful submission.

