import pandas as pd
import time


class Record:
    def __init__(self, row_id, comment='', teacher_answer='', super_answer='', task='', new_answer=''):
        self.row_id = row_id
        self.comment = comment
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
        self.headers = {
            'RowID': 'RowID',
            'comment': 'КОММЕНТАРИЙ',
            'teach_ans': 'ответ тренера',
            'super_ans': 'ответ супера',
            'task': 'Задание удобным видом',
            'new_ans': 'НОВЫЙ ОТВЕТ'
        }
        self.all_records = []

    def set_filename(self, name):
        self.filename = name

    def get_comments(self):
        if self.main_df is not None:
            self.current_df = self.main_df[self.main_df[self.header['comment']].notna()]
            comms = set()
            for i, row in self.current_df.loc[:, [self.header['comment']]].iterrows():
                comms.add(f"{row[self.header['comment']]}")
            return sorted(list(comms))

    def get_rows_by_comment(self, comment):
        if self.main_df is not None:
            self.current_df = self.main_df[self.main_df[self.header['comment']] == comment]
            self.rows_list = []
            for i, row in self.current_df.loc[:, ['RowID']].iterrows():
                self.rows_list.append(f"{row['RowID']}")
            return self.rows_list

    def get_all_records(self, refresh=True):
        if not refresh:
            return self.all_records
        self.current_df = self.main_df[self.main_df[self.header['comment']].notna()]
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
            self.main_df.loc[self.main_df['RowID'] == int(row), [self.header['new_ans']]] = answer

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
