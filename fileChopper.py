import sys
import mailbox
import io

df_name = "../smallFile"
df_ext = ".mbox"
chunk_size = 4096
output_limit = 500 * 1000 * 1000 # 500 Mbytes
bytes_written = 0
df_num = 0
sf = open('../allMail.mbox', 'rb')
df = open(df_name + str(df_num) + df_ext, "wb")

while True:
    #print "reading"
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
        df = open(df_name + str(df_num) + df_ext, "wb")


    # write read data out to output file
    df.write(chunk)
    bytes_written += len(chunk)

print "closing input file"
sf.close()