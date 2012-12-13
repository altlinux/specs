%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname nepomuk-widgets
Name: kde4-nepomuk-widgets
%define major 4
%define minor 10
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt0.1

Group: System/Libraries
Summary: Nepomuk widgets library
Url: http://projects.kde.org/projects/kde/kdelibs/nepomuk-widgets/
License: GPLv2

Source: %rname-%version.tar


# Automatically added by buildreq on Tue Dec 11 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-nepomuk-core-devel libicu libqt3-devel python-module-distribute rpm-build-ruby soprano xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4-nepomuk-core-devel xorg-xf86miscproto-devel kde-common-devel

%description
Nepomuk widgets library

%package -n libnepomukwidgets4
Summary: KDE 4 library
Group: System/Libraries
#Requires: %name-common = %version-%release
Requires: kde-common >= %major.%minor
%description -n libnepomukwidgets4
KDE 4 library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
#Requires: %name-common = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files -n libnepomukwidgets4
%_K4libdir/libnepomukwidgets.so.*

%files devel
%_K4libdir/cmake/NepomukWidgets/
%_K4includedir/nepomuk2/*.h
%_K4link/lib*.so


%changelog
* Tue Dec 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- initial build
