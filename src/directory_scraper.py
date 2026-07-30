"""
Mortgage Directory Automation
Author: Isabel Munguia

Sanitized portfolio example demonstrating the general workflow used
to collect publicly available directory information.

This example uses fictional selectors and URLs and does not contain
customer-specific code, data, or production configuration.
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
    Discover employee profile links from a directory page.

    Selectors are intentionally generic for portfolio purposes.
    """

    driver.get(directory_url)
    time.sleep(2)

    profile_links = []

    elements = driver.find_elements(By.CSS_SELECTOR, "a.employee-profile")

    for element in elements:
        link = element.get_attribute("href")

        if link:
            profile_links.append(link)

    return profile_links


def parse_profile(profile_url):
    """
    Retrieve and parse a directory profile.

    This portfolio version returns a simplified data structure.
    """

    response = requests.get(
        profile_url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    name_element = soup.select_one(".employee-name")
    title_element = soup.select_one(".employee-title")
    location_element = soup.select_one(".employee-location")

    return {
        "name": name_element.get_text(strip=True) if name_element else None,
        "job_title": title_element.get_text(strip=True) if title_element else None,
        "location": location_element.get_text(strip=True) if location_element else None,
    }


def clean_records(records):
    """Convert extracted records into a clean Pandas DataFrame."""

    df = pd.DataFrame(records)

    df.drop_duplicates(inplace=True)

    df.fillna("Not Available", inplace=True)

    return df


def export_results(df, filename="directory_results"):
    """Export structured results to CSV and Excel."""

    df.to_csv(
        f"{filename}.csv",
        index=False
    )

    df.to_excel(
        f"{filename}.xlsx",
        index=False
    )


def main():

    # Fictional demonstration URL
    directory_url = "https://example.com/employees"

    driver = create_driver()

    records = []

    try:
        profile_links = collect_profile_links(
            driver,
            directory_url
        )

        print(
            f"Discovered {len(profile_links)} profile links."
        )

        for profile_url in profile_links:

            try:
                record = parse_profile(profile_url)

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
            f"Exported {len(df)} records."
        )

    else:
        print("No records were collected.")


if __name__ == "__main__":
    main()
