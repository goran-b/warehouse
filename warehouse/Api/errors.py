from rest_framework.exceptions import NotFound


class Errors():

    @classmethod
    def throw_error_no_user(cls,username, user_response):
        if len(user_response) == 0:
            raise NotFound('User with username of ' +
                           username + ' was not found!')
