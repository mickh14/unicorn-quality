**Unicorn Attractor Quality UX Strategy**

[![Build Status](https://travis-ci.org/mickh14/unicorn-quality.svg?branch=master)](https://travis-ci.org/mickh14/unicorn-quality)

**Business Goal** : To deliver an easy to use website that will allow users of the UnicornAttractor Quality app to create tickets to track issues with the app to facilitate quality improvement.

The issues can be &#39;Bugs&#39; which will be fixed for free or &#39;Feature&#39; which will be developed when enough money is received.

Voting for bugs is free. However, users will have to pay to vote for features. When a feature reaches 100 votes then development will commence.

Vist [Unicorn Attractor Quality](https://unicorn-quality.herokuapp.com/)site

**Scope**

1. Website Opens to Landing that is good to look at
2. Navigation is obvious and intuitive
3. Header has menu with links to the pages (toggle button on mobile)
4. Footer has social links
5. Pages
  1. BASE HTML will have header, footer and search that will be visible on all pages
  2. [Registration](https://unicorn-quality.herokuapp.com/accounts/register/) – access via navbar. Can not be seen if user has logged in
  3. [Log in](https://unicorn-quality.herokuapp.com/accounts/login/)– access via navbar. Can not be seen if user has logged in
  4. [All Issues](https://unicorn-quality.herokuapp.com/) – Landing page
  5. [Issue Details](https://unicorn-quality.herokuapp.com/cart/issues/9/) – accessed by clicking on &#39;Details&#39; on issue
  6. [New Issue](https://unicorn-quality.herokuapp.com/cart/issues/new/) - access via navbar. Can only be accessed when logged in
  7. [Edit Issue](https://unicorn-quality.herokuapp.com/cart/issues/9/edit/) – when viewing an issue details click Edit Issue
  8. [Pass Issue](https://unicorn-quality.herokuapp.com/cart/issues/9/pass/) - when viewing an issue details click Pass button. Only visible when status of issue is In Test
  9. [View Cart](https://unicorn-quality.herokuapp.com/cart/) – accessed via navbar
  10. [Checkout](https://unicorn-quality.herokuapp.com/checkout/) – accessed by clicking on Checkout button when viewing cart
  11. Developed – accessed via navbar. Displays all issues with status of Done
    1. [Features](https://unicorn-quality.herokuapp.com/search/feature_done/)
    2. [Bugs](https://unicorn-quality.herokuapp.com/search/bug_done/)

1. Landing Page shows all issue
2. A user can register
3. A user can log in
4. A user can create a new issue
5. As a user I want to view all issues
6. A user can view issue details
  1. Bugs should only show details relevant for a bug
  2. Features should only show details relevant to a feature
7. A user can edit an issue
8. A user can comment on an issue
9. A user can vote for a bug
10. A user can add vote for feature to cart
11. A user can review cart
12. A user can amend cart content
13. A user can make a payment for votes
14. A user can pass an issue with a status of &#39; **In Test&#39;**
15. A user can view issues where the development is complete
16. A user can search with free text
17. A user can search for bug
18. A user can search for feature
19. A user can log out
20. An issue with a status of Done can not longer be voted for

**Design:**

**Framework:**

- [**Bootstrap**](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

To get a modern and clean layout, I used bootstrap as a framework.

- [**jQuery 3.4.0**](https://code.jquery.com/jquery/)

For Javascript, I mainly used Jquery

- [**Django 1.11.24**](https://www.djangoproject.com/)

The Django framework that runs the application

**Database:**

I used SQLite for the DB.

Objects

| Issues |
| --- |
| issue\_id |
| created\_by (user\_id) |
| Name |
| Description |
| step\_to\_Reproduce |
| expected\_Results |
| actual\_Results |
| published\_date |
| issue\_type |
| status |
| views |
| votes |
| price |
| root cause |
| resolution |

| Users |   |
| --- | --- |
| user\_id |   |
| email |   |
| password1 |   |
| password2 |   |
| Comment |
| checkout\_id |
| name |
| body |
| comment\_date |
| issue (fk) |
| author (fk) |

| Cart |
| --- |
| cart\_id |
| issue (fk) |
| quantity |

| Checkout |
| --- |
| checkout\_id |
| full\_name |
| phone\_number |
| country |
| postcode |
| town\_or\_city |
| street\_address1 |
| street\_address2 |
| county |
| date |
| order\_id (fk) |
| issue\_id(fk) |

**Colour Scheme and Typography:**

I have gone with a simple colour scheme. Blue was the strongest colour used.

### Technologies Used

#### Languages

- [**HTML**](https://html.spec.whatwg.org/multipage/) used as the markup language
- [**CSS**](https://www.w3.org/Style/CSS/) used as the base for cascading styles.
- [**JavaScript**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) used mostly for DOM manipulation
- [**Python3**](https://www.python.org/) used to run the backend application

#### Libraries

- [**Google Fonts**](https://fonts.google.com/) provided the fonts used throughout the project
- [**Bootstrap**](https://getbootstrap.com/docs/4.4/getting-started/introduction/) used as the CSS framework for the project
- [**jQuery**](https://jquery.com/) used as the primary JavaScript **functionality**.
- [**Django**](https://www.djangoproject.com/)[ ](https://www.djangoproject.com/)0.2 is the micro web **framework** that runs the application
- [**SQLite**](https://www.sqlite.org/index.html)[ ](https://www.sqlite.org/index.html)used as the DB

#### Tools

- [**GITPOD**](https://gitpod.io/workspaces/) **is the IDE I used to put the project together**
- [**GitHub**](https://github.com/mickh14/ourCookBook/blob/master/documentation/Entity%20Relationship.xlsx)[ ](https://github.com/mickh14/ourCookBook/blob/master/documentation/Entity%20Relationship.xlsx)provides hosting for software development version control using Git
- [**Balsamiq**](https://balsamiq.com/) was used to create the wireframes when initially planning this project

#### Hosting

- [**Heroku**](https://dashboard.heroku.com/apps/out-cook-book) is used to host the app

### Testing

**Functional Testing**

- I completed exploratory testing
- Friends and family completed user acceptance testing
- The following functional tests were complete
- Register a user
- Log into applicationb
- Create a new issue
- View all issues
- View issue details
  - Bugs show bug related details
  - Features show details relevant to a feature including a status bar on how close feature is to development
- Edit an issue and verify change is saved
- Add comment to an issue
- Vote for a bug
- Add a vote for feature to cart
- Review cart
- Amend cart content
- Make a payment for votes
- Pass an issue with a status of &#39; **In Test&#39;**
  - Ensure it is not possible to Pass an issue with any status other that test
- View issues where the development is complete
- Search with free text
- Search for bug
- Search for feature
- Log out
- Verify an issue can not be voted for when the status is Done

**Validation Services**

The following validation services were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate **HTML**.

Errors are detected for the Jinja in my HTML files. All other code was validated without error.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate **CSS**.
- [JSHint](https://jshint.com/) was used to validate JavaScript.
- [PEP8 Online](http://pep8online.com/) was used to validate Python.

app.py file is completely PEP8 compliant!

### Deployment

#### Deployment To Heroku

In order the deploy my project to Heroku I have completed the following steps:

#### GitPod IDE

- Created a Procfile with the command echo web: python run.py \&gt; Procfile.
- Created a requirement.txt file so Heroku know what python modules it will need to run my application with the command sudo pip freeze --local \&gt; requirements.txt
- Then git add and git commit the new prerequisites from the requirements.txt file and Procfile, then &#39;git push&#39; the undertaking to GitHub.

#### Heroku

- After loging into heroku I created a new app, using the name unicorn-quality and set the region to Europe.
- unicorn-quality application
- In the settings tab I clicked reveal config vars and entered the required environment variables, which in this case were:

IP 0.0.0.0

PORT 5000

- Click on &quot;Deploy&quot;
  - For &quot;Deployment method&quot; and select GitHub.
- Confirm the linking of the heroku app to the correct GitHub repository.
- In the heroku dashboard, click &quot;Deploy&quot;.
- The site is now successfully deployed

### Credits

#### Content

#### Media

The background image is from Google Images.

The images for the logo image,Category images on the home page were taken from google free images.

#### Acknowledgements

**Tutorials**

- [https://stackoverflow.com](https://stackoverflow.com/)
- [https://www.youtube.com/](https://www.youtube.com/watch?v=vVx1737auSE)
- Special thanks to Guido Cecilio Garcia, my Code Institute mentor.

Disclaimer

- The content of this website is educational purposes only.