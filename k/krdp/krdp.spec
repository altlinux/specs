%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname krdp

%define sover 6
%define libkrdp libkrdp%sover

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Desktop sharing using RDP server
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: /usr/bin/openssl
Requires: qml6(org.kde.kirigamiaddons.formcard)

Source: %rname-%version.tar
Patch1: kdebug-503474-avc444.patch
Patch2: alt-use_nla_security.patch


BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libfreerdp3-devel libwinpr3-devel xfreerdp3
BuildRequires: libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel
BuildRequires: qt6-wayland-devel plasma-wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libpam0-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kcrash-devel kf6-kconfig-devel kf6-kdbusaddons-devel kf6-kcmutils-devel kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kstatusnotifieritem-devel kf6-kconfigwidgets-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kirigami-addons kf6-kirigami-addons-devel
BuildRequires: plasma6-kpipewire-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkrdp
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkrdp
%name library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p2

%build
%K6build

%install
%K6install
# service should never be enabled by default
#mkdir -p %buildroot/%_userunitdir/plasma-workspace@.target.d/
#ALIAS=`grep '^Alias=' %buildroot/%_userunitdir/app-org.kde.krdpserver.service | tail -n 1 | sed 's|Alias=||'`
#[ -n "$ALIAS" ] || exit 1
#ln -sr %buildroot/%_userunitdir/app-org.kde.krdpserver.service "%buildroot/%_userunitdir/plasma-workspace@.target.d/$ALIAS"
#ln -s app-org.kde.krdpserver.service "%buildroot/%_userunitdir/$ALIAS"

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/krdpserver
%_K6plug/plasma/kcms/systemsettings/*krdp*.so
%_K6xdgapp/*krdp*.desktop
%_userunitdir/*krdp*.service
#%_userunitdir/*/*krdp*.service
%_user_presetdir/*krdp*.preset
%_datadir/qlogging-categories6/*.*categories
#%_datadir/metainfo/*.xml

%files -n %libkrdp
%_K6lib/libKRdp.so.%sover
%_K6lib/libKRdp.so.*

%files devel
%_libdir/cmake/KRdp/
%_K6link/lib*.so

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Wed Mar 04 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt4
- add upstream fixes

* Mon Mar 02 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt3
- add fix for Windows authority

* Wed Feb 18 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt2
- add fix against kdebug#503474

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Mar 05 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt2
- package systemd service alias (altbug#53246)

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Thu Oct 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- initial build

