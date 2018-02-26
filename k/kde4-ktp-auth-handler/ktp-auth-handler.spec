%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-auth-handler
Name: kde4-ktp-auth-handler
Version: 0.4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Provide UI/KWallet Telepathy Integration
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar

# Automatically added by buildreq on Mon Apr 16 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-webkit libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libtelepathy-qt4 libtelepathy-qt4-devel libxkbfile-devel phonon-devel pkg-config python-base xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-ktp-common-internals-devel kde4libs-devel libicu libqt3-devel zlib-devel-static
BuildRequires: gcc-c++
BuildRequires: kde4-ktp-common-internals-devel kde4libs-devel qjson-devel
BuildRequires: kde-common-devel

%description
Provide UI/KWallet Integration For Passwords and SSL Errors on Account Connect

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
Requires: %name-common >= %version-%release
%description -n libktpaccountskcminternal4
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

%files -f %rname.lang
%_K4exec/ktp-auth-handler
%_K4dbus_services/org.freedesktop.Telepathy.Client.KTp.SASLHandler.service
%_datadir/telepathy/clients/KTp.SASLHandler.client

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
