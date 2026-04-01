# Extract URL from string
import re

def extract_url(text):
    return re.findall(r'https?://\S+', text) # Regular expression to match URLs starting with http:// or https://


text = "Check https://example.com and http://test.com/page"
urls = extract_url(text) # Extract URLs from the given text

print(urls)    # ['https://example.com', 'http://test.com/page']