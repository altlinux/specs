%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname krdp

%define sover 6
%define libkrdp libkrdp%sover

Name: %rname
Version: 6.3.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Desktop sharing using RDP server
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: /usr/bin/openssl

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libfreerdp-devel libwinpr-devel /usr/bin/winpr-makecert
BuildRequires: libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel
BuildRequires: qt6-wayland-devel plasma-wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kcrash-devel kf6-kconfig-devel kf6-kdbusaddons-devel kf6-kcmutils-devel kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kstatusnotifieritem-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
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

%build
%K6build

%install
%K6install
#%buildroot/%_userunitdir/app-org.kde.krdpserver.service
mkdir -p %buildroot/%_userunitdir/plasma-workspace@.target.d/
ALIAS=`grep '^Alias=' %buildroot/%_userunitdir/app-org.kde.krdpserver.service | tail -n 1 | sed 's|Alias=||'`
[ -n "$ALIAS" ] || exit 1
ln -sr %buildroot/%_userunitdir/app-org.kde.krdpserver.service "%buildroot/%_userunitdir/plasma-workspace@.target.d/$ALIAS"
ln -s app-org.kde.krdpserver.service "%buildroot/%_userunitdir/$ALIAS"

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/krdpserver
%_K6plug/plasma/kcms/systemsettings/*krdp*.so
%_K6xdgapp/*krdp*.desktop
%_userunitdir/*krdp*.service
%_userunitdir/*/*krdp*.service
%_datadir/qlogging-categories6/*.*categories
#%_datadir/metainfo/*.xml

%files -n %libkrdp
%_K6lib/libKRdp.so.%sover
%_K6lib/libKRdp.so.*

%files devel
%_libdir/cmake/KRdp/
%_K6link/lib*.so

%changelog
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

