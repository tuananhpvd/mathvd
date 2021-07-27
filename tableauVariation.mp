% This software is copyright (c) 2005 by Frédéric Mazoit
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 2 of the License, or
% any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.



deltaX=10pt;
deltaY=5pt;
deltaYvariations=20pt;
deltaXsignes=30pt;

Variables_=0;
Signes_=1;
Variations_=2;

Plus_=0;
Moins_=1;
Fleche_=2;
Valeur_=3;
ValeurBarree_=4;
Vide_=5;
Barre_=6;
NonDefBarre_=7;
NonDefRegion_=8;
VidePos_=9;
Trait_=10;

def mkLabel(expr x)=
  if picture x: x
  else: x infont defaultfont scaled defaultscale fi
enddef;



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def exists(expr i,j)=
  known typeEl.[i][j]c
enddef;

def getH(expr x)= if known x: ypart(ulcorner x-llcorner x) else: 0 fi enddef;
def getL(expr x)= if known x: xpart(urcorner x-ulcorner x) else: 0 fi enddef;

vardef getHcase(expr i,j)=
  max(
    max(
      deltaY,
      if known el.[i][j]l: getH(el.[i][j]l) else: 0 fi),
    max(
      if known el.[i][j]c: getH(el.[i][j]c) else: 0 fi,
      if known el.[i][j]r: getH(el.[i][j]r) else: 0 fi)
    )
enddef;

vardef getMcase(expr i,j)=
  save type;

  if exists(i,j):
    type:=typeEl.[i][j]c;

    if (type=Plus_) or (type=Moins_) or (type=Fleche_) or (type=NonDefRegion_):
      .5deltaXsignes+.5deltaX
    elseif (type=NonDefBarre_): 2pt+.5deltaX
    elseif (type=Barre_) or (type=Vide_): 0
    else: .5deltaX+if known el.[i][j]c:.5getL(el.[i][j]c) else: 0 fi
    fi
  else: 0 fi
enddef;

vardef getGcase(expr i,j)=
  getMcase(i,j)+ if known el.[i][j]l:getL(el.[i][j]l) else: 0 fi
enddef;

vardef getDcase(expr i,j)=
  getMcase(i,j)+ if known el.[i][j]r:getL(el.[i][j]r) else: 0 fi
enddef;

vardef getGcol(expr col)=
  save res,i;
  res=0;
  for i=1 upto nbLgn: res:=max(res,getGcase(i,col)); endfor;
  res
enddef;

vardef getDcol(expr col)=
  save res,i;
  res=0;
  for i=1 upto nbLgn: res:=max(res,getDcase(i,col)); endfor;
  res
enddef;

vardef getHelsLgn(expr line)=
  save res, j;
  res:=11pt;
  for j=0 upto nbCol: res:=max(res,getHcase(line,j)); endfor;
  res
enddef;

vardef getHLgn(expr line)=
  if typeLgn[line]=Variations_:
    max(getHelsLgn(line)+deltaYvariations,40pt)+deltaY
  else:
    getHelsLgn(line)+deltaY
  fi
enddef;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def valSmp_(expr s,type,b)=
  vd:=0;
  col:=col+1;
  if col>nbCol: nbCol:=col; fi;

  typeEl.[nbLgn][col]c=type;
  pos.[nbLgn][col]c=b;
  el.[nbLgn][col]c=mkLabel(s);
enddef;

def sgnSmp_(expr s)=
  vd:=0;
  col:=col+1;
  if col>nbCol: nbCol:=col; fi;
  
  typeEl.[nbLgn][col]c=s;
enddef;

def chkCol(expr a)=
  if (col mod 2)=a:
    if ndf=1: sgn_(NonDefRegion_,1);
    elseif (typeLgn[nbLgn]=Variations_) and (vd=0): fleche;
    else: sgnSmp_(Vide_);
    fi
  fi
enddef;

def valeur_(expr s,type,b)=
  chkCol(0);
  valSmp_(s,type,b);
enddef;

