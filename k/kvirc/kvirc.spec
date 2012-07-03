Name: kvirc
Version: 4.0.4
Release: alt1.1

Summary: KDE Enhanced Visual IRC Client
License: GPLv2+
Group: Networking/IRC

URL: http://www.kvirc.net/
Source: kvirc-%version.tar.bz2

Provides: kvirc4 = %version
Obsoletes: kvirc4 < %version

Requires: %name-data = %version-%release

# Automatically added by buildreq on Sun Oct 16 2011
BuildRequires: gcc-c++ kde4libs-devel libcryptopp-devel libesd-devel perl-devel python-devel

%description
KVIrc is an enchanced visual irc client. Features:
 - MDI interface
 - CTCP's
 - DCC CHAT SEND/GET
 - Individual queries
 - Scripting
 - Aliases
 - Events (remote)
 - Complete color,background and behavior configuration
 - IPv6 support

%package devel
Summary: Header files for KVirc library
Group: Development/KDE and QT
Requires: %name = %version-%release

%description devel
Header files for KVirc library.

%package data
Summary: Data files for %name
Group: Networking/IRC
Provides: kvirc4-data = %version
Obsoletes: kvirc4-data < %version
BuildArch: noarch

%description data
KVIrc is an enchanced visual irc client.
This package contains data files for %name.

%prep
%setup -q

%build
%K4cmake \
%if_enabled debug
    -DWANT_DEBUG:BOOL=1 \
%endif
    -DUSE_ENV_FLAGS:BOOL=1 \
    -DWANT_NO_EMBEDDED_CODE:BOOL=1 \
    -DWANT_COEXISTENCE:BOOL=0 \
    -DWITH_PIZZA:BOOL=1 \
    -DWITH_BEER:BOOL=1

%K4make

%install
%K4install

%files
%_bindir/%name
%_man1dir/%name.1*
%_libdir/lib*.so.*

%define ver %(v=%version IFS=.; set $v; echo $1.$2)

%dir %_libdir/kvirc
%dir %_libdir/kvirc/%ver
%dir %_libdir/kvirc/%ver/modules
%_libdir/kvirc/%ver/modules/*.so

%_K4xdg_mime/%name.xml

%_iconsdir/hicolor/*/apps/%name.*
%_iconsdir/hicolor/*/mimetypes/*-x-kv?.*

%_datadir/applications/%name.desktop

%files data
%dir %_datadir/kvirc
%dir %_datadir/kvirc/%ver
%doc %_datadir/kvirc/%ver/doc
%_datadir/kvirc/%ver/audio
%_datadir/kvirc/%ver/config
%_datadir/kvirc/%ver/defscript
%_datadir/kvirc/%ver/pics
%_datadir/kvirc/%ver/help
%_datadir/kvirc/%ver/locale
%_datadir/kvirc/%ver/license
%_datadir/kvirc/%ver/modules
%_datadir/kvirc/%ver/msgcolors
%_datadir/kvirc/%ver/themes

%if 0
%files devel
%_bindir/kvirc4-config
%_libdir/lib*.so
#_includedir/%name
%endif

%changelog
* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.4-alt1.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 4.0.4-alt1
- 4.0.3+r4984 -> 4.0.4
- built for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 4.0.3-alt1.r4984.1
- rebuilt with perl 5.12

* Tue Sep 14 2010 Andrey Rahmatullin <wrar@altlinux.org> 4.0.3-alt1.r4984
- 4.0.3 r4984

* Tue Aug 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 4.0.3-alt1.r4887
- 4.0.3 r4887

* Fri Aug 06 2010 Andrey Rahmatullin <wrar@altlinux.org> 4.0.3-alt1.r4791
- 4.0.3 r4791
- rename to kvirc

* Sun Aug 01 2010 Andrey Rahmatullin <wrar@altlinux.org> 4.0.2-alt1
- 4.0.2

* Tue Jul 27 2010 Andrey Rahmatullin <wrar@altlinux.org> 4.0.1-alt1.r4696
- 4.0.1 r4696
  + CVE-2010-2785: Remote CTCP commands execution via specially-crafted
    CTCP parameter

* Mon Jul 12 2010 Andrey Rahmatullin <wrar@altlinux.org> 4.0.1-alt1.r4657
- 4.0.1 r4657

* Mon Jul 12 2010 Andrey Rahmatullin <wrar@altlinux.org> 4.0.1-alt1.r4650
- 4.0.1 r4650

* Mon Jun 28 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt3
- 4.0.0

* Tue Jun 01 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4411
- r4411

* Tue May 25 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4374
- r4374

* Mon May 24 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4371
- r4371

* Sat May 01 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4304
- r4304

* Sat Apr 17 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4254
- 4.0 RC3

* Fri Mar 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4223
- r4223

* Fri Mar 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4221
- r4221

* Wed Feb 24 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4028
- r4028

* Wed Feb 24 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r4024
- r4024

* Tue Feb 09 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3940
- r3940

* Tue Jan 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3890
- r3890

* Tue Jan 12 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3833
- r3833

* Fri Dec 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3750
- r3750

* Tue Dec 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3731
- r3731
- use optflags again

* Mon Dec 14 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3694
- r3694

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.r3608.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3608
- r3608
- build with system crypto++

* Tue Nov 03 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3587
- r3587

* Sun Oct 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3573
- r3573

* Mon Sep 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3534
- r3534

* Fri Sep 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3513
- r3513

* Thu Sep 10 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3489
- r3489
- disable coexistence support, add Conflicts: kvirc

* Tue Sep 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3459
- 4.0RC1

* Fri Jul 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3377
- r3377
- update versioned buildreqs
- enable ESD backend

* Sun Jul 19 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3354
- r3354

* Sun Jul 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3334
- r3334

* Thu Jul 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3327
- r3327

* Sun Jul 05 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3303
- r3303

* Fri Jun 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3288
- r3288

* Tue May 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3222
- r3222

* Sun May 10 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3212
- r3212

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3191
- r3191
- install the application icons as kvirc4.png (closes: #19894)

* Fri May 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3189
- r3189

* Sun Apr 05 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3172
- r3172

* Thu Mar 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3164
- r3164
- package %%_datadir/kvirc as a separate noarch package

* Fri Mar 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3154
- r3154

* Mon Mar 16 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3147
- r3147

* Sat Mar 07 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3120
- r3120

* Mon Mar 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3118
- r3118

* Mon Mar 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3114
- r3114

* Sun Mar 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt2.r3107
- Sisyphus build
- disable QPainter::Antialiasing (workaround for upstream #379)
- fix bot detection (upstream #381)

* Sat Feb 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r3107
- r3107

* Fri Feb 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r3091
- r3091

* Tue Feb 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r3080
- r3080

* Sat Jan 31 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r3061
- r3061

* Thu Jan 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r3022
- r3022

* Sun Jan 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r2985
- r2985

* Thu Dec 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r2948
- r2948

* Sat Nov 22 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r2912
- r2912
- remove update_*/clean_* invocations
- clean up buildreqs

