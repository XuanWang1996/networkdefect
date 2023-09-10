import numpy as np

def read_txt(Address):
	data=np.loadtxt(Address)
	return data

def AdjustType(data):
	for i in range (0,len(data)):
		if data[i,2]==1:
			if data[i,4]==data[:,4].min() or data[i,4]==data[:,4].max() or data[i,5]==data[:,5].min() or data[i,5]==data[:,5].max():
				data[i,2]=4
	return data

def Choose_Cross_Atom(Coord):
	The_Cross_Atom=[]
	for i in range (0,len(Coord)):
		if Coord[i,2]==2:
			The_Cross_Atom.append(Coord[i,0])
	The_Cross_Atom=np.array(The_Cross_Atom)
	return The_Cross_Atom

def Choose_Atoms(Coord,Defect_Coord):
	The_Defect_Atoms=[]
	for i in range (0,len(Defect_Coord)):
		for j in range (0,len(Coord)):
			if Defect_Coord[i,0]==Coord[j,4] and Defect_Coord[i,1]==Coord[j,5]:
				The_Defect_Atoms.append(Coord[j,0])
				continue
	The_Defect_Atoms=np.array(The_Defect_Atoms)
	return The_Defect_Atoms

def Choose_Defect_Carbons(The_Defect_Atoms,bond):
	The_Defect_Carbon=[]
	for i in range (0,len(The_Defect_Atoms)):
		for j in range (0,len(bond)):
			if bond[j,2]==The_Defect_Atoms[i]:
				The_Defect_Carbon.append(bond[j,3])

			if bond[j,3]==The_Defect_Atoms[i]:
				The_Defect_Carbon.append(bond[j,2])

	The_Defect_Carbon=np.array(The_Defect_Carbon)

	return The_Defect_Carbon


if __name__=='__main__':
	Perfect_Coord_Address=r'I:\python\Atom_Stress_Evolution\network0.0.txt'
	Perfect_Bond_Address=r'I:\python\Atom_Stress_Evolution\bond0.0.txt'

	Perfect_Coord=read_txt(Perfect_Coord_Address)
	Perfect_Bond=read_txt(Perfect_Bond_Address)

	No_Defect=Choose_Cross_Atom(Perfect_Coord)

	for i in range (4,5):
		for j in [2.5]:
			print(j)
			Defect1_Address=r'I:\python\Atom_Stress_Evolution\Defect\_'+str(i)+'_Single_Defect_'+str(j)+'.txt'

			Defect1=read_txt(Defect1_Address)


			Perfect_Crosslink=Choose_Atoms(Perfect_Coord,Defect1)

			Perfect_Carbon=Choose_Defect_Carbons(Perfect_Crosslink,Perfect_Bond)

			Defect_Bond_Address=r'I:\python\Atom_Stress_Evolution\_4\bond'+str(j)+'.txt'

			Defect_Bond=read_txt(Defect_Bond_Address)

			Defect_Carbon=Choose_Defect_Carbons(Perfect_Crosslink,Defect_Bond)

			Defect_Atom=[]

			No_Defect_Atom=[]

			for index in No_Defect:
				if index not in Perfect_Crosslink:
					No_Defect_Atom.append(index)

			for index in Perfect_Carbon:
				if index not in Defect_Carbon:
					Defect_Atom.append(index)

			No_Defect_Atom=np.array(No_Defect_Atom)
			Defect_Atom=np.array(Defect_Atom)

			The_Tr_Address=r'I:\python\Atom_Stress_Evolution\_4\Stress_Atom_'+str(j)+'.txt'

			The_Tr=read_txt(The_Tr_Address)

			One_Structure_Result=np.zeros((int(len(The_Tr)/38420),3))

			for Frame in range (0,int(len(The_Tr)/38420)):
				print(Frame)
				Sum=0
				Sum_Cro=0
				Frame_Dat=The_Tr[Frame*38420:Frame*38420+38420,:]

				for De_C in Defect_Atom:
					De_Index=np.where(Frame_Dat[:,0]==De_C)
					Stress_3d=(Frame_Dat[De_Index[0],5]**2+Frame_Dat[De_Index[0],6]**2+Frame_Dat[De_Index[0],7]**2)**0.5
					Sum=Sum+Stress_3d

				for De_Cro in No_Defect_Atom:
					De_Cro_Index=np.where(Frame_Dat[:,0]==De_Cro)
					Stress_Cro_3d=(Frame_Dat[De_Cro_Index[0],5]**2+Frame_Dat[De_Cro_Index[0],6]**2+Frame_Dat[De_Cro_Index[0],7]**2)**0.5
					Sum_Cro=Sum_Cro+Stress_Cro_3d


				Ave_Stress_One_Frame=Sum/len(Defect_Atom)
				Ave_Cro_Stress_One_Frame=Sum_Cro/len(No_Defect_Atom)
				One_Structure_Result[Frame,0]=Frame
				One_Structure_Result[Frame,1]=Ave_Stress_One_Frame
				One_Structure_Result[Frame,2]=Ave_Cro_Stress_One_Frame

			Result_Address=r'I:\python\Atom_Stress_Evolution\_4\relax_'+str(j)+'.txt'

			np.savetxt(Result_Address,One_Structure_Result,fmt='%0.5f')