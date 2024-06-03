from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currencry(currency="USD")
    bot.select_place_to_go(place="New York")