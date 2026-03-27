%define lname libhomfly0

Name: libhomfly
Version: 1.04
Release: alt1
Summary: Library to compute the homfly polynomial of a link
License: Unlicense
Group: Sciences/Mathematics
Url: https://github.com/miguelmarco/libhomfly
VCS: https://github.com/miguelmarco/libhomfly

# Source-url: https://github.com/miguelmarco/libhomfly/releases/download/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildRequires: libgc-devel

%description
A library to compute the homfly polynomial of a link.

%package common
Summary: Common files for the homfly library
Group: Sciences/Mathematics
BuildArch: noarch

%description common
This package provides common files for %name.

%package -n %lname
Summary: Library to compute the homfly polynomial of a link
Group: System/Libraries

%description -n %lname
A library to compute the homfly polynomial of a link.

%package devel
Summary: Development files for the homfly library
Group: Development/C++
Requires: %lname = %version

%description devel
A library to compute the homfly polynomial of a link.

This subpackage provides the development headers for it.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la

%check
%make_build check

%files common
%doc LICENSE README.md

%files -n %lname
%_libdir/libhomfly.so.0*

%files devel
%_includedir/*.h
%_libdir/libhomfly.so
%_pkgconfigdir/libhomfly.pc

%changelog
* Fri Mar 27 2026 Leontiy Volodin <lvol@altlinux.org> 1.04-alt1
- New version 1.04.

* Mon Aug 18 2025 Leontiy Volodin <lvol@altlinux.org> 1.03-alt1
- New version 1.03.
- Added VCS tag.
- Packaged docs.
- Fixed license tag.

* Thu Oct 28 2021 Leontiy Volodin <lvol@altlinux.org> 1.02r6-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
