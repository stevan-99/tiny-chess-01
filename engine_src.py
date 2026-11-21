_A='status';l='pnbrqk';k=tuple;g='Q';f='B';e='N';d=ord;c=max;b=next;a=enumerate;Z=range;V=sum;P=False;O=None;N='.';M='R';K=abs;J='P';G=True;F='K';from itertools import count;from collections import namedtuple as W;h={J:100,e:280,f:320,M:479,g:929,F:60000};D={J:(0,0,0,0,0,0,0,0,78,83,86,73,102,82,85,90,7,29,21,44,40,31,44,7,-17,16,-2,15,14,0,15,-13,-26,3,10,9,6,1,0,-23,-22,9,5,-11,-10,-2,3,-19,-31,8,-7,-37,-36,-14,3,-31,0,0,0,0,0,0,0,0),e:(-66,-53,-75,-75,-10,-55,-58,-70,-3,-6,100,-36,4,62,-4,-14,10,67,1,74,73,27,62,-2,24,24,45,37,33,41,25,17,-1,5,31,21,22,35,2,0,-18,10,13,22,18,15,11,-14,-23,-15,2,0,2,0,-23,-20,-74,-23,-26,-24,-19,-35,-22,-69),f:(-59,-78,-82,-76,-23,-107,-37,-50,-11,20,35,-42,-39,31,2,-22,-9,39,-32,41,52,-10,28,-14,25,17,20,34,26,25,15,10,13,10,17,23,17,16,0,7,14,25,24,15,8,25,20,15,19,20,11,6,7,6,20,16,-7,2,-15,-12,-14,-15,-10,-10),M:(35,29,33,4,37,33,56,50,55,29,56,67,55,62,34,60,19,35,28,33,45,27,25,15,0,5,16,13,18,-4,-9,-6,-28,-35,-16,-21,-13,-29,-46,-30,-42,-28,-42,-25,-25,-35,-26,-46,-53,-38,-31,-26,-29,-43,-44,-53,-30,-24,-18,5,-2,-18,-31,-32),g:(6,1,-8,-104,69,24,88,26,14,32,60,-10,20,76,57,24,-2,43,32,60,72,63,43,2,1,-16,22,17,25,20,-13,-6,-14,-15,-2,-5,-1,-10,-20,-22,-30,-6,-13,-11,-16,-11,-16,-27,-36,-18,0,-19,-15,-15,-21,-38,-39,-30,-31,-13,-31,-36,-34,-42),F:(4,54,47,-99,-99,60,83,-62,-32,10,55,56,56,55,10,3,-62,12,-57,44,-67,28,37,-31,-55,50,11,-4,-19,13,0,-49,-55,-43,-52,-28,-51,-47,-8,-50,-47,-42,-43,-79,-64,-32,-29,-32,-4,3,-14,-50,-57,-18,13,4,17,30,-3,-14,6,-1,40,18)}
for(Q,m)in D.items():n=lambda row:(0,)+k(A+h[Q]for A in row)+(0,);D[Q]=V((n(m[A*8:A*8+8])for A in Z(8)),());D[Q]=(0,)*20+D[Q]+(0,)*20
o,p=D[F],k(h[F]+70-10*(K(2*(A//10)-11)+K(2*(A%10)-9))for A in Z(120));L=47923;H=69290;I,R,S,T=91,98,21,28;q='         \n         \n rnbqkbnr\n pppppppp\n ........\n ........\n ........\n ........\n PPPPPPPP\n RNBQKBNR\n         \n         \n';A,B,E,C=-10,1,10,-1;r={J:(A,A+A,A+C,A+B),e:(A+A+B,B+A+B,B+E+B,E+E+B,E+E+C,C+E+C,C+A+C,A+A+C),f:(A+B,E+B,E+C,A+C),M:(A,B,E,C),g:(A,B,E,C,A+B,E+B,E+C,A+C),F:(A,B,E,C,A+B,E+B,E+C,A+C)};s=40;t=140;u=15;v=40;i=60;j=10**6;U=W('Move','i j prom')
class X(W('Position','board score wc bc ep kp')):
	def __hash__(A):return hash((A.board,A.wc,A.bc,A.ep,A.kp))
	def __eq__(A,o):return A.board==o.board and A.ep==o.ep and A.kp==o.kp and A.wc==o.wc and A.bc==o.bc
	def gen_moves(D):
		for(G,K)in a(D.board):
			if K not in'PNBRQK':continue
			for H in r[K]:
				for E in count(G+H,H):
					L=D.board[E]
					if L in' \nPNBRQK':break
					if K==J:
						if H in(A,A+A)and L!=N:break
						if H==A+A and(G<I+A or D.board[G+A]!=N):break
						if H in(A+C,A+B)and L==N and E not in(D.ep,D.kp,D.kp-1,D.kp+1):break
						if S<=E<=T:
							for M in'NBRQ':yield U(G,E,M)
							break
					yield U(G,E,'')
					if K in'PNK'or L in l:break
					if G==I and D.board[E+B]==F and D.wc[0]:yield U(E+B,E+C,'')
					if G==R and D.board[E+C]==F and D.wc[1]:yield U(E+C,E+B,'')
	def rotate(A,nullmove=P):B=nullmove;return X(A.board[::-1].swapcase(),-A.score,A.bc,A.wc,119-A.ep if A.ep and not B else 0,119-A.kp if A.kp and not B else 0)
	def move(G,move):
		D,C,W=move;V,a=G.board[D],G.board[C];H=lambda board,i,p:board[:i]+p+board[i+1:];B=G.board;L,O,U,Q=G.wc,G.bc,0,0;Y=G.score+G.value(move);B=H(B,C,B[D]);B=H(B,D,N);L=L[0]and D!=I,L[1]and D!=R;O=O[0]and C!=T,O[1]and C!=S
		if V==F:
			L=P,P
			if K(C-D)==2:Q=(D+C)//2;Z=I if C<D else R;B=H(B,Z,N);B=H(B,Q,M)
		if V==J:
			if S<=C<=T:B=H(B,C,W)
			if C-D==2*A:U=D+A
			if C==G.ep:B=H(B,C+E,N)
		return X(B[::-1].swapcase(),-Y,O,L,119-U if U else 0,119-Q if Q else 0)
	def value(G,move):
		C,A,N=move;H,L=G.board[C],G.board[A];B=D[H][A]-D[H][C]
		if L in l:B+=D[L.upper()][119-A]
		if K(A-G.kp)<2:B+=D[F][119-A]
		if H==F and K(C-A)==2:B+=D[M][(C+A)//2];B-=D[M][I if A<C else R]
		if H==J:
			if S<=A<=T:B+=D[N][A]-D[J][A]
			if A==G.ep:B+=D[J][119-(A+E)]
		return B
	def king_capture(A):return b((B for B in A.gen_moves()if A.board[B.j]=='k'or K(B.j-A.kp)<2),O)
class z:
	def __init__(A):A.tp_score,A.tp_move,A.history={},{},set();A.nodes=0
	def bound(B,pos,gamma,depth,root=P):
		M=root;D=gamma;C=depth;A=pos;B.nodes+=1;C=c(C,0)
		if A.score<=-L:return-H
		if not M:
			F=B.tp_score.get((A,C),[-H,H])
			if F[0]>=D:return F[0]
			if F[1]<D:return F[1]
			if C>0 and A in B.history:return 0
		def Q():
			F=B.tp_move.get(A)
			if not M and C>2 and K(A.score)<500 and any(B in A.board for B in'RBNQ'):
				E=-B.bound(A.rotate(nullmove=G),1-D,C-3);N=E>=D and(B.tp_move.get(A)or A.king_capture())
				if N and A.value(N)>=L:yield(N,H)
				elif E<D or B.bound(A.rotate(nullmove=G),1-L,C-3)>=1-L:yield(O,E)
			if C==0:yield(O,A.score)
			if not F and C>2:B.bound(A,D,C-3,root=G);F=B.tp_move.get(A)
			P=s-C*t
			if F and A.value(F)>=P:yield(F,-B.bound(A.move(F),1-D,C-1))
			for(R,(I,J))in a(sorted(((S,B)for B in A.gen_moves()if(S:=A.value(B))>=P),reverse=G)):
				if C<=1 and A.score+I<D:yield(J,H)if I>=L else(O,A.score+I);break
				Q=i and C>2 and R>2 and I<i;E=-B.bound(A.move(J),1-D,C-2 if Q else C-1)
				if Q and E>=D:E=-B.bound(A.move(J),1-D,C-1)
				yield(J,E)
		E,J=-H,P
		for(I,N)in Q():
			E=c(E,N);J|=I is not O and N>-H
			if E>=D:
				if I is not O and C:
					B.tp_move[A]=I
					
				break
		if C and not J and all(A.move(B).king_capture()for B in A.gen_moves()):E=-L if A.rotate(nullmove=G).king_capture()else 0
		if not M:B.tp_score[A,C]=[E,F[1]]if E>=D else[F[0],E]
		
		return E
	def search(A,history):
		K=history;A.nodes,A.history=0,set(K);A.tp_score.clear();E=A.root=K[-1];N=V(A.isupper()for A in E.board)==1 or V(A.islower()for A in E.board)==1;D[F]=p if N else o;I=0
		for L in Z(1,1000):
			B,C,M=1-H,H,0
			while B<C-u:
				J=A.bound(E,I,L,root=G)
				if J>=I:B=c(B,J)
				else:C=min(C,J)
				M+=1;yield(L,I,J,A.tp_move.get(E))
				if B>C or M>v:break
				I=(B+C+1)//2
def A0(c):return I+d(c[0])-d('a')-10*(int(c[1])-1)
def A1(i):return chr((i-I)%10+d('a'))+str(1-(i-I)//10)
def x(board,wc=(G,G),bc=(G,G),ep=0,kp=0):A=board;B=V(D[A][B]if A.isupper()else-D[A.upper()][119-B]for(B,A)in a(A)if A.isalpha());return X(A,B,wc,bc,ep,kp)
from os import environ;from http.client import HTTPConnection;import json;_c,_p=environ['MAKEFUN_ENV_URL'][7:].split(':');_q=lambda a,b:(lambda c:(c.request('POST',a,b),json.loads(c.getresponse().read()))[1])(HTTPConnection(_c,int(_p)))
while 1:
 _g=_q('/game','{}')
 if _g[_A]=='done':break
 while _g[_A]=='your_move':
  _f=[x(q)]
  for _m in _g['moves']:
   _i,_j=A0(_m[:2]),A0(_m[2:4])
   if len(_f)%2==0:_i,_j=119-_i,119-_j
   _f.append(_f[-1].move(U(_i,_j,_m[4:].upper())))
  _s=z();_s.node_cap=12e4;_b=_e=0
  try:
   for(_d,_gm,_sc,_mv)in _s.search(_f):
    if _d>1:_b,_e=_e or _b,_e
    if _s.nodes>=_s.node_cap and _b|_e:break
    if _sc>=_gm and _mv is not None:
     _i,_j=_mv.i,_mv.j
     if len(_f)%2==0:_i,_j=119-_i,119-_j
     _e=A1(_i)+A1(_j)+_mv.prom.lower()
  except:0
  _g=_q('/move','{"game":"%s","move":"%s"}'%(_g['game'],_b or _e or _g['legal_moves'][0]))