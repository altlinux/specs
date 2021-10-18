%define soname 3

Name: gf2x
Version: 1.3.0
Release: alt1
Summary: Library for multiplication over the GF2 field
License: GPL-3.0+
Group: Sciences/Mathematics
Url: https://gitlab.inria.fr/gf2x/gf2x

Source: https://gitlab.inria.fr/gf2x/gf2x/uploads/c46b1047ba841c20d1225ae73ad6e4cd/gf2x-%version.tar.gz

%description
gf2x is a library for multiplication of polynomials over the
GF2 binary field.

%package -n lib%name%soname
Summary: Library for multiplication over the GF2 field
Group: Sciences/Mathematics

%description -n lib%name%soname
gf2x is a library for multiplication of polynomials over the
GF2 binary field.

%package -n lib%name-devel
Summary: Development headers for libgf2x
Group: Development/Other

%description -n lib%name-devel
gf2x is a library for fast multiplication of polynomials over the
GF2 binary field.

This package contains the interface definitions for the gf2x library.

%prep
%setup

%build
%autoreconf
# SSE2 may not be available on all x86_32 machines.
# PCLMUL may not be available on all machines.
%configure \
        --disable-static \
%ifarch %ix86
	--disable-sse2 \
%endif
	--disable-pclmul \
	--enable-fft-interface
%make_build

%check
%make_build check

%install
%makeinstall_std
rm -f "%buildroot%_libdir"/*.la

%files -n lib%name%soname
%doc COPYING
%_libdir/libgf2x.so.%{soname}*
%_libdir/libgf2x-fft.so.%{soname}*

%files -n lib%name-devel
%_includedir/gf2x*
%_libdir/libgf2x.so
%_libdir/libgf2x-fft.so
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 18 2021 Leontiy Volodin <lvol@altlinux.org> 1.3.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for libntl44 and sagemath.
