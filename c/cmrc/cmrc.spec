%global appname cmakerc

Name: cmrc
Version: 2.0.1
Release: alt1

Summary: Standalone CMake-Based C++ Resource Compiler

License: MIT
Group: Development/C++
Url: https://github.com/vector-of-bool/cmrc

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url : %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch

# https://github.com/vector-of-bool/cmrc/pull/40
Patch100: %name-installation.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: ctest

%description
CMakeRC is a resource compiler provided in a single CMake script that can
easily be included in another project.

For the purpose of this project, a resource compiler is a tool that will
compile arbitrary data into a program. The program can then read this data
from without needing to store that data on disk external to the program.}

%prep
%setup
%patch100 -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc README.md
%doc LICENSE.txt
%_datadir/cmake/%appname/

%changelog
* Wed May 10 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Sisyphus

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.1-1
- Initial SPEC release.
