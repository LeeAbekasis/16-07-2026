print('welcome to the movie rating progrem! please enter your ratings (1-5). type -1 to finish.')
valid_ratings = 0
low_rate = (1-2)
medium_rate = (3)
high_rate = (4-5)
while True:
    rating = int(input('Enter rating: '))
    if rating == -1:
        break
    if not 1 <= int(rating) <= 5:
        print('invalid rating')
        continue
    if rating <= 2:
        low_rate += 1
        continue
    elif rating == 3:
        medium_rate = rating
        continue
    elif rating == 4:
        high_rate += 1
        continue
print('total ratings: ', low_rate + medium_rate + high_rate)