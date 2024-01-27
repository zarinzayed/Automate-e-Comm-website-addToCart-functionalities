from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver
driver = webdriver.Chrome()  # Change this to the appropriate web driver if needed
driver.maximize_window()

# Navigate to the login page
driver.get("https://www.saucedemo.com/")

# Perform login
username = "standard_user"
password = "secret_sauce"

username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "user-name"))
)
username_field.send_keys(username)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Verify successful login
inventory_page_title = WebDriverWait(driver, 10).until(
    EC.title_contains("Swag Labs")
)

if "Swag Labs" in driver.title:
    print("Login successful!")
else:
    print("Login failed.")

# Perform search functionality
search_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "search-box"))
)
search_field.send_keys("backpack")

search_button = driver.find_element(By.ID, "search-button")
search_button.click()

# Verify search results
search_results = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
if len(search_results) > 0:
    print("Search results found.")
else:
    print("No search results found.")

# Add item to cart
add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
add_to_cart_button.click()

# Verify item added to cart
cart_badge = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
)
cart_items_count = int(cart_badge.text)

if cart_items_count > 0:
    print(f"Item added to cart. Cart count: {cart_items_count}")
else:
    print("Item not added to cart.")

# Close the browser
driver.quit()
