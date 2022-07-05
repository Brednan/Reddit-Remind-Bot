import dateutil.parserfrom praw import Redditfrom praw import modelsfrom account import Accountimport dateutil.parser as parserimport datetimefrom comment_list_handler import ListHandlerclass Bot(Reddit, Account, ListHandler):    def __init__(self, account_path):        self.active = True        ListHandler.__init__(self)        Account.__init__(self, account_path)        account = self.get_account_info()        Reddit.__init__(            self,            client_id=account[2],            client_secret=account[3],            username=account[0],            password=account[1],            user_agent='windows reddit remind bot',        )    def bot_sequence(self):        mentions = self.inbox.mentions()        for mention in mentions:            self.handle_mention(mention)    def handle_mention(self, mention):        specified_date = self.get_specified_date(mention)        self.check_if_date_is_valid(specified_date)        comment_id = mention.id        if specified_date:            if type(specified_date) == dateutil.parser.ParserError:                reply_msg = f'There was an error parsing the date you specified! : {str(specified_date)}'            elif type(specified_date) == datetime.datetime:                author = mention.author                date_valid = self.check_if_date_is_valid(specified_date)                if date_valid:                    reply_msg = f'Hello u/{author}, on {str(specified_date)}, I will remind you about this comment!'                    print(reply_msg)                else:                    reply_msg = f'Hello u/{author}, the date that you specified is invalid! Please try again.'                    print(reply_msg)        else:            author = mention.author            reply_msg = f'Hello u/{author}, There was an error parsing the date that you specified! Please try again.'        self.add_to_ignore_list(comment_id)    def get_specified_date(self, comment: models.Comment):        try:            content = comment.body            content = content.split(' ')        except:            print('Error parsing comment')            return None        else:            try:                date_str = f'{content[1]} {content[2]}'                date = parser.parse(date_str, yearfirst=True)                return date            except parser.ParserError as e:                return e    def check_if_should_remind(self, specified_date):        current_date = datetime.datetime.now()        current_date = current_date.strftime('%Y/%m/%d %H:%M')        current_date = parser.parse(str(current_date))        if current_date == specified_date:            return True        else:            return False    def check_if_date_is_valid(self, date: datetime.datetime):        current_date = datetime.datetime.now()        current_date = current_date.strftime('%Y/%m/%d %H:%M')        current_date = parser.parse(current_date)        if date.year < current_date.year:            return False        elif date.month < current_date.month:            return False        elif date.day < current_date.day:            return False        elif date.hour < current_date.hour:            return False        elif date.minute < current_date.minute:            return False        else:            return True