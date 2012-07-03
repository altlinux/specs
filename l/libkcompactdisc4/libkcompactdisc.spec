%add_findpackage_path %_kde4_bindir

%define rname libkcompactdisc
Name: libkcompactdisc4
Version: 4.8.4
Release: alt1

Group: System/Libraries
Summary: KDE CDDB library
Url: http://projects.kde.org/projects/kde/kdeedu/libkcompactdisc
License: GPLv2

Source: %rname-%version.tar
Patch1: libkcompactdisc-4.8.4-alt-build.patch

# Automatically added by buildreq on Fri Jun 08 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libalsa-devel libicu libqt3-devel python-module-distribute qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libalsa-devel kde-common-devel

%description -n libkcompactdisc4
KDE CDDB library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4build


%install
%K4install

%files
#doc TODO
%_K4libdir/libkcompactdisc.so.*

%files devel
%_K4link/lib*.so
%_K4includedir/libkcompactdisc/

%changelog
* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- initial build
