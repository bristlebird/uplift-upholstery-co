# Uplift Upholstery Co.
E-commerce site built on Django for CI PP5

![device mockup](docs/images/uuc-devices-black.webp)

Uplift Upholstery Co. is a fictional small upholstery business based in Kinsale, Co. Cork. As well as designing and building a small range of custom furniture products in house which are sold onine via the website, they also provide a small range of upholstery courses for people looking to re-upholster and upcycle their own pieces of furniture, which can be booked on the website. 

[View the live site here](https://uplift-upholstery-1735a035f709.herokuapp.com/)

## Table of contents

- [E-commerce business model](#e-commerce)
- [SEO & Social Media Marketing](#seo)
- [Design & User Experience](#ux)
- [Future Features](#future-features)
- [Agile Development](#agile)
- [Technologies](#technologies)
- [Database Design](#db)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

<a name="e-comerce"></a>
## E-commerce Business Model
This is a standard B2C ( Business to Consumer) business model where the business sells a small range of pre-designed custom made & upholstered furniture products from the website. The business also runs in person upholstery courses at their studio workshop, places for which can also be puchased from the website.




<a name="seo"></a>
## SEO & Social Media Marketing

### Technical / Off page SEO
Keyword research was carried out using a free tier on semrush.com to find the highest value and most impactful short and long tail keywords that the business' target market would use to search for thier products.
 
Custom page titles & meta descriptions were implemented in all page and product models to allow every page to be individually optimised.

### SItemap
[XML-Sitemaps.com](https://xml-sitemaps.com) was used to generate [this sitemap](https://uplift-upholstery-1735a035f709.herokuapp.com/sitemap.xml) for the site. Once a site has been published to it's own custom domain, i.e. https://upliftupholstery.co, the sitemap would be submitted to [Google's Search console](https://search.google.com/search-console) and [Bing's Webmaster tools](https://www.bing.com/webmaster/tools) to pprompt thier searchbots to crawl and index the website's pages into their serach results.

### Robots.txt
A basic robots.txt file was added to the site root [here](https://uplift-upholstery-1735a035f709.herokuapp.com/robots.txt). The followiong directives were added to allow all bots (except ChatGPT) to crawl and index all pages on the site. 

```
User-Agent: *
Disallow: 

User-agent: GPTBot
Disallow: /

Sitemap: https://uplift-upholstery-1735a035f709.herokuapp.com/sitemap.xml
``` 



### Social Media

### Email Marketing


<a name="ux"></a>
## Design & User Experience

### Site Goals


### Colour

Colour pallete
![](docs/images/uuc-pallette.webp)  

### Typography


### Wireframes


<a name="future-features"></a>
##Future Features


<a name="agile"></a>
## Agile Development

Agile methodologies were used to deliver the product MVP. [Github Projects](https://github.com/bristlebird/uplift-upholstery-co/projects) and issues provided the agile tools to create a basic Kanban board on which tasks and user stories were tracked throughout the project development. [View the Kanban board here](https://github.com/users/bristlebird/projects/4).

MoSCoW prioritisation was used with the aid of Github project labels to streamline and prioritise tasks during development. To deliver the MVP, core requirements were tackled first, so the primary focus was given to 'must haves', followed by 'should haves' and finally 'could haves'.

User stories were grouped into Epics which were mapped to project milestones.

Each user story appears as a card on the kanban board with a set of acceptance criteria — this provided a task driven approach to see the project through.

<a name="technologies"></a>
## Technologies
- HTML / CSS / JavaScript — standard front end web technologies used to build out the responsive user interface
- [Bootstrap](https://getbootstrap.com/) — open-source CSS framework directed at responsive, mobile-first front-end web development
- [Python](https://www.python.org/) — main backend progamming language used for application logic
- [Django](https://www.djangoproject.com/) — Python MVC framework for building back end web app functionality
- [PostgreSQL](https://www.postgresql.org/) — object relational database system for storing app content and models
- [Heroku](https://heroku.com/) — for app deployment & hosting
- [Git](https://git-scm.com/) — for version control
- [Github](https://github.com/bristlebird/time-lord) — for code storage / this repository
- [Gitpod](https://gitpod.io/) & [Visual Studio Code for Mac](https://code.visualstudio.com/) — IDE used to write the code
- [Code Institute's Boutique Ado walkthrough project](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode) provided a significant amount of the code and guidance on the techniques.

### Python Modules, Packages, Libraries & Frameworks:
- [asgiref](https://pypi.org/project/asgiref/) — standard interface between async-capable Python web servers, frameworks, and applications
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) — form template packs to add Bootstrap styling
- [dj-database-url](https://pypi.org/project/dj-database-url/) — utility for connecting Django to PostgreSQL
Django Storage API
- [django-allauth](https://docs.allauth.org/en/latest/) — used for account management, authentication & registration
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) — used to render forms HTML
- [django-summernote](https://pypi.org/project/django-summernote/) — adds wysiwyg / rich text editor to form textfields
- [gunicorn](https://gunicorn.org/) — a Python WSGI HTTP Server
- [oauthlib](https://pypi.org/project/oauthlib/) — authentication library dependancy used by allauth package
- [psycopg2](https://pypi.org/project/psycopg2/) — PostgreSQL database adapter
- [PyJWT](https://pypi.org/project/PyJWT/) — Python library which allows you to encode and decode JSON Web Tokens
- [python3-openid](https://pypi.org/project/python3-openid/) — set of Python packages to support use of the OpenID, dependenancy of allauth
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) — allauth dependancy
- [sqlparse](https://pypi.org/project/sqlparse/) — SQL parser for Python
- [urllib3](https://pypi.org/project/urllib3/) — HTTP client for Python
- [whitenoise](https://pypi.org/project/whitenoise/) — simplified static file serving for Python web apps


### Other Tools & Apps used
1. [Macdown](https://macdown.uranusjr.com/) — open source Markdown editor for macOS, used to create this README
2. [Lucid Charts](https://lucid.app/) — used to create ERD's
3. [Website Mockup Generator](https://websitemockupgenerator.com/) — to create responsive devices mockup for this Readme
4. [Affinity Photo 2](https://affinity.serif.com/en-gb/photo/) — for Image editing
5. [ImageOptim](https://imageoptim.com/mac) — for optimising images
6. [Font Awesome](https://fontawesome.com/) — used for various icons on the site
7. [Favicon.io](https://favicon.io) — used to generate app favicon
8. [Code Institute's Pep8 Python Linter](https://pep8ci.herokuapp.com/) — used to format python code and ensure it was free from errors
9. [Autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8) — Vscode extension for checking Python code
10. [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) — Vscode extension for linting Python code


<a name="db"></a>
## Database Design
The following ERD (entity relationship diagram) was used to visualise the database models for the site.

![Uplift Upholstery ERD](docs/images/uuc-erd.webp)

<a name="deployment"></a>
##  Deployment
This site has been deployed on Heroku from this Github repository — [view the live site here](https://uplift-upholstery-1735a035f709.herokuapp.com/).

To deploy on Heroku, you'll first need to fork or clone the project by hitting Github's fork or clone buttons at top of the repository and then follow these steps:

1. Get a free Heroku account [here](https://signup.heroku.com/).
3. When creating the account, choose the country you're in, set Python as the primary development language, set your password & agree to their terms of service.
4. When logged in to the dashboard, hit the 'Create new app' button.
5. Give your app a unique name, select your region & hit 'Create app'.
6. Once the app is created, hit the 'Settings' tab then 'Reveal Config Vars' & set youe environment variables:
	- DATABASE_URL: your PostgreSQL database URL, i.e. postgresql://xxxxxxxx
	- SECRET_KEY: your Django projects secret key
7. Hit the 'Deploy' tab, select 'Github' in the Deployment method section, hit the 'Connect to Github' button and sign in to Github to authorise the connection.
8. When connected, enter the repository name in the 'Search for a repository to connect to' field, hit 'search' & then 'Connect' for the chosen repository.
9. To deploy manually, select the'main' branch and hit the 'Deploy branch' button.
10. When deployed, click the 'View' button to open the deployed app in your browser.

<a name="testing"></a>
## Testing

### Mobile
The site was found to work consistently on Safari & Google Chrome browsers on an Apple iPhone 11. Further testing on Android devices is required. 

### Desktop
On desktop, the site was also found to work pretty consistently in Google Chrome, Mozilla Firefox, Microsoft Edge & Opera on Mac OS X 12.7.6 (Monterey). Further testing in browsers running on Windows desktop operating systems is also required.

### Validator Testing 

- HTML — No errors returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fuplift-upholstery-1735a035f709.herokuapp.com), except on the form pages that contain Summernote rich text editor (3rd party code over which I have no control of the output).
- CSS — No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fresonance-podcaster-fe27f8eb1c9a.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 

### Web Performance & Accessibility

All pages on the site achieve respectably high Google Lighthouse scores, except for the podcast add / edit & episode add / edit form pages which fall down on accessibility due to the Summernote rich text editor, as mentioned above.

#### Lighthouse results
[Home page](https://pagespeed.web.dev/analysis/https-resonance-podcaster-fe27f8eb1c9a-herokuapp-com/94n0jrjpe2?form_factor=mobile) - [About page](https://pagespeed.web.dev/analysis/https-resonance-podcaster-fe27f8eb1c9a-herokuapp-com-about/t1nssyhsnl?form_factor=mobile) - [Podcast detail page](https://pagespeed.web.dev/analysis/https-resonance-podcaster-fe27f8eb1c9a-herokuapp-com-waterways-through-time/80atmgpfey?form_factor=mobile)


### User Story Testing

| Test | Result |
| -- | -- |



<a name="credits"></a>
## Credits

### Code
- [Django docs](https://docs.djangoproject.com/en/5.1/)
- [Customizing error views (Django docs)](https://docs.djangoproject.com/en/3.2/topics/http/views/#customizing-error-views)
- [Bootstrap docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- LearnDjango.com: 
    - [Customizing Django 404 and 500 Error Pages](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)
    - [Add robots.txt to Django website](https://learndjango.com/tutorials/add-robotstxt-django-website)
- [Django contact form](https://mailtrap.io/blog/django-contact-form/)
- Django authentication system: [Login required decorator used to restrict CRUD functions to logged in users](https://docs.djangoproject.com/en/5.1/topics/auth/default/#the-login-required-decorator)
- Code Institute's Django blog & Boutique Ado walkthrough projects

### Design 
- Fonts: default System UI from Bootstrap for a clean & fast user interface, no need add Google fonts.
- [Color namer by Chirag Mehta](https://chir.ag/projects/name-that-color/) — for naming hex colors in css custom properties
- [ColorKit's colour contrast checker](https://colorkit.co/contrast-checker/5e2753-e0edd2/) — for checking colour contrast 

### Content & Media
- 
- [iStockphoto](https://iStockphoto.com/) — used for some of the images

<a name="acknowledgements"></a>
## Acknowledgements
- CI mentors: [Gareth McGirr](https://github.com/Gareth-McGirr) and...
- CI cohort supervisors: [Lewis Dillon](https://github.com/LewisMDillon) for their helpful guidance, enthusiasm and encouragement throughout the project.
