%add_findpackage_path %_kde4_bindir

%define rname libkgapi
Name: libkgapi4
Version: 0.4.1
Release: alt1

Group: System/Libraries
Summary: Google services APIs
Url: http://projects.kde.org/projects/kde/kdeedu/libkdeedu
License: GPLv2

Provides: libkgoogle4 = %version-%release
Obsoletes: libkgoogle4 < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jul 10 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-webkit libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4pimlibs-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 python-module-distribute qjson-devel qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4pimlibs-devel qjson-devel

%description
LibKGAPI (previously called LibKGoogle) is a C++ library that implements APIs for
various Google services

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
License: LGPLv2 or GPLv3
Requires: %name = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install

%files
%doc README
%_K3libdir/libkgapi.so.*

%files devel
%_libdir/cmake/LibKGAPI/
%_K4includedir/libkgapi/
%_K4link/lib*.so
%_pkgconfigdir/libkgapi.pc


%changelog
* Tue Jul 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt1
- initial build
