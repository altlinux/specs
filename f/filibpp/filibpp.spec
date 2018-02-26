Name: filibpp
Version: 3.0.2
Release: alt1
Summary: filib++ is an extension of the interval library filib
License: LGPL v2 or later
Group: Sciences/Mathematics
Url: http://www2.math.uni-wuppertal.de/~xsc/software/filib.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www2.math.uni-wuppertal.de/~xsc/software/filib++/filib++-dist2010.tar.gz

BuildPreReq: gcc-c++ boost-devel
BuildPreReq: texlive-latex-recommended psutils ghostscript-utils

%description
filib++ is an extension of the interval library filib. The most
important aim of the latter was the fast computation of guaranteed
bounds for interval versions of a comprehensive set of elementary
function. filib++ extends this library in two aspects. First, it adds a
second mode, the "extended" mode, that extends the exception-free
computation mode using special values to represent infinities and
NotaNumber known from the IEEE floating-point standard 754 to intervals.
In this mode so-called containment sets are computed to enclose the
topological closure of a range of a function defined over an interval.
Second, state of the art design uses templates and traits classes in
order to get an efficient, easily extendable and portable library, fully
according to the C++ standard.

%package -n lib%name
Summary: Shared libraries of filib++, an extension of the interval library filib
Group: System/Libraries

%description -n lib%name
filib++ is an extension of the interval library filib. The most
important aim of the latter was the fast computation of guaranteed
bounds for interval versions of a comprehensive set of elementary
function. filib++ extends this library in two aspects. First, it adds a
second mode, the "extended" mode, that extends the exception-free
computation mode using special values to represent infinities and
NotaNumber known from the IEEE floating-point standard 754 to intervals.
In this mode so-called containment sets are computed to enclose the
topological closure of a range of a function defined over an interval.
Second, state of the art design uses templates and traits classes in
order to get an efficient, easily extendable and portable library, fully
according to the C++ standard.

This package contains shared libraries of filib++.

%package -n lib%name-devel
Summary: Development files of filib++, an extension of the interval library filib
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
filib++ is an extension of the interval library filib. The most
important aim of the latter was the fast computation of guaranteed
bounds for interval versions of a comprehensive set of elementary
function. filib++ extends this library in two aspects. First, it adds a
second mode, the "extended" mode, that extends the exception-free
computation mode using special values to represent infinities and
NotaNumber known from the IEEE floating-point standard 754 to intervals.
In this mode so-called containment sets are computed to enclose the
topological closure of a range of a function defined over an interval.
Second, state of the art design uses templates and traits classes in
order to get an efficient, easily extendable and portable library, fully
according to the C++ standard.

This package contains development files of filib++.

%package -n lib%name-devel-doc
Summary: Documentation for filib++, an extension of the interval library filib
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
filib++ is an extension of the interval library filib. The most
important aim of the latter was the fast computation of guaranteed
bounds for interval versions of a comprehensive set of elementary
function. filib++ extends this library in two aspects. First, it adds a
second mode, the "extended" mode, that extends the exception-free
computation mode using special values to represent infinities and
NotaNumber known from the IEEE floating-point standard 754 to intervals.
In this mode so-called containment sets are computed to enclose the
topological closure of a range of a function defined over an interval.
Second, state of the art design uses templates and traits classes in
order to get an efficient, easily extendable and portable library, fully
according to the C++ standard.

This package contains development documentation for filib++.

%package examples
Summary: Examples for filib++, an extension of the interval library filib
Group: Sciences/Mathematics
Requires: lib%name = %version-%release
Conflicts: fi_lib-examples

%description examples
filib++ is an extension of the interval library filib. The most
important aim of the latter was the fast computation of guaranteed
bounds for interval versions of a comprehensive set of elementary
function. filib++ extends this library in two aspects. First, it adds a
second mode, the "extended" mode, that extends the exception-free
computation mode using special values to represent infinities and
NotaNumber known from the IEEE floating-point standard 754 to intervals.
In this mode so-called containment sets are computed to enclose the
topological closure of a range of a function defined over an interval.
Second, state of the art design uses templates and traits classes in
order to get an efficient, easily extendable and portable library, fully
according to the C++ standard.

This package contains examples for filib++.

%prep
%setup
touch NEWS

%build
%autoreconf
%configure \
	--enable-shared \
	--enable-static=no
%make_build

%make -C doc/tex manual.pdf

%install
%makeinstall_std

%files -n lib%name
%doc AUTHORS COPYING ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/tex/*.pdf

%files examples
%doc examples/*.c* examples/*.h examples/Makefile
%_bindir/*

%changelog
* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt2
- Rebuilt for debuginfo

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus

