%define _kde_alternate_placement 1

%define rname baloo-widgets
Name: kde4-baloo-widgets
Version: 4.13.0
Release: alt1

Group: System/Libraries
Summary: Widgets for Baloo
Url: https://projects.kde.org/projects/kde/kdelibs/baloo-widgets
License: LGPLv2 or LGPLv3

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 18 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-sql libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-baloo-devel kde4-kfilemetadata-devel libicu50 python-module-protobuf qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel kde4-baloo-devel kde4-kfilemetadata-devel
BuildRequires: kde-common-devel

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Developer files for %name
Requires: kde4-baloo-devel
%description devel
%summary.

%package -n libbaloowidgets4
Group: System/Libraries
Summary: %name library
%description -n libbaloowidgets4
%name library

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install

%files -n libbaloowidgets4
%_K4libdir/libbaloowidgets.so.*

%files devel
%_K4includedir/baloo/*.h
%_K4libdir/cmake/BalooWidgets/
%_K4link/lib*.so

%changelog
* Fri Apr 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- initial build

