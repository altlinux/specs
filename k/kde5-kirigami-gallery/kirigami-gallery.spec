%define rname kirigami-gallery

Name: kde5-%rname
Version: 22.12.3
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: Widget Browser for Kirigami
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: qml(QtGraphicalEffects)
#Requires: qml(org.kde.kitemmodels)
Requires: libkf5itemmodels

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Oct 21 2022 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kcoreaddons-common libctf-nobfd0 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-svg libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel qt5-tools rpm-build-file rpm-build-python3 sh4 tzdata
#BuildRequires: appstream extra-cmake-modules git-core kf5-kirigami-devel kf5-kitemmodels-devel libkf5plasmaquick lua5.3 python3-module-setuptools python3-module-zope qt5-graphicaleffects qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-tools-devel qt5-translations qt5-wayland-devel qt5-webengine-devel rpm-build-kf5 tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-quickcontrols2-devel qt5-svg-devel qt5-tools-devel
BuildRequires: kf5-kirigami-devel kf5-kitemmodels-devel


%description
Application which uses all features from kirigami,
including links to the sourcecode, tips on how to use
the components and links to the corresponding
HIG pages and code examples on invent.

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


%prep
%setup -n %rname-%version


%build
%K5build


%install
%K5install
%K5install_move data locale
%find_lang %name --with-kde --all-name
%K5find_qtlang %name --all-name


%files -f %name.lang
%doc LICENSE*
%_K5bin/*
%_K5xdgapp/*.desktop


%changelog
* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Mon Feb 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Fri Oct 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- initial build
