function Level=xu15(A,maxL)
%A: The edge matrix
%maxL: the number of nodes

D=zeros(1,maxL); %D(i): degree of node i

[m,n]=size(A);

for i=1:maxL
    for j=1:m
        if(i==A(j,1)|i==A(j,2))
            D(i)=D(i)+1;
        end
    end
end

leaf=zeros(1,1000);

tag=1;

for i=1:maxL
    if(D(i)==1)
        leaf(tag)=i;
        tag=tag+1;
    end
end
leaf=leaf(1:tag-1);
num=length(leaf);


icur=0;

tagL=1;

for i=1:num  % leaf i
    Level=zeros(maxL,1);
    icur=leaf(i);
    Level(icur)=1;
    tag=1;

   

    while(length(find(Level~=0))<maxL)
  % for jj=1:100
         icurtemp=zeros(1,3000);
         tag1=1;
        mcur=length(icur);
        for k=1:mcur
            [row,col]=find(A==icur(k));

            mm=length(row);
            for j=1:mm
                if(Level(A(row(j),3-col(j)))==0)
                    Level(A(row(j),3-col(j)))=Level(icur(k))+1;
                    icurtemp(tag1)=A(row(j),3-col(j));
                    tag1=tag1+1;
                    tag=tag+1;
                end

            end

        end

        icurtemp=icurtemp(1:tag1-1);

        icur=icurtemp;


    end
        final(i,:)=Level;
end

[xv,pv]=prob(Level);

plot(xv,pv,'o')




function [xv,pv]=prob(X)
n=length(X);
xmin=min(X);
xmax=max(X);
dx=(xmax-xmin)/20;
xv=xmin+dx:dx:xmax;
m=length(xv);
pv=zeros(1,m);
for i=1:n
    for j=1:m
        if(X(i)>xv(j)-dx&X(i)<=xv(j))
            pv(j)=pv(j)+1;
        end
    end
end

temp=trapz(pv)*dx;

pv=pv/temp;




