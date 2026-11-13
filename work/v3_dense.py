Z=len
Y=int
K=range
import json as h,os,sys,urllib.request as A1,random
F=100000
M=128
U=0,20,64,66,100,180,0
A5=(0,0,0,0,10,10,10,10,2,2,4,6,1,1,2,5,0,0,0,4,1,-1,-2,0,1,2,2,-4,0,0,0,0,-10,-8,-6,-6,-8,-4,0,0,-6,0,2,3,-6,1,3,4,-6,0,3,4,-6,1,2,3,-8,-4,0,1,-10,-8,-6,-6,-4,-2,-2,-2,-2,0,0,0,-2,0,1,2,-2,1,1,2,-2,0,2,2,-2,2,2,2,-2,1,0,0,-4,-2,-2,-2,0,0,0,0,1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,0,0,0,1,-4,-2,-2,-1,-2,0,0,0,-2,0,1,1,-1,0,1,1,0,0,1,1,-2,1,1,1,-2,0,1,0,-4,-2,-2,-1,-6,-8,-8,-10,-6,-8,-8,-10,-6,-8,-8,-10,-6,-8,-8,-10,-4,-6,-6,-8,-2,-4,-4,-4,4,4,0,0,4,6,2,0,-10,-8,-6,-4,-6,-4,-2,0,-6,-2,4,6,-6,-2,6,8,-6,-2,6,8,-6,-2,4,6,-6,-6,0,0,-10,-6,-6,-6)
a=[0]
for i in K(7):
	j=[]
	for H in K(8):k=A5[i*32+H*4:i*32+H*4+4];j+=k+k[::-1]
	a.append(j)
a2=a[:];a2[6]=a[7]
b=[0]*3328
for O in K(1,7):
	for P in K(128):
		if P&136:continue
		H,l=P>>4,P&7;b[(O+6)*128+P]=U[O]+a[O][(7-H)*8+l];b[(-O+6)*128+P]=-(U[O]+a[O][H*8+l]);b[1664+(O+6)*128+P]=U[O]+a2[O][(7-H)*8+l];b[1664+(-O+6)*128+P]=-(U[O]+a2[O][H*8+l])
H=random.Random(999)
G=[H.getrandbits(64)for A in K(1664)]
n=H.getrandbits(64)
c=[H.getrandbits(64)for A in K(16)]
d=[H.getrandbits(64)for A in K(8)]
m=-33,-31,-18,-14,14,18,31,33
o=-17,-16,-15,-1,1,15,16,17
e=-17,-15,15,17
f=-16,-1,1,16
p='abcdefgh'
q={4:3,116:12,0:2,7:1,112:8,119:4}
A=[0]*128
C=1
D=0
E=-1
L=0
B=0
I=0
J=0
V=[]
rp=[]
kl=[0]*256
def r(sq):return p[sq&7]+str((sq>>4)+1)
def s(m):B=r(m&127)+r(m>>7&127);A=m>>14&7;return B+('nbrq'[A-2]if A else'')
def A6(fen):
	global C,D,E,L,B,I,J,V
	for Q in K(128):A[Q]=0
	B=0;I=0;J=0;H=fen.split()
	for(R,S)in enumerate(H[0].split('/')):
		O=0
		for F in S:
			if F.isdigit():O+=Y(F)
			else:
				M=(7-R)*16+O;P='pnbrqk'.index(F.lower())+1;N=P if F.isupper()else-P;A[M]=N;B^=G[(N+6)*128+M]
				if N==6:I=M
				elif N==-6:J=M
				O+=1
	C=1 if H[1]=='w'else-1;D=0
	for F in H[2]:
		if F=='K':D|=1
		elif F=='Q':D|=2
		elif F=='k':D|=4
		elif F=='q':D|=8
	E=-1
	if H[3]!='-':E=(Y(H[3][1])-1)*16+p.index(H[3][0])
	L=Y(H[4])if Z(H)>4 else 0
	if C==-1:B^=n
	B^=c[D]
	if E>=0:B^=d[E&7]
	V=[]
	rp.clear();rp.append(B)
def Q(q,by):
	D=by
	for B in(q-15,q-17)if D>0 else(q+15,q+17):
		if not B&136 and A[B]==D:return 1
	for(F,C)in((m,2),(o,6)):
		for E in F:
			B=q+E
			if not B&136 and A[B]==D*C:return 1
	for E in e+f:
		B=q+E;T=3 if E in e else 4
		while not B&136:
			C=A[B]
			if C:
				if C==D*T or C==D*5:return 1
				break
			B+=E
	return 0
