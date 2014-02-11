Name: isl
Version: 0.12.2
Release: alt1

Summary: Integer Set Library
License: MIT
Group: System/Libraries
Url: http://isl.gforge.inria.fr/
# git://git.altlinux.org/gears/i/isl.git
Source: %name-%version-%release.tar
BuildRequires: libgmp-devel

%define sover 10

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration. It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

%package -n libisl%sover
Summary: Integer Set Library
Group: System/Libraries

%description -n libisl%sover
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration. It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

This package contains isl shared library.

%package -n libisl-devel
Summary: Development tools for ISL
Group: Development/C
Requires: libisl%sover = %EVR

%description -n libisl-devel
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration. It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

This package contains files needed for building with isl library.

%prep
%setup -n %name-%version-%release
echo %name-%version > GIT_HEAD_ID

%build
%autoreconf
%configure --disable-static
%make_build

%check
%make_build -k check

%install
%makeinstall_std
rm %buildroot%_libdir/libisl.so.*.py

%files -n libisl%sover
%_libdir/libisl.so.*

%files -n libisl-devel
%_includedir/isl/
%_libdir/libisl.so
%exclude %_pkgconfigdir/isl.pc

%changelog
* Wed Jan 22 2014 Dmitry V. Levin <ldv@altlinux.org> 0.12.2-alt1
- Initial revision.
