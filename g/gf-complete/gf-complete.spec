
%def_disable check

Name: gf-complete
Version: 1.0.2
Release: alt2.gita6862d
Summary: Galois Field Arithmetic
License: BSD-3-Clause
Group: System/Libraries
Url: http://jerasure.org/jerasure/gf-complete
Source: %name-%version.tar
Patch2000: %name-e2k-simd.patch

%description
Galois Field arithmetic forms the backbone of erasure-coded storage systems,
most famously the Reed-Solomon erasure code. A Galois Field is defined over
w-bit words and is termed GF(2w). As such, the elements of a Galois Field are
the integers 0, 1, . . ., 2^w - 1. Galois Field arithmetic defines addition
and multiplication over these closed sets of integers in such a way that they
work as you would hope they would work. Specifically, every number has a
unique multiplicative inverse. Moreover, there is a value, typically the value
2, which has the property that you can enumerate all of the non-zero elements
of the field by taking that value to successively higher powers.

%package -n lib%name
Summary: Galois Field Arithmetic library
Group: System/Libraries

%description -n lib%name
Galois Field arithmetic forms the backbone of erasure-coded storage systems,
most famously the Reed-Solomon erasure code. A Galois Field is defined over
w-bit words and is termed GF(2w). As such, the elements of a Galois Field are
the integers 0, 1, . . ., 2^w - 1. Galois Field arithmetic defines addition
and multiplication over these closed sets of integers in such a way that they
work as you would hope they would work. Specifically, every number has a
unique multiplicative inverse. Moreover, there is a value, typically the value
2, which has the property that you can enumerate all of the non-zero elements
of the field by taking that value to successively higher powers.
This package contains the shared library.

%package -n lib%name-devel
Summary: Galois Field Arithmetic development files
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Galois Field arithmetic forms the backbone of erasure-coded storage systems,
most famously the Reed-Solomon erasure code. A Galois Field is defined over
w-bit words and is termed GF(2w). As such, the elements of a Galois Field are
the integers 0, 1, . . ., 2^w - 1. Galois Field arithmetic defines addition
and multiplication over these closed sets of integers in such a way that they
work as you would hope they would work. Specifically, every number has a
unique multiplicative inverse. Moreover, there is a value, typically the value
2, which has the property that you can enumerate all of the non-zero elements
of the field by taking that value to successively higher powers.

%package tools
Summary: CLI tools for %name
Group: Development/Tools

%description tools
Various utilities that come with the %name library.

%prep
%setup
%ifarch %e2k
%patch2000 -p1
%endif

%build
%autoreconf
%configure \
%ifarch %ix86
	--disable-sse \
%endif
%ifarch %e2k
	--disable-neon \
%endif
	--disable-static \
	--disable-silent-rules \
	--disable-rpath
%make_build

%check
%make_build check

%install
%makeinstall_std
# delete examples
rm -f %buildroot%_bindir/gf_example*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files tools
%doc COPYING README
%_bindir/*

%changelog
* Mon Sep 06 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.0.2-alt2.gita6862d
- Added SIMD patch for Elbrus.
- Added check (can be slow, disabled).

* Fri Mar 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.2-alt1.gita6862d
- Initial build.
