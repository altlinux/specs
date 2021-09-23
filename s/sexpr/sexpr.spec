%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define sover 1

Name: sexpr
Version: 1.3.1
Release: alt1
Summary: Small, fast s-expression library (sexpr)
License: LGPLv2.1+
Group: Development/Tools
Url: https://github.com/mjsottile/sfsexp
VCS: https://github.com/mjsottile/sfsexp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: doxygen gcc-c++

%description
This library is intended to provide a minimal C/C++ API to efficiently
create, manipulate, and parse LISP-style symbolic expressions.

%package -n lib%name%sover
Summary: Small, fast s-expression library
Group: System/Libraries

%description -n lib%name%sover
This library is intended to provide a minimal C/C++ API to efficiently
create, manipulate, and parse LISP-style symbolic expressions.

%package -n lib%name-devel
Summary: Development files of small, fast s-expression library (sexpr)
Group: Development/C
Requires: lib%name%sover = %EVR

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
%add_optflags %optflags_shared
%autoreconf
%configure
%make_build

doxygen

%install
%makeinstall_std LIBDIR=%_libdir

install -d %buildroot%_man3dir
install -m644 doxygen/man/man3/* %buildroot%_man3dir/

rm -f examples/Makefile.in tests/Makefile.in

# static lib
rm -f %buildroot%_libdir/libsexp.a

%files -n lib%name%sover
%doc COPYING README*
%_libdir/*.so.%sover
%_libdir/*.so.%sover.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*

%files -n lib%name-devel-docs
%doc doxygen/html

%changelog
* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 1.3.1-alt1
- new version
- switched to upstream git

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 1.3-alt2
- fixed build with LTO

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Fri Mar 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

