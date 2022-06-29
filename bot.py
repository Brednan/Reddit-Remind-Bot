from praw import Reddit
from account import Account


class Bot(Reddit, Account):
    def __init__(self, account_path):
        Account.__init__(self, account_path)

        account = self.get_account_info()
        
        Reddit.__init__(
            self,
            client_id=account[2],
            client_secret=account[3],
            username=account[0],
            password=account[1],
            user_agent='windows reddit remind bot',
        )

bot = Bot('./account.txt')