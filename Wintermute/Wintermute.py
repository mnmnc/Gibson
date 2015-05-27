
from Hideo.Hideo import Hideo
from Dixie.Dixie import Dixie


class Wintermute:

	def __init__(self):
		pass



def main():

	base_directory = "C:\\Data\\Projects\\Gibson\\Data"
	input = "\\csv"

	file = "\\infinz_00001_20150213025756.pcap.csv"

	hideo = Hideo(base_directory + input + file)
	hideo.load_data()

	hideo.create_dictionary("ip_src", "ttl")

	#hideo.show_dict()

	dixie = Dixie()
	dixie.initiate_2d(hideo.dict_data)

	dixie.distinct_per_first("ip_src", "ttl")

if __name__ == '__main__':
	main()

