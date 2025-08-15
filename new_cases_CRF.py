from datetime import date 
## date : 2025-07-07 , rate = 13 , morat = 30 , tenure = 60 , disb_amt = 2000000
class NewCases:
    def __init__(self ,acc_no, tenure , rate , disb_amt , disb_date : date   , morat):
        self.tenure = tenure
        self.rate = rate 
        self.disb_amt = disb_amt
        self.disb_date = disb_date 
        self.morat = morat
        self.accno = acc_no
        self.cashflow = {}
        self.duedate = date()
        self.repayamt = float()
        self.op_pos = float()
        self.clo_pos = float()
        self.chunks = self.tenure/(tenure) + 1 

    def __str__(self):
        return f'ACC_NO:{self.accno} , TENURE : {self.tenure}, RATE  : {self.rate} , DISB_AMT : {self.disb_amt} , MORAT : {self.disb_amt}'
    

    def calc_cashflow(self):
        for i in range(self.tenure+2):
            if i == 1  :
                if self.disb_date.day > 15 and self.disb_date.month == 12 :
                    self.duedate = self.disb_date

                 


