class Bank:
    def saving(self):
        print('inside saving method')
    def saving(self,a):
        print(f'saving:{a}')
    def saving(self,a,b):
        print(f'saving {a},{b}')
B1=Bank()
#B1.saving()  error
#B1.saving(10) error
B1.Bank(10,20)  #no error
