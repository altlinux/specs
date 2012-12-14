%def_disable msits

%add_findpackage_path %_kde4_bindir

%define rname okular
Name: kde4-okular
%define major 4
%define minor 10
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt0.1

Group: Office
Summary: KDE document viewer
Url: http://projects.kde.org/projects/kdegraphics/okular
License: GPLv2

Requires: kde4-icon-theme
Requires: %name-core = %version-%release

Provides: kde4graphics-okular = %version-%release
Obsoletes: kde4graphics-okular < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libpoppler3-qt4 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libtiff-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libchm-devel libdjvu-devel libpoppler-qt4-devel libqca2-devel libqimageblitz-devel libqt3-devel libspectre-devel rpm-build-ruby zlib-devel-static
BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libdjvu-devel libpoppler-qt4-devel libqca2-devel libqimageblitz-devel libspectre-devel zlib-devel kde-common-devel
BuildRequires: kde4-plasma-mobile-devel kde4-kactivities-devel
%if_enabled msits
BuildRequires: libchm-devel
%endif

%description
Document viewer; support different kinds of documents.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common >= %major.%minor
BuildArch: noarch
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package mobile
Summary: KDE mobile document viewer
Group: Office
Requires: %name-core = %version-%release
%description mobile
Document viewer; support different kinds of documents.

%package -n libokularcore4
Summary: KDE 4 core library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libokularcore4
KDE 4 core library.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install



%files common
%files
%doc AUTHORS TODO
%_K4bindir/okular
%_K4xdg_apps/okular.desktop
%_K4xdg_apps/okularApplication_*

%files core
%doc AUTHORS TODO
%_K4lib/okularGenerator_*
%_K4lib/okularpart.so
%_K4apps/okular
%_K4cfg/okular*.kcfg
%_K4cfg/gssettings.kcfg
%_K4conf_update/okular.upd
%_K4srv/libokularGenerator_*
%_K4srv/okular*
%_K4srvtyp/okularGenerator.desktop
%_K4iconsdir/hicolor/*/apps/okular.*
%_K4doc/en/okular/
%if_enabled msits
%_K4lib/kio_msits.so
%_K4srv/msits*
%endif

%files mobile
%doc AUTHORS TODO
%_K4bindir/active-documentviewer
%_K4lib/imports/org/kde/okular/
%_K4xdg_apps/active-documentviewer.desktop
%_K4apps/plasma/packages/org.kde.active.documentviewer/

%files -n libokularcore4
%_K4libdir/libokularcore.so.*

%files devel
%_K4includedir/okular/
%_K4libdir/cmake/Okular/
%_K4link/lib*.so


%changelog
* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Mon Nov 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Tue Oct 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Thu Jun 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Thu Jun 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix requires

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Mon Nov 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- rebuilt with poppler-0.18

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
