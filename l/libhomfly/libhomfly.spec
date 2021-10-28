%define lname libhomfly0

Name: libhomfly
Version: 1.02r6
Release: alt1
Summary: Library to compute the homfly polynomial of a link
License: ALT-Public-Domain
Group: Sciences/Mathematics
Url: https://github.com/miguelmarco/libhomfly

Source: https://github.com/miguelmarco/libhomfly/releases/download/%version/%name-%version.tar.gz
BuildRequires: libgc-devel

%description
A library to compute the homfly polynomial of a link.

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

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la

%check
%make_build check

%files -n %lname
%_libdir/libhomfly.so.0*

%files devel
%_includedir/*.h
%_libdir/libhomfly.so

%changelog
* Thu Oct 28 2021 Leontiy Volodin <lvol@altlinux.org> 1.02r6-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
