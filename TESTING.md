<!-- Disable warnings about inline HTML -->
<!-- markdownlint-disable MD033 -->
<!-- Disable warnings about hard tabs -->
<!-- markdownlint-disable MD010 -->
<!-- Disable warnings about fenced code blocks -->
<!-- markdownlint-disable MD040 -->

# Testing the Task Manager

Back to  `README.md`(README.md)

## Table of Contents

## User Story Testing

See the [front end documentation](https://github.com/blahosyl/task-manager-frontend/blob/main/TESTING.md#testing-user-stories).

## Code validation

### Python validation

All self-written or modified Python files in the project were validated with the [Code Institute PEP8 Linter](https://pep8ci.herokuapp.com/).
Some minor errors were found, which were corrected ([#22](https://github.com/blahosyl/task-manager-api/issues/22)).
The present version of the project contains no errors.

#### `profiles` app Python validation

##### `admin.py` | `profiles`

##### `apps.py` | `profiles`

##### `models.py` | `profiles`

##### `serializers.py` | `profiles`

##### `tests.py` | `profiles`

##### `views.py` | `profiles`

##### `urls.py` | `profiles`

#### `tasks` app Python validation

##### `admin.py` | `tasks`

##### `apps.py` | `tasks`

##### `models.py` | `tasks`

##### `serializers.py` | `tasks`

##### `tests.py` | `tasks`

##### `urls.py` | `tasks`

##### `views.py` | `tasks`

#### `watchers` app Python validation

##### `admin.py` | `watchers`

##### `apps.py` | `watchers`

##### `models.py` | `watchers`

##### `serializers.py` | `watchers`

##### `tests.py` | `watchers`

##### `urls.py` | `watchers`

##### `views.py` | `watchers`

### Project-level Python validation

#### `permissions.py`

#### `serializers.py`

#### `settings.py`

#### `urls.py`

##### `views.py`

## Manual feature testing

### Tasks manual testing

|API name	|Method	|Path|Expected result | Result|
|---	|---	|---	|---				|:---:	|
|Task List |GET|`/tasks`|Get all tasks|✅|
|Create Task  |POST|`/tasks`|Create new task|✅|
|Task Detail  |GET|`/tasks/${id}`|View existing task|✅|
|Edit Task  |PUT|`/tasks/${id}`|Edit existing task|✅|
|Delete Task  |DELETE|`/tasks/${id}`|Delete existing task|✅|

### Comments manual testing

|API name	|Method	|Path|Expected result | Result|
|---	|---	|---	|---				|:---:	|
|Comment List |GET|`/comments`|Get all comments|✅|
|Create Comment  |POST|`/comments`|Create new comment|✅|
|Comment Detail  |GET|`/comments/${id}`|View existing comment|✅|
|Edit Comment  |PUT|`/comments/${id}`|Edit existing comment|✅|
|Delete Comment  |DELETE|`/comments/${id}`|Delete existing comment|✅|

### Profiles manual testing

|API name	|Method	|Path|Expected result | Result|
|---	|---	|---	|---				|:---:	|
|Profile List |GET|`/profiles`|Get all profiles|✅|
|Profile Detail  |GET|`/profiles/${id}`|View existing profile|✅|
|Edit Profile  |PUT|`/profiles/${id}`|Edit existing profile|✅|

### Watchers manual testing

|API name	|Method	|Path|Expected result | Result|
|---	|---	|---	|---				|:---:	|
|Watchers List |GET|`/watchers`|Get all watcher instances|✅|
|Watch  |POST|`/watchers`|Create new watcher instance|✅|
|Watcher Detail  |GET|`/watchers/${id}`|View existing watcher instance|✅|
|Unwatch|DELETE|`/watchers/${id}`|Delete existing watcher instance|✅|

## Automated testing

## Bugs

All bugs are tracked in [GitHub Issues](https://github.com/blahosyl/task-manager-api/issues?q=is%3Aissue+label%3Abug).

### Known bugs

Known bugs are listed in [GitHub Issues](https://github.com/blahosyl/task-manager-api/issues?q=is%3Aissue+label%3Abug+is%3Aopen).

### Solved bugs

Solved bugs are listed in [GitHub Issues](https://github.com/blahosyl/task-manager-api/issues?q=is%3Aissue+label%3Abug+is%3Aclosed).
