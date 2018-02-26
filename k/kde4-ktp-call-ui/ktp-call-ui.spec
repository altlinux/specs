%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-call-ui
Name: kde4-ktp-call-ui
Version: 0.4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Telepathy VoIP client GUI
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar

# Automatically added by buildreq on Mon Jun 18 2012 (-bi)
# optimized out: automoc boost-devel-headers cmake cmake-modules elfutils farstream farstream-devel fontconfig fontconfig-devel glib2-devel glibc-devel-static gstreamer-devel kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbus-glib libdbus-glib-devel libdbusmenu-qt2 libfreetype-devel libgio-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-svg libqt4-xml libssl-devel libstdc++-devel libtelepathy-farstream libtelepathy-glib libtelepathy-glib-devel libtelepathy-qt4 libtelepathy-qt4-devel libxkbfile-devel libxml2-devel phonon-devel pkg-config python-base qt-gstreamer xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ kde4-ktp-common-internals-devel kde4libs-devel libqt3-devel libtelepathy-farstream-devel qt-gstreamer-devel qt4-designer zlib-devel-static
BuildRequires: gcc-c++ kde4-ktp-common-internals-devel kde4libs-devel libtelepathy-farstream-devel qt-gstreamer-devel
BuildRequires: kde-common-devel

%description
KCall is a GUI VoIP client software which uses the telepathy framework underneath.

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Common empty package for %rname

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
%_K4exec/ktp-call-ui
%_K4apps/ktp-call-ui/
%_K4dbus_services/org.freedesktop.Telepathy.Client.KTp.CallUi.service
%_datadir/telepathy/clients/KTp.CallUi.client

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- initial build