def t():return Q(I if C>0 else J,-C)
def W(cp=0):
	P=[];G=P.append;B=0
	def R(f,t):
		for A in(2,3,4,5):G(f|t<<7|A<<14)
	while B<128:
		if B&136:B+=8;continue
		J=A[B]
		if J==0 or(J>0)!=(C>0):B+=1;continue
		I=J if J>0 else-J
		if I==1:
			M=16 if C>0 else-16;V=1 if C>0 else 6;S=7 if C>0 else 0;K=B+M
			if not K&136 and A[K]==0:
				if K>>4==S:R(B,K)
				elif not cp:
					G(B|K<<7)
					if B>>4==V:
						T=B+2*M
						if A[T]==0:G(B|T<<7|4<<17)
			for N in(M-1,M+1):
				F=B+N
				if F&136:continue
				L=A[F]
				if L!=0 and(L>0)!=(C>0):
					if F>>4==S:R(B,F)
					else:G(B|F<<7)
				elif F==E:G(B|F<<7|1<<17)
		else:
			W=m if I==2 else o if I==6 else e if I==3 else f if I==4 else e+f;X=1 if 2<I<6 else 0
			for N in W:
				F=B+N
				while not F&136:
					L=A[F]
					if L==0:
						if not cp:G(B|F<<7)
					else:
						if(L>0)!=(C>0):G(B|F<<7)
						break
					if not X:break
					F+=N
		B+=1
	if not cp:
		for(H,O,Y,Z,U)in((4,6,7,1,5),(4,2,0,2,3),(116,118,119,4,117),(116,114,112,8,115)):
			if D&Z and A[H]==(6 if H<16 else-6)and A[Y]==(4 if H<16 else-4)and A[U]==0 and A[O]==0 and not Q(H,-C)and not Q(U,-C)and not Q(O,-C)and(O-H==2 or A[H-3]==0):G(H|O<<7|2<<17)
	return P
def X(m):
	global C,D,E,L,B,I,J;K=m&127;F=m>>7&127;T=m>>14&7;P=m>>17;H=A[K];O=C;M=A[F];N=F
	if P&1:N=F-16 if O>0 else F+16;M=A[N]
	V.append((m,H,M,N,D,E,L,B,I,J));B^=G[(H+6)*128+K]
	if M:B^=G[(M+6)*128+N];A[N]=0
	A[K]=0
	if P&2:
		R1=F+1 if F&7==6 else F-2;R2=F-1 if F&7==6 else F+1;R3=4 if F<16 else-4;A[R1]=0;A[R2]=R3;B^=G[(R3+6)*128+R1]^G[(R3+6)*128+R2]
	if T:U=T*O;A[F]=U;B^=G[(U+6)*128+F]
	else:A[F]=H;B^=G[(H+6)*128+F]
	if H==6:I=F
	elif H==-6:J=F
	S=D&~q.get(K,0)&~q.get(F,0)
	if S!=D:B^=c[D]^c[S];D=S
	if E>=0:B^=d[E&7]
	if P&4:E=K+16 if O>0 else K-16;B^=d[E&7]
	else:E=-1
	L=0 if(H if H>0 else-H)==1 or M else L+1;B^=n;C=-O;rp.append(B)
	if Q(I if H>0 else J,C):R();return 0
	return 1
def R():
	global C,D,E,L,B,I,J;G,M,H,N,O,P,Q,R,S,T=V.pop();U=G&127;F=G>>7&127;K=G>>17;A[U]=M;A[F]=0
	if K&1:A[N]=H
	elif H:A[F]=H
	if K&2:
		R1=F+1 if F&7==6 else F-2;R2=F-1 if F&7==6 else F+1;A[R1]=4 if F<16 else-4;A[R2]=0
	D=O;E=P;L=Q;B=R;I=S;J=T;C=-C;rp.pop()
def u():
	B=0;D=0;E=0;P=0;wb=0;bb=0
	while B<128:
		if B&136:B+=8;continue
		F=A[B]
		if F:
			G=(F+6)*128+B;D+=b[G];E+=b[1664+G];P+=(0,0,1,1,2,4,0)[abs(F)]
			if F==3:wb+=1
			elif F==-3:bb+=1
		B+=1
	if wb>1:D+=6
	if bb>1:D-=6
	H=min(P,24);S=(D*H+E*(24-H))//24
	return S if C>0 else-S
