# Mortgage Directory Automation

Python automation project for collecting, structuring, and exporting publicly available employee directory data for business research. Automated collection of publicly available loan officer directory data, including business email addresses, phone numbers, company information, and state licensing coverage, across multiple mortgage company directories.

## Overview

This project was developed to automate the collection of employee directory information from multiple mortgage company websites.

The goal was to reduce the amount of manual research required to locate and organize publicly available business contact information.

The project involved working with several directory structures, including dynamically loaded pages, pagination, and inconsistent website layouts.

---

## Technologies Used

- Python
- Selenium
- BeautifulSoup
- Requests
- Pandas
- CSV
- Excel

---

## Project Scope

The automation was used across approximately **3–5 mortgage company directories**.
Typically containing 100+ loan officer records per company, with one directory containing 300+ records.
Sizes included:

- 100+ employee records per company
- One directory containing more than 300 employee records

The collected data was structured and exported for further business research.

---

## Key Features

- Automated browser interaction using Selenium
- Parsed HTML content with BeautifulSoup
- Used Requests where direct HTTP retrieval was appropriate
- Structured collected data with Pandas
- Handled pagination and dynamically loaded content
- Exported results to CSV and Excel
- Worked across multiple website layouts
- Reduced repetitive manual data collection

---

## General Workflow

```text
Directory Website
       |
       v
Page / Profile Discovery
       |
       v
Selenium or Requests
       |
       v
HTML Parsing
       |
       v
Data Extraction
       |
       v
Pandas DataFrame
       |
       v
Data Cleaning / Structuring
       |
       v
CSV / Excel Export
```

---

## Example Data Structure

For portfolio purposes, this repository uses fictional sample data rather than customer or production data.

Example:

| Name | Job Title | Company | Location |
|---|---|---|---|
| Jordan Smith | Loan Officer | Example Mortgage Co. | Miami, FL |
| Taylor Johnson | Branch Manager | Sample Lending Group | Orlando, FL |
| Morgan Lee | Mortgage Advisor | Demo Home Loans | Tampa, FL |

---

## Challenges & Troubleshooting

### Dynamic Web Content

Some directories loaded employee information through JavaScript rather than providing all records directly in the page HTML.

Selenium was used when browser interaction was necessary to load or navigate through this content.

### Pagination

Different directories used different pagination methods, including:

- Page numbers
- Next-page buttons
- Dynamically loaded content

The automation logic had to be adapted to the structure of each website.

### Inconsistent Website Structures

Because each company directory was designed differently, selectors and extraction logic could not always be reused without modification.

This required analyzing each site's HTML structure and adjusting the automation accordingly.

### Anti-Automation Challenges

Some websites contained protections or behavior that made automated retrieval more difficult.

This required troubleshooting browser behavior, page loading, and navigation rather than relying on a single extraction method.

---

## Skills Demonstrated

This project demonstrates experience with:

- Python programming
- Browser automation
- HTML parsing
- Data extraction
- Data cleaning
- Data transformation
- Data export
- Web troubleshooting
- Debugging
- Working with dynamic websites
- Process automation

---

## Privacy & Data Handling

This repository is a sanitized portfolio representation of the original project.

It does **not** contain:

- Customer information
- Proprietary datasets
- Credentials
- Private business information
- Production exports
- Real employee contact information collected for the original customer

Any sample data included in this repository is fictional and is used only to demonstrate project structure and functionality.

---

## Repository Structure

```text
mortgage-directory-automation/
│
├── README.md
├── src/
│   └── directory_scraper.py
│
├── sample-data/
│   └── sample_output.csv
│
├── screenshots/
│
├── docs/
│   └── methodology.md
│
├── requirements.txt
│
└── .gitignore
```

---

## Future Improvements

Possible future improvements include:

- Modular scraper configuration for different directory layouts
- Improved error handling
- Logging
- Automated duplicate detection
- Data validation
- Command-line options
- Configurable export formats
- More reusable extraction functions

---

## Author

**Isabel Munguia**

[LinkedIn](https://www.linkedin.com/in/isabel-munguia/)  
[GitHub](https://github.com/IsabelMunguia)

---

## Disclaimer

This project is presented for educational and professional portfolio purposes.

Web automation and data collection should always be performed in accordance with applicable laws, website terms, privacy requirements, and authorized business use.
