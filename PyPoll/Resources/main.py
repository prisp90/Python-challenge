import os
import csv

filepath = os.path.join('..', "Resources", "election_data.csv")
output_path = os.path.join('..', "Analysis","elec_output.txt")


with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(f'"header: {csv_header}')

    total_vote = 0
    candidates_name = set()
    candidate_name_dic = {}
    


    for vote_row in reader:
        total_vote += 1
        
        temp_total_vote = 0

        candidates_name.add(vote_row[2])

        if vote_row[2] in candidates_name:

            if vote_row[2] in candidate_name_dic:

                temp_total_vote = int(candidate_name_dic[vote_row[2]])

                temp_total_vote += 1

                candidate_name_dic[vote_row[2]] = str(temp_total_vote)

            else:

                candidate_name_dic[vote_row[2]] = 1

    
    percentage_of_votes = 0.0

    temp_vote = 0

    vote_percentage_dictionary ={}

    winner = ""

    winner_vote_percent = 0.0


    for x in candidates_name:
        
        temp_vote = int(candidate_name_dic[x])

        percentage_of_votes = (temp_vote/total_vote)*100

        percentage_of_votes_round = round(percentage_of_votes, 2)

        vote_percentage_dictionary[x] = percentage_of_votes_round
        
        if percentage_of_votes_round >= winner_vote_percent:

            winner_vote_percent = percentage_of_votes_round

            winner_vote_percent_round = round(winner_vote_percent, 2)

            winner = x
 
     
    print('\n==================================================\n')
    
    print("\n Election Results \n")
    
    print('\n==================================================\n')
    
    print("\nTotal Votes: "+" "+ str(total_vote)+"\n")
    
    print('\n----------------------------------------------------\n')    

    for cand_name in candidate_name_dic:
        print("\n"+cand_name+":"+" "+str(vote_percentage_dictionary[cand_name])+"%"+"  ("+str(candidate_name_dic[cand_name])+")"+"\n")

    print('\n----------------------------------------------------\n')
    
    print("\n"+"Winner: "+ winner+"\n")
    
    print('\n----------------------------------------------------\n')



    with open(output_path, 'w', newline= '') as txt_output_file:
        
        txt_output_file.write('\n==================================================\n')

        txt_output_file.write("\n Election Results \n")

        txt_output_file.write('\n==================================================\n')

        txt_output_file.write("\nTotal Votes: "+" "+ str(total_vote)+"\n")

        txt_output_file.write('\n----------------------------------------------------\n')    

        for cand_name in candidate_name_dic:
            txt_output_file.write("\n"+cand_name+":"+" "+str(vote_percentage_dictionary[cand_name])+"%"+"  ("+str(candidate_name_dic[cand_name])+")"+"\n")

        txt_output_file.write('\n----------------------------------------------------\n')

        txt_output_file.write("\n"+"Winner: "+ winner+"\n")

        txt_output_file.write('\n----------------------------------------------------\n')

