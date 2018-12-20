from user_model import User
from database_manager import MySqlManager
from tools_manager import counting

class AccountFileManager:
    def __init__(self, file_path, common_password, sql_manager):
        self._file_path = file_path
        self._common_password = common_password
        self._sql_manager =sql_manager

    def _read_account_file(self):
        with open(self._file_path, 'r') as file:
            for file_line in file.readlines():
                _, mail, username, region = file_line.strip().split(' ')
                user = User()
                user.Username = username
                user.Password = self._common_password
                user.Mail = mail
                user.Region = region
                yield user

    def add_account_to_sql(self):
        self._sql_manager.get_session()
        with self._sql_manager.short_session(), counting("账号管理") as (session, counter):
            for user in self._read_account_file():
                session.add(user)
                counter.incr()


if __name__ == '__main__':
    dm = MySqlManager()
    ac = AccountFileManager('accounts', 'Huang123', dm)
    ac.add_account_to_sql()