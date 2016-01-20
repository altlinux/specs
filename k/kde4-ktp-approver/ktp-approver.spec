%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-approver
Name: kde4-ktp-approver
Version: 0.9.0
Release: alt2

Group: Graphical desktop/KDE
Summary: KDE Channel Approver for Telepathy
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Requires: kde4-ktp-common-internals-common

Source0: %rname-%version.tar

# Automatically added by buildreq on Mon Apr 16 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libtelepathy-qt4 libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: dbus-tools gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel libtelepathy-qt4-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: dbus-tools gcc-c++ kde4libs-devel libtelepathy-qt4-devel
BuildRequires: kde4-ktp-common-internals-devel
BuildRequires: kde-common-devel

%description
%{summary}


%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang kded_ktp_approver

%files -f %rname.lang
%_K4lib/kded_ktp_approver.so
%_K4srv/kded/ktp_approver.desktop
%_K4srvtyp/ktp-approver.desktop
%_K4conf/ktp_approverrc
%_K4dbus_services/org.freedesktop.Telepathy.Client.KTp.Approver.service

%changelog
* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt2
- fix requires

* Fri Oct 31 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M70P.1
- built for M70P

* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

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

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
