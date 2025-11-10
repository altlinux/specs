%define _unpackaged_files_terminate_build 1

Name: mustache-cpp
Version: 4.1
Release: alt2

Summary: Mustache text templates for modern C++
License: BSL-1.0
Group: Development/C++
Url: https://github.com/kainjow/Mustache
VCS: https://github.com/kainjow/Mustache
BuildArch: noarch

Source: %name-%version.tar

Patch: mustache-cpp-4.1-fedora-cmake4-fixes.patch
# https://github.com/kainjow/Mustache/pull/42
Patch100: mustache-cpp-4.1-unknown-catch-fixes.patch

BuildRequires: catch2-devel
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax

%description
Text templates implementation for modern C++ (requires C++11).

%package devel
Group: Development/C++
Summary: Development files for mustache
Provides: mustache-static = %EVR
Provides: mustache = %EVR

%description devel
The mustache-devel package contains C++ headers for developing
applications that use mustache.

%prep
%setup
%patch0 -p1
%patch100 -p2

sed -e '/-Werror/d' -i CMakeLists.txt
ln -svf %_includedir/catch2/catch.hpp ./catch.hpp

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%check
%ctest

%install
mkdir -p %buildroot%_includedir
install -m 0644 -p mustache.hpp %buildroot%_includedir

%files devel
%doc README.md
%doc --no-dereference LICENSE
%_includedir/mustache.hpp

%changelog
* Mon Nov 10 2025 Constantin Sunzow <protvin@altlinux.org> 4.1-alt2
- Fix FTBFS: cmake 4 compatibility.

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 4.1-alt1_10
- update to new release by fcimport

* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 4.1-alt1_4
- fixed build

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_1
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2
- update to new release by fcimport

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_2
- new version

