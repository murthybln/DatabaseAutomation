db_conn1 = "DRIVER={SQL SERVER};server=192.168.18.36;database=Maverick;uid=narasimha;pwd=Welcome321;"

db_conn = "DRIVER={SQL SERVER};server=192.168.18.36;database=Maverick;Trusted_Connection=yes;"
query_fail = """SELECT * FROM dbo.Employee"""


query_pass = """SELECT * FROM dbo.Employee where aGE = 21"""