def sgn_(expr s,a)=
  chkCol(a);
  sgnSmp_(s);
enddef;

def flecheBrisee(expr b)=
  sgn_(Trait_,1);
  vd:=0;
  col:=col+1;
  if col>nbCol: nbCol:=col; fi;

  typeEl.[nbLgn][col]c=VidePos_;
  pos.[nbLgn][col]c=b;
enddef;

def vide=vd:=1;sgn_(Vide_,0);enddef;
def val(expr s)=valeur_(s,Valeur_,.5); enddef;
def valBarre(expr s)=valeur_(s,ValeurBarree_,.5); enddef;
def valPos(expr s,b)=valeur_(s,Valeur_,b); enddef;
def valPosBarre(expr s,b)=valeur_(s,ValeurBarree_,b); enddef;
def barre=sgn_(Barre_,0); enddef;
def nonDefBarre=sgn_(NonDefBarre_,0); enddef;
def debutNonDef=ndf:=1;barre;enddef;
def finNonDef=barre;ndf:=0; enddef;

def bord=sgn_(Barre_,1); enddef;
def plus=sgn_(Plus_,1); enddef;
def moins=sgn_(Moins_,1); enddef;
def fleche=sgn_(Fleche_,1); enddef;

def limGauche(expr s,b)=
  chkCol(0);
  pos.[nbLgn][col+1]l=b;
  el.[nbLgn][col+1]l=mkLabel(s);
enddef;

def limDroite(expr s,b)=
  pos.[nbLgn][col]r=b;
  el.[nbLgn][col]r=mkLabel(s);
enddef;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def newLgn_(expr x,type)=
  nbLgn:=nbLgn+1;
  col:=0;
  typeLgn[nbLgn]=type;

  sgnSmp_(Vide_);
  val(x);
  bord;
enddef;

def newLigneVariables(expr x)=newLgn_(x,Variables_); enddef;
def newLigneSignes(expr x)=newLgn_(x,Signes_); enddef;
def newLigneVariations(expr x)=newLgn_(x,Variations_); enddef;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def calculPos=
  xCol[1]:=0;
  
  for i=1 upto nbCol:
    x[i]:=xCol[i]+getGcol(i);
    xCol[i+1]:=x[i]+getDcol(i);
  endfor

  yLgn[1]:=0;  
  for i=1 upto nbLgn:
    y[i]:=yLgn[i]-.5getHLgn(i);
    yLgn[i+1]:=y[i]-0.5*getHLgn(i);
  endfor;
enddef;

vardef calcP(expr i,j)=
  if exists(i,j):
    if (typeEl.[i][j]c=Valeur_) or (typeEl.[i][j]c=VidePos_):
      (x[j],y[i]+(pos.[i][j]c-.5)*(getHLgn(i)-getHelsLgn(i)))
    else: (x[j],y[i]) fi
  else: (x[j],y[i]) fi
enddef;

vardef calcPl(expr i,j)=
  (x[j]-2pt-.5(getL(el.[i][j]c)+getL(el.[i][j]l)),y[i]+(pos.[i][j]l-.5)*(getHLgn(i)-getHelsLgn(i)))
enddef;

vardef calcPr(expr i,j)=
  (x[j]+2pt+.5(getL(el.[i][j]c)+getL(el.[i][j]r)),y[i]+(pos.[i][j]r-.5)*(getHLgn(i)-getHelsLgn(i)))
enddef;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

vardef drawFleche(expr i,j,k)=
  save aa,bb;
  aa=j-1;
  bb=j+1;
  forever:
    exitif typeEl.[i][aa]c<>Vide_;
    aa:=aa-1;
  endfor
  forever:
    exitif typeEl.[i][bb]c<>Vide_;
    bb:=bb+1;
  endfor

  if k=Fleche_: drawarrow else: draw fi(
    if known el.[i][aa]r: calcPr(i,aa) else: calcP(i,aa) fi--
    if known el.[i][bb]l: calcPl(i,bb) else: calcP(i,bb) fi)
  if known el.[i][aa]r: cutbefore(bbox(thelabel(el.[i][aa]r,calcPr(i,aa)))) fi
  if known el.[i][aa]c: cutbefore(bbox(thelabel(el.[i][aa]c,calcP(i,aa)))) fi

  if known el.[i][bb]l: cutafter(bbox(thelabel(el.[i][bb]l,calcPl(i,bb)))) fi
  if known el.[i][bb]c: cutafter(bbox(thelabel(el.[i][bb]c,calcP(i,bb)))) fi;
