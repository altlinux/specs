%define libchoqok_major 1
%define libchoqok libchoqok%libchoqok_major
%define libtwitterapihelper_major 1
%define libtwitterapihelper libtwitterapihelper%libtwitterapihelper_major

Name: choqok
Version: 1.3
Release: alt1

Group: Office
Summary: KDE Micro-Blogging Client
Url: http://choqok.gnufolks.org/
License: GPLv2+

Source: %name-%version.tar
Patch1: choqok-0.9.85-alt-dbus-services-install.patch

# Automatically added by buildreq on Wed May 26 2010 (-bi)
#BuildRequires: gcc-c++ glib2-devel glibc-devel-static kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel qt4-assistant qt4-designer rpm-build-ruby
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ glib2-devel glibc-devel kde4libs-devel
BuildRequires: qjson-devel libqca2-devel qoauth-devel attica-devel

%description
Choqok is a Free/Open Source micro-blogging client for K Desktop


%package -n %libchoqok
Summary: %name library
Group: System/Libraries
Obsoletes: libchoqok0
Conflicts: libchoqok0
%description -n %libchoqok
%name library.

%package -n %libtwitterapihelper
Summary: %name library
Group: System/Libraries
Obsoletes: libtwitterapihelper0
Conflicts: libtwitterapihelper0
%description -n %libtwitterapihelper
%name library.

%package devel
Summary: %name development files
Group: Development/KDE and QT
Requires: %libchoqok = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.


%prep
%setup -q
%patch1 -p1

%build
%K4build


%install
%K4install
%K4find_lang --with-kde %name



%files -f %name.lang
%doc COPYING AUTHORS TODO changelog
%_K4bindir/choqok
%_K4lib/choqok_*.so
%_K4lib/kcm_choqok_*.so
%_K4lib/konqchoqokplugin.so
%_K4xdg_apps/choqok.desktop
%_K4apps/choqok
%_K4apps/choqok_filter
%_K4apps/choqok_searchaction
%_K4apps/choqok_nowlistening
%_K4apps/choqok_quickfilter
%_K4apps/khtml/kpartplugins/konqchoqok.*
%_K4cfg/*.kcfg
%_K4iconsdir/*/*/*/*.*
%_K4srv/choqok_*.desktop
%_K4srv/ServiceMenus/choqok_*.desktop
%_K4srvtyp/choqok*.desktop
%_K4dbus_services/org.kde.choqok.service

%files -n %libchoqok
%_K4libdir/libchoqok.so.%libchoqok_major
%_K4libdir/libchoqok.so.%libchoqok_major.*

%files -n %libtwitterapihelper
%_K4libdir/libtwitterapihelper.so.%libtwitterapihelper_major
%_K4libdir/libtwitterapihelper.so.%libtwitterapihelper_major.*

%files devel
#%_K4apps/cmake/modules/*.cmake
%_K4apps/cmake/modules/FindChoqok.cmake
%_K4link/lib*.so
%_K4includedir/choqok


%changelog
* Sat May 05 2012 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Tue Feb 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1.M60P.1
- built for M60P

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt2
- rebuilt with new attica

* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.M60P.1
- built for M60P

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for choqok

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt3
- fix conflict with libchoqok0

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- fix conflict with libtwitterapihelper0

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- 1.1

* Tue Feb 08 2011 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- 1.0

* Tue Dec 07 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.98-alt1
- 1.0-RC1

* Fri Oct 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.92-alt0.M51.1
- built for M51

* Fri Oct 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.92-alt1
- 1.0-beta4

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.90-alt0.M51.1
- built for M51

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.90-alt1
- 1.0-beta3

* Mon Aug 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.85-alt1
- 1.0-beta2

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.55-alt1.M51.1
- built for M51

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.55-alt2
- fix build requires

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.55-alt1
- initial specfile
