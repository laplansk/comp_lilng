import sys
import os

df_name = "smallTestFile"
df_ext = ".mbox"
chunk_size = 4096
output_limit = 500 * 1000 * 100 # 3.0GB
bytes_written = 0
df_num = 0

# get input file from command line
mboxfile = sys.argv[1]
# check that command line arg is valid filepath
if not os.path.isfile(mboxfile):
    print('Invalid source filepath - exiting')
    sys.exit(1)

# get destination folder from command line
destFolder = sys.argv[2]
# check that command line arg is valid filepath
if not os.path.exists(destFolder):
    print('Invalid destination folder filepath - exiting')
    sys.exit(1)

sf = open(mboxfile, 'rb')
df = open(destFolder + "/" + df_name + str(df_num) + df_ext, "wb")

while True:
    # read in some of the file
    chunk = sf.read(chunk_size)
    if chunk == "":
        print "reached end of file"
        break
    if bytes_written > output_limit:
        print "filled output file, opening another"
        # close the current file and open the next one, reset byte counter
        df.close()
        df_num += 1
        bytes_written = 0
        df = open(destFolder + "/" + df_name + str(df_num) + df_ext, "wb")


    # write read data out to output file
    df.write(chunk)
    bytes_written += len(chunk)

print "closing input file"
sf.close()