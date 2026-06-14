%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-terminal-app
Version: 2.0.6
Release: alt1

Summary: Terminal App for Lomiri Operating Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-terminal-app

Source: %name-%version.tar

# sync with version 2.0.5-2 from Debian unstable + missed ColorSchemeManager workaround
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: lomiri-ui-extras
Requires: libqt5-quick
Requires: libqt5-qml
Requires: lomiri-ui-toolkit
Requires: qt5-qmltermwidget
Requires: libqt5-qtsystems
Requires: libgsettings-qt1
Requires: fonts-ttf-google-noto-sans-mono

%if_with check
BuildRequires: ctest
BuildRequires: libqt5-quicktest
%endif

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Terminal App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF
%cmake_build

%install
%cmake_install

%find_lang %name

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README-Autopilot.md README.md README-MergeRequest.md
%_bindir/lomiri-terminal-app
%_man1dir/lomiri-terminal-app.1*
%_desktopdir/lomiri-terminal-app.desktop
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-terminal-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-terminal-app.mo
%dir %_datadir/lomiri-terminal-app
%_datadir/lomiri-terminal-app/*
%_datadir/lomiri-url-dispatcher/urls/lomiri-terminal-app.url-dispatcher

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.6-alt1
- New version 2.0.6.

* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.5-alt1
- Initial build for Sisyphus
