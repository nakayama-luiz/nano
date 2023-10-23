import user
import work
import time

perfeitio = time.localtime()
print(perfeitio.tm_year)
supinpa = str(perfeitio.tm_year) +'-' +str(perfeitio.tm_mon)+'-' + str(perfeitio.tm_mday)
print(supinpa)


# print(work.update_work_total(2))
