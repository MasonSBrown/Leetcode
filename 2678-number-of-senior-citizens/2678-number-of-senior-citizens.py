class Solution(object):
    def countSeniors(self, details):
        amount = 0
        for i in range(len(details)):
            x = details[i]
            count = 0
            age = 0
            for j in range(11, 13):
                count+=1
                if count == 2:
                    age += int(x[j])
                else:
                    age += (10 * int(x[j]))
            if age > 60:
                amount += 1
        return amount

                


        