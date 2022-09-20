SCRAPE
team: 'td.name'(clean),
year: 'td.year'(clean),
wins: 'td.wins'(clean, int),
losses: 'td.losses'(clean)
FROM 'https://www.scrapethissite.com/pages/forms/?per_page=25'
RESPONSE = 'tr.team'
WHERE [team] = 'New Jersey Devils'
OR [team] = 'St. Louis Blues'
OR [team] = 'Winnipeg Jets'
OR [team] = 'Chicago Blackhawks'
OR [team] = 'Montreal Canadiens'
OR [team] = 'New York Islanders'
PLOT
CATS = (team)
VARS = (wins, losses)