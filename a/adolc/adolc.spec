%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define soname 2

Name: adolc
Summary: A Package for Automatic Differentiation of Algorithms Written in C/C++
Version: 2.7.2
Release: alt0.2
Group: Sciences/Mathematics
License: EPL-1.0 or GPL-2.0+
Url: https://github.com/coin-or/ADOL-C

# https://github.com/coin-or/ADOL-C/archive/refs/tags/releases/%version.tar.gz
Source: %name-%version.tar
Source1: http://ftp.mcs.anl.gov/pub/ADOLC/ADOLC_current/adolc-1.10.ps.gz
Source2: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/col_jon.ps.gz
Source3: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/hutschen.ps.gz
Source4: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/jaco_Ne_Ra.ps.gz
Source5: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/juedes.ps.gz
Source6: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/newton.ps.gz
Source7: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/ode_ad_rp.ps.gz
Source8: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/par_rev.ps.gz
Source9: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/s_campb.ps.gz
Source10: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/sf_col_ver.ps.gz
Source11: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/tensors.ps.gz
Source12: http://ftp.mcs.anl.gov/pub/ADOLC/PAPERS/tr_col_ver.ps.gz
Source13: README

Patch: adolc-2.7.2-alt-loongarch64-boost.patch

Requires: lib%name = %EVR
Requires: %name-examples = %EVR

BuildPreReq: gcc-c++ libcolpack-devel chrpath boost-devel libgomp-devel

%description
The package ADOL-C facilitates the evaluation of first and higher derivatives of
vector functions that are defined by computer programs written in C or C++. The
resulting derivative evaluation routines may be called from C/C++, Fortran, or
any other language that can be linked with C.

The numerical values of derivative vectors are obtained free of truncation
errors at a small multiple of the run time and randomly accessed memory of the
given function evaluation program.

%package -n lib%name%{soname}
Summary: Shared libraries of ADOL-C
Group: System/Libraries
Provides: lib%{name} = %EVR

%description -n lib%name%{soname}
The package ADOL-C facilitates the evaluation of first and higher derivatives of
vector functions that are defined by computer programs written in C or C++. The
resulting derivative evaluation routines may be called from C/C++, Fortran, or
any other language that can be linked with C.

The numerical values of derivative vectors are obtained free of truncation
errors at a small multiple of the run time and randomly accessed memory of the
given function evaluation program.

This package contains shared libraries of ADOL-C.

%package -n lib%name-devel
Summary: Development files of ADOL-C
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
The package ADOL-C facilitates the evaluation of first and higher derivatives of
vector functions that are defined by computer programs written in C or C++. The
resulting derivative evaluation routines may be called from C/C++, Fortran, or
any other language that can be linked with C.

The numerical values of derivative vectors are obtained free of truncation
errors at a small multiple of the run time and randomly accessed memory of the
given function evaluation program.

This package contains development files of ADOL-C.

%package -n lib%name-devel-doc
Summary: Documentation for ADOL-C
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The package ADOL-C facilitates the evaluation of first and higher derivatives of
vector functions that are defined by computer programs written in C or C++. The
resulting derivative evaluation routines may be called from C/C++, Fortran, or
any other language that can be linked with C.

The numerical values of derivative vectors are obtained free of truncation
errors at a small multiple of the run time and randomly accessed memory of the
given function evaluation program.

This package contains development documentation for ADOL-C.

%package examples
Summary: Shared libraries of ADOL-C
Group: Sciences/Mathematics
Requires: lib%name = %EVR

%description examples
The package ADOL-C facilitates the evaluation of first and higher derivatives of
vector functions that are defined by computer programs written in C or C++. The
resulting derivative evaluation routines may be called from C/C++, Fortran, or
any other language that can be linked with C.

The numerical values of derivative vectors are obtained free of truncation
errors at a small multiple of the run time and randomly accessed memory of the
given function evaluation program.

This package contains examples for ADOL-C.

%prep
%setup
%patch -p1

%build
%autoreconf
FLAGS="-g -pipe -O3 -Wall %optflags_shared -pthread -I%_includedir/colpack"
%configure \
%ifarch x86_64
	--enable-ulong \
%endif
	--enable-shave=no \
	--enable-tserrno \
	--enable-atrig-erf \
	--enable-sparse \
	--enable-docexa \
	--enable-addexa \
	--with-openmp-flag="-fopenmp" \
	--with-cflags="$FLAGS" \
	--with-cxxflags="$FLAGS" \
	--with-colpack=%prefix
sed -ri \
	's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' \
	libtool
%make_build

%install
%makeinstall_std

install -d %buildroot%_docdir/lib%name-devel/papers
install -d %buildroot%_libdir/%name-examples

install -p -m644 ADOL-C/doc/*.pdf %SOURCE1 \
	%buildroot%_docdir/lib%name-devel
install -p -m644 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 \
	%SOURCE8 %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 \
	%buildroot%_docdir/lib%name-devel/papers

rm -f $(find ADOL-C/examples -name '*.o')
cp -fR ADOL-C/examples/* %buildroot%_libdir/%name-examples/

for i in %buildroot%_libdir/%name-examples/additional_examples/*/.libs/*
do
	chrpath -d $i ||:
done
chrpath -d %buildroot%_libdir/*.so

%files
%doc AUTHORS BUGS ChangeLog LICENSE NEWS README TODO

%files -n lib%name%{soname}
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%files examples
%_libdir/%name-examples

%changelog
* Tue Aug 20 2024 Ivan A. Melnikov <iv@altlinux.org> 2.7.2-alt0.2
- NMU: Fix FTBFS on loongarch64 (by k0tran@).

* Wed Aug 14 2024 L.A. Kostis <lakostis@altlinux.ru> 2.7.2-alt0.1
- Version 2.7.2.
- Enabled OpenMP support via GOMP.

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20140526
- Version 2.5.0

* Fri Nov 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.svn20131009
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.svn20130527
- New snapshot

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.svn20130129
- Version 2.4.0

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt3.svn20111024
- Avoid using of chrpath

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt2.svn20111024
- Fixed RPATH
- Disabled devel-static package

* Sun Dec 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.svn20111024
- New snapshot

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.svn20110812
- Version 2.2.1

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20110412
- Version 2.2.0

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.11-alt1.svn20101110.2
- Added -g into compiler flags

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.11-alt1.svn20101110.1
- Rebuilt for debuginfo

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.11-alt1.svn20101110
- Version 2.1.11

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2
- Rebuilt for soname set-versions

* Fri Jun 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Initial build for Sisyphus

