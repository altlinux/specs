%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-call-ui
Name: kde4-ktp-call-ui
Version: 0.8.1
Release: alt2

Group: Graphical desktop/KDE
Summary: Telepathy VoIP client GUI
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar
Patch1: ktp-call-ui-0.8.1-gstreamer1-0001-Require-farstream-0.2.patch
Patch2: ktp-call-ui-0.8.1-gstreamer1-0002-Rename-src-d-to-src_-u.patch
Patch3: ktp-call-ui-0.8.1-gstreamer1-0003-rename-enable-last-buffer-to-enable-last-sample.patch
Patch4: ktp-call-ui-0.8.1-gstreamer1-0004-rename-caps-type-name-removing-0.10-format.patch
Patch5: ktp-call-ui-0.8.1-gstreamer1-0005-ffmpegcolorspace-videoconvert.patch
Patch6: ktp-call-ui-0.8.1-gstreamer1-0006-Update-cmake-to-look-for-farstream-0.2.patch
Patch7: ktp-call-ui-0.8.1-gstreamer1-0007-videomaxrate-seems-to-have-been-generalized-into-vid.patch
Patch8: ktp-call-ui-0.8.1-gstreamer1-0008-Remove-postproc_tmpnoise-from-TfVideoContentHandler-.patch

# Automatically added by buildreq on Mon Jun 18 2012 (-bi)
# optimized out: automoc boost-devel-headers cmake cmake-modules elfutils farstream farstream-devel fontconfig fontconfig-devel glib2-devel glibc-devel-static gstreamer-devel kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbus-glib libdbus-glib-devel libdbusmenu-qt2 libfreetype-devel libgio-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-svg libqt4-xml libssl-devel libstdc++-devel libtelepathy-farstream libtelepathy-glib libtelepathy-glib-devel libtelepathy-qt4 libtelepathy-qt4-devel libxkbfile-devel libxml2-devel phonon-devel pkg-config python-base qt-gstreamer xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ kde4-ktp-common-internals-devel kde4libs-devel libqt3-devel libtelepathy-farstream-devel qt-gstreamer-devel qt4-designer zlib-devel-static
BuildRequires: gcc-c++ kde4-ktp-common-internals-devel kde4libs-devel qt-gstreamer1-devel
BuildRequires: pkgconfig(farstream-0.2) libtelepathy-farstream-devel
BuildRequires: pkgconfig(QtGStreamer-1.0)
BuildRequires: libtelepathy-qt4-devel-static
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname

%files -f %rname.lang
%_kde4_bindir/ktp-dialout-ui
%_K4exec/ktp-call-ui
%_K4apps/ktp-call-ui/
%_K4dbus_services/org.freedesktop.Telepathy.Client.KTp.CallUi.service
%_datadir/telepathy/clients/KTp.CallUi.client

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Mon Sep 29 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt2
- build with gstreamer1

* Wed May 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt0.M70P.1
- built for M70P

* Tue May 20 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Thu Apr 03 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt0.M70P.1
- built for M70P

* Wed Mar 19 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt0.M70P.1
- built for M70P

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- new version

* Tue Dec 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt0.M70P.1
- built for M70P

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
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt1
- new version

* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Wed Aug 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- new version

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- initial build
