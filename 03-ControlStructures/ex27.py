Facebook = False
Twitter = False
Instagram = False

hasFacebook = str(input("Does the person have Facebbok? (Yes or No)"))
hasTwitter = str(input("Does the person have Twitter? (Yes or No)"))
hasInstagram = str(input("Does the person have Instagram? (Yes or No)"))

if hasFacebook == "Yes" :
 Facebook = True

if hasInstagram == "Yes" :
 Instagram = True

if hasTwitter == "Yes" :
 Twitter = True

if Facebook == True and Twitter == True or Facebook == True and Instagram == True or Instagram == True and Twitter == True:
 print(f"facebook = {Facebook}")
 print(f"twitter = {Twitter}")
 print(f"instagram = {Instagram}")
 print("A person can be a good influencer!")
else:
 print("A person cann`t be a good influencer :(")
 

