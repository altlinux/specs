%define        _unpackaged_files_terminate_build 1

Name:          libcudd
Version:       3.0.0
Release:       alt1
Summary:       CUDD: Colorado University Decision Diagram Package
License:       BSD
Group:         Sciences/Mathematics
Url:           https://github.com/ivmai/cudd
Vcs:           https://github.com/ivmai/cudd.git
Source:        %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel

%description
The CUDD package provides functions to manipulate Binary Decision
Diagrams (BDDs), Algebraic Decision Diagrams (ADDs), and Zero-suppressed
Binary Decision Diagrams (ZDDs). BDDs are used to represent switching
functions; ADDs are used to represent function from {0,1}^n to an
arbitrary set. ZDDs represent switching functions like BDDs; however,
they are much more efficient than BDDs when the functions to be
represented are characteristic functions of cube sets, or in general,
when the ON-set of the function to be represented is very sparse. They
are inferior to BDDs in other cases.

The package provides a large set of operations on BDDs, ADDs, and ZDDs,
functions to convert BDDs into ADDs or ZDDs and vice versa, and a large
assortment of variable reordering methods.

This package contains shared %name.

%package       devel
Summary:       Development files of %name
Group:         Development/C

%description   devel
The CUDD package provides functions to manipulate Binary Decision
Diagrams (BDDs), Algebraic Decision Diagrams (ADDs), and Zero-suppressed
Binary Decision Diagrams (ZDDs). BDDs are used to represent switching
functions; ADDs are used to represent function from {0,1}^n to an
arbitrary set. ZDDs represent switching functions like BDDs; however,
they are much more efficient than BDDs when the functions to be
represented are characteristic functions of cube sets, or in general,
when the ON-set of the function to be represented is very sparse. They
are inferior to BDDs in other cases.

The package provides a large set of operations on BDDs, ADDs, and ZDDs,
functions to convert BDDs into ADDs or ZDDs and vice versa, and a large
assortment of variable reordering methods.

This package contains development files of %name.


%prep
%setup

%build
%autoreconf
%configure \
   --enable-shared \
   --disable-static \
   --enable-dddmp \
   --disable-silent-rules \
   --with-system-qsort

%make_build

%install
%makeinstall_std

%files
%doc dddmp/README.dddmp RELEASE.NOTES* README*
%_libdir/*.so.*

%files         devel
%doc dddmp/README.dddmp RELEASE.NOTES* README*
%_includedir/*
%_libdir/*.so


%changelog
* Sun Feb 16 2025 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.5.1 -> 3.0.0
- * rename to libcudd

* Sun Aug 12 2018 Vladislav Zavjalov <slazav@altlinux.org> 2.5.1-alt3
- fix aarch64 build (do not use -malign-double compiler flag)

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2
- Added all symbols from libutil.a into libmtr.so

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus

