%define _unpackaged_files_terminate_build 1
%define sover 7
%define libgpgmepp libgpgmepp%sover
%def_disable static

Name: gpgmepp
Version: 2.1.0
Release: alt1

Summary: C++ bindings for GPGME
License: LGPL-2.1-or-later
Group: System/Libraries
Url: https://www.gnupg.org/software/gpgme/index.html
Vcs: git://git.gnupg.org/gpgmepp.git

Source: %name-%version.tar
BuildRequires: cmake gcc-c++ gpgme2-devel libgpg-error-devel

%package -n %libgpgmepp
Group: System/Libraries
Summary: GPGME++ library

%description -n %libgpgmepp
C++ binding library for GPGME.

%package -n gpgmepp-devel
Summary: Include files for development with GPGME++
Group: Development/C++
Requires: gpgme2-devel

%description -n gpgmepp-devel
This package contains headers and CMake/pkg-config files for GPGME++.

%description
GPGME++ provides C++ bindings for GPGME.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n %libgpgmepp
%_libdir/libgpgmepp.so.%sover
%_libdir/libgpgmepp.so.*

%files -n gpgmepp-devel
%_includedir/gpgme++/
%_libdir/libgpgmepp.so
%_libdir/cmake/Gpgmepp/
%_pkgconfigdir/gpgmepp.pc

%changelog
* Thu Jul 09 2026 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- initial build
