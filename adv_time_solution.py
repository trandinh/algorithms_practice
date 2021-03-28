# input 69:59:59
# output: b (convert to second)
def to_second(str_time):
	return int(str_time[0:2])*3600 + int(str_time[3:5])*60 + int(str_time[6:8])

#input "69:59:59-89:59:59"
#output: [a, b] (convert to second) 
def time_to_second(str_time):
	return (int(str_time[0:2])*3600 + int(str_time[3:5])*60 + int(str_time[6:8]), int(str_time[9:11])*3600 + int(str_time[12:14])*60 + int(str_time[15:]))

# Function to find the maximum subarray size k
def maxSubArraySum(arr, n, k):

	# Compute sum of first
	# window of size k
	res = 0
	res_idx = 0
	for i in range(k):
	    res += arr[i]
		
	# Compute sums of remaining windows by
	# removing first element of previous
	# window and adding last element of 
	# current window.
	curr_sum = res
	for i in range(k, n):
	    curr_sum += arr[i] - arr[i-k]
	    if curr_sum>res:
	    	res = curr_sum
	    	res_idx = i-k+1

	return res_idx


#from number to hour format
def second_to_str(nb_second):
	nb_hr = int(nb_second/(3600))
	left_sencond1 = nb_second - nb_hr*(3600)

	nb_minute = int(left_sencond1/60)
	left_second2 = left_sencond1 - nb_minute*60

	return '%02d:%02d:%02d'%(nb_hr, nb_minute, left_second2)


def solution(play_time, adv_time, logs):
	play_time_s =  to_second(play_time)
	adv_time_s =  to_second(adv_time)
	if play_time_s<=adv_time_s:
		return '00:00:00'

	logs_time_s = [time_to_second(l) for l in logs]


	time_value = [0]*play_time_s

	for i in range(len(logs_time_s)):
		for j in range(logs_time_s[i][0], logs_time_s[i][1]):
			time_value[j] += 1
		
	start = maxSubArraySum(time_value, len(time_value), adv_time_s)
	return  second_to_str(start)



arr = []
play_time = '00:00:10'
adv_time = '00:00:03'
logs = ['00:00:01-00:00:04', '00:00:05-00:00:07', '00:00:00-00:00:03']
arr.append((play_time, adv_time, logs))

play_time = "50:00:00"
adv_time = "49:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
arr.append((play_time, adv_time, logs))

play_time = "02:03:55"
adv_time = "00:14:15"
logs =  ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]
arr.append((play_time, adv_time, logs))

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59",  "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
arr.append((play_time, adv_time, logs))

for (play_time, adv_time, logs) in arr:
	print(solution(play_time, adv_time, logs))


