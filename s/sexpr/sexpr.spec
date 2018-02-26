Name: sexpr
Version: 1.2.1
Release: alt1
Summary: Small, fast s-expression library (sexpr)
License: LGPLv2.1+
Group: Development/Tools
Url: http://sexpr.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: doxygen gcc-c++

%description
This library is intended to provide a minimal C/C++ API to efficiently
create, manipulate, and parse LISP-style symbolic expressions.

%package -n lib%name
Summary: Small, fast s-expression library
Group: System/Libraries

%description -n lib%name
This library is intended to provide a minimal C/C++ API to efficiently
create, manipulate, and parse LISP-style symbolic expressions.

%package -n lib%name-devel
Summary: Development files of small, fast s-expression library (sexpr)
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This library is intended to provide a minimal C/C++ API to efficiently
create, manipulate, and parse LISP-style symbolic expressions.

This package contains development files of sexpr.

%package -n lib%name-devel-docs
Summary: Development documentation, examples and tests for sexpr
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
This library is intended to provide a minimal C/C++ API to efficiently
create, manipulate, and parse LISP-style symbolic expressions.

This package contains development documentation, examples and tests for
sexpr.

%prep
%setup

%build
%autoreconf
%configure
%make_build

autoconf
doxygen

%install
%makeinstall_std LIBDIR=%_libdir

rm -f examples/Makefile.in tests/Makefile.in

%files -n lib%name
%doc LICENSE* README.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*

%files -n lib%name-devel-docs
%doc doxygen/html examples tests

%changelog
* Fri Mar 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

