%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-clock-app
Version: 4.1.1
Release: alt1

Summary: Clock App for Lomiri Operating Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-clock-app

Source: %name-%version.tar

# sync with version 4.1.1-1 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(geonames)
BuildRequires: qt5-declarative-devel

%if_with check
BuildRequires: ctest
BuildRequires: xvfb-run
BuildRequires: libu1db-qt5
BuildRequires: libusermetrics
BuildRequires: qml(Lomiri.Components)
BuildRequires: qml(Lomiri.Content)
BuildRequires: qml(Lomiri.Layouts)
BuildRequires: qml(QtMultimedia)
BuildRequires: qml(QtPositioning)
BuildRequires: qml(QtQuick.XmlListModel)
%endif

Requires: libu1db-qt5
Requires: libusermetrics
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Content)
Requires: qml(Lomiri.Layouts)
Requires: qml(QtMultimedia)
Requires: qml(QtPositioning)
Requires: qml(QtQuick.XmlListModel)

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Clock App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DCLICK_MODE=OFF \
       -DINSTALL_TESTS=OFF \
%if_with check
       -DQMLTESTRUNNER_BIN=%_qt5_bindir/qmltestrunner \
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README-Developers.md README.md README-MergeRequest.md README-Unittest.md
%_bindir/lomiri-clock-app
%_desktopdir/lomiri-clock-app.desktop
%dir %_datadir/lomiri-clock-app
%_datadir/lomiri-clock-app/*
%dir %_qt5_qmldir/ClockApp
%_qt5_qmldir/ClockApp/*
%_datadir/lomiri-url-dispatcher/urls/lomiri-clock-app.url-dispatcher

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-clock-app.mo
%exclude %_datadir/locale/zh_Hant_HK/LC_MESSAGES/lomiri-clock-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-clock-app.mo

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 4.1.1-alt1
- Initial build for Sisyphus
