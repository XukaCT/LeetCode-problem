class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d_pos =0
        r_pos = -1
        dominoes=list(dominoes)
        while(d_pos < len(dominoes)):
            if dominoes[d_pos]==".":
                d_pos +=1 
            ## L occured 
            elif dominoes[d_pos]=="L":
                if r_pos == -1:
                    j = d_pos-1
                    while (j>=0 and dominoes[j]=="."):
                        dominoes[j]="L"
                        j-=1 
                    
                else:
                    r = r_pos + 1 
                    l = d_pos - 1 
                    while(r<l):
                        dominoes[r]="R"
                        dominoes[l]="L" 
                        r+=1
                        l-=1 
                    r_pos = -1 
                d_pos += 1
            
            ## R occurs 
            elif dominoes[d_pos]=="R":
                if r_pos == -1:
                    r_pos = d_pos 
                else:
                    j = d_pos - 1 
                    while j > r_pos:
                        dominoes[j]="R"
                        j -= 1 
                    r_pos = d_pos 
                d_pos += 1  
        
        if r_pos != -1:
            j = r_pos + 1
            while(j < len(dominoes)):
                dominoes[j]="R" 
                j += 1 
        return "".join(dominoes)




           



        
