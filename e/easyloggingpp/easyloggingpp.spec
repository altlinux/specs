%define _unpackaged_files_terminate_build 1

Name: easyloggingpp
Version: 9.97.1
Release: alt1
Summary: Single header efficient logging library for C++ applications
Group: Development/C++
License: MIT

Url: https://github.com/amrayn/easyloggingpp/

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

BuildArch: noarch

%description
Easylogging++ is single header efficient logging library for C++ applications.
It is extremely powerful, highly extendable and configurable to user's
requirements.

%package devel
Summary: Single header efficient logging library for C++ applications
Group:   Development/C++

%description devel
Easylogging++ is single header efficient logging library for C++ applications.
It is extremely powerful, highly extendable and configurable to user's
requirements.

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE
%doc *.md
%_includedir/*
%_datadir/pkgconfig/*.pc

%changelog
* Thu Sep 14 2023 L.A. Kostis <lakostis@altlinux.ru> 9.97.1-alt1
- 9.97.1.

* Wed Mar 29 2023 L.A. Kostis <lakostis@altlinux.ru> 9.97.0-alt1
- Initial build for ALTLinux.

