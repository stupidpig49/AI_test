#coding=utf-8
import os
def doRename(list_len):
	fi_num_cnt = 1
	input_max_len = max(list_len)
	
	for ifile in ext_list:
		if fi_num_cnt<10:
			new_name = "00000"+str(fi_num_cnt)+'.'+ext
		if 10<=fi_num_cnt<100:
			new_name = "0000"+str(fi_num_cnt)+'.'+ext
		if 100<=fi_num_cnt<1000:
			new_name = "000"+str(fi_num_cnt)+'.'+ext
		print ifile.rjust(input_max_len,''),3*'','重命名为:'.ljust(5,''),new_name.rjust(10,'')
		try:
			os.rename(ifile,newname)
		except Exception,e:
			print e
		fi_num_cnt+=1
if __name__ =='__main__':
	while True:
		ext = raw_input("请输入要批量命名的文件后缀名：如jpg、txt。直接回车则退出程序！\n")
		if ext == '':
			exit()
		allFiles = os.listdir(os.curdir)
		ext_list=[]
		list_len=[]
		for ifile in allFiles:
			if os.path.isfile(ifile) and os.path.splitext(ifile)[1][1:].lower()==ext and ifile != os.path.basename(__file__):
				ext_list.append(ifile)
				list_len.append(len(ifile))
		if len(ext_list)==0:
			print '未发现 *.',ext,'类型的文件'
		else:
			break

	print '找到如下*.',ext,'文件:'
	for ifile in ext_list:
		print ifile
	print 25*'*'

	while True and len(ext_list)!=0:
		choice = raw_input('您确定要对这些文件批量重命名吗？（Y/y或直接回车--确定，N/n--取消）\n')
		if choice=='' or choice=='Y' or choice=='y':
			basic='0000'
			i=0
			for ifile in ext_list:
				if i<10:
					temp='0'+str(i)
					newname=basic+temp+'.jpg'
				else:
					newname=basic+str(i)+'.jpg'
				os.rename(ifile,newname)
				i+=1
			print '处理完毕！'
			raw_input()
			break
		elif choice=='N' or choice=='n':
			break
