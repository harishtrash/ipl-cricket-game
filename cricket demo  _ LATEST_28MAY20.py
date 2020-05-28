main_df = !cls

#%%

#==========================================================================
##  FUNCTIONS LIST
#==========================================================================



#==========================================================================
## --- FUNCTION 2 :  TO update excel when batsman is out-------------
#==========================================================================

def update_out_batsman_runs( batsman_id, team_name, main_df, batsman_score ):
 
    #- ----UPDATE RUNS FOR THAT PLAYER 

    main_df['RUNS'][batsman_id] = main_df['RUNS'][batsman_id] + batsman_score
    
    # -----AND UPDATE WRITE TO EXCEL 
    main_df.to_excel('D:\\HARISH\\DATA SCIENCE\\1 MY Training\\my cricket game code\\SUCCESSFUL CODE\\FULL CODE\\IPL PLAYER LIST_harish1.xlsx')
    
#==========================================================================
## --- FUNCTION 1 :  BATSMAN INTERCHANGE FUNCTION -------------
#==========================================================================

## ---  

def batsman_change(striker,runner,batsman1,batsman2):
    if (striker == batsman1):
        return(batsman2,batsman1)
    else:
        return(batsman1,batsman2)

 
 

#==========================================================================
# ============= 1. import libraries ======================= 
#==========================================================================
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', None)

import numpy as np
import time


import random
import time

  
#==========================================================================
# ============= 2. SHOW ALL TEAMS LIST======================= 
#==========================================================================

print('\n\n\n********************************************************************************************************')
print('****************\t\t WELCOME TO CRICKET GAME\t\t ********************')
print('********************************************************************************************************')
time.sleep(1)

ALL_TEAMS = [[1,'SRH'],
            [2,'CSK'],
            [3,'MI'],[4,'RCB'],[5,'RR'],[6,'KXIP'],[7,'KKR'],[8,'DD'] ]
 

print('\n\t\t\t ============  TEAMS LIST   ============\n')
for i in ALL_TEAMS:

    print('\t\t\t\t',i[0],'.',i[1])
    
    

#==========================================================================
# ============= 3. SELECT YOUR TEAM =======================
#==========================================================================


#time.sleep(1)
selected_team = 0 
print('\n\t\t\t============  SELECT YOUR TEAM   ============')


selected_team = int(input('ENTER TEAM NUMBER : '))
selected_team
while (selected_team not in range(1,len(ALL_TEAMS)+1)):
    print('Please Enter value between 1 and ',len(ALL_TEAMS))
    selected_team = int(input('ENTER TEAM NUMBER : '))
    


MY_TEAM = ALL_TEAMS[(selected_team-1)]


 
#==========================================================================
# ============= 4. YOUR RANDOM OPPONENT  =======================
#==========================================================================
ALL_TEAMS_1 = ALL_TEAMS.copy()
ALL_TEAMS_1.remove(MY_TEAM)

random_obj = random.SystemRandom()
OPP_TEAM  = random_obj.choice(ALL_TEAMS_1)

MY_TEAM
OPP_TEAM

print('\n\n********************************************************************************************************\n')
print('\t\t*****  PLAYING ELEVEN LIST OF EACH TEAM  *****')
 

print('\n\t*****   [',MY_TEAM[1],' Team ]\t******\t   VS    \t***** [',OPP_TEAM[1],' Team] ******\n')
print('********************************************************************************************************\n')
time.sleep(1)

#==========================================================================
#  ----- 4.1 show teams ------
#==========================================================================

import pandas as pd
import numpy as np

df = pd.read_excel('D:\\HARISH\\DATA SCIENCE\\1 MY Training\\my cricket game code\\SUCCESSFUL CODE\\FULL CODE\\IPL PLAYER LIST_harish1.xlsx')

# --- load only both teams  ---
team1_df  = df[df['TEAM'].str.contains(MY_TEAM[1])]
team2_df  = df[df['TEAM'].str.contains(OPP_TEAM[1])]   

team1_df = team1_df.iloc[:12,0:2]
team2_df = team2_df.iloc[:12,0:2]

#team2_df.columns = ['PLAYERS2','TYPE2']
 

team2_df = team2_df.reset_index(drop=True)
team2_df

team1_df = team1_df.reset_index(drop=True)
team1_df



player_list = pd.concat([team1_df, team2_df], axis=1)

#time.sleep(1)

print(player_list)
# 
# ============= INITIALIZE   TEAM NAMES  TO VARIABLES =============
 
team1 = MY_TEAM[1]
team2 = OPP_TEAM[1]

#time.sleep(1)
   
#==========================================================================
# ============= 5 . CALL for  TOSS   =======================
#==========================================================================

print('********************************************************************************************************\n')
print('\n',team1,' to call the toss : ')
#print('********************************************************************************************************')

