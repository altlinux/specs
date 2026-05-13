%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: lomiri-tfamanager-app
Version: 1.7.5
Release: alt1

Summary: 2-Factor-Authentication Manager App for Lomiri Operating Environment
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/cibersheep/tfamanager

Source: %name-%version.tar

# sync with version 1.7.3+dfsg-4 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ayatana-cmake-modules
BuildRequires: intltool

BuildArch: noarch

Requires: libqt5-qml
Requires: libqt5-quick
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Components.Extras)
Requires: qml(Lomiri.Content)
Requires: qt5-declarative-devel

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides a 2FA Manager App for Lomiri.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF
%cmake_build

%install
%cmake_install

%find_lang %name --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog LICENSE NEWS README.md
%_desktopdir/lomiri-tfamanager-app.desktop
%dir %_datadir/lomiri-tfamanager-app
%_datadir/lomiri-tfamanager-app/*
%_datadir/lomiri-content-hub/peers/lomiri-tfamanager-app
%_datadir/lomiri-url-dispatcher/urls/lomiri-tfamanager-app

%exclude %_datadir/locale/zh_Hans/LC_MESSAGES/tfamanager.cibersheep.mo
%exclude %_datadir/locale/zh_Hant/LC_MESSAGES/tfamanager.cibersheep.mo
%exclude %_datadir/locale/zh_Hant_HK/LC_MESSAGES/tfamanager.cibersheep.mo


%changelog
* Wed May 13 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.5-alt1
- New version 1.7.5.

* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 1.7.3-alt1
- Initial build for Sisyphus
