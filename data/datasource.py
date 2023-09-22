import pandas as pd
import time


class Record:
    def __init__(self, row_id, teacher_answer='', super_answer='', task='', new_answer=''):
        self.row_id = row_id
        self.teacher_answer = teacher_answer
        self.super_answer = super_answer
        self.task = task
        if "```" in self.task:
            self.code = self.task.split("```")[1].split('\n')
        self.new_answer = new_answer


class Dataframe:
    def __init__(self):
        self.filename = None
        self.main_df = None
        self.current_df = None
        self.current_row = None
        self.rows_list = None

    def set_filename(self, name):
        self.filename = name

    def get_comments(self):
        if self.main_df is not None:
            self.current_df = self.main_df[self.main_df['КОММЕНТАРИЙ'].notna()]
            comms = set()
            for i, row in self.current_df.loc[:, ['КОММЕНТАРИЙ']].iterrows():
                comms.add(f"{row['КОММЕНТАРИЙ']}")
            return sorted(list(comms))

    def get_rows_by_comment(self, comment):
        if self.main_df is not None:
            self.current_df = self.main_df[self.main_df['КОММЕНТАРИЙ'] == comment]
            self.rows_list = []
            for i, row in self.current_df.loc[:, ['RowID']].iterrows():
                self.rows_list.append(f"{row['RowID']}")
            return self.rows_list

    def set_answer(self, row, answer):  # 42476
        if self.main_df is not None:
            self.main_df.loc[self.main_df['RowID'] == int(row), ['НОВЫЙ ОТВЕТ']] = answer

    def open(self):
        self.main_df = pd.read_excel(self.filename, sheet_name='Лист1')

    def save(self):
        if self.main_df is not None:
            new_filename = self.filename.replace('.xlsx', time.strftime("%Y%m%d-%H%M%S") + '.xlsx')
            self.main_df.to_excel(new_filename, sheet_name='Лист1', index=False)


if __name__ == '__main__':
    data = Dataframe()
    data.set_filename('Григорович.xlsx')
    data.open()
    # comments = data.get_comments()
    # print('\n'.join(comments))
    # rows = data.get_rows_by_comment('нужен пример кода')
    # print('\n'.join(rows))
    data.set_answer('42476', 'Тестовый ответ')
    data.save()
