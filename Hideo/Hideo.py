from csv import reader

class Hideo:

	data = []

	def __init__(self, input_file):
		self.input = input_file

	def load_data(self):
		with open(self.input) as input:
			self.data = list(reader(input))

	def set_intput(self, filename):
		self.input = filename


def main():

	base_directory = "C:\\Data\\Projects\\Gibson\\Data"
	input = "\\csv"

	file = "\\infinz_00001_20150213025756.pcap.csv"

	hideo = Hideo(base_directory + input + file)
	hideo.load_data()
	for row in hideo.data:
		print(row)

if __name__ == '__main__':
	main()