g={}
S=[0]
T=[0]
N=[0]
def v(ms,pl,tm):
	E=[]
	for(G,B)in enumerate(ms):
		C=0;H=B>>7&127;D=A[H]
		if D:C=100000+10*U[abs(D)]-abs(A[B&127])
		elif B>>17&1:C=101000-abs(A[B&127])
		F=B>>14&7
		if F:C+=200000+U[F]
		if B==tm:C=1000000
		elif C==0:
			if B==kl[pl*2]:C=90000
			elif B==kl[pl*2+1]:C=80000
		E.append((-C,G,B))
	E.sort();ms[:]=[A[2]for A in E]
def w(a,be,pl):
	S[0]+=1
	if T[0]and S[0]>=T[0]:N[0]=1;return 0
	if pl>=M:return u()
	D=t();C=-F-1
	if not D:
		B=u()
		if B>=be:return B
		C=B
		if B>a:a=B
	E=W(1)if not D else W(0);v(E,pl,0);G=0
	for H in E:
		if not X(H):continue
		G+=1;A=-w(-be,-a,pl+1);R()
		if N[0]:return 0
		if A>C:C=A
		if A>=be:return A
		if A>a:a=A
	if D and G==0:return-F+pl
	return C
def x(d,a,be,pl):
	G=be
	if pl>0 and L>=100 or rp.count(B)>1:return 0
	if d<=0 or pl>=M:return w(a,G,pl)
	S[0]+=1
	if T[0]and S[0]>=T[0]:N[0]=1;return 0
	l=t()
	I=g.get(B);J=0
	if I is not None:
		U,H,E,V=I;J=V
		if U>=d:
			D=E-pl if E>F-M else E+pl if E<-F+M else E
			if H==1 or H==2 and D>=G or H==3 and D<=a:return D
	Y=a;K=W();v(K,pl,J);O=0;C=-F-1;P=0
	for Q in K:
		J=A[Q>>7&127]or Q>>17&1 or Q>>14&7
		if not X(Q):continue
		O+=1
		if d>=3 and O>3 and not l and not J:
			D=-x(d-2,-G,-a,pl+1)
			if not N[0] and D>a:D=-x(d-1,-G,-a,pl+1)
		else:D=-x(d-1,-G,-a,pl+1)
		R()
		if N[0]:return 0
		if D>C:C=D;P=Q
		if D>a:a=D
		if a>=G:
			if not J:
				if kl[pl*2]!=Q:kl[pl*2+1]=kl[pl*2];kl[pl*2]=Q
			break
	if O==0:return-F+pl if l else 0
	H=3 if C<=Y else 2 if C>=G else 1;E=C+pl if C>F-M else C-pl if C<-F+M else C;g[B]=d,H,E,P;return C
A7=Y(os.environ.get('CHESS_NODES','60000'))
A8=12
def A9(nodes=A7,maxd=A8):
	A=[]
	for B in W():
		if X(B):A.append([B,0]);R()
	if Z(A)==1:return s(A[0][0])
	g.clear();S[0]=0;I=A[0][0]
	for J in K(1,maxd+1):
		T[0]=0 if J==1 else nodes;N[0]=0;E=-F-1
		for G in A:
			B=G[0]
			if not X(B):G[1]=-F;continue
			H=-x(J-1,-F-1,-E,1);R()
			if N[0]:break
			G[1]=H
			if H>E:E=H
		if N[0]:break
		A.sort(key=lambda x:-x[1]);I=A[0][0]
		if A[0][1]>=F-M:break
	return s(I)
y=os.environ.get('MAKEFUN_ENV_URL')or''
def z(p,b):
	with A1.urlopen(y+p,h.dumps(b).encode())as r:return h.load(r)
def AA(g):
	A6(g['fen'])
	n3=A7//3 if g.get('plies',0)>120 else A7
	try:return A9(n3)
	except Exception:return g['legal_moves'][0]
def AB():
	C='game';B='status'
	if not y:sys.exit('MAKEFUN_ENV_URL is not set')
	while 1:
		A=z('/game',{})
		if A[B]=='done':break
		while A[B]=='your_move':A=z('/move',{C:A[C],'move':AA(A)})
if __name__=='__main__':AB()