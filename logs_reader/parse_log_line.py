from pathlib import Path
import re
import sys

def reed_logs_from_file(path: str)-> list[str]:
    with open(f"{path}", 'r') as log_file:
        # print(log_file.readlines())                 
        return log_file.readlines()



def parse_logs(logs: list[str]):
    result_list = []  
    for log in logs:
        named_log_pattern = r'(?P<date_time>\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>[\w \.]+)'
        result_list.append(re.search(named_log_pattern, log).groupdict())
    return result_list






# path = sys.argv[1]
path = Path( sys.argv[1])
print(path)
logs = reed_logs_from_file(path)
parsed_logs = parse_logs(logs)



for log in parsed_logs:
    print(log['level']) 