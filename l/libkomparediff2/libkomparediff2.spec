
Name: libkomparediff2
Version: 4.12.3
Release: alt1

Group: System/Libraries
Summary: Library to compare files and strings
Url: https://projects.kde.org/projects/kde/kdesdk/libkomparediff2
# Library: GPLv2+ (some files LGPLv2+), CMake scripts: BSD
License: GPLv2+ and BSD

Requires: diffutils
Conflicts: kde4sdk-kompare < 4.12

Source: %name-%version.tar

# Automatically added by buildreq on Tue Mar 11 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu50 qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel kde-common-devel


%description
A shared library to compare files and strings using kdelibs and GNU diff,
used in Kompare and KDevelop.

%package devel
Group: Development/KDE and QT
Summary: Developer files for %name
Conflicts: kde4sdk-kompare < 4.12
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %name-%version

%build
%K4build \
    -DKDE4_BUILD_TESTS:BOOL=OFF

%install
%K4install

%check

%files
%_K4libdir/libkomparediff2.so.*

%files devel
%_K4includedir/libkomparediff2/
%_K4link/libkomparediff2.so
%_libdir/cmake/libkomparediff2/

%changelog
* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- initial build
