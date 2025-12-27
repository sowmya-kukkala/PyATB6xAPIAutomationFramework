# API Constants -> Class which contain all the endpoints

# Restful Booker API -> /booking, /booking/id, /auth, /ping

class APIConstants:

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # Update -> PUT, PATCH, DELETE - bookingid
    def url_patch_put_delete(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+str(bookingid)
