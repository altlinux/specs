%add_findpackage_path %_kde4_bindir

%define rname libkexiv2
Name: libkexiv24
Version: 4.8.0
Release: alt1

Group: System/Libraries
Summary: Wrapper around Exiv2 library
Url: http://projects.kde.org/projects/kdegraphics/libs/libkexiv2
License: GPLv2+

Provides: libkexiv24-common = %version-%release
Obsoletes: libkexiv24-common < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Sep 09 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libexiv2-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libexiv2-devel zlib-devel kde-common-devel

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures 
metadata as EXIF/IPTC and XMP.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Conflicts: libkexiv2-devel
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
%_K4libdir/libkexiv2.so.*
%_K4apps/libkexiv2/

%files devel
%_K4includedir/libkexiv2/
%_K4link/lib*.so
%_pkgconfigdir/libkexiv2.pc


%changelog
* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- rebuilt with new exiv2

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
