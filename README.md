# JIRA Field Finder

This Python script can either provide a dump of JIRA fields or allow you to search for a field based on the value. This is helpful for identifying custom fields that may need to be pulled from another script, such as the JIRA to Google Sheets script.

## Setup

* Create and enable your virtual environment.

* Install dependencies from requirements.txt.
```
pip install -r requirements.txt
```

* Place your JIRA token into the token variable of gsjiraconfig.py.

* Replace the domain in the apiBase URL with your company's JIRA domain.

* Run either dumpFields(issueKey) to get all of the fields and their values or searchFields(issueKey, value) to find fields with the corresponding value.