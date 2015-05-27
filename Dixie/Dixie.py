
from Hideo import Hideo

class Dixie:

	data2d = []
	distinct_first2d = []

	def __init__(self):
		print("DIXIE. Initiation.")
		pass

	def initiate_2d(self, dict_data):
		print("DIXIE. Initiation of 2D data.")
		self.data2d = dict_data

	def distinct_per_first(self, key_name, other_key):
		print("DIXIE. Making distinct per first.")
		unique_first = []
		unique_dictionary = []

		for row in self.data2d:
			if row[key_name] not in unique_first:
				unique_first.append(row[key_name])

		for item in unique_first:
			seconds = []
			for row in self.data2d:
				if item == row[key_name]:
					seconds.append(row[other_key])

			unique_dictionary.append({item: seconds})

		for row in unique_dictionary:
			print(row)

def main():

	dixie = Dixie()



	pass

if __name__ == '__main__':
	main()