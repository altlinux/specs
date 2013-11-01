%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-desktop-applets
Name: kde4-ktp-desktop-applets
Version: 0.7.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Telepathy plasmoids
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Requires: kde4-ktp-common-internals-core

Provides: kde4-ktp-contact-applet = %EVR
Obsoletes: kde4-ktp-contact-applet < %EVR
Provides: kde4-ktp-presence-applet = %EVR
Obsoletes: kde4-ktp-presence-applet < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Apr 10 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbus-glib libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libtelepathy-glib libtelepathy-logger libtelepathy-logger-qt41 libtelepathy-qt4 libtelepathy-qt4-devel libxkbfile-devel phonon-devel pkg-config python-base qt-gstreamer rpm-build-gir ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-ktp-common-internals-devel kde4libs-devel libqt3-devel python-module-distribute rpm-build-ruby xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ kde4-ktp-common-internals-devel kde4libs-devel
BuildRequires: kde-common-devel

%description
%summary

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Common empty package for %rname

%package -n libktpaccountskcminternal4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n libktpaccountskcminternal4
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libtelepathy-qt4-devel
%description devel
%summary development files.

%prep
%setup -qn %rname-%version
#%patch1 -p1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang plasma_applet_org.kde.ktp-presence
%K4find_lang --with-kde --append --output=%rname.lang plasma_applet_org.kde.ktp-contact

%files -f %rname.lang
%_K4lib/plasma_applet_ktp_*.so
%_K4apps/plasma/plasmoids/org.kde.ktp-*/
%_K4apps/plasma-desktop/updates/*
%_K4srv/plasma-applet-ktp-*.desktop

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Fri Nov 01 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- new version

* Wed Oct 09 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt0.M70P.1
- built for M70P

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt1
- new version

* Tue Jun 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Fri May 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- new version

* Wed Apr 10 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- initial build
