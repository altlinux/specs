%add_findpackage_path %_kde4_bindir

%define rname gwenview
Name: kde4-gwenview
Version: 4.10.0
Release: alt0.4

Group: Graphics
Summary: KDE support for digital cameras
Url: http://projects.kde.org/projects/kdegraphics/gwenview
License: GPLv2+

Requires: libgwenview4 = %EVR
Provides: kde4graphics-gwenview = %version-%release
Obsoletes: kde4graphics-gwenview < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4base-devel libexiv2-devel libjpeg-devel libkipi4-devel libqt3-devel rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4base-devel libexiv2-devel libjpeg-devel libkipi4-devel zlib-devel kde-common-devel
BuildRequires: kde4-nepomuk-core-devel kde4-kactivities-devel liblcms2-devel
BuildRequires: soprano soprano-backend-redland

%description
Digital camera io_slave for Konqueror. Together gPhoto this allows you
to access your camera's picture with the URL camera:/

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%package -n libgwenview4
Summary: KDE 4 core library
Group: System/Libraries
Requires: libgwenview4 = %EVR
%description -n libgwenview4
KDE 4 core library.

%prep
%setup -qn %rname-%version

%build
%K4build


%install
%K4install


%files
%doc NEWS
%_K4bindir/gwenview
%_K4bindir/gwenview_importer
%_K4lib/gvpart.so
%_K4apps/gwenview/
%_K4apps/gvpart/
%_K4apps/solid/actions/gwenview_*.desktop
%_K4srv/ServiceMenus/slideshow.desktop
%_K4srv/gvpart.desktop
%_K4xdg_apps/gwenview.desktop
%_K4iconsdir/hicolor/*/actions/document-share.*
%_K4iconsdir/hicolor/*/apps/gwenview.*
%_K4doc/en/gwenview/

%files -n libgwenview4
%_K4libdir/libgwenviewlib.so.*

#%files devel
#%_K4includedir/gwenview/
#%_K4link/lib*.so


%changelog
* Fri Jan 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.4
- fix requires

* Thu Jan 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- rebuilt whith new exiv2

* Mon Jan 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Wed Dec 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
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

* Wed Jun 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Thu Apr 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- rebuilt with new exiv2

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
