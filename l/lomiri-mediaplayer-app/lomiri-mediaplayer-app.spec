%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-mediaplayer-app
Version: 1.1.1
Release: alt1

Summary: Media Player application for Ubuntu Touch devices
License: GPL-3.0-only and CC-3.0-BY-SA
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-mediaplayer-app

Source: %name-%version.tar

# sync with version 1.1.1+dfsg-3 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Multimedia)

%if_with check
BuildRequires: ctest
%endif

Requires: lomiri-mediaplayer-app-common

Requires: liblomiri-action-api-qt5
Requires: libqt5-quick
Requires: mpris-qt5-devel
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Content)
Requires: qml(QtMultimedia)
Requires: qml(QtQuick.XmlListModel)

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Media Player App capable of playing a
variety of audio and video formats both on mobile devices and desktop
computers.

%package common
Summary: Media Player App for Lomiri Operating Environment (common files)
Group: Graphical desktop/Other
BuildArch: noarch

%description common
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Media Player App capable of playing a
variety of audio and video formats both on mobile devices and desktop
computers.

This package contains architecture independent files of the Lomiri
Media Player App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DADD_MPRIS=ON \
%if_with check
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

%files
%doc AUTHORS ChangeLog COPYING COPYING.LGPL NEWS README.md
%_bindir/lomiri-mediaplayer-app

%files common -f %{name}.lang
%_desktopdir/lomiri-mediaplayer-app.desktop
%_datadir/lomiri-content-hub/peers/lomiri-mediaplayer-app
%dir %_datadir/lomiri-mediaplayer-app
%_datadir/lomiri-mediaplayer-app/*
%_datadir/lomiri-url-dispatcher/urls/lomiri-mediaplayer-app.url-dispatcher

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-mediaplayer-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-mediaplayer-app.mo

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
