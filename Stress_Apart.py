import numpy as np

def read_txt(Address):
	data=np.loadtxt(Address)
	return data


if __name__=='__main__':
	N=int(input("请输入粒子数："))
	for defect in [5.0,7.5]:
		print(defect)
		Address=r'I:\python\Atom_Stress_Evolution\Stress_Apart\3\_'+str(defect)+'_3.txt'
		data=read_txt(Address)
		Defect_Atom_Address=r'I:\python\Atom_Stress_Evolution\_3\tensile\Result_'+str(defect)+'_3.txt'
		Network_Address=r'I:\python\Atom_Stress_Evolution\_3\tensile\Total_Result_'+str(defect)+'.txt'
		Defect_Address=r'I:\python\Atom_Stress_Evolution\_3\tensile\Defect_Result_'+str(defect)+'.txt'
		Nodefect_Address=r'I:\python\Atom_Stress_Evolution\_3\tensile\Nodefect_Result_'+str(defect)+'.txt'

		Defect_Atoms=read_txt(Defect_Atom_Address)
		Defect_Stress=read_txt(Defect_Address)
		Nodefect_Stress=read_txt(Nodefect_Address)
		Network_Stress=read_txt(Network_Address)
		Frames1=int(len(Network_Stress[:,0]))
		Frames2=int(len(data[:,0])/N)
		Frames=min(Frames1,Frames2)

		Result_Stress_List=np.zeros(shape=(Frames,6))
		Defect_Stress_List=np.zeros(shape=(Frames,6))
		Nodefect_Stress_List=np.zeros(shape=(Frames,6))
		sumx=0
		sumy=0
		sumz=0
		for Frame in range (0,Frames):
			print(Frame)
			Defectx=0
			Defecty=0
			Defectz=0
			Frame_data=data[Frame*N:Frame*N+N,:]
			sumx=sum(-Frame_data[:,5]**2)
			sumy=sum(-Frame_data[:,6]**2)
			sumz=sum(-Frame_data[:,7]**2)
			Result_Stress_List[Frame,0]=sumx/N
			Result_Stress_List[Frame,1]=sumy/N
			Result_Stress_List[Frame,2]=sumz/N
			Result_Stress_List[Frame,3]=(Network_Stress[Frame,0]-sumx)/N
			Result_Stress_List[Frame,4]=(Network_Stress[Frame,1]-sumy)/N
			Result_Stress_List[Frame,5]=(Network_Stress[Frame,2]-sumz)/N

			for i in range (0,len(Defect_Atoms)):
				Defect_Index=np.where(Frame_data[:,0]==Defect_Atoms[i])
				Defectx=Defectx-Frame_data[Defect_Index[0][0],5]**2
				Defecty=Defecty-Frame_data[Defect_Index[0][0],6]**2
				Defectz=Defectz-Frame_data[Defect_Index[0][0],7]**2
			#Defect_Index=np.where(Frame_data[:,0]==Defect_Atoms)
			#print(Defect_Index[0])
			#Defectx=sum(Frame_data[Defect_Index[0],5])
			#Defecty=sum(Frame_data[Defect_Index[0],6])
			#Defectz=sum(Frame_data[Defect_Index[0],7])

			#print(Defectx,Defecty,Defectz)

			Defect_Stress_List[Frame,0]=Defectx/len(Defect_Atoms)
			Defect_Stress_List[Frame,1]=Defecty/len(Defect_Atoms)
			Defect_Stress_List[Frame,2]=Defectz/len(Defect_Atoms)
			Defect_Stress_List[Frame,3]=(Defect_Stress[Frame,0]-Defectx)/len(Defect_Atoms)
			Defect_Stress_List[Frame,4]=(Defect_Stress[Frame,1]-Defecty)/len(Defect_Atoms)
			Defect_Stress_List[Frame,5]=(Defect_Stress[Frame,2]-Defectz)/len(Defect_Atoms)

			Nodefect_Stress_List[Frame,0]=(sumx-Defectx)/(N-len(Defect_Atoms))
			Nodefect_Stress_List[Frame,1]=(sumy-Defecty)/(N-len(Defect_Atoms))
			Nodefect_Stress_List[Frame,2]=(sumz-Defectz)/(N-len(Defect_Atoms))
			Nodefect_Stress_List[Frame,3]=(Nodefect_Stress[Frame,0]-(sumx-Defectx))/(N-len(Defect_Atoms))
			Nodefect_Stress_List[Frame,4]=(Nodefect_Stress[Frame,1]-(sumy-Defecty))/(N-len(Defect_Atoms))
			Nodefect_Stress_List[Frame,5]=(Nodefect_Stress[Frame,2]-(sumz-Defectz))/(N-len(Defect_Atoms))


		Network_Result_Address=r'I:\python\Atom_Stress_Evolution\Stress_Apart\3\Total_Apart_'+str(defect)+'.txt'
		Defect_Result_Address=r'I:\python\Atom_Stress_Evolution\Stress_Apart\3\Defect_Apart_'+str(defect)+'.txt'
		Nodefect_Result_Address=r'I:\python\Atom_Stress_Evolution\Stress_Apart\3\Nodefect_Apart_'+str(defect)+'.txt'
		np.savetxt(Network_Result_Address,Result_Stress_List,fmt='%0.5f')
		np.savetxt(Defect_Result_Address,Defect_Stress_List,fmt='%0.5f')
		np.savetxt(Nodefect_Result_Address,Nodefect_Stress_List,fmt='%0.5f')