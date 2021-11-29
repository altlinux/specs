%def_without openblas

Name: linbox
%define lname   liblinbox0
Version: 1.6.3
Release: alt2
Summary: C++ library for computation with matrices over ints and finite fields
License: LGPL-2.1+
Group: Sciences/Mathematics
Url: https://linalg.org/

Source: https://github.com/linbox-team/linbox/releases/download/v%version/linbox-%version.tar.gz

Patch: remove-linboxsage-libs-from-pc.patch
Patch1: fix-ksh-pkgconfig.patch
Patch2: linbox-pr-256.patch

# Couldn't find package libatlas-devel on aarch64, armh and ppc64le.
ExclusiveArch: i586 x86_64

BuildRequires: autoconf >= 2.61
BuildRequires: automake >= 1.8
BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: libiml-devel
BuildRequires: libm4ri-devel
BuildRequires: libm4rie-devel
BuildRequires: libmpfr-devel
BuildRequires: libntl-devel
BuildRequires: libflint2-devel
%if_with openblas
BuildRequires: libopenblas-devel
%else
BuildRequires: libatlas-devel
%endif
BuildRequires: fflas-ffpack-devel
BuildRequires: libtinyxml2-devel

%description
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

%package -n %lname
Summary: C++ library for computation with matrices over ints and finite fields
Group: System/Libraries

%description -n %lname
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

%package -n lib%name-devel
Summary: Development files for LinBox, a library for computation over finite fields
Group: Development/Other

%description -n lib%name-devel
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

This subpackage contains the include files and library links for
developing against the Givaro library.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --disable-static \
%ifarch %ix86
	--disable-sse --disable-sse2 \
%endif
	--disable-sse3 --disable-ssse3 --disable-sse41 --disable-sse42 \
	--disable-avx --disable-avx2 --disable-fma --disable-fma4
%make_build

%install
%makeinstall_std
rm -f "%buildroot/%_libdir"/*.la

%files -n %lname
%_libdir/liblinbox.so.0*

%files -n lib%name-devel
%_bindir/*-config
%_includedir/%name/
%_libdir/liblinbox.so
%_pkgconfigdir/*.pc
%_man1dir/*.1*
%doc COPYING*

%changelog
* Mon Nov 29 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.3-alt2
- Fixed build with sagemath.
- Added buildrequires.

* Thu Nov 11 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