print('\n\n********************************************************************************************************\n')
#toss_call = int(input('plz call heads(0) or tails(1) : '))
print('TOSS : plz call heads(0) or tails(1)')

time.sleep(0.5)
toss_call = int(np.random.randint(2))
print('********************************************************************************************************\n')
#print(team1,' to call the toss')

while (toss_call not in [0,1]):
#   print('\nWRONG INPUT : please input value 0 or 1 for toss')
   toss_call = int(np.random.randint(2))
#   int(input('\n\t plz call heads(0) or tails(1)'))
   print('TOSS : plz call heads(0) or tails(1)')
   time.sleep(0.5)
   
   
#print('toss value is : ',toss_call)

toss_result = int(np.random.randint(2))

if (toss_call == toss_result) :
    
   print('\n\n********************************************************************************************************\n')
   print('\t\t***',team1,' *** has Won the toss and   will BAT  first ***')
   print('********************************************************************************************************\n')
   firstbatting = team1
   firstbatting_team = team1_df
   
   secondbatting = team2
   secondbatting_team = team2_df
   
   time.sleep(2)

else :

   print('\n\n********************************************************************************************************\n')
   print('\t\t***',team2,' *** has Won the toss and   will BAT  first ***')
   print('********************************************************************************************************\n')
   firstbatting = team2
   firstbatting_team = team2_df
   
   secondbatting = team1
   secondbatting_df = team1_df
   
   time.sleep(3)
   
#time.sleep(1)
 
print('********************************************************************************************************')
print('***************************\t CRICKET MATCH \t******************************************************** \n\n')
print('***********************      \t',firstbatting,'   vs ',secondbatting,' \t************************************************')
print('********************************************************************************************************')


  
 
#==========================================================================
# ============= 6 . FIRST BATTING SCORES  =======================
#==========================================================================

print('********************************************************************************************************') 
print('*************************** \t ',firstbatting ,' Batting\t    **************************************************** \n')
print('********************************************************************************************************')
time.sleep(1)

# ----initialize variables  ---- 
boundaries = 0 
overs =0
MAX_OVERS =10
balls = 0
tot_runs=0
runs_per_ball =0
extra_runs =0
extras = [3,5]
total_balls = 19
ball_by_ball = [] 
wd_or_nb =0
extra_per_over =0 
#team1_sixers =0
firstbatting_sixers = 0
wickets = 1
batsman1_score = 0
batsman2_score = 0
# print('1')
 


# ---- LOAD THE FIRST TWO BATSMEN -----

main_df = pd.read_excel('D:\\HARISH\\DATA SCIENCE\\1 MY Training\\my cricket game code\\SUCCESSFUL CODE\\FULL CODE\\IPL PLAYER LIST_harish1.xlsx')


striker = batsman1 = firstbatting_team['PLAYER'][wickets-1]
batsman1_id = main_df[main_df['TEAM'] == firstbatting ].iloc[wickets-1:wickets,:] ['PLAYER_ID'] 

runner = batsman2 = firstbatting_team['PLAYER'][wickets]
batsman2_id = main_df[main_df['TEAM'] == firstbatting ].iloc[wickets:wickets+1,:] ['PLAYER_ID'] 
 
playing_team_df = firstbatting_team.copy()
striker = batsman1
runner = batsman2
 
print('\n\t\t*********** Openers at crease ***********\n')
print('\t Striker : ',striker)
print('\t Runner  : ',runner,'\n')

 

# --- for loop for counting overs ---
for overs  in range(0,MAX_OVERS):
   
   time.sleep(.5)   
   over_boundaries = 0
   extra_per_over =0
   balls = 0
   ball_by_ball = []
   runs_per_over =0 
   out = 0
#   print('overs ',overs)
   
   # --------- while loop for "COUNTING BALLS " in each over  -------
   
   while (balls <6):
       #       print('inside while loop')
       
       wd_or_nb =0
       balls +=1      

# ----- IF "OUT code" --------------
       out = int(np.random.randint(30))
       if (out == 1):
           wickets +=1
           if(wickets == 10) :
               print(firstbatting,' Team is all out')
                 
           
           
#           input()
           if (wickets == 10 ):
               print (firstbatting_team,' is ALL OUT')
               break
