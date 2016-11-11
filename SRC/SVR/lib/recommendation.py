#!/usr/python3


# import numpy as np

class recommend(object):
    def __init__(self, database):
        self.db = database

    def update_train_set(self):
        user_item = self.db.user_get_all()
        self.train = dict()
        for user, item in user_item:
            if None == self.train.get(user):
                self.train[user] = list()

            self.train[user] += item

        for user, items in self.train.items():
            print(user, ':', items)

    def update_item_similarity(self):
        C = dict()
        N = dict()

        for user, items in self.train.items():
            for i in items:
                if None == N.get(i):
                    N[i] = 0
                N[i] += 1
                for j in items:
                    if i == j:
                        continue
                    if None == C.get(i):
                        C[i] = dict()
                    if None == C[i].get(j):
                        C[i][j] = 0
                    C[i][j] += 1
        print(C)

    def recommendation(self, user_id, K):
        pass


if __name__ == '__main__':
    print('Run By Server.')
