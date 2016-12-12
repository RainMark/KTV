#!/usr/python3

import math
import operator

class recommend(object):
    def __init__(self, database):
        self.db = database

    def train_set(self):
        user_item = self.db.user_get_all()
        self.train = dict()
        for user, item in user_item:
            # print(user, type(user), item, type(item))
            if None == self.train.get(user):
                self.train[user] = list()
            self.train[user].append(item)

        # for user, items in self.train.items():
        #     print(user, ':', items)

    def item_similarity(self):
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
        W = dict()
        for item, related_items in C.items():
            # print(related_items)
            for related_item, Cij in related_items.items():
                # print(Cij)
                if None == W.get(item):
                    W[item] = dict()
                W[item][related_item] = Cij / math.sqrt(N[item] * N[related_item])

        # for i, j in W.items():
        #     print(i, ' ', j)
        self.sim = W

    def do_recommend(self, user_id, K):
        rk = dict()
        play_list= self.db.playing_list_fetch(user_id)
        CI = [item[0] for item in play_list]
        for i in CI:
            if None == self.sim.get(i):
                continue

            for j, Wij in sorted(self.sim[i].items(), key = operator.itemgetter(1), reverse = True)[:K]:
                if j in CI:
                    continue
                if None == rk.get(j):
                    rk[j] = Wij
                else:
                    rk[j] += Wij

        # ids = [it[0] for it in sorted(rk.items(), key = operator.itemgetter(1), reverse = True)] # No need to sort from here.
        ids = list(rk.keys())
        return self.db.song_fetch_by_ids(ids)

if __name__ == '__main__':
    print('Run By Server.')
