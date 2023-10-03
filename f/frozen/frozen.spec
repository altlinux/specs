%define _unpackaged_files_terminate_build 1
%def_enable test

%define commit_id .gee73729
%define commit_num .23

Name: frozen
Version: 1.1.1.0%commit_num%commit_id
Release: alt1

Summary: Header-only library that provides 0 cost initialization for immutable containers, fixed-size containers, and various algorithms.
Group: Development/C++
License: Apache-2.0

Url: https://github.com/serge-sans-paille/frozen.git

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libstdc++-devel
%{?_enable_test:BuildRequires: ctest}

%description
%summary

%package devel
Summary: headers and cmake files for %name
Group: Development/C++

%description devel
%summary


%prep
%setup

%build
%cmake \
%if_disabled test
	-D frozen.tests=OFF\
%endif

%cmake_build

%install
%cmake_install

%check
%if_enabled test
%ctest
%endif

%files devel
%doc README.rst AUTHORS examples
%_includedir/%name
%_datadir/cmake/%name

%changelog
* Tue Oct 03 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.1.1.0.23.gee73729-alt1
- Initial build for Sisyphus.
