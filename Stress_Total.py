import numpy as np

def read_txt(Address):
	data=np.loadtxt(Address)
	return data


if __name__=='__main__':
	N=int(input("请输入粒子数："))
	for defect in [2.5,5.0,7.5,10.0,12.5]:
		print(defect)
		Address=r'I:\netdefect\50_network\relax_dangling_stress\2\Stress_Atom_'+str(defect)+'.txt'
		data=read_txt(Address)
		Frames=int(len(data)/N)
		Defect_Atom_Address=r'I:\python\Atom_Stress_Evolution\_2\tensile\Result_'+str(defect)+'_2.txt'
		Defect_Atoms=read_txt(Defect_Atom_Address)
		Result_Stress=np.zeros(shape=(Frames,1))
		Defect_Stress=np.zeros(shape=(Frames,1))
		Nodefect_Stress=np.zeros(shape=(Frames,1))
		#sumx=0
		#sumy=0
		sumz=0
		for Frame in range (0,Frames):
			#Defectx=0
			#Defecty=0
			Defectz=0
			Frame_data=data[Frame*N:Frame*N+N,:]
			#sumx=sum(Frame_data[:,5])
			#sumy=sum(Frame_data[:,6])
			sumz=sum(Frame_data[:,7])
			Result_Stress[Frame,0]=sumz/N
			#Result_Stress[Frame,1]=sumy
			#Result_Stress[Frame,2]=sumz

			for i in range (0,len(Defect_Atoms)):
				Defect_Index=np.where(Frame_data[:,0]==Defect_Atoms[i])
				print(Defect_Index[0])
				#Defectx=Defectx+Frame_data[Defect_Index[0][0],5]
				#Defecty=Defecty+Frame_data[Defect_Index[0][0],6]
				Defectz=Defectz+Frame_data[Defect_Index[0][0],7]
			#Defect_Index=np.where(Frame_data[:,0]==Defect_Atoms)
			#print(Defect_Index[0])
			#Defectx=sum(Frame_data[Defect_Index[0],5])
			#Defecty=sum(Frame_data[Defect_Index[0],6])
			#Defectz=sum(Frame_data[Defect_Index[0],7])

			#Defect_Stress[Frame,0]=Defectx
			#Defect_Stress[Frame,1]=Defecty
			Defect_Stress[Frame,0]=(Defectz)/len(Defect_Atoms)

			#Nodefect_Stress[Frame,0]=sumx-Defectx
			#Nodefect_Stress[Frame,1]=sumy-Defecty
			Nodefect_Stress[Frame,0]=(sumz-Defectz)/(N-len(Defect_Atoms))


		Result_Address=r'I:\netdefect\50_network\relax_dangling_stress\2\Total_Result_'+str(defect)+'.txt'
		Defect_Address=r'I:\netdefect\50_network\relax_dangling_stress\2\Defect_Result_'+str(defect)+'.txt'
		Nodefect_Address=r'I:\netdefect\50_network\relax_dangling_stress\2\Nodefect_Result_'+str(defect)+'.txt'
		np.savetxt(Result_Address,Result_Stress,fmt='%0.5f')
		np.savetxt(Defect_Address,Defect_Stress,fmt='%0.5f')
		np.savetxt(Nodefect_Address,Nodefect_Stress,fmt='%0.5f')

