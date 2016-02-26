%def_disable msits
%def_disable activities

%add_findpackage_path %_kde4_bindir

%define rname okular
Name: kde4-okular
%define major 15
%define minor 12
%define bugfix 2
Version: %major.%minor.%bugfix
Release: alt1

Group: Office
Summary: KDE document viewer
Url: http://projects.kde.org/projects/kdegraphics/okular
License: GPLv2

Requires: kde4-icon-theme
Requires: %name-core = %version-%release

Provides: kde4graphics-okular = %version-%release
Obsoletes: kde4graphics-okular < %version-%release

Source: %rname-%version.tar
Patch1: okular-4.11.5-alt-print-truncate-title.patch

# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libpoppler3-qt4 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libtiff-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libchm-devel libdjvu-devel libpoppler-qt4-devel libqca2-devel libqimageblitz-devel libqt3-devel libspectre-devel rpm-build-ruby zlib-devel-static
BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libdjvu-devel
BuildRequires: libpoppler-qt4-devel libqca2-devel libqimageblitz-devel libspectre-devel zlib-devel
BuildRequires: libkscreen-devel qjson-devel
BuildRequires: libtiff-devel libjpeg-devel
BuildRequires: kde-common-devel kde4-plasma-mobile-devel libkexiv24-devel
%if_enabled activities
BuildRequires: kde4-kactivities-devel
%endif
%if_enabled msits
BuildRequires: libchm-devel
%endif

%description
Document viewer; support different kinds of documents.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common
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
%patch1 -p1


%build
%K4build


%install
%K4install

find %buildroot/%_K4xdg_apps -type f -name \*.desktop | \
while read f ; do
    sed -i '/^Exec=/s/-caption[[:space:]]*%%c//' $f
done


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
%_K4cfg/pdfsettings.kcfg
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
%_K4xdg_apps/active-documentviewer_*.desktop
%_K4apps/plasma/packages/org.kde.active.documentviewer/

%files -n libokularcore4
%_K4libdir/libokularcore.so.*

%files devel
%_K4includedir/okular/
%_K4libdir/cmake/Okular/
%_K4link/lib*.so


%changelog
* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt3
- remove captions from desktop-files Exec

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt2
- build without activities support

* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Nov 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Fri Oct 23 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.1-alt1
- new version

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- new version

* Wed Apr 01 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt1.M70P.1
- build for M70P

* Wed Apr 01 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt2
- fix build requires

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt0.M70P.1
- build for M70P

* Fri Mar 13 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt1
- new version

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Mon Nov 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Wed Oct 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Thu Aug 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Tue Jul 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Tue Apr 22 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Sat Jan 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt0.M70P.1
- built for M70P

* Fri Jan 10 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt1
- new version

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Tue Oct 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Tue Oct 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version
- truncate document title for lpr (ALT#29507)

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Thu Jul 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Tue May 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Mon Jan 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

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
