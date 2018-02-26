%define triver 10

%define somver 0
%define sover %somver.0.0
Name: CoinCppAD
Version: 20120130
Release: alt1.svn20120211
Summary: A Package for Differentiation of C++ Algorithms
License: CPL v1.0 or GPL v2.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/CppAD.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/CppAD/trunk
Source: %name-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel boost-devel libadolc-devel
BuildPreReq: libipopt-devel liblapack-devel
BuildPreReq: gcc-fortran libsacado%triver-devel
BuildPreReq: texlive-latex-recommended

%description
Given a C++ algorithm that computes function values, CppAD generates an
algorithm that computes corresponding derivative values.

%package -n lib%name
Summary: Shared libraries of COIN-OR CppAD
Group: System/Libraries

%description -n lib%name
Given a C++ algorithm that computes function values, CppAD generates an
algorithm that computes corresponding derivative values.

This package contains shared libraries of COIN-OR CppAD.

%package -n lib%name-devel
Summary: Development files of COIN-OR CppAD
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Given a C++ algorithm that computes function values, CppAD generates an
algorithm that computes corresponding derivative values.

This package contains development files of COIN-OR CppAD.

%package -n lib%name-devel-static
Summary: Static libraries of COIN-OR CppAD
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Given a C++ algorithm that computes function values, CppAD generates an
algorithm that computes corresponding derivative values.

This package contains static libraries of COIN-OR CppAD.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR CppAD
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Given a C++ algorithm that computes function values, CppAD generates an
algorithm that computes corresponding derivative values.

This package contains development documentation for COIN-OR CppAD.

%prep
%setup

%build
%autoreconf
export ADOLC_DIR=%prefix
export SACADO_DIR=%prefix
export IPOPT_DIR=%prefix
export BOOST_DIR=%prefix
export CXX_FLAGS="%optflags %optflags_shared"
%configure \
	--with-Documentation \
	--with-stdvector
%make_build

./build.sh doxygen

%install
mv doxydoc doc
%makeinstall_std

mkdir %buildroot%_libdir/tmp
pushd %buildroot%_libdir/tmp
for i in libcppad_ipopt; do
	ar x ../$i.a
	g++ -shared -Wl,-soname,$i.so.%somver *.o \
		-o ../$i.so.%sover -lipopt
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir %buildroot%_libdir/tmp

install -d %buildroot%_pkgconfigdir
mv %buildroot%_datadir/pkgconfig/cppad.pc \
	%buildroot%_pkgconfigdir/

%files -n lib%name
%doc AUTHORS COPYING ChangeLog LICENSE NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/cppad-%version

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20120130-alt1.svn20120211
- Version 20120130

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110906-alt1.svn20110907
- Version 20110906

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110419-alt1.svn20110420
- Version 20110419

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100821-alt3.svn20101129.3
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100821-alt3.svn20101129.2
- Rebuilt with Boost 1.46.1

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100821-alt3.svn20101129.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100821-alt3.svn20101129
- New snapshot

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100821-alt2
- Rebuilt for soname set-versions

* Fri Sep 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100821-alt1
- Initial build for Sisyphus

