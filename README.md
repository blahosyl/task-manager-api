<!-- Disable warnings about inline HTML -->
<!-- markdownlint-disable MD033 -->
<!-- Disable warnings about hard tabs -->
<!-- markdownlint-disable MD010 -->
<!-- Disable warnings about fenced code blocks -->
<!-- markdownlint-disable MD040 -->
<!-- Disable warnings about list markers -->
<!-- markdownlint-disable MD004 -->

# On Fire 🔥 - the cheerful productivity app API

This repository contains the ReSt API backend to [On Fire 🔥 - the cheerful productivity app](https://github.com/blahosyl/task-manager-frontend), developed for the Advanced Front-end specialization at [Code Institute](https://codeinstitute.net/).

![API viewed in the browser](/documentation-assets/readme/api-preview.png)

Developer: [Dr. Sylvia Blaho](https://www.linkedin.com/in/blahosylvia/)

- [Deployed API](https://pp5-task-manager-api-380974d293dd.herokuapp.com/)
- [Front end GitHub repository](https://github.com/blahosyl/task-manager-frontend)
- [Front end deployed app](https://pp5-task-manager-frontend-eebb66e2c99d.herokuapp.com/)

See the development progress and further plans on the [Project Kanban board](https://github.com/users/blahosyl/projects/6).

<!-- Shield.io badges -->
![GitHub last commit](https://img.shields.io/github/last-commit/blahosyl/task-manager-api?color=red)
![GitHub contributors](https://img.shields.io/github/contributors/blahosyl/task-manager-api?color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/blahosyl/task-manager-api?color=black)

## Table of contents

- [Database structure](#data-structure)
  * [Database](#database)
  * [Data models](#data-models)
    + [Comment model](#comment-model)
    + [Profile model](#profile-model)
    + [Task model](#task-model)
    + [Watchers model](#watchers-model)
    + [User model](#user-model)
  * [Future features](#future-features)
  * [Code features](#code-features)
    + [Regular testing](#regular-testing)
    + [Security](#security)
- [API endpoints](#api-endpoints)
- [Testing](#testing)
- [Technologies used](#technologies-used)
  * [Languages used](#languages-used)
  * [Frameworks used](#frameworks-used)
  * [Other dependencies used](#other-dependencies-used)
  * [Tools used](#tools-used)
- [Deployment](#deployment)
  * [Prerequisites](#prerequisites)
  * [Fork the repository](#fork-the-repository)
  * [Deploy in the development environment](#deploy-in-the-development-environment)
  * [Deploy to production](#deploy-to-production)
    + [Pre-deployment steps](#pre-deployment-steps)
    + [Steps on Heroku](#steps-on-heroku)
- [Credits](#credits)
  * [Code credits](#code-credits)
  * [Related advice](#related-advice)
  * [Study/lookup sources](#studylookup-sources)
  * [Readmes](#readmes)

<small><i><a href='http://github.com/3kh0/readme-toc/'>Table of contents generated with readme-toc</a></i></small>

## Data structure

### Database

[Neon](https://neon.tech/), a serverless Postgres database was used for Production, while the built-in [SQLite](https://www.sqlite.org/index.html) dababase for used for API development & testing.

### Data models

The diagram below shows the custom models for this project, along with the User model by Allauth (only the fields that are utilized in this project are shown on the User model below).

Individual field names, types and and their specifications are also shown.

![Entity Relationship Diagram](/documentation-assets/readme/erd-task-manager.png)

The assessment criteria specify "a minimum of ONE custom model" for the MVP.
The current implementation  has 2 heavily customized models (Profile and Task), and 2 models based on the [walkthrough project](https://github.com/Code-Institute-Solutions/drf-api), which are slightly customized in the way they are used (Comment and Watchers).

#### Comment model

The Comment model is based on the [walkthrough project](https://github.com/Code-Institute-Solutions/drf-api), but 2 more extra fields are added to the serialzer: the first and last name of the owner's profile. This is used for conditionally rendering the user's name on the Front End depending on whether a `firstname` and `lastname` is filled in in their profile (the `username` is always present).

1. show first and last name if both are available
2. show first or last name if either are available
3. show username if neither are available

In some cases, 1. is shortened to only show the first name even if a last name is available.

#### Profile model

The Profile is heavily customized compared to the [walkthrough project](https://github.com/Code-Institute-Solutions/drf-api): not only are many more fields specified in it, but the extra fields specified in the serializer also work in a different way.

These are not only used for filtering in the API, but also for in custom hooks in the frontend that refresh individual components of the Task List pages without reloading the page.

Filtering based on the extra fields in the `profile` serializer forms the frame of displaying tasks on 3 different pages in the frontend.

#### Task model

The task model is the most extensive one of the app – unsurprisingly, since its primary purpose is tracking tasks. It is based on the Post model of the walkthough project, but it differs significantly in the number and type of fields it has, how fields relate to other models, how they are configured and how they are used in the frontend.

The Task model has 2 fields that relate to the User model: in addition to `owner` (the user creating the task), an `assignee` can also be spefcified. This is extensively used for filtering and presenting data in the frontend.

A further difference is that tasks should remain intact even when their creator (owner) or assignee are deleted (e.g., when a team member leaves an organization). In this case, the respective fields for the deleted user are set to `null`. Accordingly, the `owner` and `assignee` fields are allowed to be `null`.

A `due_date` field is added to the model. This is used to indicate overdue tasks in the frontend with a range of 🔥 emojis that features throughout the app branding (the longer the due date is in the past, the more 🔥 emojis appear on a task).

The `status` field is restricted to a pre-defined range, and it is used to automatically sort tasks into the corresponding columns in the frontend.

The `priority` field is also based on a pre-defined range, and is used to automatically change the color scheme of individual tasks in the frontend.

As described in the [Frontend documentation](https://github.com/blahosyl/task-manager-frontend/blob/main/README.md#tasks-without-an-image),
 image upload is optional and there is no placeholder image added to tasks without images.
 These improvements are reflected in the Task model and the `tasks` serializer.

#### Watchers model

This model is based on Like in the [walkthrough project](https://github.com/Code-Institute-Solutions/drf-api), but it has additional uses beyond statically filtering tasks: changes in Watchers instances trigger custom hooks refetching Profile and Task data without refreshing the page in the frontend.

#### User model

The standard User model is extended by `profile_lastname` and `profile_firstname` fields in the `task_manager_api` serializer. These fields are used to render users' names thourhout the app, as described in the Comments model section.

### Future features

The Project model has not been part of the MVP, as development time for the 1st version of this project was only 3 and a half weeks. It was thus relegated to version 2 of the app.

### Code features

#### Regular testing

Code was manually tested and validated throughout development.
At the end of the development process, a final, comprehensive round of testing and validating was completed.
The results are detailed in [TESTING.md](TESTING.md).

#### Adequate

Apart from making sure that the app functions as intended, I have also taken special care to make sure the code is well organized and appropriately commented. Since I am just becoming familiar with Django REST Framework (and dealing with executive functioning issues), I have erred on the side of "more is more" for code comments and docstrings for methods that were new to me.

#### Security

Sensitive information such as secret keys, Cloudinary URL and Database URL are stored in environment variables that are never committed to GitHub.
They are not sent through unsecured channels, and not written down on paper.

All passwords are stored in a password manager, and not written down in plain text electronically or on physical paper.

Unfortunately, the infrastructure for project submission at Code Institute requires the admin credentials to be submitted in plain text.

## API endpoints

The available endpoints, paths and actions are described under [Manual feature testing in`TESTING.md`](TESTING.md/#manual-feature-testing) for details.

## Testing

See the document [`TESTING.md`](TESTING.md) for details.

## Technologies used

### Languages used

- [Python](https://www.python.org/) 3.12.2

### Frameworks used

- [Django](https://pypi.org/project/Django/)
- [Django ReSt Framework](https://pypi.org/project/djangorestframework/)

### Other dependencies used

- [`asgiref`](https://pypi.org/project/asgiref/) – asynchronous communication between web apps & servers
- [`cloudinary`](https://pypi.org/project/cloudinary/) – storing images
- [`dj-database-url`](https://pypi.org/project/dj-database-url/) – use an environment variable to configure databases
- [`dj-rest-auth`](https://pypi.org/project/dj-rest-auth/) – access management
- [`django-allauth`](https://pypi.org/project/django-allauth/) – access management
- [`django-cloudinary-storage`](https://pypi.org/project/django-cloudinary-storage/) – interaction between Django and Cloudinary
- [`django-cors-headers`](https://pypi.org/project/django-cors-headers/) – CORS (Cross-Origin Resource Sharing) headers in responses
- [`django-filter`](https://pypi.org/project/django-filter/) – queryset filtering
- [`djangorestframework-simplejwt`](https://pypi.org/project/djangorestframework-simplejwt/) – JSON Web Token authentication
- [`gunicorn`](https://pypi.org/project/gunicorn/) – HTTP server for deployment
- [`oauthlib`](https://pypi.org/project/oauthlib/) – framework-agnostic OAuth implementation
- [`Pillow`](https://pypi.org/project/Pillow/) – image processing
- [`psycopg2`](https://pypi.org/project/psycopg2/) – PostgreSQL database adapter
- [`PyJWT`](https://pypi.org/project/PyJWT/) – encoding and decoding JWT tokens
- [`python3-openid`](https://pypi.org/project/python3-openid/) – support for the OpenID decentralized identity system
- [`pytz`](https://pypi.org/project/pytz/) – timezone calculation
- [`requests-oauthlib`](https://pypi.org/project/requests-oauthlib/) – OAuthlib authentication support for Requests
- [`sqlparse`](https://github.com/MikeR94/drf-api-league-hub/blob/main/documentation/readme_images/urls_pep8.png) – SQL parser
- [`urllib3`](https://pypi.org/project/urllib3/) – HTTP client

### Tools used

- [CI Python Linter](https://pep8ci.herokuapp.com/) – validate Python code
- [Git](https://git-scm.com/) – version control
- [GitHub](https://github.com/) – store the source files
- [GitHub Desktop](https://desktop.github.com/) – GitHub UI
- [GitHub Issues](https://github.com/features/issues) – feature management, bug tracking
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) – project management
- [GitHub TOC generator](http://github.com/3kh0/readme-toc/) – automatically generate a Markdown TOC
- [GitHub web editor](https://github.com/)
- [GitPod](https://gitpod.io/) – Integrated Development Environment
- [Google Sheets](https://docs.google.com/spreadsheets) – planning user stories
- [Heroku](https://heroku.com/) – host the production version of the app
- [Lucidchart](https://www.lucidchart.com/) – make the ERD
- [markdownlint extension for VS Code](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) – Markdown linting & style checking
- [Neon](https://neon.tech/) – serverless Postgres database
- [Preview](https://support.apple.com/guide/preview/welcome/mac) – cropping and annotating images
- [Shields.io](https://shields.io/) – add badges to README
- [Slack](https://slack.com/) – mentor communication
- [Typos spell checker for VS Code](https://open-vsx.org/extension/tekumara/typos-vscode)

## Deployment

The following instructions describe the deployment process with the tools used for this project.
Of course, you can choose other tools/providers for the individual functions described below, e. g., a different Postgres database instead of Neon, or a different development environment instead of GitPod.
Naturally, detailed instructions are only provided for the tools used in this project.

### Prerequisites

- [GitPod](https://www.gitpod.io/) (or another IDE)
- [Python 3.12](https://www.python.org/)
- [pip](https://github.com/pypa/pip)
- [git](https://git-scm.com/)
- [Neon](https://neon.tech/) (or another Postgres database)
- [Cloudinary](https://cloudinary.com/) (or another media hosting provider)
- [Heroku](https://www.heroku.com/) (or another could platform)
- Dependencies listed in [`requirements.txt`](requirements.txt)

> [!WARNING]
> The setup has been known to be prone to version conflicts, so use the exact versions specified in [`requirements.txt`](requirements.txt)

### Fork the repository

You can fork the repository by following these steps:

1. Log in to [GitHub](https://github.com/) (if you don't have a GitHub account yet, you can [create one](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) for free).
2. Navigate to the project website [https://github.com/blahosyl/task-manager-api](https://github.com/blahosyl/task-manager-api).
3. Click on **Fork** in the upper right part of the screen.
4. On the next page you have the possibility to change the repository name. To do this, simply write your desired name in the text field in the center part of the screen. You can also leave the name as it is.
5. Click **Fork** in the bottom right part of the screen.

>[!TIP]
>If you do rename the repository, make sure to keep the [GitHub naming conventions](https://github.com/bcgov/BC-Policy-Framework-For-GitHub/blob/master/BC-Gov-Org-HowTo/Naming-Repos.md) in mind.

### Deploy in the development environment

1. Open the repository in a new workspace in GitPod. GitPod will automatically run the Python virtual environment for you. If you're using a different development environment, see [this documentation](https://docs.python.org/3/library/venv.html).
2. Install the required dependencies:

	```
	pip3 -r requirements.txt.
	```

3. To store access credentials and other secrets, create a file called `env.py` in your top-level project directory.
Before adding any content to it, add `env.py` to `.gitignore` and commit your changes.
This will prevent the contents of `env.py` from being pushed to the Git repository.
4. Add the following information to your `env.py` file:
    - `CLOUDINARY_URL` - you can find this in your [Cloudinary](https://cloudinary.com/) console under **API Keys**
    - `DATABASE_URL`
    - `ALLOWED_HOST` - the URL of your local server
    - `CLIENT_ORIGIN_DEV` - the URL of your Frontend development server
    - `SECRET_KEY`
    - `DEV` - set this value to '1' in your development setup. This is used to determine if the app runs in Development or Production mode
5. In `settings.py`, add your GitPod workspace URL to `ALLOWED_HOSTS`
6. Run a migration to create your database tables:

	```
	python manage.py migrate
	```

7. Create a superuser (make sure you save the username and password you use here):

	```
	python manage.py createsuperuser
	```

8. Run the development server

	```
	python manage.py runserver
	```

### Deploy to production

#### Pre-deployment steps

Make sure to complete the following pre-deployment steps in your development environment, especially if you made changes to the project:

1. (Re-)create a list of requirements by going to the terminal and typing `pip3 freeze > requirements.txt`. This populates your `requirements.txt` file with the list of required files.
2. In `settings.py`, make sure `DEBUG=False` (or set conditionally based on the value of `DEV`)
3. Commit and push your changes to GitHub.

#### Steps on Heroku

1. Log in to your [Heroku](https://www.heroku.com/) account (or create a new one if you have not done so yet).
2. [Create a new Heroku app](https://dashboard.heroku.com/new-app) by selecting your region and app name.
3. Under **Settings > Config Vars** in Heroku, add the following variables:
    - `CLOUDINARY_URL` - you can find this in your [Cloudinary](https://cloudinary.com/) console under **API Keys**
    - `DATABASE_URL`
    - `SECRET_KEY`
    - `ALLOWED_HOST` - your Front End app URL
    - `CLIENT_ORIGIN_DEV` - the URL of your Frontend development server (if you want to use the deployed app with your Frontend Dev setup)
    - `CLIENT_ORIGIN` - the URL of your deployed Frontend app
    - `DISABLE_COLLECTSTATIC` – set value to 1 (this tells the deployed app not to collect static files)
4. Under **Deploy > Deployment method** in Heroku, select **GitHub** and connect Heroku to your GitHub account.
	- Type in your repository name, then click **Search**.
	- When your repository appears, click **Connect** next to it.
5. Under **Deploy > Manual deploy** in Heroku, select **Deploy branch** to deploy manually.
	- Once the process is finished, the following message will appear:<br>
	_Your app was successfully deployed_
	- Click **View** under the message, and a new tab will appear with your deployed app.
6. (optional) Under **Deploy > Automatic deploy** in Heroku, select **Enable Automatic Deploys** if you want your app to be rebuilt each time you push to the `main` branch of your GitHub repository (but make sure your `settings.py` file always has `DEBUG=False` when you do).

## Credits

### Code credits

This project was developed on the basis of the [DRF-API](https://github.com/Code-Institute-Solutions/drf-api) by [Code Institute](https://github.com/Code-Institute-Solutions/).

Tutor Thomas [suggested](https://github.com/blahosyl/task-manager-frontend/issues/28) changing the `due_date` field in my Tasks model to a `DateField` from a `DateTimeField`.

### Related advice

### Study/lookup sources

- [Django model field reference](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
- [Django `on_delete` options](https://www.queworx.com/django/django-on_delete/)
- [Django REST Framework generic API views](https://www.django-rest-framework.org/api-guide/generic-views/)
- [Django REST model field reference](https://www.django-rest-framework.org/api-guide/fields/)

### Readmes

- [Creating your first README with Kera Cudmore](https://www.youtube.com/watch?v=XbYJ4VlhSnY) by Code Institute
- [Creating your first README](https://github.com/kera-cudmore/readme-examples) by Kera Cudmore
- [Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club) by Kera Cudmore
- [Bodelschwingher Hof](https://github.com/4n4ru/CI_MS1_BodelschwingherHof/tree/master) by Ana Runje
- [Travel World](https://github.com/PedroCristo/portfolio_project_1/) by Pedro Cristo
- [Sourdough Bakes](https://github.com/siobhanlgorman) by Siobhan Gorman
- [Horizon Photo](https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#mobile-testing) by Rory Patrick Sheridan
- [BackeStock](https://github.com/amylour/BakeStock/) by [Amy Richardson](https://github.com/amylour)
- [American Pizza Order System](https://github.com/useriasminnaamerican_pizza_order_system/) by [Iasmina Pal](https://github.com/useriasminna)
- [Neverlost](https://github.com/Ri-Dearg/neverlost-thrift) by [Rory Patrick Sheridan](https://github.com/Ri-Dearg)
- [EastStr](https://github.com/ndsurgenor/east-street) by Nathan Surgenor
- [League Hub](https://github.com/MikeR94/drf-api-league-hub) by [MikeE94](https://github.com/MikeR94)
- [Tick it](https://github.com/jkingportfolio/CI_PP5_Tick_It_drf_api) by [Jamie King](https://github.com/jkingportfolio)
- [The README of my first Code Institute project](https://github.com/blahosyl/academic-publishing)
- [The README of my second Code Institute project](https://github.com/blahosyl/operator-game)
- [The README of my third Code Institute project](https://github.com/blahosyl/dinner-party)
- [The README of my fourth Code Institute project](https://github.com/blahosyl/task-manager-api)
