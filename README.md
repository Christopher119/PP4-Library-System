
# CODERS LIBRARY
This is a simple DJango-based website for a library system to showcase and checkout books to users.

# Five UX Planes

## Strategy

Users will want a clean and easily digestible site.<br>
Users will want every page to be consistent.<br>
Users will want the ability to login and logout.<br>
Users will want the ability to see what books are available.<br>
Users will want the option to search for specific books by criteria.<br>
Users will want to be able to request specific books if they are unavailable.<br>
Users will want to be able to learn more about available books.<br>
Users will want to be able to reserve books for collection.<br>
Users will want to be able to review books.<br>
Users will want to be able to read reviews left by other users.<br>
Users will want to remain on the book they are viewing after submitting a review.<br>

Admins will want to be able to view book requests.<br>
Admins will want to be able to moderate and approve or disapprove reviews.<br>
Admins will want to be able to mark a book as returned to make it available.<br>

## Scope

The site should be cleanly presented, with all information clearly presented.<br>
The site should allow users to login and logout.<br>
The site should easily present a list of all available books for users to view.<br>
The site should have search functionality to allow users to filter book results.<br>
The site should have a form request to allow users to request books be added.<br>
The site should create dynamic views for each book to present more details information when a user accesses them.<br>
The site should have a button to allow users to request a book be reserved for collection.<br>
The site should disable this button if the book is currently unavailable.<br>
The site should have a form to allow users to submit reviews.<br>
The site should display approved reviews to users.

## Structure

In order to fulfill the users wants from the Strategy plane and the plans from the Scope plane I created a flowchart to understand how site flow.<br>
![Image of a flowchart for the site](README-Images/PP4-FlowChart.png)

I also created a Entity-Relationship Diagram to get a better idea of what I would need to construct to make the site function as required.<br>
![Image of an ERD for the site](README-Images/PP4-ERD.png)

### Main Scripts



#### Helper Scripts



## Skeleton

A wireframes was drawn up before any code was written to understand how to present information on the home page.<br>
![Image of a wireframe for the home page](README-Images/PP4-Home-Page-Wired.png)

A wireframes was drawn up before any code was written to understand how to present information on the book list page.<br>
![Image of a wireframe for the book list page](README-Images/PP4-Book-Page-Wired.png)

A wireframes was drawn up before any code was written to understand how to present information on the book details page.<br>
![Image of a wireframe for the book details page](README-Images/PP4-Book-Details-Page-Wired.png)

A wireframes was drawn up before any code was written to understand how to present information on the signup page.<br>
![Image of a wireframe for the login and signup page](README-Images/PP4-Sign-Up-Page-Wired.png)

A wireframes was drawn up before any code was written to understand how to present information on the login and logout pages.<br>
![Image of a wireframe for the login pages](README-Images/PP4-Sign-Out-Page-Wired.png)

## Surface

I wanted everything on the site to be presented cleanly.<br>

# Features

## Home
The site initially loads a view of the Home page which contains the name of the library and a brief "About Us" description.<br>
![Image of the Home page]()

## Books
The site will display a list of books in the library's database and display them to the user. The user will be able to search and filter to find the books they want.<br>
![Image of the Books List page]()

### Request-Form
The Books List page has a button to prompt a modal to fill a form to leave a request for a specific book to be added to the library.<br>
![Image of the Request Modal page]()

## Book-Details
The Books List contains more information about a book as well as shows any possible reviews the books may have been left by other users.<br>
![Image of the Detailed Book view page]()

### Reviews
This is simply an area of the Book-Details page which contains both a form to submit a review of a book as well as pre-existing and approved reviews.<br>

## Login-Form & Logout-Form
These are simple forms to allow users to login or logout of the site.<br>
![Images of the Signup, Login and Logout forms]()




## Features Left to Implement

1. Placeholder.<br>
    Placeholder.<br>

2. Placeholder.<br>
    Placeholder.<br>

# Testing


|TEST|PROCESS|EXPECTATION|RESULT|
|--|--|--|--|
| Placeholder | Placeholder | Placeholder | Placeholder |


# Validating

Placeholder for code validation. HTML, CSS, JS, Python

## Placeholder
The run.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Placeholder]()

# Bugs

Placeholder.<br>

1. Placeholder.<br>

2. Placeholder.<br>

# Deployment

This app will be deployed through Heroku by being linked to the Github repository.<br>
In order to deploy the site:<br>

1. I created the app in the Heroku Dashboard.<br>
2. I modified the Config Vars of the app to restrict the collection of static data.<br>
3. I installed gunicorn.<br>
4. I created a procfile to instruct heroku on which file to run.<br>
5. I added heroku as an allowed host in settings.py.<br>
6. I disabled DEBUG.<br>
7. I linked the heroku app to my GitHub repo.<br>
8. I clicked Deploy Branch.<br>

The live link can be found here - Placeholder

# Database Creation

This site will use a PostgreSQL database.<br>
In order to create and link the database:<br>

1. I used the CodeInstitute PostgreSQL tool.<br>
2. I created an env.py file and ensured it was listed in the .gitignore file.<br>
3. In env.py I imported python's os module.<br>
4. I set the value of DATABASE_URL to the url provided by CodeInstitute.<br>
5. I installed the required packages to connect my database and added them to requirements.txt<br>
6. I imported these packages and the env.py file into settings.py<br>
7. I replaced the existing sqlite3 database connections with my created database connection.<br>
8. I then created database tables using the migrate command.<br>
9. I created a superuser for the site and database.<br>
10. I deployed the project again.<br>
11. I added the DATABASE_URL to heroku's Config Vars.

# Model Creation

In order to add Models to the database:

1. I added the codeinstitute and heroku server urls to the CSRF_TRUSTED_ORIGINS<br>
1. I created the model in the models.py file.<br>
1. I assigned it's various attributes and values.<br>
1. I added any required Foreign Keys.<br>
1. I made migrations to the database table structure.<br>
1. I migrated the table to the database.<br>
1. I imported the model to the admin.py file.<br>
1. I registered the model in the admin.py file.<br>

# Serving Static Files

In order to allow Heroku to serve static files without relying on CDN:

1. I install the whitenoise package and add to requirements.txt.
2. I authorise the whitenoise packagae by adding it to the settings.text MIDDLEWARE.
3. I add a path to the STATIC_ROOT.
4. I run a command to collect all static files.
5. I create a runtime.txt file and add the used python version.
6. I delete the DISABLE_COLLECTSTATIC Config Vars I created for the initial deployment.
7. Heroku now runs collectstatic on each deployment.

# Allowing User Authentication

In order to allow users to register and login to the site:

1. I installed the django-allauth package and added it to requirements.txt.
2. I listed it in settings.txt under INSTALLED_APPS
3. I listed the site id as one as django can handle multiple and requires a specification.
4. I listed the login and logout redirects to point to the home page.
5. I listed the allauth middleware in settings MIDDLEWARE section.
8. I decided against adding email verification as a library may not require it.
9. I migrated the changes.
10. I included an "accounts" url path in the urls.py file.


# Credits

## Content
Placeholder:<br>
