%define _unpackaged_files_terminate_build 1

Name: ayatana-cmake-modules
Version: 1.6
Release: alt1

Summary: Ayatana CMake modules
License: LGPLv3
Group: Development/Other
Url: https://gitlab.com/ubports/development/core/cmake-extras

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

Patch: 1004_switch-to-python3.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake gcc-c++

BuildArch: noarch

%description
Extra CMake modules shared in Ubuntu Ayatana projects.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md examples
%dir %_datadir/cmake
%_datadir/cmake/*

%changelog
* Fri Dec 30 2022 Nikolay Strelkov <snk@altlinux.org> 1.6-alt1
- Initial build for Sisyphus