* Wed Nov 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r2851
- r2851
- add buildreqs

* Fri Nov 07 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r2836
- r2836
- build with KDE4

* Tue Nov 04 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.0-alt1.r2814
- 4.0 (trunk) r2814
- package as kvirc4

* Tue Aug 12 2008 Sergey V Turchin <zerg at altlinux dot org> 3.4.0.2228-alt1
- update from svn 3.4/branch r2228

* Thu Mar 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Fri Mar 07 2008 Sergey V Turchin <zerg at altlinux dot org> 3.2.6-alt3.r1070
- udpate from svn r1070

* Wed Jun 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.2.6-alt2
- add fix for CVE-2007-2951

* Tue Jan 09 2007 Sergey V Turchin <zerg at altlinux dot org> 3.2.6-alt1
- new version

* Mon Oct 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.5-alt2
- fix dock icon

* Fri Sep 22 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.5-alt1
- new version
- add patch to set main window active when click dock
- update some icons

* Mon Sep 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.4-alt3
- fix menu entry

* Wed Aug 30 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.4-alt2
- add new icons

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.4-alt1
- new version

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- fix built on x86_64
- fix showing minimized main window by clicking on dock

* Thu Jun 01 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Mon Apr 24 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt0.14.cvs20060424
- new cvs snapshot

* Fri Mar 31 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt0.13.cvs20060329
- remove rpath

* Wed Mar 29 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt0.12.cvs20060329
- built for Sisyphus

* Wed Mar 22 2006 Zerg <zerg at altlinux dot org> 3.2.1-alt0.11.M30
- update from cvs

* Wed Mar 15 2006 Zerg <zerg at altlinux dot org> 3.2.1-alt0.10.M30
- update from cvs

* Sat Mar 04 2006 Zerg <zerg at altlinux dot ru> 3.2.0.20051230-alt0.9.M30
- update from cvs

* Tue Feb 28 2006 Zerg <zerg at altlinux dot ru> 3.2.0.20051230-alt0.8.M30
- update from cvs

* Fri Feb 24 2006 Zerg <zerg at altlinux dot ru> 3.2.0.20051230-alt0.7.M30
- fix alias(avatar) script

* Fri Feb 24 2006 Zerg <zerg at altlinux dot ru> 3.2.0.20051230-alt0.6.M30
- update from cvs

* Thu Feb 23 2006 Zerg <zerg at altlinux dot ru> 3.2.0.20051230-alt0.5.M30
- add patch to don't exit on close main window

* Thu Feb 23 2006 Zerg <zerg at altlinux dot ru> 3.2.0.20051230-alt0.4.M30
- update from cvs

* Thu Feb 23 2006 Zerg <zerg at altlinux dot ru> 3.2.0.20051230-alt0.3.M30
- update from cvs

* Wed Jan 25 2006 Zerg <zerg at altlinux dot ru> 3.2.0-alt0.2.M30
- rebuilt for M30

* Sun Aug 28 2005 Zerg <zerg at altlinux dot ru> 3.2.0-0.1
- built for ALT
