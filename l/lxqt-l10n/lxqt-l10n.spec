Name: lxqt-l10n
Version: 0.13.0
Release: alt1

Summary: Translations of LXQt
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: cmake rpm-macros-cmake
BuildRequires: qt5-tools-devel
BuildRequires: lxqt-build-tools

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%dir %_datadir/*
%_datadir/*/translations
%doc AUTHORS CHANGELOG COPYING README.md

%changelog
* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- built for sisyphus

