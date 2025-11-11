%global soname 45

Name: ntl
Version: 11.6.0
Release: alt1
Summary: High-performance algorithms for vectors, matrices, and polynomials
License: LGPL-2.1-or-later
Group: Sciences/Mathematics
Url: https://libntl.org/
VCS: https://github.com/libntl/ntl

# Source-url: https://libntl.org/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libgf2x-devel
BuildRequires: libgmp-devel
BuildRequires: perl-base
BuildRequires: gnu-config

%description
NTL is a high-performance, portable C++ library providing data structures
and algorithms for arbitrary length integers; for vectors, matrices, and
polynomials over the integers and over finite fields; and for arbitrary
precision floating point arithmetic.

NTL provides high quality implementations of state-of-the-art algorithms for:
* arbitrary length integer arithmetic and arbitrary precision floating point
  arithmetic;
* polynomial arithmetic over the integers and finite fields including basic
  arithmetic, polynomial factorization, irreducibility testing, computation
  of minimal polynomials, traces, norms, and more;
* lattice basis reduction, including very robust and fast implementations of
  Schnorr-Euchner, block Korkin-Zolotarev reduction, and the new
  Schnorr-Horner pruning heuristic for block Korkin-Zolotarev;
* basic linear algebra over the integers, finite fields, and arbitrary
  precision floating point numbers.

%package -n lib%name%soname
Summary: %summary
Group: Sciences/Mathematics

%description -n lib%name%soname
NTL is a high-performance, portable C++ library providing data structures
and algorithms for arbitrary length integers; for vectors, matrices, and
polynomials over the integers and over finite fields; and for arbitrary
precision floating point arithmetic.

NTL provides high quality implementations of state-of-the-art algorithms for:
* arbitrary length integer arithmetic and arbitrary precision floating point
  arithmetic;
* polynomial arithmetic over the integers and finite fields including basic
  arithmetic, polynomial factorization, irreducibility testing, computation
  of minimal polynomials, traces, norms, and more;
* lattice basis reduction, including very robust and fast implementations of
  Schnorr-Euchner, block Korkin-Zolotarev reduction, and the new
  Schnorr-Horner pruning heuristic for block Korkin-Zolotarev;
* basic linear algebra over the integers, finite fields, and arbitrary
  precision floating point numbers.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other

%description -n lib%name-devel
%summary.

%prep
%setup
%patch -p1
cp /usr/share/gnu-config/config.{guess,sub} src/libtool-origin/

%build
pushd src
./configure \
  CXX="${CXX-g++}" \
  CXXFLAGS="%optflags -fPIC" \
  LDFLAGS="$RPM_LD_FLAGS" \
  DEF_PREFIX=%prefix \
  DOCDIR=%_docdir \
  INCLUDEDIR=%_includedir \
  LIBDIR=%_libdir \
  PKGDIR=%_pkgconfigdir \
  LDLIBS="-lpthread -lm" \
  NATIVE=off \
  NTL_GF2X_LIB=on \
  NTL_STD_CXX14=on \
%ifarch %e2k
  NTL_SAFE_VECTORS=off \
%endif
  SHARED=on
popd

# not smp-safe
make -C src V=1

%check
make -C src check

%install
make -C src install \
  PREFIX=%buildroot%prefix \
  DOCDIR=%buildroot%_docdir \
  INCLUDEDIR=%buildroot%_includedir \
  LIBDIR=%buildroot%_libdir \
  PKGDIR=%buildroot%_pkgconfigdir

# Fix permissions
chmod 0755 %buildroot%_libdir/libntl.so.*

# Unpackaged files
rm -rfv %buildroot%_docdir/NTL
rm -fv  %buildroot%_libdir/libntl.la
rm -fv  %buildroot%_libdir/libntl.a

%files -n lib%name%soname
%doc README
%doc doc/copying.txt
%_libdir/libntl.so.%{soname}*

%files -n lib%name-devel
%doc doc/*
%_includedir/NTL/
%_libdir/libntl.so
%_pkgconfigdir/ntl.pc

%changelog
* Tue Nov 11 2025 Leontiy Volodin <lvol@altlinux.org> 11.6.0-alt1
- New version 11.6.0.
- Added VCS tag.

* Fri Nov 03 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 11.5.1-alt1.2
- NMU: fixed FTBFS on LoongArch (use fresh config.{sub,guess}).

* Tue Jan 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 11.5.1-alt1.1
- Fixed build for Elbrus.

* Mon Oct 18 2021 Leontiy Volodin <lvol@altlinux.org> 11.5.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
