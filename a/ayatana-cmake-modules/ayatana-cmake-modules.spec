%define _unpackaged_files_terminate_build 1

Name: ayatana-cmake-modules
Version: 1.7
Release: alt1

Summary: Ayatana CMake modules
License: LGPLv3
Group: Development/Tools
Url: https://gitlab.com/ubports/development/core/cmake-extras

Source: %name-%version.tar

Patch: %name-%version-debian-python3-compat.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: gcc-c++

Requires: cmake

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
%_datadir/cmake/*

%changelog
* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 1.7-alt1
- New version 1.7.

* Sun Nov 12 2023 Nikolay Strelkov <snk@altlinux.org> 1.6-alt2
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + break BuildRequires(pre) to multiple lines
  + do not own %%_datadir/cmake
  + add "Requires: cmake"
  + changed Group to Development/Tools
  + renamed patch

* Fri Dec 30 2022 Nikolay Strelkov <snk@altlinux.org> 1.6-alt1
- Initial build for Sisyphus
