%define soversion 2
Name: libscfg
Version: 0.2.0
Release: alt1
Summary: C library for a simple configuration file format
License: MIT
Group: Development/C
URL: https://codeberg.org/emersion/libscfg
VCS: https://codeberg.org/emersion/libscfg

Source: %name-%version.tar

BuildRequires:  gcc
BuildRequires:  meson

%description
C library for a simple configuration file format.

%package -n libscfg%soversion
Summary: C library for a simple configuration file format
Group: Development/C

%description -n libscfg%soversion
C library for a simple configuration file format.

%package devel
Summary: Development files for libscfg
Group: Development/C
Requires: libscfg%soversion = %EVR

%description    devel
The libscfg-devel package contains libraries and header files for
developing applications that use libscfg.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n libscfg%soversion
%doc LICENSE README.md
%_libdir/libscfg.so.%soversion
%_libdir/libscfg.so.%version

%files devel
%_includedir/scfg.h
%_libdir/libscfg.so
%_libdir/pkgconfig/scfg.pc

%changelog
* Tue Oct 21 2025 Andrey Kovalev <ded@altlinux.org> 0.2.0-alt1
- Updated to upstream version 0.2.0.

* Wed Oct 09 2024 Andrey Kovalev <ded@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
