list_of_words = ["butt", "stuff", "stupid", "stuntmen"]
def give_words(words, substring): 
    holder_set = set()
    for word in words:
        if(word.find(substring)>=0):
            holder_set.add(word)
    return holder_set
hw_phone_book = {
		"Dillon": "111-222-3333",
		"Arielle": "331-229-9024",
		"Sam": "989-012-8942",
		"James": "320-999-2661",
		"Samantha": "901-420-6969"
	}

def call_your_friends(phone_book, who_to_call):
    call_list = {}
    for person in phone_book:
        for name in who_to_call:
            if(person==name):
                call_list[person] = phone_book[person]
    return call_list

call_list = call_your_friends(hw_phone_book, ["Dillon", "Sam"])
for friend in call_list:
    print("Calling", friend, "at", call_list[friend])

