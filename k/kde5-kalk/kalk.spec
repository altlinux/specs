%define rname kalk

Name: kde5-%rname
Version: 23.01.0
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Convergent calculator
Url: http://www.kde.org
License: GPL-3.0-or-later

Requires: qt5-feedback

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Aug 27 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgmp-devel libqt5-core libqt5-dbus libqt5-feedback libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-test libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream extra-cmake-modules flex kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-kunitconversion-devel libmpfr-devel python3-dev qt5-feedback-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: qt5-feedback-devel qt5-quickcontrols2-devel qt5-svg-devel
BuildRequires: flex bison
BuildRequires: libmpfr-devel libgmp-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-kunitconversion-devel

%description
Kalk is a convergent calculator application.
Although it is mainly targeted for mobile platforms.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5alk
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf5alk
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/kalk
%_K5xdgapp/*kalk*desktop
%_K5icon/*/*/apps/*kalk*

#%files devel
#%_K5inc/kalk_version.h
#%_K5inc/kalk/
#%_K5link/lib*.so
#%_K5lib/cmake/kalk
#%_K5archdata/mkspecs/modules/qt_kalk.pri

#%files -n libkf5alk
#%_K5lib/libkalk.so.*

%changelog
* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 23.01.0-alt1
- new version

* Mon Dec 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.11-alt1
- new version

* Wed Oct 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.09-alt1
- new version

* Tue Jul 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.06-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 22.04-alt1
- new version

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 22.02-alt1
- new version

* Fri Dec 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.12-alt1
- new version

* Wed Sep 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt2
- fix requires

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- new version
