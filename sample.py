import subprocess

f = open("filename.txt")

for line in f:
    filename_old = "/data/avro/location2/" + line.strip()
    filename_new = filename_old.replace(".avr", ".avro")

    print "{0} {1}".format(filename_old, filename_new)

    print "hadoop fs -mv {0} {1}".format(filename_old, filename_new)

