class Account:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def get_account_info(self):
        file = open(self.file_path, 'r')
        
        acc_info = file.read()
        acc_info = acc_info.split(':')

        file.close()
        return acc_info