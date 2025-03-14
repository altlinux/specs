%define _unpackaged_files_terminate_build 1

Name: libcng-dpapi
Version: 0.0.2
Release: alt2

Summary: Client library for CNG-DPAPI
License: GPLv2+
Group: Development/C
Url: https://github.com/august-alt/libcng-dpapi

BuildRequires: rpm-macros-cmake cmake cmake-modules gcc-c++
BuildRequires: libkrb5-devel samba-devel samba-common-libs libgkdi-devel
BuildRequires: libssl-devel libldap-devel libsasl2-devel
BuildRequires: doxygen

Requires: cmake

Source0: %name-%version.tar

%description
Client library for CNG-DPAPI

%package devel
Summary: CNG-DPAPI Libraries and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libcng-dpapi.so.*

%files devel
%doc README.md
%doc INSTALL.md

%_includedir/cng-dpapi/*.h
%_libdir/libcng-dpapi.so
%_libdir/cng-dpapi/CNGDpApiConfig.cmake

%changelog
* Fri Mar 14 2025 Vladimir Rubanov <august@altlinux.org> 0.0.2-alt2
- 0.0.2-alt2
- Update build dependencies

* Sun Feb 02 2025 Vladimir Rubanov <august@altlinux.org> 0.0.2-alt1
- 0.0.2-alt1
- Update packaging

* Sun May 12 2024 Vladimir Rubanov <august@altlinux.org> 0.0.1-alt1
- 0.0.1-alt1
- Initial build
