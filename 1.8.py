#  If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).

distance = 10
time = 43.50

paceKilo = (distance / time) * 60  # kilos per hour

paceMiles = paceKilo / 1.61

print paceMiles
