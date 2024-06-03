from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currencry(currency="USD")
    bot.select_place_to_go(place="sangli")
    bot.select_dates(checkin_date="2024-06-10", checkout_date="2024-06-15")
    bot.select_adults(count='5')
    bot.click_search()