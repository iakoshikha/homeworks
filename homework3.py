#len 
import random 

students = ["iako", "salome", "lela", "ekuna" , "lile"]

while students:
    selected_members = random.choice(students)
    question = f"{selected_members}, answer this question: what is 2+2?"
    respose = input(question)

    if respose == "4":
        print(f"{selected_members}anwered correctly! 1 point added.")
    else:
        print(f"{selected_members}did not answer correctly.")

    students.remove(selected_members)
print("all group members have aswered for the day")    





























# jguufi 5is video funqciebze
# sololears bolomde


