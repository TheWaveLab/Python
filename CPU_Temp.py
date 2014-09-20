# -*- encoding:utf-8 -*-

def Get_cpu_temp():
	fp = open("/sys/class/thermal/thermal_zone0/temp")
	cpu_temp = fp.read()
	fp.close()
	return float(cpu_temp)/1000

if __name__ == '__main__':
	print "CPU Tempature is %s"%str(Get_cpu_temp())

