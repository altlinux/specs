Name: cloog
Version: 0.18.2
Release: alt1

Summary: The Chunky Loop Generator
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.cloog.org/
# git://git.altlinux.org/gears/c/cloog.git
Source: %name-%version-%release.tar
BuildRequires: libgmp-devel libisl-devel

%define sover 4
Requires: libcloog-isl%sover = %EVR

%description
CLooG is a free software and library to generate code for scanning
Z-polyhedra.  That is, it finds a code (e.g. in C, FORTRAN...) that
reaches each integral point of one or more parameterized polyhedra.
CLooG has been originally written to solve the code generation problem
for optimizing compilers based on the polytope model.  Nevertheless it
is used now in various area e.g. to build control automata for
high-level synthesis or to find the best polynomial approximation of a
function.  CLooG may help in any situation where scanning polyhedra
matters.  While the user has full control on generated code quality,
CLooG is designed to avoid control overhead and to produce a very
effective code.

%package -n libcloog-isl%sover
Summary: Integer Set Library
Group: System/Libraries

%description -n libcloog-isl%sover
CLooG is a free software and library to generate code for scanning
Z-polyhedra.  That is, it finds a code (e.g. in C, FORTRAN...) that
reaches each integral point of one or more parameterized polyhedra.
CLooG has been originally written to solve the code generation problem
for optimizing compilers based on the polytope model.  Nevertheless it
is used now in various area e.g. to build control automata for
high-level synthesis or to find the best polynomial approximation of a
function.  CLooG may help in any situation where scanning polyhedra
matters.  While the user has full control on generated code quality,
CLooG is designed to avoid control overhead and to produce a very
effective code.

This package contains CLooG shared library.

%package -n libcloog-isl-devel
Summary: Development tools for ISL
Group: Development/C
Requires: libcloog-isl%sover = %EVR

%description -n libcloog-isl-devel
CLooG is a free software and library to generate code for scanning
Z-polyhedra.  That is, it finds a code (e.g. in C, FORTRAN...) that
reaches each integral point of one or more parameterized polyhedra.
CLooG has been originally written to solve the code generation problem
for optimizing compilers based on the polytope model.  Nevertheless it
is used now in various area e.g. to build control automata for
high-level synthesis or to find the best polynomial approximation of a
function.  CLooG may help in any situation where scanning polyhedra
matters.  While the user has full control on generated code quality,
CLooG is designed to avoid control overhead and to produce a very
effective code.

This package contains files needed for building with CLooG library.

%prep
%setup -n %name-%version-%release
echo %name-%version > GIT_HEAD_ID

%build
%autoreconf
%configure --disable-static --with-isl=system
%make_build

%check
# SMP-incompatible
make -k check

%install
%makeinstall_std
rm -r %buildroot%_libdir/{cloog-isl,isl}

%files
%_bindir/cloog

%files -n libcloog-isl%sover
%_libdir/libcloog-isl.so.*

%files -n libcloog-isl-devel
%_includedir/cloog/
%_libdir/libcloog-isl.so
%exclude %_pkgconfigdir/cloog-isl.pc

%changelog
* Wed Jan 22 2014 Dmitry V. Levin <ldv@altlinux.org> 0.18.2-alt1
- Initial revision.
