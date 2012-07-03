%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-common-internals
Name: kde4-ktp-common-internals
Version: 0.4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Common internals for KDE Telepathy
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 03 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libtelepathy-qt4 libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel libtelepathy-qt4-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libtelepathy-qt4-devel python-module-distribute
BuildRequires: kde-common-devel

%description
%summary.

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Common empty package for %rname

%package -n libktpcommoninternalsprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpcommoninternalsprivate4
%name library.

%package -n libktpmodelsprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpmodelsprivate4
%name library.

%package -n libktpwidgetsprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpwidgetsprivate4
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libtelepathy-qt4-devel
%description devel
%summary.

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname


%files common -f %rname.lang
%_kde4_iconsdir/hicolor/*/actions/im-*.*
%_kde4_iconsdir/hicolor/*/actions/sort-*.*
%_kde4_iconsdir/hicolor/*/apps/telepathy-kde.*
%_K4apps/ktelepathy/

%files  -n libktpcommoninternalsprivate4
%_K4libdir/libktpcommoninternalsprivate.so.*
%files  -n libktpmodelsprivate4
%_K4libdir/libktpmodelsprivate.so.*
%files  -n libktpwidgetsprivate4
%_K4libdir/libktpwidgetsprivate.so.*

%files devel
%_K4link/lib*.so
%_K4includedir/KTp/

%changelog
* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
