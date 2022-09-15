CRAWL
brand: 'div.vendor a'(clean, text),
name: 'h1.title'(clean, text),
price: 'span.price'(clean, text)
FROM 'http://sipwhiskey.com/'
DOMAIN = 'sipwhiskey.com'
RULES = [{allow: 'collections/japanese-whisky', deny: 'products'}, {allow: 'products', callback: 'parse_item'}]