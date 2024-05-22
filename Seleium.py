from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Flipkart website
driver.get("https://www.flipkart.com")
driver.maximize_window()

# Close the login popup if it appears
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_button.click()
except:
    pass

# Search for "iPhone 15 Pro Max"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("iphone 15 pro max")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(3)

# Print the main page handle
main_page = driver.current_window_handle
print("Main page =", main_page)

# Click on the specific product link
driver.find_element(By.XPATH, "//div[contains(text(),'Apple iPhone 15 Pro Max (Blue Titanium, 256 GB)')]").click()

# Wait for the new window/tab to open
time.sleep(3)

# Switch to the new window/tab
all_pages = driver.window_handles
for page in all_pages:
    if page != main_page:
        driver.switch_to.window(page)
        break

# Print the current URL of the new page
print(driver.current_url)

# Get the list of products (this part may vary depending on the actual page structure)
products = driver.find_elements(By.CLASS_NAME, "_21Ahn-")
print(len(products))
for product in products:
    print(product.text)

# Wait for the pincode input field to load
time.sleep(3)

# Enter the delivery pincode
pincode_input = driver.find_element(By.ID, "pincodeInputId")
pincode_input.clear()  # Clear any existing value in the input field
pincode_input.send_keys("335001")  # Enter the desired pincode

# Delay to ensure pincode is entered properly
time.sleep(2)

# Locate and click the "Check" button
check_button = driver.find_element(By.XPATH, "//span[contains(text(),'Check')]")
check_button.click()

time.sleep(5)
# Close the driver
driver.quit()
