%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname plasma-mediacenter
Name: kde4-plasma-mediacenter
Version: 1.2.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Plasma Media Center
License: GPLv2 / LGPLv2.1
Url: http://kde.org/

Requires: kde4-kffmpegthumbnailer kde4-nepomuk-core qt4-mobility

Source: %rname-%version.tar


# Automatically added by buildreq on Thu Mar 21 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby ruby-stdlibs shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-nepomuk-core-devel libicu libqt3-devel libtag-devel python-module-distribute rpm-build-ruby soprano xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ kde4-nepomuk-core-devel kde4base-workspace-devel libtag-devel
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano shared-desktop-ontologies-devel
BuildRequires: kde-common-devel

%description
Plasma Media Center

%package -n libplasmamediacenter4
Summary: %name library
Group: System/Libraries
#Requires: %name-common = %version-%release
%description -n libplasmamediacenter4
%name library

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
#Requires: %name-common = %version-%release
%description devel
Devel stuff for %name


%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname


%files -n libplasmamediacenter4
%_K4libdir/libplasmamediacenter.so.*

%files -f %rname.lang
%_kde4_bindir/plasma-mediacenter
%_K4lib/imports/org/kde/plasma/mediacenter/
%_K4lib/pmc_*.so
%_kde4_xdg_apps/plasma-mediacenter.desktop
%_K4apps/plasma/packages/org.kde.plasma.mediacenter/
%_K4srv/*.desktop
%_K4srvtyp/*.desktop
%_kde4_iconsdir/*/*/*/*pmc*.*

%files devel
%_K4includedir/mediacenter/
%_K4link/lib*.so

%changelog
* Wed Dec 25 2013 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- initial build

