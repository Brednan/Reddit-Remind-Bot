import json


class ListHandler:
    def __init__(self):
        self.comments_to_notify_path = './comments_to_notify.json'
        self.comments_to_ignore_path = './comments_to_ignore.json'

    def add_to_ignore_list(self, comment_id):
        ignore_file_read = open(self.comments_to_ignore_path, 'r')
        ignore_list: list = json.load(ignore_file_read)

        ignore_list.append(comment_id)

        ignore_file_read.close()

        ignore_file_write = open(self.comments_to_ignore_path, 'w')

        json.dump(ignore_list, ignore_file_write)

        ignore_file_write.close()

    def check_comment_ignore(self, comment_id):
        """
        This function will take a comment id, and go through the list of comments that are to be ignored.
        If it is already in the list, then the function will return True. Otherwise, it returns false.
        """

        file = open(self.comments_to_ignore_path, 'r')

        ignore_list = json.load(file)

        file.close()

        for ignore_comment_id in ignore_list:
            if comment_id == ignore_comment_id:
                return True

        return False

    def add_to_notify_list(self, comment_id, date):
        notify_list_file = open(self.comments_to_notify_path, 'r')
        notify_list: list = json.load(notify_list_file)
        notify_list_file.close()

        comment_ = {
            "comment_id": comment_id,
            "date": str(date)
        }

        if comment_ not in notify_list:
            notify_list.append(comment_)

        notify_list_file_out = open(self.comments_to_notify_path, 'w')

        json.dump(notify_list, notify_list_file_out)

        notify_list_file_out.close()

    def get_notify_list(self):
        notify_list_file = open(self.comments_to_notify_path, 'r')

        notify_list = json.load(notify_list_file)

        notify_list_file.close()

        return notify_list

    def remove_from_notify_list(self, comment_to_remove):
        notify_list: list = self.get_notify_list()

        notify_list = [i for i in notify_list if not i['comment_id'] == comment_to_remove['comment_id']]

        to_notify_file = open(self.comments_to_notify_path, 'w')

        json.dump(notify_list, to_notify_file)

        to_notify_file.close()
