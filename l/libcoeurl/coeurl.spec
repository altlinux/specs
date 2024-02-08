%define _unpackaged_files_terminate_build 1

Name: libcoeurl
Version: 0.3.0
Release: alt1

Summary: A simple async wrapper around CURL for C++

Group: Development/Other
License: MIT
Url: https://nheko.im/nheko-reborn/coeurl.git

Source: %name-%version.tar

Patch0: coeurl-fmt10-fix.patch
Patch1: coeurl-libcurl-wrap-privide-fix.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson gcc-c++ libspdlog-devel
BuildRequires: libevent-devel libcurl-devel

%description
Simple library to do http requests asynchronously via CURL in C++.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Simple library to do http requests asynchronously via CURL in C++.

This package contains C++ header files for developing and the static
library.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%doc LICENSE
%_libdir/*.so.*

%files devel
%doc examples
%_includedir/coeurl
%_libdir/*.so
%_libdir/pkgconfig/coeurl.pc

%changelog
* Wed Feb 07 2024 Paul Wolneykien <manowar@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Sat Oct 14 2023 Nazarov Denis <nenderus@altlinux.org> 0.1.1-alt2.1
- NMU: Fix build with fmt 10

* Mon Jan 10 2022 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt2
- Add missing pkgconfig (patch).

* Mon Jan 10 2022 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Initial version for Sisyphus.
