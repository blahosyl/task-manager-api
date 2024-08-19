<!-- Disable warnings about inline HTML -->
<!-- markdownlint-disable MD033 -->
<!-- Disable warnings about hard tabs -->
<!-- markdownlint-disable MD010 -->

# Task Manager API

- [Front end GitHub repository](https://github.com/blahosyl/task-manager-frontend)
- [Front end deployed app](https://pp5-task-manager-frontend-eebb66e2c99d.herokuapp.com/)
- [Deployed API](https://pp5-task-manager-api-380974d293dd.herokuapp.com/)
- [Project Kanban board](https://github.com/users/blahosyl/projects/6)

## Table of contents

## Database

NeonDB

Developmental database user for testing (as connecting API to Frontend was very problematic for many)

### Data models

The diagram below shows the custom models for this project, along with the User model by Allauth (only the fields that are utilized in this project are shown on the User model below).

![Entity Relationship Diagram](/documentation-assets/readme/erd-task-manager.png)

The assessment criteria specify "a minimum of ONE custom model" for the MVP.
The current implementation  has 2 custom models (Profile an Task), and 2 models based on the walkthrough, which are slightly customized in the way they are used.

#### Comments model

#### Profile model

#### Task model

Tasks should remain intact even when their creator (owner) or assignee are deleted (e.g., when a team member leaves an organization). In this case, the respective fields for the deleted user are set to `null`. Accordingly, the `owner` and `assignee` fields are allowed to be `null`.

As described in the [Frontend documentation](https://github.com/blahosyl/task-manager-frontend/blob/main/README.md#tasks-without-an-image),
 image upload is optional and there is no placeholder image added to tasks without images.
 These improvements are reflected in the Task model and the `tasks` serializer.

#### Watchers model

### Future features

### Code features

#### Regular testing

#### Adequate commenting

#### DRY

#### Security

## Testing

See the document [`TESTING.md`](TESTING.md) for details.

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

Tutor Thomas [suggested](https://github.com/blahosyl/task-manager-frontend/issues/28) changing the `due_date` field in my Tasks model to a `DateField` from a `DateTimeField`.

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
- [The README of my fourth Code Institute project](https://github.com/blahosyl/spicy)
