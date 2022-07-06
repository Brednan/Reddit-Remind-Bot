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
