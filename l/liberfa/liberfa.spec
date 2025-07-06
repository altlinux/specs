Name: liberfa
Version: 2.0.1
Release: alt1

Summary: Essential Routines for Fundamental Astronomy

License: BSD-3-Clause
Group: Development/C
URL: https://github.com/liberfa/erfa
Source: %name-%version.tar

BuildRequires: meson

%description
ERFA is a C library containing key algorithms for astronomy, and is
based on the SOFA library published by the International Astronomical
Union (IAU).

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.rst LICENSE
%_libdir/liberfa.so.*

%files devel
%_libdir/liberfa.so
%_includedir/erfa*.h
%_libdir/pkgconfig/erfa.pc

%changelog
* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Initial buiild for Sisyphus.