# **************************************************           
           # --- load new batsman as striker ---- 

           if (striker == batsman1 ):         
               print ('\n\t  ========== THATS OUT !!  ==========\n\tAfter',overs,'.',balls,'overs  \t [',batsman1  ,'(',batsman1_score,') ] is out \t\n ')    
               
               # -- UPDATE EXCEL WITH BATSMAN OUT DETAILS ---
               update_out_batsman_runs( batsman1_id, firstbatting , main_df, batsman1_score )
               
              # --- new batsman loading --- 
               striker =batsman1 = playing_team_df['PLAYER'][wickets]
               batsman1_id = main_df[main_df['TEAM'] == firstbatting ].iloc[wickets:wickets+1,:] ['PLAYER_ID'] 
               batsman1_score = 0               
               
           elif (striker == batsman2 ):              
               print ('\n\t  ========== THATS OUT !!  ==========\n\tAfter',overs,'.',balls,'overs  \t [',batsman2  ,'(',batsman2_score,') ] is out \t\n ')    
              
                # -- UPDATE EXCEL WITH BATSMAN OUT DETAILS ---
               update_out_batsman_runs( batsman2_id, firstbatting , main_df, batsman2_score )
               
                # --- new batsman loading ---               
               striker =batsman2 = playing_team_df['PLAYER'][wickets]   
               batsman2_id = main_df[main_df['TEAM'] == firstbatting ].iloc[wickets:wickets+1,:] ['PLAYER_ID']                
               batsman2_score = 0
               
           print('\tNEXT TO BAT : [',striker,' ] \t (PRESS ENTER TO CONTINUE)')
           input()
# **************************************************
               
       else :
# ----- IF " NOT OUT" --------------           
            #       print(" 2.while loop")
            
    #  --- RUNS SCORED FOR EACH BALL : random runs scored per each ball ---
           runs_per_ball=np.random.randint(7)        
    
        
    #  ---- sixer count  ----
           
           if(runs_per_ball == 6):
               firstbatting_sixers +=1
    
    #  ---- each over boundaries count  ----       
           if (runs_per_ball in [4,6]) :
               over_boundaries +=1
    
    #  --- extras  (enable extra status - CHECKING FOR WIDES ) ---    
           if (runs_per_ball in [5]):   
               extra_per_over +=1
               wd_or_nb =1
               runs_per_ball = 1
    
           if (runs_per_ball in [3]):        
               runs_per_ball =1 
    
    #  --  calculate total runs --           
           if (wd_or_nb == 1):
               ball_by_ball.append('Wd')
               balls -=1 
               tot_runs= tot_runs + runs_per_ball
               
           else:
    #           print(" 4. ")
               tot_runs= tot_runs + runs_per_ball
               ball_by_ball.append(runs_per_ball)
     
    #  ---- ADD RUNS TO THE STRIKER  ----
               if (striker == batsman1):
                   batsman1_score += runs_per_ball
               else :
                   batsman2_score += runs_per_ball  
                   
                   
               # ----- IF LOOP : CALCULATING TOTAL RUNS ENDS HERE  ---- 
           # ----- Interchange batsman if runs per ball is odd
           
           if((runs_per_ball % 2 != 0) and  wd_or_nb == 0):
                 striker,runner = batsman_change(striker,runner,batsman1,batsman2)
 
       
 
   #  ------ WHILE LOOP ENDS HERE -----

   if (wickets == 10 ):
       print (firstbatting_team,' is ALL OUT')
       break         
#   if (balls ==6):                           
#       balls =0
#       print('\t              ',batsman1,'(',batsman1_score,')\t  ',batsman2,'(',batsman2_score,')')
#       print('Overs :',overs+1,'.',balls,'             [ball by ball ] : ',ball_by_ball,'')          
#       print(firstbatting,'s Score :',tot_runs,' [ boundaries :', over_boundaries,' ,  Extras  :',extra_per_over,' ]            \n\n')       

   if (balls ==6):                           
       balls =0
       
       print('Overs :',overs+1,'.',balls,'             [ball by ball ] : ',ball_by_ball,'')          
       print(firstbatting,'s Score :',tot_runs,'          [ boundaries :', over_boundaries,' ,  Extras  :',extra_per_over,' ]  ')  #,end ='')
       
       if(striker == batsman1):
           print('                           [ * ',batsman1,'(',batsman1_score,')\t ,  ',batsman2,'(',batsman2_score,') ]\n')

       else :
           print('                           [',batsman1,'(',batsman1_score,')\t , * ',batsman2,'(',batsman2_score,') ]\n')



       # --- AT END OF OVER CHANGE OVER BATSMAN CREASE 
   striker,runner = batsman_change(striker,runner,batsman1,batsman2)

       
    
#    print(" 5. ")           
    

#    input('Press ENTER for next over')
   
 
#print('***  END OF FOR LOOP  ****')            


firstbatting_score = tot_runs

print('********************************************************************************************************')
print('\n\n\t\t\t\t\t*****  ',firstbatting,'s Innings Ended  ******')
print('********************************************************************************************************')
print()
print('\t\t\t\t\t\t',firstbatting,' Total Score           :',firstbatting_score,'/',wickets-1 )
#print( 'Extras                :',extra_runs)
print ('\t\t\t\t\t\tTotal SIXERS          : ',firstbatting_sixers )
print ('\t\t\t\t\t\tTotal OVERS           : ',overs,'.',balls)
print ('\n\n\t\t\t\t\t\t',secondbatting,'"s" Target is  : ',firstbatting_score+1,' in ',MAX_OVERS,' Overs')

