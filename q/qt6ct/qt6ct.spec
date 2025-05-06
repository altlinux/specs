
%define _unpackaged_files_terminate_build 1

%define qt6_version %{get_version libqt6-core}

Name:     qt6ct
Version:  0.9
Release:  alt2.git55dba87

Summary:  Qt6 Configuration Tool
License:  BSD-2-Clause
Group:    Other
Url:      https://github.com/trialuser02/qt6ct

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source:   %name-%version.tar

BuildRequires: cmake
BuildRequires: qt6-base-devel qt6-tools-devel qt6-svg-devel
BuildRequires: pkgconfig(xkbcommon)

%if "%qt6_version"
# this package requires rebuild on every qt6 update
Requires: libqt6-core = %qt6_version
%endif

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
%_libdir/lib%{name}*
%_datadir/%name
%_desktopdir/*
%_qt6_archdatadir/plugins/*/*%{name}*.so

%doc README

%changelog
* Tue May 06 2025 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt2.git55dba87
- build from a git snapshot;
- rebuild with recent Qt6;
- require the Qt6 version we've been build with.

* Tue Sep 26 2023 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt1
- 0.9

* Mon Mar 13 2023 Ivan A. Melnikov <iv@altlinux.org> 0.8-alt1
- 0.8

* Mon Oct 31 2022 Ivan A. Melnikov <iv@altlinux.org> 0.7-alt1
- 0.7

* Fri Sep 30 2022 Ivan A. Melnikov <iv@altlinux.org> 0.6-alt1
- 0.6

* Tue Mar 15 2022 Ivan A. Melnikov <iv@altlinux.org> 0.5-alt1
- Initial build for Sisyphus
