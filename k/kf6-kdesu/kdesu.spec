%define rname kdesu
%define kdesu_user _kdesu6
%define kdesu_user_dir %_localstatedir/%kdesu_user

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 user interface for running shell commands with root privileges
Url: http://www.kde.org
License: CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL

Source: %rname-%version.tar
Patch1: alt-fix-su-to-different-non-root-user.patch
Patch2: alt-export-vars.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kpty-devel kf6-kservice-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel

%description
KDESU provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.

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

%package -n libkf6su
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6su
KF6 library

%prep
%setup -n %rname-%version
%patch1 -p2
%patch2 -p1

%build
%K6build \
    -DKDESU_USE_SUDO_DEFAULT=OFF \
    #

%install
%K6install

mkdir -p %buildroot/%kdesu_user_dir

%find_lang %name --all-name
%K6find_qtlang %name --all-name

%pre -n libkf6su
/usr/sbin/useradd -M -r -d %kdesu_user_dir -s /sbin/nologin -c 'KDE SU wrapper' %kdesu_user 2>/dev/null || :

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/kdesu_version.h
%_K6inc/KDESu/
%_K6link/lib*.so
%_K6lib/cmake/KF6Su

%files -n libkf6su
%attr(0750,root,%kdesu_user) %dir %kdesu_user_dir
%_K6exec/kdesu_stub
%attr(2711,root,%kdesu_user) %_K6exec/kdesud
%_K6lib/libKF6Su.so.*


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

