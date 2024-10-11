%define soversion 1
Name: libscfg
Version: 0.1.1
Release: alt1
Summary: C library for a simple configuration file format
License: MIT
Group: Development/C
URL: https://sr.ht/~emersion/libscfg/
VCS: https://git.sr.ht/~emersion/libscfg

Source: %name-%version.tar

Patch1: libscfg-0.1.1-upstream-build-set-library-version-and-soversion.patch

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

%patch1 -p1

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
* Wed Oct 09 2024 Andrey Kovalev <ded@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
