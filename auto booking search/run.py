from booking.booking import Booking


with Booking() as bot:
    try:    
        bot.land_first_page()
        bot.change_currencry(currency="USD")
        bot.select_place_to_go(place="sangli")
        bot.select_dates(checkin_date="2024-06-10", checkout_date="2024-06-15")
        bot.select_adults(count='5')
        bot.click_search()
        bot.apply_star_rating(star=4)
        bot.sort_lowest_to_highest()
    except Exception as e:
        if 'in PATH' in str(e):
            print("Someting went wrong in PATH \n"
                  "Please read the Readme.txt"
            )    
        else:
            raise