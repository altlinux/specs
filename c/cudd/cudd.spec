Name: cudd
Version: 2.5.1
Release: alt1
Summary: CUDD: Colorado University Decision Diagram Package
License: BSD
Group: Sciences/Mathematics
Url: http://vlsi.colorado.edu/~fabio/CUDD/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# ftp://vlsi.colorado.edu/pub/cudd-2.5.1.tar.gz
Source: %name-%version.tar

Requires: lib%name = %EVR

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++

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

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
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

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
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

%package -n lib%name-devel-docs
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
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

This package contains development documentation for %name.

%prep
%setup

%ifarch x86_64
sed -i 's|#@x86_64@||' Makefile
%else
sed -i 's|#@i586@||' Makefile
%endif

%build
%add_optflags %optflags_shared
%make_build_ext build
%make_build_ext nanotrav
%make_build_ext -C mnemosyne

%install
install -d %buildroot{%_bindir,%_includedir/%name,%_libdir,%_man1dir}
install -m755 nanotrav/nanotrav %buildroot%_bindir/
install -m755 nanotrav/nanotrav.1 %buildroot%_man1dir/
install -m644 include/* %buildroot%_includedir/%name/
cp -P */*.so* %buildroot%_libdir/

ln -s %name/doc %name.doc
ln -s dddmp/RELEASE_NOTES RELEASE_NOTES.dddmp
ln -s dddmp/doc dddmp.doc
ln -s mnemosyne/README README.mnemosyne
ln -s mtr/doc mtr.doc
ln -s nanotrav/README nanotrav.README
ln -s nanotrav/doc nanotrav.html
ln -s st/doc st.doc

%files
%doc README RELEASE.NOTES nanotrav.README nanotrav.html
%_bindir/*
%_man1dir/*

%files -n lib%name
%doc dddmp/README.dddmp RELEASE_NOTES.* README.*
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-docs
%doc *.doc

%changelog
* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus

