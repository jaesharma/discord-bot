import os

# Set environment variables
os.environ['client_id'] = '_EtunUH8kMdJ-g'
os.environ['client_secret'] = 'ZzW7E0fmJ7jhDnjKGUCzAfVGWvU'
os.environ['token']='NjM1MTk2MDk1MDM4NzUwNzUw.Xa40Lw.lxsPhzO5Ri_2_MpJKLzm2VLHTs4'
def getuser():
	return os.getenv('client_id')

def getsecret():
	return os.getenv('client_secret')

def gettoken():
	return os.getenv('token')