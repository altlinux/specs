%define soname 4

Name: gf2x
Version: 1.3.0.0.81.f8f1
Release: alt1
Summary: Library for multiplication over the GF2 field
License: GPL-3.0+
Group: Sciences/Mathematics
Url: https://gitlab.inria.fr/gf2x/gf2x
Vcs: git://gitlab.inria.fr/gf2x/gf2x.git

Source: https://gitlab.inria.fr/gf2x/gf2x/-/archive/%version/gf2x-%version.tar.gz

BuildRequires: makeinfo

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

%package info
Summary: Info docs for %name
Group: Documentation
BuildArch: noarch

%description info
This package contains the info documentation for the gf2x library.

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
	--disable-pclmul
%make_build

%check
%make_build check

%install
%makeinstall_std
rm -f "%buildroot%_libdir"/*.la

%files -n lib%name%soname
%doc COPYING
%_libdir/libgf2x.so.%{soname}*

%files -n lib%name-devel
%_includedir/gf2x*
%_libdir/libgf2x.so
%_pkgconfigdir/*.pc

%files info
%_infodir/*.info.xz

%changelog
* Thu Nov 21 2024 Leontiy Volodin <lvol@altlinux.org> 1.3.0.0.81.f8f1-alt1
- New version gf2x-1.3.0-81-gf8f16d4.
- Added vcs tag.

* Mon Oct 18 2021 Leontiy Volodin <lvol@altlinux.org> 1.3.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for libntl44 and sagemath.
