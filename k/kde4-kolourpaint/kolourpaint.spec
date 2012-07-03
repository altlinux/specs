%add_findpackage_path %_kde4_bindir

%define rname kolourpaint
Name: kde4-kolourpaint
Version: 4.8.4
Release: alt1

Group: Graphics
Summary: KDE paint program
Url: http://projects.kde.org/projects/kdegraphics/kolourpaint
License: BSD

Provides: kde4graphics-kolourpaint = %version-%release
Obsoletes: kde4graphics-kolourpaint < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqimageblitz-devel libqt3-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel zlib-devel kde-common-devel libqimageblitz-devel

%description
An easy-to-use paint program designed for everyday tasks like drawing
simple diagrams/logos/icons and editing screenshots.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%package -n libkolourpaint4
Summary: KDE 4 core library
Group: System/Libraries
%description -n libkolourpaint4
KDE 4 core library.

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%doc COPYING
%_K4bindir/kolourpaint
%_K4apps/kolourpaint/
%_K4xdg_apps/kolourpaint.desktop
%_K4iconsdir/hicolor/*/apps/kolourpaint.*
%_K4doc/*/kolourpaint/

%files -n libkolourpaint4
%_K4libdir/libkolourpaint_lgpl.so.*

#%files devel
#%_K4includedir/kolourpaint/
#%_K4link/lib*.so


%changelog
* Wed Jun 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
