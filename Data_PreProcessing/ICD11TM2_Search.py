import pandas as pd
import time
import unidecode
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Input and output Excel files
input_excel = r"C:\Users\ATHARVA M JOSHI\Desktop\IMP files\NATIONAL SIDDHA MORBIDITY CODES.xls"
output_excel = r"C:\Users\ATHARVA M JOSHI\Desktop\IMP files\icd_results.xlsx"

# Read Excel
df = pd.read_excel(input_excel)

# Setup Selenium Chrome 
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://icd.who.int/browse/2025-01/mms/en")

# Wait for the search box
search_box = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ctw-input.embeddedBrowserSearchbox"))
)

# Add columns for ICD results
df['ICD_Code'] = ''
df['ICD_Title'] = ''

# Loop through each term
for index, row in df.iterrows():
    term = str(row['NAMC_TERM']).strip()
    term_ascii = unidecode.unidecode(term)  # Transliterate to ASCII
    print(f"Searching: {term_ascii}")

    try:
        # Clear and type slowly to trigger autocomplete
        search_box.clear()
        for char in term_ascii:
            search_box.send_keys(char)
            time.sleep(0.1)

        # Wait for the dropdown suggestions
        top_suggestion = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.entityInList"))
        )

        # Click the top suggestion using JavaScript
        driver.execute_script("arguments[0].click();", top_suggestion)

        # Wait for ICD code and title to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".entityTitle .entityTitlePointer"))
        )

        # Get ICD code and title
        code_elem = driver.find_element(By.CSS_SELECTOR, ".entityTheCode span")
        title_elem = driver.find_element(By.CSS_SELECTOR, ".entityTitle .entityTitlePointer")
        df.at[index, 'ICD_Code'] = code_elem.text.strip()
        df.at[index, 'ICD_Title'] = title_elem.text.strip()
        print(" → Found:", code_elem.text.strip(), "|", title_elem.text.strip())

        time.sleep(1)

    except:
        print(" → No suggestions / result found")
        time.sleep(1)

    # Save progress every 20 rows
    if (index + 1) % 20 == 0:
        df.to_excel(output_excel, index=False)
        print(f"Progress saved after {index + 1} terms.")

# Save final results
df.to_excel(output_excel, index=False)
driver.quit()
print(f"Done! Results saved in {output_excel}")
