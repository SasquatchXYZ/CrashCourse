def invite_guest(name):
    message = f"Hello {name.title()}, please come to my dinner."
    print(message)


guests = ["Rick", "Robbie", "John", "Jason"]

invite_guest(guests[0])
invite_guest(guests[1])
invite_guest(guests[2])
invite_guest(guests[3])

canceled_guest = 'Jason'
print(
    f"I am sorry to inform you that {canceled_guest.title()} can't make it to dinner.")

del guests[3]
print(guests)

guests.insert(3, 'Patrick')
print(guests)

invite_guest(guests[0])
invite_guest(guests[1])
invite_guest(guests[2])
invite_guest(guests[3])
