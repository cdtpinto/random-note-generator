import random

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
STRINGS = ["high E", "B", "G", "D", "A", "low E"]

def generate_random():
	note = random.choice(NOTES)
	string = random.choice(STRINGS)

	return note, string

def loop():
	while True:
		user_input = input()

		if user_input == "q":
			break

		note, string = generate_random()

		print()
		print("-------------------")
		print(f"{note} on {string} string")
		print("-------------------")
		print()

if __name__ == "__main__":
	print(" #########################################")
	print("#                                         #")
	print("#          Random Note Generator          #")
	print("#                                         #")
	print("# For practicing guitar neck memorization #")
	print("#                                         #")
	print(" #########################################")
	print()
	print("Press enter for the next note or 'q' to quit...")

	loop()

	exit(0)
