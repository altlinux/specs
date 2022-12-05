%define rname alligator

Name: kde5-%rname
Version: 22.11
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: RSS/Atom feed reader
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf5-kirigami-addons

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Aug 18 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-sql libqt5-test libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-syndication-devel python3-dev qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-syndication-devel
BuildRequires: kf5-kirigami-addons-devel

%description
Alligator is a convergent RSS/Atom feed reader.

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
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5alligator
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf5alligator
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
%_K5bin/alligator
%_K5xdgapp/*alligator*.desktop
%_K5icon/hicolor/*/apps/alligator.*

#%files devel
#%_K5inc/alligator_version.h
#%_K5inc/alligator/
#%_K5link/lib*.so
#%_K5lib/cmake/alligator
#%_K5archdata/mkspecs/modules/qt_alligator.pri

#%files -n libkf5alligator
#%_K5lib/liballigator.so.*

%changelog
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

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- initial build
