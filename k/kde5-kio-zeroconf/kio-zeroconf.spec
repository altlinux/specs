%define rname kio-zeroconf

Name: kde5-%rname
Version: 22.12.1
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: DNS-SD Service Discovery for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPL-2.0-only

Source: %rname-%version.tar
Patch1: alt-zeroconf-autonet.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
# Automatically added by buildreq on Wed Dec 20 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel perl python-base python-modules qt5-base-common qt5-base-devel
#BuildRequires: extra-cmake-modules kf5-kdbusaddons-devel kf5-kdnssd-devel kf5-ki18n-devel kf5-kio-devel libssl-devel
BuildRequires: extra-cmake-modules
BuildRequires: libssl-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdnssd-devel kf5-ki18n-devel kf5-kio-devel

%description
DNS-SD Service Discovery for KDE

#%package -n kde5-kio-zeroconf
#Summary: DNS-SD Service Discovery for KDE
#Group: Graphical desktop/KDE
#Requires: avahi-daemon libnss-mdns
#%description -n kde5-kio-zeroconf
#DNS-SD Service Discovery for KDE

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data remoteview
%find_lang %name --with-kde --all-name

#files -n kde5-kio-zeroconf -f %name.lang
%files -f %name.lang
%doc LICENSES/*
%_K5plug/kf5/kded/dnssdwatcher.so
%_K5plug/kf5/kio/zeroconf.so
%_K5data/remoteview/*

%changelog
* Tue Jan 17 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Tue Sep 20 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Thu May 19 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Thu Aug 26 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Thu May 20 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Fri Jan 15 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Mon Dec 21 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Tue Sep 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1%ubt
- new version

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1%ubt
- initial build
