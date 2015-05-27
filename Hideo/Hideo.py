from csv import reader

class Hideo:

	data = []
	dict_data = []

	def __init__(self, input_file):
		print("HIDEO. Initiation.")
		self.input = input_file

	def load_data(self):
		print("HIDEO. Loading data.")
		with open(self.input) as input:
			self.data = list(reader(input))

	def set_intput(self, filename):
		print("HIDEO. Setting input")
		self.input = filename

	def create_dictionary(self, item_name_1, item_name_2):
		print("HIDEO. Creating dictionary.")
		for row in self.data:
			self.dict_data.append({item_name_1: row[0], item_name_2: row[1]})

	def show_dict(self):
		print("HIDEO. Showing dictionary.")
		for row in self.dict_data:
			for key in row.keys():
				print(row[key], end="\t")
			print()

def main():

	base_directory = "C:\\Data\\Projects\\Gibson\\Data"
	input = "\\csv"

	file = "\\infinz_00001_20150213025756.pcap.csv"

	hideo = Hideo(base_directory + input + file)
	hideo.load_data()

	hideo.create_dictionary("ip_src", "ttl")

	hideo.show_dict()


if __name__ == '__main__':
	main()

