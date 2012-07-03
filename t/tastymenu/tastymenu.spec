Name:		tastymenu
Version:	1.0.8
Release:	alt1.3
Summary:	Tasty Menu is a KMenu replacement
Packager:	Motsyo Gennadi <drool@altlinux.ru>
License:	LGPLv2
Group:		Graphical desktop/KDE
Url:		http://www.kde-look.org/content/show.php?content=41866
Source0:	http://www.notmart.org/files/%name-%version.tar.bz2

BuildRequires: gcc-c++ imake kdelibs-devel libXext-devel libXt-devel xml-utils xorg-cf-files libtqt-devel
BuildRequires: chrpath

%description
Tasty Menu is a K-Menu replacement for KDE 3.x series
aiming to provide the maximum usability and flexibility. 

It provides three columns where you can always have all
your favourite applications in handy.

Key features:
- One column for all your favourite applications and two
  columns for browsing all the installed programs
- Search engine for the applications
- Optional integration with Kerry Beagle or Strigi
- Highlighting of recently installed applications
- Fast user switching
- Drag and drop support

%prep
export UNSERMAKE=no
%setup -q

%__subst "s/\(Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g" admin/acinclude.m4.in
%__subst "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in
%__subst "s/\.la/.so/g" admin/acinclude.m4.in

%build
export OPTFLAGS="%optflags"
%add_optflags -I%_includedir/tqtinterface
make -f admin/Makefile.common cvs ||:
%K3configure --without-arts
%make_build
chrpath -d src/.libs/tastymenu_panelapplet.so

%install
%K3install
%K3find_lang %name --with-kde

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README TODO
%_K3datadir/apps/kicker/applets/%name.desktop
%_K3datadir/config.kcfg/tastymenu.kcfg
%_K3lib/tastymenu_panelapplet.so*

%changelog
* Thu Jan 26 2012 Motsyo Gennadi <drool@altlinux.ru> 1.0.8-alt1.3
- dropped RPATH on the floor
- minor spec cleanup

* Tue Mar 08 2011 Motsyo Gennadi <drool@altlinux.ru> 1.0.8-alt1.2
- move to alternate place

* Tue Feb 15 2011 Motsyo Gennadi <drool@altlinux.ru> 1.0.8-alt1.1
- build without aRts

* Wed Nov 18 2009 Motsyo Gennadi <drool@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Tue May 12 2009 Motsyo Gennadi <drool@altlinux.ru> 1.0.7-alt3
- fix build with GCC4.4 (thanks to damir@ for help)

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0.7-alt2
- delete post/postun scripts (new rpm)

* Tue Feb 12 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0.7-alt1
- 1.0.7 (Fixed a typo in the config dialog)

* Fri Dec 14 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0.6-alt1
- 1.0.6 (Now all the applications should be displayed again)
- fix license

* Fri Nov 23 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0.5-alt1
- 1.0.5
- update description

* Wed Nov 21 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sun Oct 28 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Oct 20 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt2
- fix find locale

* Thu Oct 18 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Oct 13 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sat Sep 22 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- release version

* Tue Sep 11 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt0.rc2
- new beta version
- cleanup BuildRequires (qt3-designer)

* Mon Aug 27 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt0.1.rc1
- fix License (GPL to LGPL)

* Sun Aug 26 2007 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt0.rc1
- new beta version

* Fri Aug 10 2007 Motsyo Gennadi <drool@altlinux.ru> 0.9-alt1
- new version

* Sat Jun 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt1
- build for Sisyphus

* Sat Jun 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt0.M40.1
- new version
- build for M40
- run buildreq -bi
- fix filesystem intersections

* Sun Apr 29 2007 Andrey Yurkovsky <anyr@tut.by> 0.7.1-alt1.M30
- add some changes to po files & menu

* Wed Apr 04 2007 Andrey Yurkovsky <anyr@tut.by> 0.7-alt3
- version 0.7

* Sat Mar 31 2007 Andrey Yurkovsky <anyr@tut.by> 0.6.5.1-alt3
- add some changes to spec

* Wed Feb 28 2007 Yurkovsky Andrey <anyr@tut.by> 0.6.5.1-alt2
- add russian menu

* Wed Feb 28 2007 Yurkovsky Andrey <anyr@tut.by> 0.6.5.1-alt1
- initial build
