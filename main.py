import os
import sys
from datetime import datetime
import requests as requests


def date_difference_in_days(date1_str, date2_str):
    date1 = datetime.fromisoformat(date1_str.replace('Z', '+00:00'))
    date2 = datetime.fromisoformat(date2_str.replace('Z', '+00:00'))
    difference = date2 - date1

    return difference.days


def find_mean(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)


def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]


github_token = os.environ['GITHUB_GPG_KEY']
url = f"{sys.argv[1]}issues"

params = {
    "state": "closed",
    "per_page": 100,
}

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

all_issues = []
while True:
    response = requests.get(url, params=params, headers=headers)
    issues = response.json()
    filtered_issues = [issue for issue in issues if
                       not any('enhancement' in label['name'] for label in issue['labels'])]
    issues = [filtered_issue for filtered_issue in filtered_issues if
              not any('new feature' in label['name'] for label in filtered_issue['labels'])]
    all_issues.extend(issues)
    if 'next' in response.links:
        url = response.links['next']['url']
    else:
        break

days = list()
for r in all_issues:
    date_diff = date_difference_in_days(r['created_at'], r['closed_at'])
    if date_diff != 0:
        days.append(date_diff)
print(f"Median:{find_median(days)}")
print(f"Mean: {find_mean(days)}")


