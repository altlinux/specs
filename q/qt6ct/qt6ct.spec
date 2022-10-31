
%define _unpackaged_files_terminate_build 1

Name:     qt6ct
Version:  0.7
Release:  alt1

Summary:  Qt6 Configuration Tool
License:  BSD-2-Clause
Group:    Other
Url:      https://github.com/trialuser02/qt6ct

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source:   %name-%version.tar

BuildRequires: cmake
BuildRequires: qt6-base-devel qt6-tools-devel qt6-svg-devel
BuildRequires: pkgconfig(xkbcommon)

%description
This program allows users to configure Qt6 settings (theme, font,
icons, etc.) under DE/WM without Qt integration.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_qt6_archdatadir/plugins/*/*%{name}*.so

%doc README

%changelog
* Mon Oct 31 2022 Ivan A. Melnikov <iv@altlinux.org> 0.7-alt1
- 0.7

* Fri Sep 30 2022 Ivan A. Melnikov <iv@altlinux.org> 0.6-alt1
- 0.6

* Tue Mar 15 2022 Ivan A. Melnikov <iv@altlinux.org> 0.5-alt1
- Initial build for Sisyphus
