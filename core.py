
class CostMatrix:
    def get_cost(self, di, dj, ni, nj, A):
        # print(di, dj, ni, nj, A)
        ci1 = max(0, (A-di-dj)) * ((ni-di)/ni)
        ci2 = (ni-di)/ni
        ci3 = max(0, (nj-(A-di))) * (1/nj)
        ci4 = max(0, (di+dj-A)) * ((di/ni)/(di/ni+dj/nj))
        return round(ci1 + ci2 + ci3 + ci4, 1)

    def __init__(self, arr1, arr2, A_val):
        self.player1 = arr1
        self.player2 = arr2
        self.n1 = len(arr1)
        self.n2 = len(arr2)
        self.A = A_val
        self.cost_matrix = [[(0, 0) for i in range(len(self.player2))]
                            for j in range(len(self.player1))]

        for i, row in enumerate(self.cost_matrix):
            for j, elem in enumerate(row):
                item1 = self.get_cost(self.player1[i], self.player2[j], len(
                    self.player1), len(self.player2), self.A)
                item2 = self.get_cost(self.player2[j], self.player1[i], len(
                    self.player2), len(self.player1), self.A)
                self.cost_matrix[i][j] = (item1, item2)

        self.candidate_psne = []
        for i in range(len(self.player1)):
            for j in range(len(self.player2)):
                if(self.player1[i]+self.player2[j] == self.A):
                    self.candidate_psne.append((i, j))

        self.psne = []

    def print_cand_psne(self):
        op = str(self.candidate_psne)
        return op

    def print_cost_matrix(self):
        op = ""
        for row in self.cost_matrix:
            for elem in row:
                op += "( " + str(elem[0])+", " + str(elem[1])+") "
            op += "\n"
        return op

    def __str__(self):
        return "candidate psne => {} \n cost_matrix => {}".format(str(self.print_cand_psne()), str(self.print_cost_matrix()))


p2 = [1, 2, 3, 4, 5, 6, 7]
p1 = [1, 2, 3]

a = CostMatrix(p1, p2, 8)
print(a)
