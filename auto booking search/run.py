from booking.booking import Booking


# with Booking() as bot:
#     try:    
#         bot.land_first_page()
#         # bot.change_currencry(currency="USD")
#         bot.select_place_to_go(place="goa")
#         bot.select_dates(checkin_date="2024-06-10", checkout_date="2024-06-15")
#         # bot.select_adults(count='5')
#         bot.click_search()
#         # bot.apply_star_rating(star=4)
#         # bot.sort_lowest_to_highest()
#         # bot.refresh()
#         bot.report_results()
        
#     except Exception as e:
#         if 'in PATH' in str(e):
#             print("Someting went wrong in PATH \n"
#                   "Please read the Readme.txt"
#             )    
#         else:
#             raise
        
# to give custtom input
with Booking() as bot:
    try:    
        bot.land_first_page()
        # bot.change_currencry(currency="USD")
        bot.select_place_to_go(input("Where you wanna go: "))
        bot.select_dates(checkin_date=input("checkin date: "), checkout_date=input("checkout date: "))
        bot.select_adults(count=input("no of adults: "))
        bot.click_search()
        bot.apply_star_rating(star=input("how many stars: "))
        bot.sort_lowest_to_highest()
        # bot.refresh()
        bot.report_results()
        
    except Exception as e:
        if 'in PATH' in str(e):
            print("Someting went wrong in PATH \n"
                  "Please read the Readme.txt"
            )    
        else:
            raise