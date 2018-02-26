Name: glpk
Version: 4.47
Release: alt1

Summary: GNU Linear Programming Kit
License: GPL
Group: Development/Other
Url: http://www.gnu.org/software/glpk/glpk.html

Source0: %name-%version.tar.gz
Requires: lib%name = %version-%release

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Obsoletes: %{name}4
Conflicts: %{name}4

BuildRequires: glibc-devel-static zlib-devel libgmp-devel libltdl7-devel

%package -n lib%name
Summary: GNU Linear Programming Kit shared libraries
Group: System/Libraries
Obsoletes: lib%{name}4
Conflicts: lib%{name}4

%package -n lib%name-devel
Summary: Development headers and files for GLPK
Group: Development/C
Requires: lib%name = %version-%release, pkgconfig
Provides: lib%{name}4-devel = %version-%release
Obsoletes: lib%{name}4-devel < %version-%release
Conflicts: lib%{name}4-devel < %version-%release

%package -n lib%name-devel-static
Summary: Static version of GLPK libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%package -n lib%name-devel-doc
Summary: Development documentation for GLPK
Group: Development/Documentation
BuildArch: noarch
Obsoletes: lib%{name}4-devel-doc
Conflicts: lib%{name}4-devel-doc

%description
The glpk (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

glpk supports the GNU MathProg language, which is a subset of the AMPL
language.

The glpk package includes the following main components:

 * Revised simplex method.
 * Primal-dual interior point method.
 * Branch-and-bound method.
 * Translator for GNU MathProg.
 * Application program interface (API).
 * Stand-alone LP/MIP solver.

%description -n lib%name
The glpk (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains shared library required for run glpk-based software.

%description -n lib%name-devel
The glpk (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains headers and files for developing applications
which use glpk (GNU Linear Programming Kit).

%description -n lib%name-devel-static
The glpk (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains GLPK static libraries.

%description -n lib%name-devel-doc
The glpk (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains documentation for developing applications
which use glpk (GNU Linear Programming Kit).

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
	--includedir=%_includedir/%name \
	--enable-dl \
	--with-gmp \
	--with-zlib
sed -i -e '1a\echo=echo' libtool
%make_build

%install
%makeinstall_std

install -d %buildroot%_docdir/%name
cp -fR doc/* %buildroot%_docdir/%name/
rm -fR examples/.libs
rm -f examples/*.o
cp -fR examples %buildroot%_docdir/%name/

ln -s glpk/glpk.h %buildroot%_includedir

%files 
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
#_libdir/pkgconfig/*
%doc AUTHORS ChangeLog COPYING NEWS README THANKS

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
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

