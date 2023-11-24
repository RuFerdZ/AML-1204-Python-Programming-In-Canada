import time

gm_time = time.gmtime()
print(gm_time)
print(gm_time.tm_year)
print(f"{gm_time.tm_year}-{gm_time.tm_mon}-{gm_time.tm_mday}")
print(f"{gm_time.tm_hour}:{gm_time.tm_min}:{gm_time.tm_sec}")

# looks the device timezone and display time formatted
asc_time = time.asctime()
print(asc_time)
print(type(asc_time))
print(asc_time.split(" "))

c_time = time.ctime()
print(c_time)
print(type(c_time))

# def complex_function():
#     j = 0
#     n = 2
#     for i in range(5):
#         print(f"iteration {i}")
#         j += i
#         print(f"waiting for {n} seconds...\n")
#         time.sleep(n)
#
# start_time = time.time()
# complex_function()
# end_time = time.time()
# print("the runtime :", round(end_time - start_time, 2))


# string to date
my_str_time = "2023/11/24 10:21:56"
print(type(my_str_time))
formatted_time = time.strptime(my_str_time, "%Y/%m/%d %H:%M:%S")
print(formatted_time)
print(type(formatted_time))

