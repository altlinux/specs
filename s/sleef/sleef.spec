%define _unpackaged_files_terminate_build 1
%def_disable static

%define abiversion 3

%def_with devel
%def_with doc
%def_with dft
%def_with tlfloat
%def_with quad

Name:    sleef
Version: 3.9.0
Release: alt1

Summary: SIMD Library for Evaluating Elementary Functions, vectorized libm and DFT
License: BSL-1.0
Group:   System/Libraries
Url:     https://sleef.org/
Vcs:     https://github.com/shibatch/sleef.git

Source: %name-%version.tar

ExcludeArch: %ix86

%ifarch aarch64
%define optflags_lto %nil
%endif

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
#for test-only:
BuildRequires: pkgconfig(mpfr)
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
%if_with dft
BuildRequires: libgomp-devel
BuildRequires: pkgconfig(fftw3) 
%endif

%if_with tlfloat
BuildRequires: libtlfloat-devel 
%endif

%global gnuabi_arches %ix86 x86_64 aarch64

%if_enabled static
%global inline_enabled 1
%endif

%description
SLEEF stands for SIMD Library for Evaluating Elementary Functions. It
implements vectorized versions of all C99 real floating point math functions.
It can utilize SIMD instructions that are available on modern processors. SLEEF
is designed to efficiently perform computation with SIMD instructions by
reducing the use of conditional branches and scatter/gather memory access.

The library contains implementations of all C99 real FP math functions in
double precision and single precision. Different accuracy of the results can be
chosen for a subset of the elementary functions; for this subset there are
versions with up to 1 ULP error (which is the maximum error, not the average)
and even faster versions with a few ULPs of error. For non-finite inputs and
outputs, the functions return correct results as specified in the C99 standard.

%package -n lib%name%abiversion
Summary: %summary
Group: System/Libraries

%description -n lib%name%abiversion
SLEEF stands for SIMD Library for Evaluating Elementary Functions. It
implements vectorized versions of all C99 real floating point math functions.
It can utilize SIMD instructions that are available on modern processors. SLEEF
is designed to efficiently perform computation with SIMD instructions by
reducing the use of conditional branches and scatter/gather memory access.

The library contains implementations of all C99 real FP math functions in
double precision and single precision. Different accuracy of the results can be
chosen for a subset of the elementary functions; for this subset there are
versions with up to 1 ULP error (which is the maximum error, not the average)
and even faster versions with a few ULPs of error. For non-finite inputs and
outputs, the functions return correct results as specified in the C99 standard.

%if_with devel
%package -n lib%name-devel
Summary: Development files for sleef
Group: Development/C
Requires: lib%name%abiversion = %EVR 

%description -n lib%name-devel
The sleef-devel package contains libraries and header files for
developing applications that use sleef.
%endif

%if 0%{?inline_enabled}
%package -n lib%name-static
Summary:        Inline headers and static library for sleef
Group: 		Development/C
Requires:       lib%name-devel = %EVR 
 
%description -n lib%name-static
The sleef-static package contains libraries and header files for
developing applications that use sleef.
%endif

%if_with doc
%package -n lib%name-doc
Summary: Documentation for sleef
Group: Documentation
BuildArch: noarch

%description -n lib%name-doc
The sleef-doc package contains detailed API documentation for developing 
applicatons that use sleef
%endif

%ifarch %gnuabi_arches
%package -n lib%name-gnuabi
Summary:        GNUABI version of sleef
Group: 		System/Libraries
 
%global gnuabi_enabled 1
 
%description -n lib%name-gnuabi
The GNUABI version of the library (libsleefgnuabi.so) is built for x86 and
aarch64 architectures. This library provides an API compatible with libmvec in
glibc, and the API conforms to the x86 vector ABI, AArch64 vector ABI and Power
Vector ABI.

%package -n lib%name-gnuabi-devel
Summary:        Development files for GNUABI version of sleef
Requires:       lib%name-gnuabi = %EVR
Group: 		Development/C

%description -n lib%name-gnuabi-devel
The sleef-gnuabi-devel package contains libraries for developing applications
that use the GNUABI version of sleef. Note that this package does not contain
any header files.
%endif

