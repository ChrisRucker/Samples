file_handle = open('vcal.txt')                             # load dataset 

count = 0                                                  # initialize variables                  
count_cn = 0
count_sy = 0
count_id = 0

for line_cn in file_handle:                                # iterate dataset
    line_cn = line_cn.rstrip()
    if not line_cn.startswith('ORGANIZER;'):
        continue
    pos = line_cn.find(':')
    print 'meetingOrganizer:', line_cn[13:pos+0]
    count_cn = count_cn + 1
    file_handle = open('vcal.txt')                             
    for line_id in file_handle:                         
        line_id = line_id.rstrip()
        if not line_id.startswith('ORGANIZER;'):
            continue
        pos = line_id.find(':mailto')
        print 'meetingOrganizerID:', line_id[pos+8:]
        count_id = count_id + 1
        for line_sy in file_handle:
            line_sy = line_sy.rstrip()
            if not line_sy.startswith('SUMMARY;'):
                continue
            pos = line_sy.find(':')
            print 'meetingSummary:', line_sy[23:]
            count_sy = count_sy + 1
            for line in file_handle:
                line = line.rstrip()
                if not line.startswith('DTSTART;'):
                    continue
                word = line.split()
                count = count + 1
    
time = word[2]                                            # initialize variables                                   
time_pm = int(time[14:18]) - 1200
time_am = int(time[14:18]) 
    
if time_am < 1200:                                        # use logic                               
    print "meetingStartTime:", time_am, "AM EST"
else:
    print "meetingStartTime:", time_pm, "PM EST"