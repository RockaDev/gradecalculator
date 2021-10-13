class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BPurple="\033[1;35m"


def percentage():
	a = float(input(bcolors.ENDC + "Počet bodov na písomke >> "))
	b = float(input(bcolors.ENDC + "Maximálny počet bodov na písomke >> "))
	percent = 100 * float(a)/float(b)
	result = print(bcolors.OKCYAN + bcolors.UNDERLINE + str(percent) + "%" + bcolors.ENDC)
	if percent >= 90 and percent <= 100:
		print(bcolors.BOLD + bcolors.WARNING + "známka: 1")
	elif percent <= 90 and percent >= 75:
		print(bcolors.BOLD + bcolors.OKBLUE + "známka: 2")
	elif percent <= 75 and percent >= 50:
		print(bcolors.BOLD + bcolors.OKGREEN + "známka: 3")
	elif percent <= 50 and percent >= 30:
		print(bcolors.BOLD + bcolors.BPurple + "známka: 4")
	elif percent <= 30 and percent >= 0:
		print(bcolors.BOLD + bcolors.FAIL + "známka: 5")
	else:
		print("Chyba. Počet bodov je vyšší ako maximálny.")

if __name__ == '__main__':
	while True:
		percentage()



