#######################################################################
#                          Import Sistem
#######################################################################
import os

#######################################################################
#                          MODULE UTAMA
#######################################################################
#top  	= "protection" # Ganti sesuai nama module yang akan di kompile
#top  	= "alu_8bit" # Ganti sesuai nama module yang akan di kompile
top  	= "alu_8bit" # Ganti sesuai nama module yang akan di kompile

#######################################################################
#                    	MAIN PROSES (JANGAN GANTI)
#######################################################################
# dir  	= "./module/selesai/"
dir  	= "./module/"
file 	= "cmp.ys"
target  = "alu_8bit.v"
#target  = "alu_8bit.v"
# target  = "alu_min.v"
#liberty = "lib/cmos_cells.lib"
#liberty = "lib/begadang.lib.js"
liberty = "lib/begadang33.lib.js"
#liberty = "lib/begadang44.lib.js"
# liberty = "lib/cells.lib"
# liberty = "lib/simple.lib"


compiled= "cmp.v"
def read():
	x=0
	out  = open(file,"w")
	rtl_files = os.listdir(dir)
	"""
	while(x<len(rtl_files)):
		print(rtl_files[x])
		out.write("read_verilog " + dir + rtl_files[x] + "\n")
		x+=1
	"""
	out.write("read_verilog " + dir + target + "\n")
	out.write("hierarchy -check -top "+top+"\n")
	out.write("proc; opt; memory; fsm; opt\n")
	out.write("techmap; opt\n")
	out.write("dfflibmap -liberty "+liberty+"\n")
	out.write("abc -liberty "+liberty+"\n")
	out.write("clean\n")
	out.write("write_verilog -norename -noattr "+compiled+"\n")
	#out.write("dffsr2dff\n")
	out.close()
	os.system("yosys " + file)
if __name__ == "__main__":
	read()
