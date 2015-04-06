# Scrumptious
Dashboard view for scrum note taking.
Scrumptious will open a vim instance with 4 splits in two rows

## Features

* Facilitates preparation for your scrum meeting.
* Allows you to take notes during your scrum meeting
* Lists active jira issues for the current user.
* Pulls recent issues from jira

# Dependencies

* python2
* [ jira ] (https://pypi.python.org/pypi/jira)
* [ jinja2 ] (https://pypi.python.org/pypi/Jinja2)

## Configuration
Scrumptions reads its configuration from file `~/.scrumptious.config`

```bash
template_filename=    # FILE PATH the template for the new minutes
minute_directory=     # DIRECTORY PATH where scrum minutes are stored
jira_username=        # USERNAME for your jira password
jira_password=        # PASSWORD for your jira account
jira_server=          # URL of the jira server
minute_epoch=         # DATE limit for backwards e.g.:2014-11-20
```

## Splits
Row 1
- Current Session space.
- Previous Session space.
- Session template file.

Row 2
- Output from the jira query(s).

## Usage

```bash
scrumptious [-+0-9]
```

When running scrumptious without any arguments will open the day's session
configuration. If it doesn't exists the days session file will be creates with.

Scrumptious can be instructed to open a session other than the current day's by
specifying an increment or decrement of session.

Open tomorrow's session:

```bash
scrumptious +1
```

Open the previous session view

```bash
scrumptious -1
```

Open the second previous session view

```bash
scrumptious -2
```

## Notes
Script will be migrated to python entirely.
