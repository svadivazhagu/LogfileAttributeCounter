from collections import defaultdict

def scan_file(fname):
    #creating a dictionary to map the hosts to their requests in the log, Key = hostname, Value = NumRequests (integer)
    hosts_req = defaultdict(int)
    #opening the logfile via provided fname now
    with open(fname) as logfile:
        #go through each line in the logfile and map it to the dictionary hosts_req
        for line in logfile:
            #split each line into an element in a List logfile_lines 
            logfile_lines = line.split()
            #map each record to its corresponding host and increment host of the request line
            hosts_req[logfile_lines[0]] += 1
    
    #now open output file "records_" followed by the fname like "records_hosts_access_log_00.txt"
    output_file = open("records_"+fname+"., "w")
    #start loop to write the key value pairing of <hostname, numRequests> to this output file
    for host in hosts_req:
        #format is the hostname followed by one space followed by the numRequests for that host, endline. cast numRequests to String.
        output_file.write(host+" "+str(hosts_req[host])+"\n")
    output_file.close()

#filename will be read in from stdin so
input_file = input()
scan_file(input_file)