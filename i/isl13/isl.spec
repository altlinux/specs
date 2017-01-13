%def_disable devel

Name: isl13
Version: 0.14.1
Release: alt2

Summary: Integer Set Library
License: MIT
Group: System/Legacy libraries
Url: http://isl.gforge.inria.fr/
# git://git.altlinux.org/gears/i/isl.git
Source: %name-%version-%release.tar
BuildRequires: libgmp-devel

%define sover 13

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
Group: System/Legacy libraries

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

%package -n libisl%sover-devel
Summary: Development tools for ISL
Group: Development/C
Requires: libisl%sover = %EVR

%description -n libisl%sover-devel
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

%if_enabled devel
%files -n libisl%sover-devel
%_includedir/isl/
%_libdir/libisl.so
%exclude %_pkgconfigdir/isl.pc
%endif

%changelog
* Wed Nov 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.14.1-alt2
- Packaged libisl13 as a legacy library.

* Wed May 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.14.1-alt1
- Updated to 0.14.1.

* Wed Jan 22 2014 Dmitry V. Levin <ldv@altlinux.org> 0.12.2-alt1
- Initial revision.
