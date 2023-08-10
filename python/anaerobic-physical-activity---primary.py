# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"1388.00","system":"readv2"},{"code":"1389.00","system":"readv2"},{"code":"138A.00","system":"readv2"},{"code":"138B.00","system":"readv2"},{"code":"138C.00","system":"readv2"},{"code":"138D.00","system":"readv2"},{"code":"138E.00","system":"readv2"},{"code":"138F.00","system":"readv2"},{"code":"138P.00","system":"readv2"},{"code":"138Q.00","system":"readv2"},{"code":"138R.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('physical-activity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anaerobic-physical-activity---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anaerobic-physical-activity---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anaerobic-physical-activity---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
