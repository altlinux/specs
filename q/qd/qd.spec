# TODO: fix for ALT:
# Fortran module directory
%{!?_fmoddir: %global _fmoddir %_libdir/gfortran/modules}

%def_without check
%def_disable fortran

Name: qd
Version: 2.3.23
Release: alt1

Summary: C++/Fortran-90 double-double and quad-double package

License: BSD
Group: Sciences/Mathematics
Url: https://www.davidhbailey.com/dhbsoftware/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://www.davidhbailey.com/dhbsoftware/qd-%version.tar.gz
Source: %name-%version.tar

Patch1: qd-lto.patch

BuildRequires: gcc-c++
%if_enabled fortran
BuildRequires: gcc-fortran libgfortran-devel
%add_verify_elf_skiplist %_libdir/libqd_f_main.so.0.0.0
%endif

Requires: lib%name = %EVR

%description
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

In addition to the basic arithmetic operations (add, subtract,
multiply, divide, square root), common transcendental functions such
as the exponential, logarithm, trigonometric and hyperbolic functions
are also included.

%package -n lib%name
Summary: Shared libraries  of QD
Group: System/Libraries

%description -n lib%name
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains shared libraries of QD.

%package -n lib%name-devel
Summary: Development files of QD
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains development files of QD.

%package -n lib%name-devel-doc
Summary: Documentation for QD
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains documentation for QD.

%prep
%setup
%patch1 -p1

%build
%ifarch s390x aarch64 ppc64le
%global optflags %optflags -ffp-contract=off
%endif

%add_optflags %optflags_shared

export CC=gcc
export CXX=g++
export FC=gfortran
export FCFLAGS="%optflags"

%autoreconf
%configure \
	--enable-shared \
	--disable-static \
	%{subst_enable fortran} \
	--enable-ieee-add \
	--enable-debug

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="gfortran"|CC="gfortran -Wl,--as-needed"|' \
    -e 's|CC=.g[c+][c+]|& -Wl,--as-needed|' \
    -i libtool

# Supply missing fortran tags
%__subst '/F77/s/\$(AM_V_lt)/& --tag=FC/' fortran/Makefile

#make -C fortran f_main.o
%make_build
%make cpp-demo
%if_enabled fortran
%make cpp-demo fortran-demo
%endif

%install
%makeinstall_std

# Fix location of documentation
mv %buildroot%_docdir/qd/* .
rm -rf %buildroot%_datadir

%if_enabled fortran
# Move Fortran modules to %_fmoddir
mkdir -p %buildroot%_fmoddir/%name
mv %buildroot%_includedir/qd/*.mod %buildroot%_fmoddir/%name
%endif

# Remove la file
rm %buildroot%_libdir/*.la

# Fix pkgconfig file on 64-bit systems
if [ "%_lib" = "lib64" ]; then
  sed -i 's/^libdir=.*/&64/' %buildroot%_pkgconfigdir/qd.pc
fi

%check
LD_LIBRARY_PATH=$PWD/src/.libs:$PWD/fortran/.libs make check

%files
%doc AUTHORS COPYING NEWS README* TODO
%_bindir/*
%exclude %_bindir/qd-config
#_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/qd-config
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/qd.pc

%files -n lib%name-devel-doc
%doc docs/qd.pdf

%changelog
* Sat Aug 28 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.23-alt1
- new version 2.3.23 (with rpmrb script) (ALT bug 40821)
- package qd.pc (ALT bug 40821)
- add fixes from Fedora
- disable build with fortran libs

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.14-alt2
- cleanup spec and repo, drop obsoletes itself
- temp. disable check ([ppc64le] FAIL: qd_test)

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.14-alt1
- Version 2.3.14

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.13-alt1
- Version 2.3.13

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.12-alt2
- Fixed build with new automake

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.12-alt1
- Version 2.3.12
- Disabled devel-static package

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt4
- Added -g for gfortran flags

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt3
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt2
- Rebuilt for soname set-versions

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt1
- Version 2.3.11

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt3
- Added shared libraries

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt2
- Rebuild with PIC

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt1
- Version 2.3.8

* Thu May 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.7-alt1
- Initial build for Sisyphus

