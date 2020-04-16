import requests
import hashlib
import sys

def reqeust_api_data(query_check):
    url="https://api.pwnedpasswords.com/range/"+query_check
    res=requests.get(url)
    if res.status_code!=200:
        raise Exception(f'Error Fetching {res.status_code}')
    return res
def get_pass_leaks_counts(hash,hash_to_check):

    hash=(i.split(':') for i in hash.text.splitlines())
    for key,val in hash:
        if key==hash_to_check:
            return val
    return 0

def request_sh1_check(password):
    shapassword=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_fivechar,tail=shapassword[:5],shapassword[5:]
    res=reqeust_api_data(first_fivechar)
    return get_pass_leaks_counts(res,tail)

def main(args):
    for passi in args:
        no=request_sh1_check(passi)
        if no:
            print(f'This password used {no} times please dont use it')
        else:
            print(passi+" IS the secure password")
main(sys.argv[1:])


