
# with open('torrent_info', 'r') as file:
# 	infos = file.readlines()

# with open('torrent_info_server', 'r') as file:
# 	server_infos = file.readlines()

# info_dict = {info.split('=')[0].strip(): info.split('=')[1].strip() for info in infos}

# num = 0
# zero_num = 0
# for server_info in server_infos:
# 	name = server_info.split('=')[0].strip()
# 	size = server_info.split('=')[1].strip()

# 	if name not in info_dict:
# 		continue

# 	if size == '0':
# 		zero_num += 1
# 		content = 'name: {} \n  local:  {} \n  server: {}'.format(name, size, info_dict[name])
# 		print(content)

# 	if size != info_dict[name] or size == 0:

# 		num += 1
# 		content = 'name: {} \n  local:  {} \n  server: {}'.format(name, size, info_dict[name])
# 		print(content)
# print(zero_num)
# print(num)


with open('0807', 'r') as file:
	data1 = file.readlines()

with open('all', 'r') as file:
	data2 = file.readlines()

data1 = [x.strip() for x in data1]
data2 = [x.strip() for x in data2]

num = 0
for name in data1:
	if name not in data2:
		print(name)
		num += 1

print(num)





