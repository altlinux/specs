%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-text-ui
Name: kde4-ktp-text-ui
Version: 0.4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Telepathy text chat handler
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
# GPLv2+: most code
# (BSD or AFL): data/styles/renkoo.AdiumMessageStyle
# MIT:  data/styles/simkete/, fadomatic javascript code used in Renkoo
License: GPLv2+ and (BSD or AFL) and MIT

Requires: telepathy-logger

Source0: %rname-%version.tar
Patch1: ktp-text-ui-0.3.0-alt-libktpchat-soname.patch

# Automatically added by buildreq on Tue Apr 17 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgio-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-webkit libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libtelepathy-qt4 libtelepathy-qt4-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ kde4-ktp-common-internals-devel kde4libs-devel libicu libqt3-devel libtelepathy-glib-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ libtelepathy-glib-devel
BuildRequires: kde4-ktp-common-internals-devel kde4libs-devel
BuildRequires: kde-common-devel
BuildRequires: libtelepathy-logger-devel telepathy-logger-qt4-devel qt-gstreamer-devel

%description
%summary

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Common empty package for %rname

%package -n libktpchat4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpchat4
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libtelepathy-qt4-devel kde4-ktp-common-internals-devel
%description devel
%summary.

%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name
#K4find_lang --with-kde --append --output=%rname.lang ktp-text-ui
find %buildroot/%_K4i18n -type f -name k\*.mo | sed "s|\.mo$||" | \
while read f; do echo `basename "$f"`; done | sort -u | \
while read n
do
    %K4find_lang --with-kde --append --output=%rname.lang "$n"
done


%files common

%files -n libktpchat4
%_K4libdir/libktpchat.so.*


%files -f %rname.lang
%doc data/styles/renkoo.AdiumMessageStyle/Contents/Resources/Renkoo\ LICENSE.txt
%doc data/styles/SimKete.AdiumMessageStyle/Contents/README
%_kde4_bindir/ktp-log-viewer
%_K4lib/kcm_ktp_chat_appearance.so
%_K4lib/kcm_ktp_chat_behavior.so
%_K4lib/imports/org/kde/telepathy/
%_K4exec/ktp-adiumxtra-protocol-handler
%_K4exec/ktp-text-ui
%_K4srv/kcm_ktp_chat_appearance.desktop
%_K4srv/kcm_ktp_chat_behavior.desktop
%_K4apps/ktelepathy/
%_K4apps/ktp-text-ui/
%_K4apps/plasma/plasmoids/org.kde.ktp-chatplasmoid/
%_K4srv/adiumxtra.protocol
%_K4srv/plasma-applet-ktpchat.desktop
%_kde4_xdg_apps/ktp-log-viewer.desktop
%_K4dbus_services/org.freedesktop.Telepathy.Client.KTp.TextUi.service
%_datadir/telepathy/clients/KTp.TextUi.client

%files devel
%_K4link/lib*.so
%_K4includedir/KTp/*

%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt3
- fix build requires

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt2
- built with telepathy-logger-qt

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