enddef;

vardef rempli(expr xa,xb,ya,yb)=
  save i;
  for i=1 step 5pt until xb-xa+ya-yb-1:
    draw (xa,ya-i)--(xa+i,ya) cutbefore ((xa,yb)--(xb,yb)) cutafter ((xb,ya)--(xb,yb));
  endfor
enddef;

def afficheSigne(expr s,i,j)=
  label(s,.5[calcP(i,j-1),calcP(i,j+1)]);
enddef;

def afficheTableau=
  calculPos;
  for i=1 upto nbLgn:    
    for j=1 upto nbCol:  
      if exists(i,j):
	t:=typeEl.[i][j]c;
	if t=Plus_:
	  afficheSigne(btex $+$ etex,i,j);
	elseif t=Moins_:
	  afficheSigne(btex $-$ etex,i,j);
	elseif t=Fleche_:
	  drawFleche(i,j,Fleche_);

	elseif t=Trait_:
	  drawFleche(i,j,Trait_);

	elseif t=NonDefRegion_:
	  rempli(x[j-1],x[j+1],yLgn[i],yLgn[i+1]);

	elseif t=Barre_:
	  draw (x[j],yLgn[i])--(x[j],yLgn[i+1]);
	
	elseif t=ValeurBarree_:
	  label(el.[i][j]c,calcP(i,j));
	  draw (x[j],yLgn[i])--(x[j],yLgn[i+1]) dashed evenly;

	elseif t=NonDefBarre_:
	  draw (x[j]-1pt,yLgn[i])--(x[j]-1pt,yLgn[i+1]);
	  draw (x[j]+1pt,yLgn[i])--(x[j]+1pt,yLgn[i+1]);
	  
	elseif t=Valeur_:
	  label(el.[i][j]c,calcP(i,j));
	fi
	if known el.[i][j]l: label(el.[i][j]l,calcPl(i,j)); fi;
	if known el.[i][j]r: label(el.[i][j]r,calcPr(i,j)); fi;
      fi
    endfor
  endfor

  for i=2 upto nbLgn:
    draw (xCol[1],yLgn[i])--(xCol[nbCol+1],yLgn[i]);
  endfor;
% Bang bien thien cua VN khong co khung nen bo 4 dong sau day:
%  draw(xCol[1],yLgn[1])--(xCol[nbCol+1],yLgn[1]); 
%  draw(xCol[1],yLgn[nbLgn+1])--(xCol[nbCol+1],yLgn[nbLgn+1]);
%  draw(xCol[1],yLgn[1])--(xCol[1],yLgn[nbLgn+1]);
  % draw(xCol[nbCol+1],yLgn[1])--(xCol[nbCol+1],yLgn[nbLgn+1]);   
enddef;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def beginTableau(expr c) =
  begingroup
  charcode:=c;
  clearxy; clearit; clearpen;
  pickup defaultpen;
  drawoptions();

  initTableau;
enddef;

def initTableau=
  picture el.[][]l;
  picture el.[][]c;
  picture el.[][]r;
  numeric typeLgn[];
  numeric col;
  numeric nbLgn;
  numeric nbCol;
  numeric pos.[][]l;
  numeric pos.[][]c;
  numeric pos.[][]r;
  numeric typeEl.[][]c;
  numeric yLgn[];
  numeric xCol[];

  ndf:=0;
  vd:=0;
  col=0;
  nbLgn=0;
  nbCol=0;
enddef;

def endTableau=
  afficheTableau;
  
  shipit;
  endgroup
enddef;
