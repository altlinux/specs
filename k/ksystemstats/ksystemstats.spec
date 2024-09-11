%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname ksystemstats

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 system statistics daemon
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-ksystemstats = %EVR
Obsoletes: plasma5-ksystemstats < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: libnl-devel libsensors3-devel libudev-devel
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-networkmanager-qt-devel
BuildRequires: plasma6-libksysguard-devel

%description
KSystemStats is a daemon that collects statistics about the running system.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*stat*
%_K6plug/ksystemstats/
%_K6dbus_srv/*.service
%_userunitdir/*.service


%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

