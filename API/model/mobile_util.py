from API import db
from API.Tables.User import User


class MobileUtil:
    def __init__(self):
        pass

    def register_user(self, payload=None) -> bool:
        """
        This method is to register the user in our database
        Args:
            payload: payload for registration of the end user
                e.g.:-

        Returns: status of registration
            e.g.:- True/False
        """
        result = True
        try:
            usr_tbl = User(first_name=payload['first_name'],
                           last_name=payload['last_name'],
                           mobile=payload['mobile'],
                           email=payload['email'],
                           gender=payload['gender'],
                           pincode=payload['pincode'],
                           city=payload['city'],
                           state=payload['state'])
            db.session.add(usr_tbl)
            db.session.commit()
        except Exception as error:
            result = False
        return result

