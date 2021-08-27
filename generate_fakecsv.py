"""
+Full name (a combination of first name and last name)
Job
Email
Domain name
Phone number
Company name
Text (with specified range for a number of sentences)
Integer (with specified range)
Address

"""
from faker import Faker
import pandas as pd


class gen_csv:
    def __init__(self, rows_num, rows):
        self.fake = Faker()
        self.rows_num = rows_num
        self.rows = rows

    def gen_res(self):
        result = {}
        for i in self.rows:
            if i == 'name': result['name'] = self.name()
            if i == 'job': result['job'] = self.job()
        return result
    def to_frame(self):
        return pd.DataFrame.from_dict(self.gen_res())
    def to_csv(self):
        return self.to_frame().to_csv('./media.csv')
    def name(self):
        return [self.fake.name() for _ in range(self.rows_num)]

    def job(self):
        return [self.fake.job() for _ in range(self.rows_num)]


a = gen_csv(5, ['name', 'job']).to_csv()
print(a)
