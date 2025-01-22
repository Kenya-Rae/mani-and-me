<h1 allign="center" id="title"> Mani & Me </h1>

![Mani & Me]()

[Live Project can be viewed here.]()
![Logo]()

Mani & Me is site that sells beautifully printed gifts for all.

## Table of Contents

### User Experience (UX)

- [Project Goals](#project-goals)
- [User Goals](#user-experience-ux)
- [Developer Goals](#developers-goals)
- [User Stories](#user-stories)
- [Design Choices](#design-choices)
- [Wireframes](#wireframes)

### Features

- [Future Features](#future-feautres)

### Testing

- [Manual Testing](#manual-testing)
- [Bugs](#bugs)

### Deployment

- [How to Deploy Site](#deployments)

### Credits

- [Credits](#credits)
- [Code](#code)
- [Acknowledgments](#acknowledgments)

## User Experience (UX)

### Project Goals

This project's goal is to build a full-stack site that allows your users to browse and find products. As well as place orders and pay on the site. I would like to make this the base of the site that I will be gifting to a relative that has recently started up a small business.

#### Recruiters Goals

#### User Goals:

- Easily find products via search or browsing the site.
- Able to add products to shopping bag.
- View my shopping bag context and the total.
- Ability to provide details for shipping.
- Contact information for the business.

#### Developers goals:

- Create a functional site for a relative who has started up a business recently..
- Demonstrate the use of full-stack development in its entirety.
- Make a site that allows users to find products and place orders.
- Make a compelling site that can be used by superusers and customers.

#### User Stories

As a user I want:

- To search for products.
- Easy navigation.
- Able to place an order and pay online.
- Consistent functionalities i.e search, add to bag.

As the site owner I want:

- A site that provides search and share functions.
- A structured and PEP8 compliant.
- Demonstrate what I have learnt with Python and external libiraries.
- A site that functions and is consistent with handling data. As well as accepts payments and send email confirmations.

## Design Choices

### Languages Used

- HTML
- CSS
- JavaScript
- Django
- Python

### Fonts

- Google Fonts

### Icons

- Font Awesome and Favicon were both used within this project.
-

### Colours

-

### Images

- The images sourced have been taken by a relative, who will be gifted this site. They have created all of the products that are displayed on the site.

### Wireframes

Wireframes were created using [Balsamiq](https://balsamiq.com/).

- [Home]()
- [CRUD - Functionality](/readme/wireframes/crud-creating-update-selete-section.png)
- []()
- []()
- []()
- []()
- []()
- []()

## Features

- Navigation bar that alllows users to access different parts of the sites.
- Search box, allows users to find what they are looking for within the site.
- Sign up, login and logout feature to allow a user to sign up. They can logout of the session when they are finished using the site.(Superusers to have site control)
- Add, edit and delete products on the site as a superuser.
- Dashboard, for users to view their past orders and edit/update shipping information.

### Loaded page:

When you first load on the page you are met with the homepage.

<details>
<summary>User Interface</summary>
<IMG src=""  alt="User Interface"/>
</details>

### Navigation:

<details>
<summary> </summary>
<IMG src=""  alt=""/>
</details>

### Product Page:

<details>
<summary> </summary>
<IMG src=""  alt=""/>
</details>

### Checkout Page:

<details>
<summary> </summary>
<IMG src=""  alt=""/>
</details>

### CRUD Functionality:

<details>
<summary>Create</summary>
<IMG src=""  alt="Create functionality"/>
</details>

<details>
<summary>Read</summary>
<IMG src=""  alt="Read functionality"/>
</details>

<details>
<summary>Update</summary>
<IMG src=""  alt="Update functionality"/>
</details>

<details>
<summary>Delete</summary>
<IMG src=""  alt="Delete functionality"/>
</details>

## Future Features

-

## Accessibility

-

## Testing

### Manual Testing

| What to test        | Expected Results                          | Passed |
| ------------------- | ----------------------------------------- | ------ |
| Navigation Menu     | Navigate through the site correctly.      |        |
| Search for product  | Search function for finding products.     |        |
| View prodcucts      | View products in categories.              |        |
| Sign Up and Login   | Sign up/Login to site as user/superuser.  |        |
| Sorting products    | Sort products by price, rating, category. |        |
| Add products        | Superusers to add products to site.       |        |
| Delete products     | Superusers to delete products from site.  |        |
| Edit products       | Superusers to edit products on site.      |        |
| Upload images       | Superusers to add product images.         |        |
| Shopping bag - Add  | Users can add products to shopping bag.   |        |
| Shopping bag - View | Users can view products in shopping bag.  |        |
| Payment             | Allow payments to be made for orders.     |        |
| Confirmation        | Web/email confirmation of the order.      |        |
| Inventory           | To be able to add stock control.          |        |

### For this project I have had friends and family, test amongst various devices. Such as;

-

### Lighthouse - Developer Chrome Tools

<details>
<summary>Lighthouse Overview</summary>
<IMG src="readme/validation/lighthouse-overview.png"  alt="Lighthouse Overview Score"/>
</details>
<br>

<details>
<summary>Lighthouse Acessibility</summary>
<IMG src=""  alt="Lighthouse Accessibility Score"/>
</details>
<br>

## Validators

W3c was used to validate HTML, CSS. JShint was used for JavaScript code.

### HTML Validator:

<details>
<summary>HTML Validator Overview Part 1</summary>
<IMG src=""  alt="HTML Validator Overview Part 1"/>
</details>
<br>
<details>
<summary>HTML Validator </summary>
<IMG src=""  alt="HTML Validator"/>
</details>

<br>

### CSS Validator:

<br>
<details>
<summary>CSS Validator </summary>
<IMG src=""  alt="CSS Validator "/>
</details>

### JavaScript Validator:

<details>
<summary>JavaScript Validator</summary>
<IMG src=""  alt="JavaScript Validator Results"/>
</details>

## Bugs

### Current Bugs

-

<br>
  <details>
  <summary></summary>
  <IMG src=""  alt="Console message"/>

</details>

### Fixed Bugs

- Sorting and filtering via ascending descending was not consitently working for some categories. In order to fix this, I had to change the if statement to include elif to handle the logic correctly.
- Payment input box was not display due to file path and typo within views.
- Recieved "Bad Request: /checkout/cache_checkout_data/" after debugging my stripe_elements.js, checkout views.py and checkout.html. I found that JSON was not imported within checkout views.py file. After adding this payments and webhooks where successful again.

## Deployments

This project was deployed to GitHub Pages using the steps below;

### How to Deploy to GitHub Pages.

1. Open the browser, search GitHub and log in. If you do not have an account, sign up [here](https://github.com/login).
2. Locate and select the [Mani & Me]().
3. Once the repository is open, select settings.
4. Select 'Pages', which is found on the left-hand side under the Code and Automation category.
5. Underneath build and deployment, there are two sub-heading 'Source' and 'Branch'. Select the 'None' dropdown below the branch sub-heading.
6. Change the 'None' option to 'Main', then press "Save".
7. Wait a few moments whilst the pages refresh. (This could take up to 5 minutes.)
8. You may need to refresh the page, to see the saved changes. You should have seen that the site and the link to the live site. An orange icon will display which will indicate that the save changes are still loading.
9. You can also check your deployment by selecting 'Code'. On the right-hand side, you should see 'Deployments'. Select 'Deployments' to view the status of your deployments.

### How to run this project locally.

To clone this project to Gitpod use the following steps;

1. Open the browser, search GitHub and log in. If you do not have an account, sign up [here](https://github.com/login).
2. Open a new tab, search Gitpod and log in. If you don't have an account, you can sign in with GitHub.
3. Open a new workspace.
4. Go back to the GitHub tab and locate [Mani & Me]().
5. Click the green "<> Code" button.
6. Under the HTTPS tab, copy the URL for the repository.
7. Go back to your Gitpod Workspace and open the terminal.
8. Change the location of your current working directory to where you want the cloned directory.
9. Type "git clone", then paste the URL that you had copied earlier from GitHub.
10. Press Enter to create your local clone.

### How to Fork this project.

To fork this project from Gitpod, please follow the steps below;

1. Open the browser, search GitHub and log in. If you do not have an account, sign up [here](https://github.com/login).
2. Locate the GitHub tab and locate the project you want to fork. [Mani & Me]()
3. At the top right-hand side of the page, you will see a "Fork" button. Click on the button and wait a few moments. You should see the new forked repository under your own GitHub account.
4. By default the folk is named as their upstream repositories, you can rename the repositories by typing a name in the "Repository name" field.
5. You can also add a description to your fork and/or copy the default branch only.
6. To also access the files in the repository. Head over to your forked repository. Click the green "<> Code" button.
7. Under the HTTPS tab, copy the URL for the repository.
8. Go to the workspace you have created earlier.
9. To change the current directory to the location where you want the cloned directory.
10. Type "git clone" and paste the URL you copied from GitHub. Press "Enter" and your local clone will be created.

### How to Deploy to Heroku.

To deploy to Heroku, follow the steps below;

1. Within your project coding environment. Open the terminal and generate a requirements file via typing " pip freeze --local > requirements.txt "
2. In the root directory create a file called Procfile, ensure that a capital "P" is used to ensure Heroku reads this. Then within this file add " web: python run.py.
3. Use a database or object storage instead of writing to your local filesystem.
4. In Heroku, create a new app.
5. Add a app name. Complete language-specific setup.
6. Select "Create App".
7. Explore the Heroku platform.
8. Within the settings, click "Reveal Config Vars". Use the variable within the env.py. Ensure that DEBUG, DEVELOPMENT and DB_URL is not included. As well as no strings in qoutes when adding the values.
9. Locate to the Deploy tab and navigate towards the "Deployment method" section, select “Connect to GitHub”.
10. Search for your repository and click Connect.
11. You can click "Enable Automatic Deploys" in case of any further changes to the project. This will push over when you make the push to GitHub.
12. If you are using the Manual deploy section and click Deploy Branch. This will start the build process.
13. Once this is completed. Navigate to the top of the page to the “More” button and select “Run console”.
14. Type python3 into the console and click Run.
15. Then type "from recipes import db". This will pull the database through
16. Type "db.create_all()" this will create all the models. You can exit the terminal by typing "exit()" and hitting enter, and close the console.
    <br> <strong>Note: If any changes are made to models you will need to manually make the migrations within Heroku.</strong>
17. The app should running now, click the “Open app” button.
    <br> <strong>Note: The deployed app will load, but as the new database is empty you will need to add in some data.</strong>

## Credits

### Frameworks, Libraries and Programs Used

- [Balsamiq](https://balsamiq.com/) - For creating wireframes.
- [GitHub](https://github.com/) - To store my repository and deploy site.
- [Gitpod](https://www.gitpod.io/) - Used to write code for this project.
- [Heroku](https://www.heroku.com/) - To deploy my application.
- [Django](https://www.djangoproject.com/) - For developing this web application.
- [EmailJs](https://www.emailjs.com/docs/) - Used in my forgot password route/function.
- [HTML Validation](https://validator.w3.org/) - To validate my HTML Code.
- [CSS Validation](https://jigsaw.w3.org/css-validator/) - To validate my CSS code.
- [JS Validation](https://jshint.com/) - To validate my script.

### Code

- [Boutque Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+4/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/) - Where comments are added this is where I had gotten it from. Made changes to most sections that were used from this walkthrough.
- []() -

### Acknowledgments

- Friends and Family that tested and supported through my final project. Aswell the entirety of the course
- []() -
- []() -

[Back to top](#title)
