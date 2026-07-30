"""
Mortgage Loan Officer Directory Automation
Author: Isabel Munguia

Sanitized portfolio example demonstrating the general workflow used
to collect publicly available loan officer information from mortgage
company directories.

This version uses fictional selectors and URLs and does not contain
customer-specific code, private datasets, or production configuration.
"""

import time
import requests
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def create_driver():
    """Create and configure a Selenium Chrome driver."""

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    return webdriver.Chrome(options=options)


def collect_profile_links(driver, directory_url):
    """
    Discover loan officer profile links from a directory page.

    Selectors are intentionally generic for portfolio purposes.
    """

    driver.get(directory_url)
    time.sleep(2)

    profile_links = []

    elements = driver.find_elements(
        By.CSS_SELECTOR,
        "a.loan-officer-profile"
    )

    for element in elements:
        link = element.get_attribute("href")

        if link and link not in profile_links:
            profile_links.append(link)

    return profile_links


def parse_licensed_states(soup):
    """
    Extract states where the loan officer is listed as licensed.

    The selector below is fictional and provided only to demonstrate
    how state licensing data could be collected and structured.
    """

    state_elements = soup.select(".licensed-state")

    states = []

    for element in state_elements:
        state = element.get_text(strip=True)

        if state and state not in states:
            states.append(state)

    return ", ".join(states) if states else "Not Available"


def parse_profile(profile_url, company_name):
    """
    Retrieve and parse a loan officer profile.

    This sanitized portfolio version extracts:
    - name
    - business email
    - business phone
    - licensed states
    - mortgage company
    """

    response = requests.get(
        profile_url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    name_element = soup.select_one(".loan-officer-name")
    email_element = soup.select_one(".loan-officer-email")
    phone_element = soup.select_one(".loan-officer-phone")

    return {
        "loan_officer_name": (
            name_element.get_text(strip=True)
            if name_element
            else "Not Available"
        ),
        "email": (
            email_element.get_text(strip=True)
            if email_element
            else "Not Available"
        ),
        "phone": (
            phone_element.get_text(strip=True)
            if phone_element
            else "Not Available"
        ),
        "licensed_states": parse_licensed_states(soup),
        "company": company_name,
    }


def clean_records(records):
    """
    Convert extracted records into a clean Pandas DataFrame.
    """

    df = pd.DataFrame(records)

    df.drop_duplicates(inplace=True)

    df.fillna("Not Available", inplace=True)

    return df


def export_results(
    df,
    filename="loan_officer_directory_results"
):
    """
    Export structured loan officer records to CSV and Excel.
    """

    df.to_csv(
        f"{filename}.csv",
        index=False
    )

    df.to_excel(
        f"{filename}.xlsx",
        index=False
    )


def main():
    """
    Demonstration workflow.

    The URL and company below are fictional and are included only
    to show the structure of the original automation process.
    """

    directory_url = "https://example.com/loan-officers"
    company_name = "Example Mortgage Co."

    driver = create_driver()

    records = []

    try:
        profile_links = collect_profile_links(
            driver,
            directory_url
        )

        print(
            f"Discovered {len(profile_links)} loan officer profiles."
        )

        for profile_url in profile_links:

            try:
                record = parse_profile(
                    profile_url,
                    company_name
                )

                records.append(record)

            except requests.RequestException as error:
                print(
                    f"Unable to process {profile_url}: {error}"
                )

    finally:
        driver.quit()

    if records:

        df = clean_records(records)

        export_results(df)

        print(
            f"Exported {len(df)} loan officer records."
        )

    else:
        print("No loan officer records were collected.")


if __name__ == "__main__":
    main()
