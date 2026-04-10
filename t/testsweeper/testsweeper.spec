%define        _unpackaged_files_terminate_build 1
%def_disable   check

Name:          testsweeper
Version:       2025.05.28
Release:       alt1
Summary:       TestSweeper is a C++ testing framework for parameter sweeps
License:       BSD-3-Clause
Group:         Development/Other
Url:           https://github.com/icl-utk-edu/blaspp
Vcs:           https://github.com/icl-utk-edu/blaspp.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libgomp-devel
%{?_enable_check:BuildRequires: ctest}

%description
TestSweeper is a C++ testing framework for parameter sweeps. It handles parsing
command line options, iterating over the test space, and printing results. This
simplifies test functions by allowing them to concentrate on setting up and
solving one problem at a time.

TestSweeper is part of the SLATE project (Software for Linear Algebra Targeting
Exascale), which is funded by the Department of Energy as part of its Exascale
Computing Initiative (ECP).


%package       -n lib%name
Summary:       C++ testing framework for parameter sweeps library
Group:         System/Libraries

%description   -n lib%name
TestSweeper is a C++ testing framework for parameter sweeps. It handles parsing
command line options, iterating over the test space, and printing results. This
simplifies test functions by allowing them to concentrate on setting up and
solving one problem at a time.

TestSweeper is part of the SLATE project (Software for Linear Algebra Targeting
Exascale), which is funded by the Department of Energy as part of its Exascale
Computing Initiative (ECP).

This package contains shared libraries of testsweeper.


%package       -n lib%name-devel
Summary:       C++ testing framework for parameter sweeps development files
Group:         Development/C++

Requires:      /proc
Requires:      gcc-c++
Requires:      cmake
Requires:      libgomp-devel
%{?_enable_check:Requires: ctest}

%description   -n lib%name-devel
TestSweeper is a C++ testing framework for parameter sweeps. It handles parsing
command line options, iterating over the test space, and printing results. This
simplifies test functions by allowing them to concentrate on setting up and
solving one problem at a time.

TestSweeper is part of the SLATE project (Software for Linear Algebra Targeting
Exascale), which is funded by the Department of Energy as part of its Exascale
Computing Initiative (ECP).

This package contains development files of testsweeper.


%prep
%setup

%build
%cmake \
%if_disabled check
   -Dbuild_tests=OFF \
%endif
   -Duse_openmp=ON \
   %nil

%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files         -n lib%name
%doc README.md CHANGELOG.md INSTALL.md LICENSE
%_libdir/lib%{name}*.so.*

%files         -n lib%name-devel
%doc README.md CHANGELOG.md INSTALL.md LICENSE
%_libdir/lib%{name}*.so
%_includedir/%{name}.hh
%_cmakedir/%name/


%changelog
* Fri Apr 10 2026 Pavel Skrylev <majioa@altlinux.org> 2025.05.28-alt1
- initial build for Sisyphus
