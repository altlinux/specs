
%add_findpackage_path %_kde4_bindir
%add_findreq_skiplist %_K4apps/konversation/scripts/bug

%define rname konversation
Name: %rname

Version: 1.4
Release: alt1
%define beta %nil

Group: Networking/IRC
Summary: Konversation is a user friendly Internet Relay Chat client.
License: GPLv2
Url: http://konversation.kde.org
Packager: Sergey V Turchin <zerg@altlinux.org>


%ifdef _kde_alternate_placement
%else
Provides: kde4-%name = %version-%release
Obsoletes: kde4-%name < %version-%release
%endif

Source0: %rname-%version.tar.bz2

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ kde4base-runtime-devel kde4pimlibs-devel libqca2-devel

%description
Konversation is a simple and easy-to-use IRC client for KDE with support for 
SSL connections, strikeout, multi-channel joins, away/unaway messages, 
ignore list functionality, full Unicode support, the ability to auto-connect 
to a server, optional timestamps in chat windows, configurable background colors, 
and much more. 

%prep
#%setup -q -n %rname-%version%{?beta:-%beta}
%setup -q -n %rname-%version


%build
%K4cmake
%K4make


%install
%K4install

%K4find_lang --with-kde %rname


%files -f %rname.lang
%doc AUTHORS README TODO NEWS
#%_K4doc/en/%rname/
%ifdef _kde_alternate_placement
%_kde4_bindir/*
%_kde4_xdg_apps/%rname.desktop
%_kde4_iconsdir/hicolor/*/*/*.*
%else
%_K4bindir/*
%_K4xdg_apps/%rname.desktop
%_K4iconsdir/hicolor/*/*/*.*
%endif
%_K4apps/kconf_update/*
%_K4apps/%rname/
%_K4srv/*


%changelog
* Mon Jun 25 2012 Sergey V Turchin <zerg@altlinux.org> 1.4-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1
- Rebuild with Python-2.7

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt2
- fix build requires

* Mon Jul 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt0.M51.1
- built for M51

* Mon Jul 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt0.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1
- new version

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1.M51.1
- built for M51

* Tue Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt2
- 1.2.1 release

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.1
- Rebuilt with python 2.6

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.M50P.1
- built for M50P

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- 1.2 release

* Mon Sep 21 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.9
- 1.2-beta1

* Tue Aug 18 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.8
- fix requires

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.7
- 1.2-alpha6

* Thu Aug 06 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.6
- 1.2-alpha5

* Wed Jul 08 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.5
- 1.2-alpha4

* Wed Jul 01 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.4
- fix files placement

* Thu Jun 18 2009 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.3
- 1.2-alpha3

* Sun Sep 14 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.1-alt1
-  1.1.

* Thu Feb 14 2008 Grigory Batalov <bga@altlinux.ru> 1.0.1-alt2.1
- Rebuilt with python-2.5.

* Wed Jan 09 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.0.1-alt2
-  fix build on new sisyphus;
-  add scripts.

* Mon Dec 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- NMU:
  + 1.0.1
  + updated build dependencies
  + removed scripts on perl, python, ruby (patch1)
  + fixed tray icons size

* Mon Jun 26 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.19-alt1.1
-  fix build.

* Thu Feb 02 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.19-alt1
-  0.19.
-  #9057 fix. 10x to zerg@.
-  specfile cleanup.

* Mon Oct 03 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.18-alt0.2
-  build fix ("--disable-rpath" added to configure options).

* Wed Jun 15 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.18-alt0.1
-  0.18.
-  patch0 removed (upstream fix).

* Fri May 27 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17-alt0.5
-  patch for connection count control.

* Fri May 20 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17-alt0.4
-  default (first run) channel changed to #ALTLinux.
-  old style menu file.

* Wed May 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17-alt0.3
-  update/clean menus added.

* Wed May 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17-alt0.2
-  missing requres added.

* Wed May 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17-alt0.1
-  initial build.
