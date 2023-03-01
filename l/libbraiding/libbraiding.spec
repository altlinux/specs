%define lname libbraiding0

Name: libbraiding
Version: 1.2
Release: alt1

Summary: Library for computations on braid groups

License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://github.com/miguelmarco/libbraiding

Source: %url/releases/download/%version/%name-%version.tar.gz

BuildRequires: gcc-c++

%description
CBraid is a C++ library for various computations on braid groups,
such as normal forms.

%package -n %lname
Summary: Library for computations on braid groups
Group: System/Libraries

%description -n %lname
CBraid is a C++ library for various computations on braid groups,
such as normal forms.

%package devel
Summary: Development files for the CBraid library
Group: Development/C++

%description devel
CBraid is a C++ library for various computations on braid groups,
such as normal forms.

This subpackage provides the development headers for it.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%files -n %lname
%_libdir/libbraiding.so.0*

%files devel
%_libdir/libbraiding.so
%_includedir/*braid*.h

%changelog
* Wed Mar 01 2023 Leontiy Volodin <lvol@altlinux.org> 1.2-alt1
- New version (1.2).

* Thu Oct 28 2021 Leontiy Volodin <lvol@altlinux.org> 1.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
