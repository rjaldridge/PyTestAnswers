
import re

def stopwatch(t1,t2):
  match_obj1 = re.match(r'([0-5][0-9]):([0-5][0-9]):([0-9][0-9])',t1)

	match_obj2 = re.match(r'([0-5][0-9]):([0-5][0-9]):([0-9][0-9])',t2)

	if match_obj1 and match_obj2:
		t1_total_hs = (60 * 100 * int(match_obj1.group(1))) + \
		(100 * int(match_obj1.group(2))) + int(match_obj1.group(3))

		t2_total_hs = (60 * 100 * int(match_obj2.group(1))) + \
		(100 * int(match_obj2.group(2))) + int(match_obj2.group(3))

		avg = (t1_total_hs + t2_total_hs) / 2

		avg_hs = avg % 100
		avg /= 100
		avg_ss = avg % 60
		avg /= 60
		avg_mm = avg 

		avg_t = format("%02d:%02d:%02d" % (avg_mm, avg_ss, avg_hs))

		return avg_t
	
	return None


print ("%s" % stopwatch("15:12:01","15:12:05"))

