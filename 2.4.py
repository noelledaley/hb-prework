#  The volume of a sphere with radius r is 4/3 pi r3. What is the volume of a sphere with radius 5?

pi = 3.1415926535897931
radius = 5
volume = (4.0/3.0)*(pi*(radius**3))

print volume

#  Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

cover = 24.95
bookstorePrice = 24.95*0.60
shipping = 3.0
shippingNext = 0.75
total = 60
wholesale = bookstorePrice * total + shipping + (shippingNext*(total - 1))

print wholesale

#  If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

startTime = 6 + 52 / 60.0
easyPace = (8 + 15 / 60.0) / 60.0
tempoPace = (7 + 12 / 60.0) / 60.0
timeRunning = 2 * easyPace + 3 * tempoPace
breakfastHours = startTime + timeRunning
breakfastMins = breakfastHours*60
breakfastSec = breakfastMins*60

print int(breakfastHours), int(breakfastMins), int(breakfastSec)
