import pandas as pd
import time
from PyQt5.QtWidgets import QMessageBox


class Record:
    def __init__(self, row_id, comment='', teacher_answer='', super_answer='', task='', new_answer=''):
        self.row_id = row_id
        self.comment = comment
        self.teacher_answer = teacher_answer
        self.super_answer = super_answer if str(super_answer) != 'nan' else ''
        self.task = task.replace('\\"', '"')
        if "```\n```" in self.task:
            t = self.task.split("```\n```")[1].strip()
            self.code = t.split('\n')
        elif "```" in self.task:
            t = self.task.split("```")[1].strip()
            self.code = t.split('\n')
        else:
            self.code = ['код не распознан']
        # self.code = self.code.replace('\"', '"')
        self.new_answer = new_answer if str(new_answer) != 'nan' else ''
        self.changed = False

    def get_row(self):
        return [
            str(self.row_id),
            self.comment,
            self.teacher_answer,
            "" if str(self.super_answer) == 'nan' else str(self.super_answer),
            self.task,
            "" if str(self.new_answer) == 'nan' else str(self.new_answer)
        ]

    def __str__(self):
        return '\n'.join(self.get_row())


class Dataframe:
    def __init__(self):
        self.filename = None
        self.main_df = None
        self.current_df = None
        self.current_row = None
        self.rows_list = None
        self.headers = {
            'RowID': 'RowID',
            'comment': 'Комментарий',
            'teach_ans': 'answer',
            'super_ans': 'super_answer',
            'task': 'задача',
            'new_ans': 'Новый ответ'
        }
        self.all_records = []

    def set_filename(self, name):
        self.filename = name

    def get_comments(self):
        if self.main_df is not None:
            self.current_df = self.main_df[self.main_df[self.headers['comment']].notna()]
            comms = set()
            for i, row in self.current_df.loc[:, [self.headers['comment']]].iterrows():
                comms.add(f"{row[self.headers['comment']]}")
            return sorted(list(comms))

    def get_rows_by_comment(self, comment):
        if self.main_df is not None:
            self.current_df = self.main_df[self.main_df[self.headers['comment']] == comment]
            self.rows_list = []
            for i, row in self.current_df.loc[:, ['RowID']].iterrows():
                self.rows_list.append(f"{row['RowID']}")
            return self.rows_list

    def get_all_records(self, refresh=True):
        if not refresh:
            return self.all_records
        self.current_df = self.main_df[self.main_df[self.headers['comment']].notna()]
        self.all_records.clear()
        for index, row in self.current_df.iterrows():
            new_rec = Record(row[self.headers['RowID']],
                             row[self.headers['comment']],
                             row[self.headers['teach_ans']],
                             row[self.headers['super_ans']],
                             row[self.headers['task']],
                             row[self.headers['new_ans']]
                             )
            self.all_records.append(new_rec)
        return self.all_records

    def set_answer(self, row, answer):  # 42476
        if self.main_df is not None:
            self.main_df.loc[self.main_df['RowID'] == int(row), [self.headers['new_ans']]] = answer

    def save_record(self, record):
        self.main_df.loc[self.main_df['RowID'] == int(record.row_id), [self.headers['new_ans']]] = record.new_answer
        new_filename = self.filename.replace('.xlsx', '-auto.xlsx')
        self.main_df.to_excel(new_filename, sheet_name='Лист1', index=False)


    def open(self):
        self.main_df = pd.read_excel(self.filename, sheet_name='Лист1',
                                     converters={self.headers['new_ans']: str})

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
