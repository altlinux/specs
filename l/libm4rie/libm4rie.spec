Name: libm4rie
# Note that libm4rie is not always updated in lockstep with libm4ri,
# and that is absolutely normal.
%define lname libm4rie0
Version: 20200125
Release: alt1
Summary: Library for linear arithmetic over GF(2^e)
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://bitbucket.org/malb/m4rie

# Git-Clone:	https://bitbucket.org/malb/m4rie.git
Source: https://bitbucket.org/malb/m4rie/downloads/m4rie-%version.tar.gz

BuildRequires: libm4ri-devel

%description
M4RIE is a library for arithmetic with dense matrices over the
Galois Field GF(2^e).

%package -n %lname
Summary: Library for linear arithmetic over GF(2^e)
Group: System/Libraries

%description -n %lname
M4RIE is a library for arithmetic with dense matrices over the
Galois Field GF(2^e).

%package devel
Summary: Development files for GF(2^e) arithmetic with libm4rie
Group: Development/C

%description devel
M4RIE is a library for arithmetic with dense matrices over the
Galois Field GF(2^e).

This subpackage contains libraries and header files for developing
applications that want to make use of libm4rie.

%prep
%setup -n m4rie-%version

%build
%add_optflags -L/%_lib -lm
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n %lname
%_libdir/libm4rie-0.0.20200115.so

%files devel
%_libdir/libm4rie.so
%_pkgconfigdir/*.pc
%_includedir/m4rie/

%changelog
* Tue Nov 16 2021 Leontiy Volodin <lvol@altlinux.org> 20200125-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
