# vim: set ft=spec: -*- rpm-spec -*-

Name: fortunes-ALT
Version: 20090821
Release: alt1

Summary: ALT Linux Team members' quotes from ALT Linux mailing list
Group: Games/Other
License: distributable

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

Source0: ALT
Source1: ALT-lists

BuildPreReq: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

%package lists
Summary: Non-members quotes from ALT Linux mailing list
Group: Games/Other

%description
%summary

%description lists
%summary

%install
install -pDm0644 %SOURCE0 %buildroot%_gamesdatadir/fortune/ALT
strfile %buildroot%_gamesdatadir/fortune/ALT %buildroot%_gamesdatadir/fortune/ALT.dat

install -pDm0644 %SOURCE1 %buildroot%_gamesdatadir/fortune/ALT-lists
strfile %buildroot%_gamesdatadir/fortune/ALT-lists %buildroot%_gamesdatadir/fortune/ALT-lists.dat

%files
%_gamesdatadir/fortune/ALT
%_gamesdatadir/fortune/ALT.dat

%files lists
%_gamesdatadir/fortune/ALT-lists
%_gamesdatadir/fortune/ALT-lists.dat

%changelog
* Fri Aug 21 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 20090821-alt1
- ALT: 37 new quotes
- ALT-lists: 1 new quotes

* Fri Jun 27 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 20080627-alt1
- ALT: 34 new quotes
- ALT-lists: 4 new quotes

* Fri Feb 08 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 20080208-alt1
- Separate package fortunes-ALT-lists for quotes from non-members
- ALT: 32 new quotes
- ALT-lists: 2 new quotes

* Mon Sep 12 2005 Sir Raorn <raorn@altlinux.ru> 20050912-alt1
- More quotes from abulava, aen, alb, algor, at, avp, eostapets,
  eugvv, genix, gik, gns, icesik, inger, jaa, ktirf, lakostis,
  lav, ldv, legion, mb, mike, mithraen, mrkooll, mutabor, nikon,
  ns, php-coder, pilot, sbolshakov, slava, stalker, ulfr, voins,
  vsu, vyt, wrar, zerg

* Wed Jun 22 2005 Sir Raorn <raorn@altlinux.ru> 20050622-alt1
- More quotes from ab, abr, abulava, aen, alb, algor, avm, cray,
  dlebkov, genix, gns, inger, jaa, kirill, koka, ktirf, lakostis,
  lav, ldv, legion, mhz, mike, mithraen, mouse, mrkooll, nikon,
  ns, peet, pilot, taf, tosick, wrar, zerg

* Mon Mar 14 2005 Sir Raorn <raorn@altlinux.ru> 20050314-alt1
- More quotes from abulava, akhavr, alb, aris, force, genix,
  gns, inger, kirill, ktirf, lakostis, lav, ldv, legion, mhz,
  mike, mrkooll, mutabor, nikon, pilot, seriv, slava, svd, vyt,
  wrar, yust
- Removed summary/description translations (use specspo ;-)

* Mon Feb 14 2005 Sir Raorn <raorn@altlinux.ru> 20050214-alt1
- More quotes from abulava, aen, alb, aris, at, avp, cray,
  dketov, dlebkov, genix, george, gns, inger, jaa, kirill,
  lakostis, lav, ldv, legion, mhz, mike, mithraen, morozov,
  mouse, mrkooll, mutabor, nikon, ns, oddity, pilot, sbolshakov,
  shrek, slava, smi, voins, vserge, vyt, wrar, zerg

* Fri Dec 31 2004 Sir Raorn <raorn@altlinux.ru> 20041231-alt1
- HNY release!
- More quotes from avp, lakostis, legion, mhz, mike, mithraen,
  mrkooll, peet, shrek, slava, wrar, zerg

* Wed Dec 22 2004 Sir Raorn <raorn@altlinux.ru> 20041222-alt1
- More quotes from aen, andrei, aris, avp, horror, jaa,
  lakostis,   ldv, mike, mithraen, ns, peet, pilot, shrek,
  slava, vyt, wrar, zerg

* Sun Dec 12 2004 Sir Raorn <raorn@altlinux.ru> 20041212-alt1
- More quotes from abr, abulava, avp, boyarsh, const, cray,
  crux, horror, jaa, lakostis, lav, ldv, mhz, mike, mithraen,
  morozov, mutabor, ns, peet, pilot, shrek, slava, vserge, vsu,
  vvzhy, vyt, wrar, zerg

* Sat Oct 23 2004 Sir Raorn <raorn@altlinux.ru> 20041023-alt1
- More quotes from ab, asy, const, crux, gns, inger, lakostis,
  ldv, legion, mike, mithraen, morozov, mrkooll, mutabor,
  nikon, ott, peet, shrek, taf, zerg

* Mon Sep 13 2004 Sir Raorn <raorn@altlinux.ru> 20040912-alt1
- More quotes from ab, aen, asy, avp, crux, dlebkov, gns,
  horror, lav, ldv, mhz, mike, mithraen, morozov, nikon, pilot,
  security, slava, voins, wrar, zerg

* Fri Aug 13 2004 Sir Raorn <raorn@altlinux.ru> 20040813-alt1
- Friday 13th release
- More quotes from aen, aris, cray, gns, hiddenman, inger, 
  jaa, ldv, legion, mike, mrkooll, ns, shrek, slava, voins, 
  vsl, vyt, wrar

* Sat Jun 26 2004 Sir Raorn <raorn@altlinux.ru> 20040625-alt2
- Restored lost part of spec changelog (thanx to wrar)

* Fri Jun 25 2004 Sir Raorn <raorn@altlinux.ru> 20040625-alt1
- More quotes from ab, aen, aris, asy, at, avl, cray, gns,
  inger, jaa, lav, ldv, legion, mike, mithraen, ott, pilot,
  rider, sass, voins, zerg

* Sat Apr 24 2004 Sir Raorn <raorn@altlinux.ru> 20040424-alt1
- More quotes from ab, abr, aen, at, dav, inger, ldv, mhz, mike,
  mithraen, morozov, mrkooll, mutabor, peet, vsu, zerg

* Tue Feb 17 2004 Sir Raorn <raorn@altlinux.ru> 20040217-alt1
- More quotes from aen, at, avl, avp, darkstar, ed, inger,
  jaa, lav, ldv, mhz, mike, mithraen, morozov, mouse, mrkooll,
  rider, slava, vsu, wrar, zerg

* Mon Dec 29 2003 Sir Raorn <raorn@altlinux.ru> 20031229-alt1
- More quotes from ab, at, avp, cray, force, ivv, lav, ldv,
  mike, morozov, pilot, rider, vsu, vvzhy
 
* Mon Dec 01 2003 Sir Raorn <raorn@altlinux.ru> 20031130-alt1
- More quotes from aen, at, avp, cornet, force, ldv, legion,
  mike, mithraen, nidd, pilot, rider, voins, vsl, vsu, zerg

* Mon Sep 08 2003 Sir Raorn <raorn@altlinux.ru> 20030906-alt1
- More quotes from ab, abr, aen, at, avp, boyarsh, inger, ldv,
  mike, mouse, voins, vsl, zerg

* Sun Jun 01 2003 Sir Raorn <raorn@altlinux.ru> 20030601-alt1
- More quotes from aen, avl, avp, homyakov, inger, ivv, ldv,
  mike, nidd, rider, smi, vsl
- Datafile now in UTF-8 encoding, updated requires on fortune-mod

* Mon May 26 2003 Sir Raorn <raorn@altlinux.ru> 20030526-alt1
- First release. LOTS of quotes from ldv and one from mhz. More to come...


