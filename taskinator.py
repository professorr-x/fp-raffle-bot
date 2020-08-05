import pandas as pd

class Dataframe:

    task = {}

    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def createTaskObj(self):
        for i in range(self.df.shape[0]):
            self.task['task_' + str(i)] = {}
            self.task['task_' + str(i)]['rafflesID'] = self.df['rafflesID'][i]
            self.task['task_' + str(i)]['firstName'] = self.df['firstName'][i]
            self.task['task_' + str(i)]['lastName'] = self.df['lastName'][i]
            self.task['task_' + str(i)]['email'] = self.df['email'][i]
            self.task['task_' + str(i)]['paypalEmail'] = self.df['paypalEmail'][i]
            self.task['task_' + str(i)]['mobile'] = self.df['mobile'][i]
            self.task['task_' + str(i)]['dateofBirth'] = self.df['dateofBirth'][i]
            self.task['task_' + str(i)]['shoeSize'] = self.df['shoeSize'][i]
            self.task['task_' + str(i)]['address1'] = self.df['address1'][i]
            self.task['task_' + str(i)]['address2'] = self.df['address2'][i]
            self.task['task_' + str(i)]['city'] = self.df['city'][i]
            self.task['task_' + str(i)]['county'] = self.df['county'][i]
            self.task['task_' + str(i)]['postCode'] = self.df['postCode'][i]
            self.task['task_' + str(i)]['siteCode'] = self.df['siteCode'][i]
        return self.task