%if_with dft
%package -n lib%name-dft
Summary:        Discrete Fourier Transform (DFT) library
Requires:       lib%name%abiversion = %EVR 
Group: 		System/Libraries

%description -n lib%name-dft
SLEEF includes subroutines for discrete Fourier transform(DFT). These
subroutines are fully vectorized, heavily unrolled, and parallelized in such a
way that modern SIMD instructions and multiple cores can be utilized for
efficient computation. It has an API similar to that of FFTW for easy
migration. The subroutines can utilize long vectors up to 2048 bits.

%package -n lib%name-dft-devel
Summary:        Development files for sleef-dft
Requires:       lib%name-dft = %EVR 
Group: 		Development/C

%description -n lib%name-dft-devel
The sleef-dft-devel package contains libraries and header files for
developing applications that use sleef-dft.
%endif

%if_with quad
%package -n lib%name-quad
Summary:        Vectorized quad-precision math library
Group: 		System/Libraries

%description -n lib%name-quad
An experimental quad-precision library

%package -n lib%name-quad-devel
Summary:        Development files for sleef-quad
Requires:       lib%name-quad = %EVR 
Group: 		Development/C 

%description -n lib%name-quad-devel
The sleef-quad-devel package contains libraries and header files for
developing applications that use sleef-quad.
%endif

%prep
%setup -n %name-%version

%build
%cmake \
    -GNinja \
    %{?_with_dft:-DSLEEF_BUILD_DFT:BOOL=ON -DSLEEF_ENFORCE_DFT:BOOL=ON} \
    %{!?_with_dft:-DSLEEF_BUILD_DFT:BOOL=OFF -DSLEEF_ENFORCE_DFT:BOOL=OFF} \
%ifarch x86_64
    -DSLEEFDFT_ENABLE_STREAM:BOOL=TRUE \
%else
    -DSLEEFDFT_ENABLE_STREAM:BOOL=FALSE \
%endif
    -DSLEEF_BUILD_GNUABI_LIBS:BOOL=%{?gnuabi_enabled:TRUE}%{?!gnuabi_enabled:FALSE} \
    -DSLEEF_BUILD_INLINE_HEADERS:BOOL=%{?inline_enabled:TRUE}%{?!inline_enabled:FALSE} \
    -DSLEEF_BUILD_QUAD:BOOL=%{?_with_quad:TRUE}%{!?_with_quad:FALSE} \
    -DSLEEF_BUILD_SHARED_LIBS:BOOL=TRUE \
    -DSLEEF_ENFORCE_TESTER3:BOOL=TRUE \
    -DSLEEF_ENFORCE_TESTER4:BOOL=%{?_with_tlfloat:TRUE}%{!?_with_tlfloat:FALSE} \
    -DSLEEF_ENABLE_TLFLOAT:BOOL=%{?_with_tlfloat:TRUE}%{!?_with_tlfloat:FALSE} 

%cmake_build

%install
%cmake_install

%files -n lib%name%abiversion
%doc LICENSE.txt
%_libdir/lib%name.so.*

%if_with devel
%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so
%_pkgconfigdir/sleef.pc
%_cmakedir/sleef/
%endif

%if_with doc
%files -n lib%name-doc
%doc LICENSE.txt CHANGELOG.md README.adoc
%doc docs/
%endif

%ifarch %gnuabi_arches
%files -n lib%name-gnuabi
%{_libdir}/lib%{name}gnuabi.so.*
 
 
%files -n lib%name-gnuabi-devel
%{_libdir}/lib%{name}gnuabi.so
%endif
 
 
%if_with dft
%files -n lib%name-dft
%{_libdir}/lib%{name}dft.so.*
 
 
%files -n lib%name-dft-devel
%{_includedir}/%{name}dft.h
%{_libdir}/lib%{name}dft.so
%endif
 
 
%if_with quad
%files -n lib%name-quad
%{_libdir}/lib%{name}quad.so.*
 
 
%files -n lib%name-quad-devel
%{_includedir}/%{name}quad.h
%{_libdir}/lib%{name}quad.so
%endif

%changelog
* Thu Aug 28 2025 Nikita Shmatko <nash@altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus.
