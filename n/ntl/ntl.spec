%global multilib_arches %ix86 x86_64 ppc ppc64 ppc64le s390 s390x sparcv9 sparc64
%global soname 44

Name: ntl
Version: 11.5.1
Release: alt1.2
Summary: High-performance algorithms for vectors, matrices, and polynomials
License: LGPL-2.0+
Group: Sciences/Mathematics
Url: https://libntl.org/

Source: https://libntl.org/%name-%version.tar.gz
Source1: multilib_template.h
# Detect CPU at load time, optionally use PCLMUL, AVX, FMA, and AVX2 features.
# This patch was sent upstream, but upstream prefers that the entire library
# be built for a specific CPU, which we cannot do in Fedora.
Patch: %name-loadtime-cpu.patch

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
%patch -p0
cp /usr/share/gnu-config/config.{guess,sub} src/libtool-origin/

%build
# TODO: Once we can assume z15, add TUNE=linux-s390x to the flags for s390x
pushd src
./configure \
  CXX="${CXX-g++}" \
  CXXFLAGS="%optflags -fPIC" \
  LDFLAGS="$RPM_LD_FLAGS" \
  DEF_PREFIX=%prefix \
  DOCDIR=%_docdir \
  INCLUDEDIR=%_includedir \
  LIBDIR=%_libdir \
  LDLIBS="-lpthread -lm" \
  NATIVE=off \
  NTL_GF2X_LIB=on \
  NTL_STD_CXX14=on \
%ifarch x86_64
  NTL_LOADTIME_CPU=on \
  TUNE=x86 \
%else
  TUNE=generic \
%endif
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
  LIBDIR=%buildroot%_libdir

# Fix permissions
chmod 0755 %buildroot%_libdir/libntl.so.*

# Unpackaged files
rm -rfv %buildroot%_docdir/NTL
rm -fv  %buildroot%_libdir/libntl.la
rm -fv  %buildroot%_libdir/libntl.a

#%ifarch %multilib_arches
## hack to allow parallel installation of multilib factory-devel
#for header in NTL/config NTL/gmp_aux NTL/mach_desc  ; do
#mv  %buildroot%_includedir/${header}.h \
#%buildroot%_includedir/${header}-%{__isa_bits}.h
#install -p -m644 %SOURCE1 %buildroot%_includedir/${header}.h
#sed \
#  -e "s|@@INCLUDE@@|${header}|" \
#  -e "s|@@INCLUDE_MACRO@@|$(echo ${header} | tr '/.' '_')|" \
#%buildroot%_includedir/${header}.h
#done
#%endif

%files -n lib%name%soname
%doc README
%doc doc/copying.txt
%_libdir/libntl.so.%{soname}*

%files -n lib%name-devel
%doc doc/*
%_includedir/NTL/
%_libdir/libntl.so

%changelog
* Fri Nov 03 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 11.5.1-alt1.2
- NMU: fixed FTBFS on LoongArch (use fresh config.{sub,guess}).

* Tue Jan 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 11.5.1-alt1.1
- Fixed build for Elbrus.

* Mon Oct 18 2021 Leontiy Volodin <lvol@altlinux.org> 11.5.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
