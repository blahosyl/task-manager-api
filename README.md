# Task Manager

## UX/UI

### Strategy

### Scope

### Structure

#### Data models

##### Comments model

##### Profile model

##### Task model

Tasks should remain intact even when their creator (owner) or assignee are deleted (e.g., when a team member leaves an organization). In this case, the respective fields for the deleted user are set to `null`. Accordingly, the `owner` and `assignee` fields are allowed to be `null`.

As described in the [Frontend documentation](https://github.com/blahosyl/task-manager-frontend/blob/main/README.md#tasks-without-an-image),
 image upload is optional and there is no placeholder image added to tasks without images.
 These improvements are reflected in the Task model and the `tasks` serializer.

##### Watch model

#### Access management structure

#### CRUD

#### UI information design

##### Navigation bar design

##### Footer design

### Skeleton

#### Home page wireframes

#### Task list wireframes

#### Task detail wireframes

### Surface

#### Visual design

##### Logo

##### Minimalism

##### Color schemes

#### UX Improvements

## Project Management | Agile Methodologies

### Themes, Epics, Stories & Tasks

### Estimation

### Project Board

### Labels

#### Prioritization: MoSCoW

#### Timeboxing

#### Sprint planning

#### Sprint retroactives

## Features

### Navigation bar

### Footer

#### Home page

#### Task list

##### Filtering

##### Searching

#### Task detail page

#### Profile list

#### Profile detail page

### Access management

### Admin Panel

### Future features

### Code features

#### Regular testing

#### Adequate commenting

#### DRY

#### Security

## Testing

## Technologies used

### Languages used

### Other dependencies used

### Tools used

- [markdownlint extension for VS Code](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint): Markdown linting & style checking
- [Typos spell checker](https://open-vsx.org/extension/tekumara/typos-vscode)

## Deployment

### Prerequisites

### Fork the repository

### Deploy in the development environment

### Deploy to production

#### Pre#deployment steps

#### Steps on Heroku

## Credits

### Code credits

This project was developed on the basis of the [DRF-API](https://github.com/Code-Institute-Solutions/drf-api) by [Code Institute](https://github.com/Code-Institute-Solutions/).

I have also consulted the project [Tick It](https://github.com/Code-Institute-Submissions/ci_pp5_tick_it_react) by [Jamie King](https://github.com/jkingportfolio).

Front End based on [Moments](https://github.com/Code-Institute-Solutions/moments0) by [Code Institute](https://github.com/Code-Institute-Solutions/).

### Related advice

### Study/lookup sources

- [Django model field reference](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
- [Django `on_delete` options](https://www.queworx.com/django/django-on_delete/)
- [Django REST Framework generic API views](https://www.django-rest-framework.org/api-guide/generic-views/)
- [Django REST model field reference](https://www.django-rest-framework.org/api-guide/fields/)

### Text

### Media

#### Images

### Readmes

### Acknowledgements
