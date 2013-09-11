%add_findpackage_path %_kde4_bindir

%define rname libkmahjongg
Name: libkmahjongg4
%define major 4
%define minor 11
%define bugfix 1
Version: %major.%minor.%bugfix
Release: alt1

Group: System/Libraries
Summary: Library for the kmahjongg
Url: http://projects.kde.org/projects/kde/kmahjongg/libkmahjongg
License: GPLv2

Requires: %name-common = %version-%release

Source: %rname-%version.tar


# Automatically added by buildreq on Wed Oct 10 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel libicu libkdegames4-devel libqt3-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ libkdegames4-devel
BuildRequires: kde-common-devel

%description
This package contains the library used for loading and rendering
of Mahjongg tilesets and associated backgrounds, used by KMahjongg and KShisen.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common >= %major.%minor
Conflicts: kde4games-core < 4.9
BuildArch: noarch
%description common
%name common package

#%package core
#Summary: Core files for %name
#Group: Graphical desktop/KDE
#Requires: %name-common = %version-%release
#%description core
#Core files for %name

%package -n libkmahjongglib4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmahjongglib4
KDE 4 library.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Conflicts: kde4games-devel < 4.9
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install

%files common
%doc README
%_K4apps/kmahjongglib/

%files -n libkmahjongglib4
%_K4libdir/libkmahjongglib.so.*

%files devel
%_K4includedir/*.h
%_K4link/lib*.so


%changelog
* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Wed Oct 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- initial build
