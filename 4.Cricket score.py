
class Cric:

    balls=int(input("How many balls:"))

    array=[]
        
    b1=0        #first batsman initial score

    b2=0        #second batsman initial score
    
    
    def totalruns(self):
        
        for i in range(1,Cric.balls+1):
            Runs=int(input("Enter the Runs:"))
            Cric.array.append(Runs)
        print("Runs:=",Cric.array)
        self.teamscore=sum(Cric.array)
        print("----------------------------------------")
        print("----------------------------------------")
        
        
        
    def ballbyball(self):
        print("Ball\tRun")
        for i in range(0,Cric.balls,1):
            print(i+1,"\t",Cric.array[i])

            
    def Sachin(self):
        self.batting='Sachin'
               
        
        for i in range(0,Cric.balls,1):
            if(self.batting=='Sachin'):
                Cric.b1=Cric.b1+Cric.array[i]
                
            if(self.batting=='Sachin'):
                if(Cric.array[i]%2!=0):
                    self.batting='Dhoni'
                    
            elif(self.batting=='Dhoni'):
                if(Cric.array[i]%2!=0):
                    self.batting='Sachin'
                    
            if((i+1)%6==0):
                if(self.batting=="Sachin"):
                    self.batting="Dhoni"
                else:
                    self.batting="Sachin"
        print("Total Runs:=",self.teamscore)
        print("The first batsman(sachin) Runs:",Cric.b1)

    def dhoni(self):
        
        Cric.b2=self.teamscore-Cric.b1
        print("The second batsman(Dhoni) Runs:",Cric.b2)
        
        
            
        

a=Cric()
a.totalruns()
a.ballbyball()
a.Sachin()
a.dhoni()
