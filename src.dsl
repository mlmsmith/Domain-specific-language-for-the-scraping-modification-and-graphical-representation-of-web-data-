SCRAPE
team: 'td.name'(clean, upper),
year: 'td.year'(clean),
wins: 'td.wins'(clean, int),
losses: 'td.losses'(clean, float)
FROM 'https://www.scrapethissite.com/pages/forms/?per_page=25'
RESPONSE = 'tr.team'
WHERE [team] = 'New Jersey Devils'
OR [team] = 'ST. LOUIS BLUES'
OR [team] = 'WINNIPEG JETS'
OR [team] = 'CHICAGO BLACKHAWKS'
OR [team] = 'MONTREAL CANADIENS'
OR [team] = 'NEW YORK ISLANDERS'
PLOT
CATS = (team),
VARS = (wins, losses)







