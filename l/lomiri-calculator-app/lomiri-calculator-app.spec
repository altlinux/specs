%define _unpackaged_files_terminate_build 1

Name: lomiri-calculator-app
Version: 4.1.0
Release: alt1

Summary: Calculator App for Lomiri Operating Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-calculator-app

Source: %name-%version.tar

# sync with version 4.1.0-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)

Requires: libqt5-quick
Requires: lomiri-ui-toolkit
Requires: lomiri-ui-extras
Requires: qqc2-suru-style

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Calulcator App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF \
       -DINSTALL_TESTS=OFF
%cmake_build

rm -vf %buildroot/usr/share/lomiri-calculator-app/lomiri-calculator-app-migrate.py

%install
%cmake_install

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog CODE_OF_CONDUCT.md LICENSE NEWS README-Autopilot.md README.md
%_bindir/lomiri-calculator-app
%_desktopdir/lomiri-calculator-app.desktop
%dir %_datadir/lomiri-calculator-app
%_datadir/lomiri-calculator-app/*
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-calculator-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-calculator-app.mo

%changelog
* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus
