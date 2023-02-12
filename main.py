from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# Set up the options for the Chrome driver
options = Options()
options.headless = True

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Kelangit Hakim\Downloads\chromedriver_win32\chromedriver.exe")

# Open the Twitter page
driver.get("https://twitter.com/OhitzChloe28/status/1624517632991932417")

# Find the video element on the page
video_element = driver.find_element_by_css_selector("video")

# Get the video URL from the source attribute of the video element
video_url = video_element.get_attribute("src")

# Download the video
response = requests.get(video_url)

# Save the video to a file
with open("video.mp4", "wb") as f:
    f.write(response.content)

# Close the browser
driver.quit()
