# first we take nominee input

nominee1 = input("Enter The Name Of First Nominee ")
nominee2 = input("Enter The Name Of Second Nominee ")

# initial vote count for boot must be 0

nm1_votes = 0
nm2_votes = 0

voter_id = {1,2,3,4,5,6,7,8,9,10}

no_of_voter = len(voter_id)

while True:
    if voter_id == []: # to check when vote is completed
        print("Voting session is over")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voter)*100
            print(nominee1,"Has won the election with ",percent,"% of votes")     
            break # to end infinite loop
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2,"Has won the election with ",percent,"% of votes")
            break
        else:
            print("Both have equal number of votes !!!! Government will decide who will win")
        break
    
    voter = int(input("Enter Your Voter Id : "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter) # we will remove so same voter again cant vote
        print("----------------------------------")
        print("To give vote to",nominee1,"press 1")
        print("To give vote to",nominee2,"press 2")
        print("----------------------------------")
        vote = int(input("Enter your precious vote : "))
        if vote == 1:
            nm1_votes += 1
            print(f"Thanks to give your important vote to {nominee1}")
        elif vote == 2:
            nm2_votes += 1
            print(f"Thanks to give your important vote to {nominee2}")
        elif vote > 2:
            print("Please Check Your Pressed Key!!")
        else:
            print("You are not a voter anymore OR You have already voted")
            
        
            
        
