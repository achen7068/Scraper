from bs4 import BeautifulSoup
import requests
import csv


page = requests.get(
    'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# Extract first <h1>(...)</h1>text
first_h1 = soup.select('h1')[0].text

# Create all_h1_tags as empty list
all_h1_tags = []

# Set all_h1_tags to all h1 tags of the soup
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# Create seventh_p_text and set it to 7th element text of the page
seventh_p_text = soup.select('p')[6].text

#print(all_h1_tags, seventh_p_text)


# Create top_items as empty list
top_items = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        'title': title.strip(),
        'review': review_label.strip()
    }
    top_items.append(info)

# print(top_items)

# Create image_data as a empty list
image_data = []

# Extract and store in image_data according to instructions on the left
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_data.append({'src': src, 'alt': alt})

# print(image_data)

# Create all_links as empty link
all_link = []

# Extract and store in all_link according to intructions on the left
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_link.append({'href': href, 'text': text})

# print(all_link)

# Create all_products as empty list
all_products = []

# Extract and store in all_products according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        'name': name,
        'description': description,
        'price': price,
        'review': reviews,
        'image': image
    })

keys = all_products[0].keys()

with open('product.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)

txt = page.text
status = page.status_code

#print(txt, status)
