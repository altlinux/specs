%define _unpackaged_files_terminate_build 1

Name: lomiri-sounds
Version: 25.01
Release: alt1

Summary: Sounds for the Lomiri operating environment
License: CC0-1.0 AND CC-BY-3.0 AND CC-BY-SA-3.0 AND CC-BY-4.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/core/lomiri-sounds

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++

BuildArch: noarch

%description
The Lomiri shell is the primary user interface for Lomiri based mobile
devices.

Provides notification and ringtones sound effects for the Lomiri
operating environment.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog LICENSE README.md
%_datadir/pkgconfig/lomiri-sounds.pc
%dir %_datadir/sounds/lomiri
%_datadir/sounds/lomiri/*

%changelog
* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 25.01-alt1
- Initial build for Sisyphus
