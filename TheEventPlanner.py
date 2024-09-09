#Task 1
attendees = int(input("Enter number of attendees: "))
venue = "conference room" if attendees < 100  else "large hall"
print(venue)

#Task 2
attendees = int(input("Enter number of attendees: "))
venue = "conference room" if attendees < 100  else "large hall"
suggested_items = "a projector" if attendees > 100 else "an audio system"
print(f"You will be in the {venue}. We would suggest: {suggested_items}")

#Task 3
attendees = int(input("Enter number of attendees: "))
catering = input("Do you require vegetarian food? (yes/no): ")
venue = "conference room" if attendees < 100  else "large hall"
suggested_items = "a projector" if attendees > 100 else "an audio system"
print(f"You will be in the {venue}. We would suggest: {suggested_items}")
if catering == "yes":
    print("We recommend Veggie Delight Caterers!")
else:
    print("We recommend Gourmet Meals Caterers!") 