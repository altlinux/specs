%add_findpackage_path %_kde4_bindir

%define rname libkipi
Name: libkipi4
Version: 4.8.0
Release: alt1

Group: System/Libraries
Summary: Interface to use kipi-plugins
Url: http://projects.kde.org/projects/kdegraphics/libs/libkipi
License: GPLv2+

Conflicts: libkipi <= 1:0.1.6-alt3
Provides: libkipi4-common = %version-%release
Obsoletes: libkipi4-common < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Sep 09 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel zlib-devel kde-common-devel

%description
Libkipi is an interface to use kipi-plugins from a KDE image management 
program like digiKam

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Conflicts: libkipi-devel
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%doc README AUTHORS NEWS README TODO
%_K4libdir/libkipi.so.*
%_K4iconsdir/hicolor/*/apps/kipi.*
%_K4apps/kipi/
%_K4srvtyp/kipiplugin.desktop

%files devel
%_K4includedir/libkipi/
%_K4link/lib*.so
%_pkgconfigdir/libkipi.pc


%changelog
* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
