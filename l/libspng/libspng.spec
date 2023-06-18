%define sover 0

Name: libspng
Version: 0.7.4
Release: alt1

Summary: Simple, modern libpng alternative
License: BSD-2-Clause
Group: System/Libraries

Url: https://%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/randy408/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: meson
BuildRequires: zlib-devel

%description
Libspng is a C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security and ease of use.

Libspng is an alternative to libpng, the projects are separate and the APIs are
not compatible.

%package -n %name%sover
Summary: Simple, modern libpng alternative
Group: System/Libraries

%description -n %name%sover
Libspng is a C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security and ease of use.

Libspng is an alternative to libpng, the projects are separate and the APIs are
not compatible.

%package devel
Summary: Development files for  %name
Group: Development/C

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%meson -Denable_opt=false
%meson_build

%install
%meson_install

%check
%meson_test

%files -n %name%sover
%doc LICENSE README.md SECURITY.md
%_libdir/%name.so.*

%files devel
%_includedir/spng.h
%_pkgconfigdir/spng.pc
%_libdir/%name.so

%changelog
* Sun Jun 18 2023 Nazarov Denis <nenderus@altlinux.org> 0.7.4-alt1
- Initial build for ALT Linux
