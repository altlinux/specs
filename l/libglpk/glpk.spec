%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc

%define        nomen glpk
%define        NOMEN GLPK

Name:          lib%nomen
Version:       5.0.1
Release:       alt1
Summary:       GLPK glpsol utility
License:       GPLv3+
Group:	       Sciences/Mathematics
Url:	       https://www.gnu.org/software/glpk/glpk.html
Vcs:           https://github.com/Mizux/GLPK.git

Source:	       http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: /proc
%{?_enable_check:BuildRequires: ctest}
%{?_enable_doc:BuildRequires: texlive-dist}
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(zlib)

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the library needed to run programs dynamically
linked with GLPK.

%package       -n glpsol
Summary:       GLPK shared libraries
Group:	       Sciences/Mathematics
Obsoletes:     %{nomen} < %EVR

%description   -n glpsol
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the utility glpsol.


%package       devel
Summary:       GLPK development files
Group:	       Development/C
Provides:      %nomen-devel = %EVR

%description   devel
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the headers needed to develop applications using
GLPK.


%if_enabled    doc
%package       doc
Group:         Sciences/Mathematics
Summary:       Documentation for %{name}
BuildArch:     noarch

%description   doc
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

Documentation subpackage for %{name}.
%endif


%if_enabled    check
%package       -n %nomen-examples
Summary:       GLPK examples
Group:	       Development/C

%description   -n %nomen-examples
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the exampels needed to test applications using
GLPK.
%endif


%prep
%setup

%build
%cmake \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   %{!?_enable_check:-DBUILD_EXAMPLES=OFF} \
   %nil

%cmake_build

%if_enabled    doc
# Trust Knuth to produce a single-pass compiler for a multiple-pass language.
pushd doc
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex
popd
%endif

%install
%cmake_install
%if_enabled    doc
install -D -m 644 doc/glpk.pdf %buildroot%_docdir/%name/%nomen.pdf
%endif

%check
%ctest


%files
%_libdir/*.so.*

%files         -n glpsol
%_bindir/glpsol

%files         devel
%doc examples doc/*.txt doc/*.pdf AUTHORS ChangeLog NEWS README.md
%doc --no-dereference COPYING
%_includedir/%{nomen}*
%_cmakedir/%{NOMEN}/
%_libdir/*.so

%if_enabled    doc
%files         doc
%doc doc examples
%_docdir/%name/%nomen.pdf
%endif

%if_enabled    check
%files         -n %nomen-examples
%_bindir/*
%endif


%changelog
* Sun Aug 30 2026 Pavel Skrylev <majioa@altlinux.org> 5.0.1-alt1
- ^ 5.0 -> 5.0.1 (with rename package)
- * rebased to new upstream

* Sat Oct 16 2021 Igor Vlasenko <viy@altlinux.org> 5.0-alt1_1
- new version

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.48-alt1
- Version 4.48

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.47-alt2
- Rebuilt with gmp 5.0.5

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.47-alt1
- Version 4.47
- Disabled devel-static package

* Sun Sep 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.46-alt1
- Version 4.46

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.45-alt2
- Rebuilt for debuginfo

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.45-alt1
- Version 4.45

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.44-alt3
- Renamed glpk4 -> glpk

* Thu Sep 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.44-alt2
- Added link to glpk.h into %_includedir

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.44-alt1
- Version 4.44

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.40-alt1
- Version 4.40

* Thu Oct 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.39-alt1
- Version 4.39

* Wed Jul 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.38-alt1
- Version 4.38

* Thu Apr 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.37-alt2
- Move doc and examples into lib%name-devel-doc package

* Tue Apr 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.37-alt1
- Version 4.37

* Tue Apr 18 2006 Grigorij Mogaev <zcrendel@altlinux.ru> 4.9-alt1
- initial rpm, separate source project into four packages.

