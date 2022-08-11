import pandas as pd
from data import Data


class Data_filter:

    def __init__(self, dataset_name, list_gender=None, list_sec=None, list_level=None, list_exp=None, list_sub=None,
                 min_sub=0, status_sub=True):
        self.status_sub = status_sub
        self.min_sub = min_sub
        self.list_sub = list_sub
        self.list_exp = list_exp
        self.list_level = list_level
        self.list_sec = list_sec
        self.list_gender = list_gender
        self.dataset_origin = Data(dataset_name).data
        self.dataset = Data(dataset_name).data
        self.save = ''
        self.edit_data()

    def edit_data(self):
        """modify all your data"""
        self.dataset = self.filter_gender(self.list_gender)

        self.dataset = self.filter_group_sec(self.list_sec)

        self.dataset = self.filter_level_edu(self.list_level)

        self.dataset = self.filter_exp_code(self.list_exp)

        self.dataset = self.filter_subject(self.list_sub, self.min_sub, self.status_sub)

    def filter_gender(self, chose):
        """filter your data by dataframe will show specific gender that you chose"""
        data = pd.DataFrame(self.dataset)
        if chose is None or chose == []:
            chose = ["male",
                     "female"
                     ]
        new_data = data[data['gender'].isin(chose)]
        return new_data

    def filter_group_sec(self, list_sec=None):
        """filter your data by dataframe will show specific group_sec that you chose"""
        data = pd.DataFrame(self.dataset)
        if list_sec is None or list_sec == []:
            list_sec = ['group A',
                        'group B',
                        'group C',
                        'group D',
                        'group E'
                        ]
        new_data = data[data['group_sec'].isin(list_sec)]
        return new_data

    def filter_level_edu(self, list_level=None):
        """filter your data by dataframe will show specific are group parental level of education that you chose"""
        data = pd.DataFrame(self.dataset)
        if list_level is None or list_level == []:
            list_level = [" bachelor's degree ",
                          " some college ",
                          " master's degree ",
                          " associate's degree ",
                          " high school ",
                          " some high school "
                          ]

        new_data = data[data[' parental level of education '].isin(list_level)]
        return new_data

    def filter_exp_code(self, chose=None):
        """filter your data by dataframe will show specific Experienced in writing code that you want to know"""
        data = pd.DataFrame(self.dataset)
        if chose is None or chose == []:
            chose = ["none",
                     "completed"]
        new_data = data[data['Experienced in writing code'].isin(chose)]
        return new_data

    def filter_subject(self, list_subject_name=None, min_point=0, more_point=True):
        """return all score of subject that you chose, and it can show score that more that you determine"""
        self.save = pd.DataFrame(self.dataset)
        if list_subject_name is None or list_subject_name == []:
            list_subject_name = ["discrete math score",
                                 "writing score",
                                 "engineer math score",
                                 "physic score",
                                 "computer programing score"]

        if "discrete math score" in list_subject_name:

            if more_point:
                self.save = self.save[self.save["discrete math score"] >= min_point]
            elif not more_point:
                self.save = self.save[self.save["discrete math score"] <= min_point]
        if "writing score" in list_subject_name:

            if more_point:
                self.save = self.save[self.save["writing score"] >= min_point]
            elif not more_point:
                self.save = self.save[self.save["writing score"] <= min_point]
        if "engineer math score" in list_subject_name:

            if more_point:
                self.save = self.save[self.save["engineer math score"] >= min_point]
            elif not more_point:
                self.save = self.save[self.save["engineer math score"] <= min_point]
        if "physic score" in list_subject_name:

            if more_point:
                self.save = self.save[self.save["physic score"] >= min_point]
            elif not more_point:
                self.save = self.save[self.save["physic score"] <= min_point]

        if "computer programing score" in list_subject_name:

            if more_point:
                self.save = self.save[self.save["computer programing score"] >= min_point]
            elif not more_point:
                self.save = self.save[self.save["computer programing score"] <= min_point]
        new_data = self.save
        return new_data

        #     lst_all = main + list_subject_name
        #     new_data = pd.DataFrame(self.dataset, columns=lst_all)
        #     if min_point is not None:
        #         if more_point:
        #             for sub in list_subject_name:
        #                 new_data = new_data[new_data[sub] >= min_point]
        #         elif not more_point:
        #             for sub in list_subject_name:
        #                 new_data = new_data[new_data[sub] <= min_point]
        # else:
        #     lst_all = main + list_subject_name
        #     new_data = pd.DataFrame(self.dataset[lst_all])
        # return new_data

# list_ = ['discrete math score', 'writing score', 'engineer math score', 'physic score', 'computer programing score']

# x = Data_filter("StudentsPerformance_n.csv",
#                 list_gender=['male'],
#                 list_sec=["group B", "group C"],
#                 list_level=[" some college ", " master's degree "],
#                 list_sub=["discrete math score", "writing score"],
#                 min_sub=50,
#                 status_sub=True
#                 )
# x = Data_filter("StudentsPerformance_n.csv",
#                 list_gender=[],
#                 list_sec=[],
#                 list_level=[],
#                 list_sub=["discrete math score", "writing score"],
#                 min_sub=50,
#                 status_sub=True
#                 )
# print(x.dataset.iloc[:,9])
# x = Data_filter("StudentsPerformance_n.csv",
#                 list_gender=[],
#                 list_sec=[],
#                 list_level=[],
#                 list_sub=[],
#                 min_sub=0,
#                 status_sub=True
#                 )
# print(x.dataset)
