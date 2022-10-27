# Programmer:KC
# Helped By: Kaylee

# Ask the user about their site
page_views = input("How many pageviews will your site have? ")
snap_shots = input("How many snapshots will you need? ")
recordings = input("How many recordings will you need? ")
print("")

#this will convert the number to a integer or whole number
page_views = int(page_views)
snap_shots = int(snap_shots)
recordings = int(recordings)

#This part will give the user's need based on the inputs
if page_views < 0 or snap_shots < 0 or recordings < 0:
    print("These values can't be negative")
elif page_views < 500000 or snap_shots < 100 or recordings < 5000:
    print("You should subscribe to our BASIC tier")
    print("The cost is $24 per month")
elif page_views > 150000 or snap_shots > 75 or recordings > 1000:
    print("You should subscribe to our PRO tier")
    print("The cost is $249 per month")
elif page_views < 75000 or snap_shots > 50 or recordings > 500:
    print("You should subscribe to our PLUS tier")
    print("The cost is $99 per month")
elif page_views < 30000 or snap_shots > 25 or recordings > 100:
    print("You should subscribe to our STANDARD tier")
    print("The cost is $49 per month")
else:
    print("You should subscribe to our ENTERPRISE tier")
    print("Contact us for a quote")
