
# Implement tuple packing and unpacking in sorting and filtering tasks.

# Problem Statement:
# You have a list of contacts, where each contact is represented as a tuple containing a name, email, and phone number. Your task is to:

# Sort the contacts by name.
# Filter and display contacts whose names start with a specific letter.
# Sample Contact Data:

contacts = [
 ('Dana', 'dana_195@email.com', '484-933-1440'),
 ('Julia', 'julia_752@email.com', '509-640-1988'),
 ('Hannah', 'hannah_611@email.com', '855-428-8608'),
 ('Fiona', 'fiona_431@email.com', '758-560-5528'),
 ('Ivan', 'ivan_616@email.com', '426-514-8284'),
 ('Bob', 'bob_283@email.com', '660-424-2692'),
 ('Julia', 'julia_708@email.com', '820-808-1872'),
 ('George', 'george_619@email.com', '830-696-5247'),
 ('Dana', 'dana_538@email.com', '624-992-6885'),
 ('Bob', 'bob_786@email.com', '336-388-9539'),
 ('Ivan', 'ivan_280@email.com', '152-498-2354'),
 ('Charlie', 'charlie_270@email.com', '760-403-4047'),
 ('Eli', 'eli_740@email.com', '411-573-8355'),
 ('Ivan', 'ivan_295@email.com', '924-487-3557'),
 ('Alice', 'alice_871@email.com', '849-537-5524'),
 ('George', 'george_515@email.com', '791-192-1662'),
 ('Hannah', 'hannah_977@email.com', '811-673-3973'),
 ('Charlie', 'charlie_408@email.com', '207-146-5895'),
 ('Fiona', 'fiona_299@email.com', '261-968-9696'),
 ('Eli', 'eli_421@email.com', '728-560-5488'),
 ('Julia', 'julia_246@email.com', '727-309-4577'),
 ('George', 'george_671@email.com', '706-616-3250'),
 ('Fiona', 'fiona_381@email.com', '759-631-4624'),
 ('Bob', 'bob_191@email.com', '118-760-9505'),
 ('Eli', 'eli_567@email.com', '522-202-4686'),
 ('Charlie', 'charlie_252@email.com', '475-172-9203'),
 ('Dana', 'dana_984@email.com', '764-312-7081'),
 ('Alice', 'alice_956@email.com', '780-555-1490'),
 ('Hannah', 'hannah_556@email.com', '174-893-6002'),
 ('Alice', 'alice_696@email.com', '542-630-9808')
]

def sort_list(contact_list):
    return sorted(contact_list, key=lambda contact: contact[0])

def filter_contacts(contacts, letter):
    filtered_contacts = [contact for contact in contacts if contact[0].lower().startswith(letter)]
    for name, email, phone in filtered_contacts:
        print(f"Name: {name}, Email: {email}, Phone: {phone}")

sorted_list = sort_list(contacts)

print("Sorted List: ")
for contact in sorted_list:
    print(contact)
print("")

letter = input("Enter the first letter of a name you would like to search for: ")
filter_contacts(contacts, letter.lower())