
class CostMatrix:
    def get_cost(self, di, dj, ni, nj, A):
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
        for cand in self.candidate_psne:
            a, b = cand[0], cand[1]
            val1, val2 = self.cost_matrix[a][b][0], self.cost_matrix[a][b][1]
            row = []
            col = []
            for i in range(len(self.player2)):
                if(i != b):
                    row.append(self.cost_matrix[a][i][1])
            for i in range(len(self.player1)):
                if(i != a):
                    col.append(self.cost_matrix[i][b][0])

            if val1 <= min(col) and val2 <= min(row):
                self.psne.append((a, b))

    def get_cand_psne(self):
        op = str(self.candidate_psne)
        return op

    def get_psne(self):
        op = str(self.psne)
        return op

    def get_cost_matrix(self):
        op = ""
        for row in self.cost_matrix:
            for elem in row:
                op += "( " + str(elem[0])+", " + str(elem[1])+") "
            op += "\n"
        return op

    def __str__(self):
        return "candidate psne =>\n {} \n\n cost_matrix =>\n {} \n psne's =>\n {}".format(str(self.get_cand_psne()), str(self.get_cost_matrix()), str(self.get_psne()))