# 
 
 
#==========================================================================
# ============= 7 . SECOND BATTING SCORES  ================================
#==========================================================================



print('\n\n***************************\tSECOND INNINGS : ',secondbatting ,' Batting\t****************************************** \n\n')
#time.sleep(1)
print(' PRESS ENTER TO START ',secondbatting,'S BATTING')
#input('')

# ----initialize variables  ---- 
boundaries = 0 
overs =0
MAX_OVERS =10
balls = 0
tot_runs=0
runs_per_ball =0
extra_runs =0
extras = [3,5]
total_balls = 19
ball_by_ball = [] 
wd_or_nb =0
extra_per_over =0 
secondbatting_sixers =0

# ---- for loop for scores ---- 
# print('1')
 

# --- counting overs ---
for overs  in range(0,MAX_OVERS):
   
   time.sleep(.5)   
   over_boundaries = 0
   extra_per_over =0
   balls = 0
   ball_by_ball = []
    
    
#   print('overs ',overs)
# --- counting balls in each over  ---
   while (balls <6):
#       print('inside while loop')
# -- pause for a second ---
       wd_or_nb =0
    
       balls +=1      

#       print(" 2.while loop")
#  --- runs scored per ball ---
       runs_per_ball=np.random.randint(7)        

    

#  ---- sixer count  ----
       
       if(runs_per_ball == 6):
           secondbatting_sixers +=1

#  ---- each over boundaries count  ----       
       if (runs_per_ball in [4,6]) :
           over_boundaries +=1

#  --- extras  ---    
       if (runs_per_ball in [5]):   
           extra_per_over +=1
           wd_or_nb =1

       if (runs_per_ball in [3]):        
           runs_per_ball =1 

#  --  calculate total runs --           
       if (wd_or_nb == 1):
           ball_by_ball.append('Wd')
           balls -=1 
           extra_runs +=1
#           print(" 3. wide ball ")           

       else:
#           print(" 4. ")
           tot_runs= tot_runs + runs_per_ball
           ball_by_ball.append(runs_per_ball)
#           print( 'over :',overs,'.',  balls,'          ','              runs   :',runs_per_ball)           
           

    #  --  if second batting has won the match exit --     
    
       if (tot_runs > firstbatting_score ):
           secondbatting_score = tot_runs 
           winner = secondbatting
           print('Overs :',overs,'.',balls,'             [ball by ball ] : ',ball_by_ball,'')          
           print(secondbatting,'s Score :',tot_runs,' [ boundaries :', over_boundaries,' ,  Extras  :',extra_per_over,' ]            \n\n')       
           print('********************************************************************************************************')
           print('\n \t\t***** [',secondbatting,'] has defeated  :[',firstbatting,'] by reaching target of [',firstbatting_score+1,'] ***** \n')
           break
       
   if (tot_runs > firstbatting_score):        
       break
       
   if (balls ==6):
       balls =0
       print('Overs :',overs+1,'.',balls,'             [ball by ball ] : ',ball_by_ball,'')          
       print(secondbatting,'s Score :',tot_runs,' [ boundaries :', over_boundaries,' ,  Extras  :',extra_per_over,' ]            \n\n')       
 
 
#    input('Press ENTER for next over')
#   
#print('***  END OF FOR LOOP  ****')            
secondbatting_score =  tot_runs


if (secondbatting_score < firstbatting_score ): 
    print('********************************************************************************************************')
    print( '\n\t\t\t*****',secondbatting,'(',secondbatting_score,' ) Failed to chase the target of :',firstbatting,'(',firstbatting_score+1,' ) ******\n')
    winner = firstbatting
    

 
print('********************************************************************************************************')
print('\n\t\t\t\t\t*****  ',secondbatting,'s Innings Ended  ******')
print('********************************************************************************************************')
print()
print('\t\t\t\t\t\t',secondbatting,' Total Score           :',secondbatting_score )
#print( 'Extras                :',extra_runs)
print ('\t\t\t\t\t\tTotal SIXERS          : ',secondbatting_sixers )
print ('\t\t\t\t\t\tTotal OVERS           : ',overs+1,'.',balls)
        





 
#==========================================================================
# ============= 8 . CONGRATULATING WINNER  ======================================
#==========================================================================

print('\n ')
print('\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('\n      ')
print('\t\t !!  CONGRATULATIONS TO TEAM ***[',winner,' ] *** FOR WINNING THE MATCH !!   !! ')
print('\n      ')
print('\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#

 

#%%   