"""
A module housing project constants, such as user credentials, urls and objects
"""


class UserCredentials:
    """Class housing the user related data"""
    EMAIL = 'TestCheckPointUser@gmail.com'
    EMAIL_INVALID = 'FakeUserEmail@gmail.com'
    EMAIL_WRONG_DOMAIN = 'FakeUserEmail@fake.com'
    PASSWORD = 'Abc123!!'
    PASSWORD_INVALID = 'FakePassword'


class WebPageUrl:
    """Class housing the Web page urls"""
    HOME_PAGE = 'https://workspace.google.com/intl/en-US/gmail/'
