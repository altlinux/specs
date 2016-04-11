%ifarch x86_64
%define abi 64
%define arch x86_64
%else
%define abi 32
%define arch i586
%endif
%define target %arch-alt-linux
%define make_include configs/make.include.%target

Name: yices
Version: 2.3.0
Release: alt2
Summary: The Yices SMT Solver
License: Noncommercial use only
Group: Sciences/Mathematics
Url: http://yices.csl.sri.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libgmp-devel gperf flex

%description
Yices 2 is an SMT solver that decides the satisfiability of formulas
containing uninterpreted function symbols with equality, linear real and
integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions
2.0 and 1.2 are supported). Alternatively, you can write specifications
using Yices 2's own specification language, which includes tuples and
scalar types. You can also use Yices 2 as a library in your software.

%package docs
Summary: Documentation and examples for %name
Group: Documentation
BuildArch: noarch

%description docs
Yices 2 is an SMT solver that decides the satisfiability of formulas
containing uninterpreted function symbols with equality, linear real and
integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions
2.0 and 1.2 are supported). Alternatively, you can write specifications
using Yices 2's own specification language, which includes tuples and
scalar types. You can also use Yices 2 as a library in your software.

This package contains documentation and examples for %name.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
Yices 2 is an SMT solver that decides the satisfiability of formulas
containing uninterpreted function symbols with equality, linear real and
integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions
2.0 and 1.2 are supported). Alternatively, you can write specifications
using Yices 2's own specification language, which includes tuples and
scalar types. You can also use Yices 2 as a library in your software.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Yices 2 is an SMT solver that decides the satisfiability of formulas
containing uninterpreted function symbols with equality, linear real and
integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions
2.0 and 1.2 are supported). Alternatively, you can write specifications
using Yices 2's own specification language, which includes tuples and
scalar types. You can also use Yices 2 as a library in your software.

This package contains development files of %name.

%prep
%setup

%build
%add_optflags %optflags_shared -m%abi
%autoreconf
%configure \
	--enable-shared \
	--disable-static \
	--with-pic-gmp=%_libdir/libgmp.so

sed -i 's|^STRIP=.*|STRIP=echo|' %make_include
sed -i 's|^YACC=.*|YACC=yacc|' %make_include
sed -i 's|^LEX=.*|LEX=flex|' %make_include
# It fails during parallel builds randomly (sometimes); therefore:
NPROCS=1
%make_build YICES_MAKE_INCLUDE=%make_include ARCH=%target lib bin

%install
sed -i 's|%prefix|%buildroot%prefix|' %make_include
%make dist YICES_MAKE_INCLUDE=%make_include ARCH=%target
%makeinstall_std YICES_MAKE_INCLUDE=%make_include ARCH=%target

%check
%make YICES_MAKE_INCLUDE=%make_include ARCH=%target check
%make YICES_MAKE_INCLUDE=%make_include ARCH=%target test

%files
%doc LICENSE NOTICES README doc/NOTES doc/YICES-LANGUAGE
%_bindir/*

%files docs
%doc doc/*.pdf examples

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt2
- It fails during parallel builds randomly (sometimes); therefore: NPROCS=1

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus

