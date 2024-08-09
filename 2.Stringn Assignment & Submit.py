firstline_RavenPoem = input("type in the first line of a poem Raven by Edgar Allen Poe: ");
print(len(firstline_RavenPoem));
start_number = input("please enter the starting integer: ");
ending_number = input("please enter the ending integer: ");
ending_number = int(ending_number);
start_number = int(start_number);
print(firstline_RavenPoem[start_number:ending_number]);