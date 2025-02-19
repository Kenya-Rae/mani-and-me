<h1 allign="center" id="title"> Mani & Me </h1>

![Mani & Me](readme/wireframes/am_i_responsive.png)

[Live Project can be viewed here.](https://mani-and-me-3a77440a82f2.herokuapp.com/)
![Logo](static/favicon.ico)

Mani & Me is a site that sells beautifully printed gifts for all: a heart-filled business that celebrates creativity, family, and the joy of personalisation.

## Table of Contents

### User Experience (UX)

- [Project Goals](#project-goals)
- [User Goals](#user-experience-ux)
- [Developer Goals](#developers-goals)
- [User Stories](#user-stories)
- [Design Choices](#design-choices)
- [Wireframes](#wireframes)

### Features

- [Current Features](#current-features)
- [Future Features](#future-features)

### Testing

- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Validators and Lighthouse](#validators-and-lighthouse)

### Deployment

- [How to Deploy Site](#deployments)

### Credits

- [Credits](#credits)
- [Code](#code)
- [Acknowledgments](#acknowledgments)

## User Experience (UX)

### Project Goals

This project's goal is to build a full-stack site that allows your users to browse and find products. As well as place orders and pay on the site. I would like to make this the base of the site that I will be gifting to a relative who has recently started up a small business.

#### User Goals:

- Easily find products via search or browsing the site.
- Able to add products to shopping bag.
- View my shopping bag context and the total.
- Ability to provide details for shipping.
- Contact information for the business.

#### Developers goals:

- Create a functional site for a relative who has started up a business recently.
- Demonstrate the use of full-stack development in its entirety.
- Make a site that allows users to find products and place orders.
- Make a compelling site that can be used by superusers and customers.

#### User Stories

As a user I want:

- To search for products.
- View individual product details
- Ability to view the total of shopping at any moment.
- Able to filter products.
- Easily create an account and log in.
- Easy navigation.
- Able to place an order and pay online.
- Securely enter my payment information
- Receive an immediate order confirmation email with details of my purchase.
- Easily manage my account details including shipping addresses.
- Able to save items to a wishlist for future purchases.

As a returning customer:

- Access my saved shipping addresses to expedite checkout.
- I want to see my order history.

As the site owner I want:

- A site that provides search and share functions.
- A structured and PEP8 compliant.
- Easily add, edit and delete products on the online store.
- Manage product categories and subcategories to organize my store effectively, allowing customers to navigate easily
- Demonstrate what I have learnt with Python and external libraries.
- A site that functions and is consistent with handling data. As well as accept payments and send email confirmations.
- Navigation bar that allows users to access different parts of the sites.
- Sign up, login and logout feature to allow a user to sign up. They can log out of the session when they are finished using the site.
- Dashboard, for users to view their past orders and edit/update shipping information.

## Design Choices

### Main Technologies, Languages, Libraries and APIs Used

- HTML
- CSS
- JavaScript
- Django + Python
- Relational database
- Flake8

### Fonts

- Playfair Display was used through the site from Google Fonts.

### Icons

- Font Awesome has been used throughout the project to provide easily identifiable icons to help users navigate through the site.
- Favicon was also used to create the tab icon for the browser. I had already had a previous logo so I had converted this via the favicon website to use.

### Colours

- Coolors were used to generate random colours that could be used in my site for buttons, background and borders.

### Images

- The images sourced have been taken by a relative, who will be gifted this site. They have created all of the products that are displayed on the site.
- All images and static files have been uploaded/managed by Amazon Web Services (AWS).

### Wireframes

Wireframes were created using [Balsamiq](https://balsamiq.com/).

- [Home](/readme/wireframes/homepage.png)
- [Products Page](/readme/wireframes/shop-products.png)
- [Product Info](/readme/wireframes/product-page.png)
- [Add to Bag](/readme/wireframes/product-page-add-to-bag.png)
- [Shopping Bag](/readme/wireframes/checkout.png)
- [Checkout Success](/readme/wireframes/checkout-success.png)
- [Checkout Complete Order](/readme/wireframes/checkout-complete-order.png)
- [Order History](/readme/wireframes/order-history-my-profile.png)
- [About Us](/readme/wireframes/about-us-page.png)
- [Contact Us](/readme/wireframes/contact-us-page.png)
- [Product Management](/readme/wireframes/product-management.png)
- [Inventory Management](/readme/wireframes/inventory-management.png)

## Schema

The schema overview for my Django application:

<details>
<summary>Schema</summary>
<IMG src="readme/wireframes/schema.jpg"  alt="Schema"/>
- This schema supports an e-commerce platform where users can make orders, track inventory, categorize products, manage their wishlists, and save shipping preferences in their profiles. The Order and OrderLineItem models manage the transaction details, while the Product and Inventory models handle product catalog and stock management.
</details>

## Features

### Current Features

The current features on the site are to ensure that users have a positive experience and achieve the website goals.

- Easy navigation across the whole site, for products and site/profile.
- Responsive design for mobile, tablet and desktop.
- Grid or list view for easier viewing.
- Sort and filtering for products.
- Contact and about us information.
- Images along with content.
- Wishlist, A signed-in user can create a wishlist and view it.
- Logo and favicon icon.
- Search functionality.
- Security/validations.
- Superusers can add, edit and delete products from the site and admin view.

### Future Features

I hope to make this a live site for a relative. There are a few things that I would like to implement/change after this course is complete.

- I would like to implement a rating after purchasing products. Where an email will be sent to review the product a week or a few days after the purchase/delivery date.
- As well as this, when logging/signing up I would like to add social media accounts eventually.
- Within the future of my relative business, I would like to incorporate a trust pilot rating type of functionality. So any new users can see the business is trustworthy and worth using.
- Going on from my last point, once the business starts to grow. I think the site will need to have a Frequently Asked Questions section.
- Potentially add a live chat system for people who need to contact in.
- I would like to implement a personalised page/section to enable users to add what they would like to customise on their product. Without having to contact in after purchase.
- Tracking on deliveries for users. As well as different types of shipping.
- It would also be beneficial to add different payment options to the site instead of just card payments.
- Sales data/ customer insight pages/reports to understand trends and make improvements to marketing decisions.
- Shortly I would like to develop the profile section more, allowing settings, and delete profile functionality.
- Add more security to the site overall once(if) this site becomes a used one.

### Loaded page:

When you first load on the page you are met with the homepage.

<details>
<summary>User Interface</summary>
<IMG src="readme/pages/user_interface.png"  alt="User Interface"/>
</details>

### Navigation:

<details>
<summary>Navigation</summary>
<IMG src="readme/pages/nav_1.png"  alt="Navigation"/>
<IMG src="readme/pages/nav_2.png"  alt="Main Navigation"/>
</details>

### Product Page:

<details>
<summary>Product Infomation</summary>
<IMG src="readme/pages/product_info.png"  alt="Product Details"/>
</details>

### Checkout Page:

<details>
<summary>Checkout Bag</summary>
<IMG src="readme/pages/bag_page.png"  alt="Checkout Bag"/>
</details>

<details>
<summary>Checkout Order</summary>
<IMG src="readme/pages/checkout_order.png"  alt="Checkout Order"/>
</details>

<details>
<summary>Checkout Sucess</summary>
<IMG src="readme/pages/checkout-successed.png"  alt="Order Successful"/>
</details>

### CRUD Functionality:

<details>
<summary>Create</summary>
<IMG src="readme/pages/crud_add.png"  alt="Create functionality"/>
</details>

<details>
<summary>Read</summary>
<IMG src="readme/pages/crud_read.png"  alt="Read functionality"/>
</details>

<details>
<summary>Update</summary>
<IMG src="readme/pages/crud_edit.png"  alt="Update functionality"/>
</details>

<details>
<summary>Delete</summary>
<IMG src="readme/pages/crud_delete_2.png"  alt="Delete functionality"/>
<br>
<IMG src="readme/pages/crud_delete_1.png"  alt="Delete functionality Success"/>
</details>

## Accessibility

- Limited bright colours to reduce the contrasts.
- Added name tags to elements, and included alt tags to images.

## Testing

### Manual Testing

| What to test         | Expected Results                                  | Passed   |
| -------------------- | ------------------------------------------------- | -------- |
| Navigation Menu      | Navigate through the site correctly.              | &#x2714; |
| Product Search       | Search function for finding products.             | &#x2714; |
| View Products        | View products in categories.                      | &#x2714; |
| Sign Up and Login    | Sign up/log in to the site as a user/superuser.   | &#x2714; |
| Sorting Products     | Sort products by price, rating, and category.     | &#x2714; |
| Add Products         | Superusers to add products to the site.           | &#x2714; |
| Delete Products      | Superusers to delete products from the site.      | &#x2714; |
| Edit Products        | Superusers to edit products on site.              | &#x2714; |
| Upload Images        | Superusers to add product images.                 | &#x2714; |
| Shopping Bag - Add   | Users can add products to shopping bag.           | &#x2714; |
| Shopping Bag - View  | Users can view products in shopping bag.          | &#x2714; |
| Payment              | Allow payments to be made for orders.             | &#x2714; |
| Confirmation         | Web/email confirmation of the order.              | &#x2714; |
| Inventory            | To be able to add stock control.                  | &#x2714; |

### For this project I have had friends and family, test various devices. Such as;

- I had a hand few testing the deployed site. There was no overall negative feedback other than a server error that happened when accessing edit/add products. Which was quickly resolved. The feedback given was that the site was easy to use and understand. I had asked each tester to use the site as a new user, returning user and superuser. Some features/pages stood out more than others, generally a good user experience.

### The devices that the site was tested on :

- iPhone 11 Pro
- HP Pavillion 17 Laptop
- iPad 10th Gen
- iPhone XR

## Validators and Lighthouse

W3c was used to validate HTML and CSS. JShint was used for JavaScript code.

### Lighthouse - Developer Chrome Tools

<details>
<summary>Lighthouse Overview</summary>
<IMG src="readme/validation/lighthouse.png"  alt="Lighthouse Overview Score"/>
</details>
<br>

<details>
<summary>Lighthouse Acessibility</summary>
<IMG src="readme/validation/lighthouse-access.png"  alt="Lighthouse Accessibility Score"/>
- Screen reader elements were added for better accessibility.
</details>
<br>

### HTML Validator:

<details>
<summary>HTML Validator Overview</summary>
<IMG src="readme/validation/html-validators.png"  alt="HTML Validator Overview"/>
</details>
<br>
<details>
<summary>HTML Validator - After Changes</summary>
<IMG src="readme/validation/html-validators-changed.png"  alt="HTML Validator"/>
- The error within the screenshot is due to the base template there is a duplicate ID, as this code was used twice for mobile view and once for larger screens. 
</details>

### CSS Validator:

<details>
<summary>CSS Validator </summary>
<IMG src="readme/validation/css-validator.png"  alt="CSS Validator"/>
</details>

### JavaScript Validator:

<details>
<summary>JavaScript Validator</summary>
<IMG src="readme/validation/js-validator-1.png"  alt="JavaScript Validator Results"/>
<IMG src="readme/validation/js-validator-2.png"  alt="JavaScript Validator Results pt2"/>
<IMG src="readme/validation/js-validator-3.png"  alt="JavaScript Validator Results pt3"/>
</details>

### Flake8:

<details>
<summary>Python Validator </summary>
<IMG src="readme/validation/flake8-validator-1.png"  alt="Python Validator pt1"/>
<IMG src="readme/validation/flake8-validator-2.png"  alt="Python Validator pt2"/>
<IMG src="readme/validation/flake8-validator-3.png"  alt="Python Validator pt3"/>
- Exlcuding the migrations and the venv as this was due to the VScode migration that i hadnt used. There are view lines left with the longer characters. Due to not knowing how to correctly breakdown the lines without breaking the code. I have chosen to leave them as they are. As well as the imports, some were removed but this was another area I wasn't sure what to take away as I noticed some imports are needed but not being used at the current time.
</details>

## Bugs

### Current Bugs

- Crispy forms seem to not work to the fullest extent. The layout seems to be off, as boxes are in the wrong place or not the full width it is supposed to be. The functionality of the forms works as it should. I had been problem-solving this for a few days. With that being said I have asked the Slack community what they had thought, yet no response. [Crispy forms query](https://code-institute-room.slack.com/archives/C026PTF46F5/p1738750770135619).

<br>
  <details>
  <summary>Current Console Message</summary>
  <IMG src="readme/validation/console-message.png"  alt="Console message"/>

</details>

### Fixed Bugs

- Sorting and filtering via ascending descending was not consistently working for some categories. In order to fix this, I had to change the if statement to include elif to handle the logic correctly.
- Payment input box was not displayed due to file path and typo within views.
- Recieved "Bad Request: /checkout/cache_checkout_data/" after debugging my stripe_elements.js, checkout views.py and checkout.html. I found that JSON was not imported within the checkout views.py file. After adding this payments and webhooks were successful again.
- Order history was unable to be viewed when clicked due to no import of the order model.
- Product management form displayed a 'BoundWidget' object that has no attribute 'field' error. I was trying to access the fields directly in the template in an invalid manner. I have removed the field from the form and tried {{ product_form|crispy }} instead.
- When deleting products in the admin view, a page 404 error would display on the site. Making the site unusable, this was due to the products being deleted were still in the session ID.
- Due to migrating to the VScode mid-project there were numerous amounts of issues on VScode, from stripe elements, edit function, and terminal commands to project missing files and not running. I decided to work as much as possible on the original workspace I was using, Gitpod. This resolved a lot of issues for me and I was able to continue and finish the project within the given time. I had to manually make the merge for the changes I made when trying to code on VScode.
- The Django countries version was newer than the Django version I was using, this caused the issue in deployment as Django countries had some incompatibilities. To overcome this, I had to install the LTS version of Django. Version 4.2 in particular. I have a runtime.txt to ensure the version of Python 3.12 was used in this project.
- Favicon 404 error due to not accessing it through {% static 'path here' %}.
- Server 500 error that was related to my custom-clearable widget template was not being accessed correctly. Due to making my project compliant with Flake8, I had broken the line where this template was being accessed. I undone the change to the file and everything was able to be accessed and used correctly.

## Deployments

This project was deployed to GitHub Pages using the steps below;

### How to Deploy to GitHub Pages.

1. Open the browser, search GitHub and log in. If you do not have an account, sign up [here](https://github.com/login).
2. Locate and select the [Mani & Me](https://github.com/Kenya-Rae/mani-and-me).
3. Once the repository is open, select settings.
4. Select 'Pages', which is found on the left-hand side under the Code and Automation category.
5. Underneath build and deployment, there are two sub-heading 'Source' and 'Branch'. Select the 'None' dropdown below the branch sub-heading.
6. Change the 'None' option to 'Main', then press "Save".
7. Wait a few moments whilst the pages refresh. (This could take up to 5 minutes.)
8. You may need to refresh the page, to see the saved changes. You should have seen the site and the link to the live site. An orange icon will display which will indicate that the save changes are still loading.
9. You can also check your deployment by selecting 'Code'. On the right-hand side, you should see 'Deployments'. Select 'Deployments' to view the status of your deployments.

### How to run this project locally.

To clone this project to Gitpod use the following steps;

1. Open the browser, search GitHub and log in. If you do not have an account, sign up [here](https://github.com/login).
2. Open a new tab, search Gitpod and log in. If you don't have an account, you can sign in with GitHub.
3. Open a new workspace.
4. Go back to the GitHub tab and locate [Mani & Me](https://github.com/Kenya-Rae/mani-and-me).
5. Click the green "<> Code" button.
6. Under the HTTPS tab, copy the URL for the repository.
7. Go back to your Gitpod Workspace and open the terminal.
8. Change the location of your current working directory to where you want the cloned directory.
9. Type "git clone", then paste the URL that you had copied earlier from GitHub.
10. Press Enter to create your local clone.

### How to Fork this project.

To fork this project from Gitpod, please follow the steps below;

1. Open the browser, search GitHub and log in. If you do not have an account, sign up [here](https://github.com/login).
2. Locate the GitHub tab and locate the project you want to fork. [Mani & Me](https://github.com/Kenya-Rae/mani-and-me)
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

1. Within your project coding environment. Open the terminal and generate a requirements file by typing " pip freeze --local > requirements.txt "
2. In the root directory create a file called Procfile, ensure that a capital "P" is used to ensure Heroku reads this. Then within this file add " web: python run.py.
3. Use a database or object storage instead of writing to your local filesystem.
4. In Heroku, create a new app.
5. Add an app name. Complete language-specific setup.
6. Select "Create App".
7. Explore the Heroku platform.
8. Within the settings, click "Reveal Config Vars". Use the variable within the env.py. Ensure that DEBUG, DEVELOPMENT and DB_URL are not included. As well as no strings in quotes when adding the values.
9. Locate to the Deploy tab and navigate towards the "Deployment method" section, select “Connect to GitHub”.
10. Search for your repository and click Connect.
11. You can click "Enable Automatic Deploys" in case of any further changes to the project. This will push over when you make the push to GitHub.
12. If you are using the Manual Deploy section click Deploy Branch. This will start the build process.
        <br> <strong>Note: If any changes are made to models you will need to manually make the migrations within Heroku.</strong>
13. The app should run now, click the “Open app” button.
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
- [AWS](https://aws.amazon.com/) - To store my static and media files.
- [Favicon](https://favicon.io/) - To make an icon for the browser tab.
- [Google Fonts](https://fonts.google.com/) - Provided the font style for the site.
- [Font Awesome](https://fontawesome.com/) - For icons in the site.
- [Coolors](https://coolors.co/) - Randomly generate colours.

### Code

- [Boutque Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+4/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/) - Where comments are added this is where I had gotten it from. Made changes to most sections that were used from this walkthrough.
- [Go Back W3schools](https://www.w3schools.com/jsref/met_his_back.asp) - Just for the go back function.

### Acknowledgments

- Friends and Family who tested and supported me through my final project. As well as the entirety of the course
- Tutor support for helping me during deployment and migration as there were some bugs that I wasn't able to fix.
- Slack community as they had helped me during my migrating progress, though I had chosen to use gitpod. As well as this, reading through similar issues/bugs that I faced in the project.

[Back to top](#title)
