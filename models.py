# models.py
class EmailViewModel:
    def __init__(self, user_name, sender_name, user_data1, user_data2):
        self.user_name = user_name
        self.sender_name = sender_name
        self.user_data1 = user_data1
        self.user_data2 = user_data2
