# Project Methodology

## Objective

The objective of this project was to automate repetitive employee-directory research across multiple mortgage company websites.

The original business process required manually navigating company directories, identifying employee profiles, collecting relevant information, and organizing the results for additional business research.

Python automation was used to reduce repetitive manual work and produce structured datasets.

---

## Technology Selection

Different websites required different approaches.

### Requests

Requests was useful when website content could be retrieved directly through HTTP without browser interaction.

### BeautifulSoup

BeautifulSoup was used to parse HTML content and locate relevant page elements.

### Selenium

Selenium was necessary for directories that relied on:

- JavaScript-generated content
- Interactive navigation
- Next-page buttons
- Dynamic loading
- Browser-based page interactions

### Pandas

Pandas was used to structure collected records and prepare them for export.

Outputs were produced in:

- CSV
- Excel

---

## General Process

The general workflow consisted of:

1. Inspecting the directory website
2. Identifying how employee profiles were structured
3. Determining whether Requests or Selenium was appropriate
4. Discovering profile URLs
5. Navigating individual profiles
6. Extracting relevant information
7. Storing records in structured Python objects
8. Creating a Pandas DataFrame
9. Cleaning and reviewing the results
10. Exporting the final dataset

---

## Website Differences

One of the main challenges was that the directories did not use a standardized layout.

Each company required examination of:

- HTML structure
- CSS selectors
- Pagination method
- Profile URLs
- JavaScript behavior
- Page loading behavior

As a result, extraction logic often required modification for each directory.

---

## Dynamic Content

Some directories did not place all employee records directly in the initial HTML response.

Selenium was used when browser interaction was required.

This included situations involving:

- Pagination buttons
- Content loaded after page rendering
- Scrolling
- Interactive navigation

---

## Troubleshooting

Troubleshooting was an important part of the project.

Issues encountered included:

- Pages loading differently through automation
- Pagination behavior
- Changing HTML structures
- Dynamic elements
- Browser timing
- Inconsistent profile layouts
- Automated-access challenges

These issues required iterative testing and modification of selectors, page navigation, and extraction logic.

---

## Data Processing

Collected records were organized using Pandas.

Processing included:

- Creating structured columns
- Reviewing missing values
- Removing duplicate records when necessary
- Preparing exports

The final results were provided in CSV and Excel formats.

---

## Scale

The project involved approximately 3–5 mortgage company directories.

Most directories contained more than 100 employee records.

One of the larger directories contained more than 300 employee records.

---

## Privacy

This public GitHub repository does not contain original customer datasets, private information, production exports, or customer-specific source code.

All sample information published here is fictional and exists only to demonstrate the technical structure of the project.
