%def_disable quanta
%def_disable xsldbg

%add_findpackage_path %_kde4_bindir
%add_findreq_skiplist %_K4apps/klinkstatus/scripts/statistics.rb

%define rname kdewebdev
Name: kde4webdev
%define major 4
%define minor 8
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: A web development for the KDE Desktop Environment
Url: http://kdewebdev.org/
License: GPLv2+

Requires: %name-klinkstatus = %version-%release
Requires: %name-kfilereplace = %version-%release
Requires: %name-kommander = %version-%release
Requires: %name-kimagemapeditor = %version-%release
%if_enabled quanta
Requires: %name-quanta = %version-%release
%endif
%if_enabled kxsldbg
Requires: %name-kxsldbg = %version-%release
%endif


#Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar.bz2
Source: %rname-%version.tar



BuildRequires(pre): kde4base-runtime-devel kde4pimlibs-devel
BuildRequires: gcc-c++ libtidy-devel
BuildRequires: libbfd-devel libjpeg-devel libreadline-devel libruby-devel libxslt-devel xsltproc
BuildRequires: kde4base-runtime-devel >= %version kde4pimlibs-devel >= %version

%description
Kommander: a GUI script builder and executor tool. Needed for some Quanta functionality.
KFileReplace: powerful search and replace in multiple files
KXSLDbg: XSL debugger
KImageMapEditor: image map editor
KLinkStatus: link checker

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common >= %major.%minor
Conflicts: kdewebdev-common <= 3.5.12-alt1
%description common
%name common package

%package quanta
Summary: Quanta
Group: Development/Other
Requires: %name-common = %version-%release
%description quanta
A HTML editor for the K Desktop Environment.

%package klinkstatus
Summary: Link checker
Group: Networking/Other
Requires: %name-common = %version-%release
%description klinkstatus
* Support several protocols (allowing fast checking of
local documents): http, ftp, ssh (fish or sftp) and file.
* Proxy support
* Allows authentication when checking restricted documents
* Supports the latest Web standards-- HTML 4.0, HTTP 1.1
* Server-Side Includes (SSI, aka SHTML) are supported and checked
* Regular expressions to restrict which URLs are searched
* Show link results as they are checked
* Tree like view (that reflects the file structure of the documents) or
  flat view
* Limit the search depth
* Fragment identifiers ("#" anchor links that point to a specific
 section in a document) are supported and checked
* Pause/Resume of checking session
* History of checked URLs
* Tabbed checking (allow multiple sessions at the same time)
* Filter checked links (good, broken, malformed and undetermined)
* Configurable number of simultaneous connections (performance tunning)
* Other configurable options like "check external links",
"check parent folders", "timeout"
* Good integration with Quanta+

%package -n libklinkstatuscommon4
Summary: KDE 4 core library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libklinkstatuscommon4
KDE 4 core library.

%package kfilereplace
Summary: Search and replace in multiple files
Group: Text tools
Requires: %name-common = %version-%release
%description kfilereplace
Search and replace in multiple files

%package -n libkommanderwidgets4
Summary: KDE 4 core library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkommanderwidgets4
KDE 4 core library.

%package -n libkommandercore4
Summary: KDE 4 core library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkommandercore4
KDE 4 core library.

%package kommander
Summary: GUI script builder and executor tool
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description kommander
GUI script builder and executor tool

%package kimagemapeditor
Summary: HTML image map editor
Group: Development/Other
Requires: %name-common = %version-%release
%description kimagemapeditor
HTML image map editor

%package kxsldbg
Summary: XSL debugger
Group: Development/Other
Requires: %name-common = %version-%release
%description kxsldbg
XSL debugger

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.

%prep
%setup -q -n %rname-%version

%build
%K4build

%install
%K4install


%files
%files common
%doc README
%_K4iconsdir/hicolor/*/actions/*.*

%if_enabled quanta
%files quanta
%_K4bindir/quanta
%_K4lib/libkdev*
%_K4lib/quanta*
%_K4libdir/libkdevquanta.so.*
%_K4xdg_apps/quanta.desktop
%_K4cfg/quanta.kcfg
%_K4srv/kdev*
%_K4srv/quanta*
%_K4srvtyp/kdev*
%_K4apps/kdev*/*
%_K4apps/quanta*/*
%_kde4_iconsdir/*/*/apps/quanta*
%_K4doc/en/quanta
%endif

%files klinkstatus
%_K4bindir/klinkstatus
%_K4lib/klinkstatuspart.so
%_K4lib/automationklinkstatus.so
%_K4lib/krossmoduleklinkstatus.so
%_K4xdg_apps/klinkstatus.desktop
%_K4apps/klinkstatus
%_K4apps/klinkstatuspart
%_K4iconsdir/*/*/apps/klinkstatus.png
%_K4srv/klinkstatus_part.desktop
%_K4conf/klinkstatus.knsrc
%_K4srv/klinkstatus_automation.desktop
%_K4srv/krossmoduleklinkstatus.desktop
%_K4doc/en/klinkstatus
%_K4dbus_interfaces/org.kde.kdewebdev.klinkstatus.SearchManager.xml

%files -n libklinkstatuscommon4
%_K4libdir/libklinkstatuscommon.so.*

%files kfilereplace
%_K4bindir/kfilereplace
%_K4xdg_apps/kfilereplace.desktop
%_K4apps/kfilereplace
%_K4apps/kfilereplacepart
%_K4iconsdir/hicolor/*/apps/kfilereplace.png
%_K4srv/kfilereplacepart.desktop
%_K4lib/libkfilereplacepart.so
%_K4doc/en/kfilereplace
%_K4dbus_interfaces/org.kde.kfilereplace.xml

%files -n libkommanderwidgets4
%_K4libdir/libkommanderwidgets.so.*

%files -n libkommandercore4
%_K4libdir/libkommandercore.so.*

%files kommander
%_K4bindir/kommander
%_K4applnk/.hidden/kommander.desktop

%files kimagemapeditor
%_K4bindir/kimagemapeditor
%_K4xdg_apps/kimagemapeditor.desktop
%_K4apps/kimagemapeditor
%_K4iconsdir/hicolor/*/apps/kimagemapeditor.png
%_K4srv/kimagemapeditorpart.desktop
%_K4lib/libkimagemapeditor.so
%_K4doc/*/kimagemapeditor

%if_enabled kxsldbg
%files kxsldbg
%_K4bindir/kxsldbg
%_K4bindir/xsldbg
%_K4xdg_apps/kxsldbg.desktop
%dir %_K4apps/kxsldbg
%_K4apps/kxsldbg/*
%dir %_K4apps/xsldbg
%_K4apps/xsldbg/*
%dir %_K4apps/kxsldbgpart
%_K4apps/kxsldbgpart/*
%_kde4_iconsdir/*/*/*/*xsldbg*
%_K4srv/kxsldbg_part.desktop
%_K4lib/libkxsldbgpart.so
%_K4doc/en/kxsldbg
%_K4doc/en/xsldbg
%_K4dbus_interfaces/org.kde.kxsldbg.kxsldbg.xml
#%_man1dir/xsldbg.1.*
%endif

%files devel
#%_K4dbus_interfaces/*
%_K4includedir/*
%_K4link/*.so

%changelog
* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Sun Sep 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version
- move to standart place

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Tue Jan 26 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Mon Jul 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Fri Mar 06 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- removed deprecated macroses from specfile

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Mon Oct 27 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- initial specfile

