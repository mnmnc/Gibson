
from Hideo.Hideo import Hideo
from Dixie.Dixie import Dixie
from Armitage.Armitage import Armitage

class Wintermute:

	def __init__(self):
		pass



def main():

	base_directory = "C:\\Data\\Projects\\Gibson\\Data"
	input_pcap = "\\pcap"
	output = "\\csv"
	file = "infinz_00001_20150213025756.pcap"
	tshark = "C:\\Data\\Projects\\Gibson\\Wireshark\\tshark.exe"

	# Processing pcap file. Results in csv file.
	armitage = Armitage(base_directory + input_pcap , base_directory + output, tshark)
	armitage.add_field("ip", "src")
	armitage.add_field("ip", "ttl")
	armitage.add_filter("ip")
	armitage.create_command("\\" + file, "\\" + file + ".csv")
	armitage.execute()


	input_csv = "\\csv"
	file_csv = "\\" + file + ".csv"

	# Load file content to dictionary
	hideo = Hideo(base_directory + input_csv + file_csv)
	hideo.load_data()
	hideo.create_dictionary("ip_src", "ttl")

	# List modifications
	dixie = Dixie()
	dixie.initiate_2d(hideo.dict_data)
	dixie.distinct_per_first("ip_src", "ttl")

if __name__ == '__main__':
	main()

