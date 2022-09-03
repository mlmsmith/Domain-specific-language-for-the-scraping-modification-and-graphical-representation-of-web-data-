SCRAPE
name: 'a'(clean, text),
price: 'p.price.larger'(clean, float)
FROM 'http://jessops.com/drones/'
RESPONSE = 'div.details-pricing'
WHERE [price] > 1000
