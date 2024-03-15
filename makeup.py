import urllib.parse, urllib.request, urllib.error, json

def get_makeup_data(type_of_product):
    paramstr = urllib.parse.urlencode({'product_type': type_of_product})
    baseurl = 'http://makeup-api.herokuapp.com/api/v1/products.json'
    url = (baseurl + '?' + paramstr)
    return json.loads(urllib.request.urlopen(url).read())

def safe_get(url):
    try:
        makeup_request = (url)
        with urllib.request.urlopen(makeup_request) as response:
            make_up_str = response.read()
        return json.loads(make_up_str)
    except urllib.error.URLError as exceptions:
        print(f"Error: {exceptions}")
        return None

def makeup_info(makeup_data, wanted_tag=None):
    results = []
    if makeup_data:
        for product in makeup_data:
            product_info = {
                'Name': product['name'],
                'Brand': product['brand'],
                'Product Type': product['product_type'],
                'category': product['category'],
                'Image': product['image_link']

            }


            price = product['price_sign']
            if price:
                product_info['Price'] = f"{product['price_sign']} {product['price']} {product['currency']}"
            elif product['currency']:
                product_info['Price'] = f"{product['price']} {product['currency']}"
            else:
                product_info['Price'] = f"{product['price']}"


            product_info['Link'] = f"{product['product_link']}"
            product_info['Description'] = f"{product['description']}"

            tags = product['tag_list']
            if tags:
                if wanted_tag:
                    if wanted_tag in tags:
                        product_info["tags"] = ', '.join(tags)
                        results.append(product_info)
                else:
                    product_info["tags"] = ', '.join(tags)
                    results.append(product_info)
            else:
                product_info["tags"] = "No tags"

        return results

