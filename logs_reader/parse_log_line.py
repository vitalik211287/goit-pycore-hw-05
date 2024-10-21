from pathlib import Path
import re, sys
from collections import Counter


def reed_logs_from_file(path: str)-> list[str]:
    path_path = Path(path)
    with open(f"{path_path}", 'r') as log_file:               
        return log_file.readlines()



def parse_log_line(logs: list[str]):
    result_list = []  
    for log in logs:
        named_log_pattern = r'(?P<date_time>\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>[\w \.]+)'
        result_list.append(re.search(named_log_pattern, log).groupdict())
    return result_list



def count_logs_by_level(parsed_logs: list) -> dict:
    count = []
    count = [log['level'] for log in parsed_logs]
    counts = dict(Counter(count))
    return counts

def filter_logs_by_level(parsed_logs, all_ifo_log):
    print(f"Деталі логів для рівня '{all_ifo_log.upper()}':")
    [print(log) for log in parsed_logs if log["level"].lower() == all_ifo_log.lower()]



def display_log_counts(counts: dict):
    print(f"{'Level':<10} | {'Count':<5}")
    print("-" * 20)
    for level, count in counts.items():
        print(f"{level:<10} | {count:<5}")




log_file_path  = sys.argv[1]
all_ifo_log = sys.argv[2]
logs = reed_logs_from_file(log_file_path )      
parsed_logs = parse_log_line(logs)
log_counts  = count_logs_by_level(parsed_logs)
display_log_counts(log_counts )
filter_logs_by_level(parsed_logs, all_ifo_log)


