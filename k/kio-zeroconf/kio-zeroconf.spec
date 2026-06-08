%define rname kio-zeroconf

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: DNS-SD Service Discovery for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPL-2.0-only

Provides: kde5-kio-zeroconf = %EVR
Obsoletes: kde5-kio-zeroconf < %EVR

Source: %rname-%version.tar
Patch1: alt-zeroconf-autonet.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libssl-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdnssd-devel kf6-ki18n-devel kf6-kio-devel

%description
DNS-SD Service Discovery for KDE

#%package -n kio-zeroconf
#Summary: DNS-SD Service Discovery for KDE
#Group: Graphical desktop/KDE
#Requires: avahi-daemon libnss-mdns
#%description -n kio-zeroconf
#DNS-SD Service Discovery for KDE

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%K6install_move data remoteview
%find_lang %name --with-kde --all-name

#files -n kio-zeroconf -f %name.lang
%files -f %name.lang
%doc LICENSES/*
%_K6plug/kf6/kded/dnssdwatcher.so
%_K6plug/kf6/kio/zeroconf.so
%_K6data/remoteview/*
%_datadir/metainfo/*.xml


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

