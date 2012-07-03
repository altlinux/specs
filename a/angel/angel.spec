Name: angel
Version: 2011.06.30
Release: alt1
Summary: ANGEL stands for Automatic differentiation Nested Graph Elimination Library
License: BSD
Group: Sciences/Mathematics
Url: http://sourceforge.net/projects/angellib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://angellib.svn.sourceforge.net/svnroot/angellib/trunk/
Source: %name-%version.tar

BuildPreReq: doxygen gcc-c++ boost-devel rpm-macros-make
BuildPreReq: libxaifBooster-devel graphviz

%description
ANGEL stands for Automatic differentiation Nested Graph Elimination
Library. It implements graph elimination techniques in order to find the
cheapest accumulation of Jacobian matrices. It provides:

* Sparse representation of c-graphs and their dual line graphs including
  many helper functions to work with them
* Vertex, edge, and face elimination

* Structured graph generator
* Heuristics for selecting next vertex, edge or face to eliminate

  * Lowest Markowitz degree first
  * Lowest relative Markowitz degree first
  * Minimal Fill-in
  * Maximal overall path length reduction
  * Maximal overall Markowitz degree reduction
  * Lowest Markowitz minimal damage
  * Scarcity-aware edge eliminations

* Stochastic methods

  * It is intended to optimize elimination sequences but written as
    universally as possible and can be applied to any problem where
    neighborhood relation and objective function are provided as functor
  * Metropolis with fixed temperature
  * Metropolis with fixed temperature

%package -n lib%name
Summary: ANGEL stands for Automatic differentiation Nested Graph Elimination Library
Group: System/Libraries

%description -n lib%name
ANGEL stands for Automatic differentiation Nested Graph Elimination
Library. It implements graph elimination techniques in order to find the
cheapest accumulation of Jacobian matrices. It provides:

* Sparse representation of c-graphs and their dual line graphs including
  many helper functions to work with them
* Vertex, edge, and face elimination

* Structured graph generator
* Heuristics for selecting next vertex, edge or face to eliminate

  * Lowest Markowitz degree first
  * Lowest relative Markowitz degree first
  * Minimal Fill-in
  * Maximal overall path length reduction
  * Maximal overall Markowitz degree reduction
  * Lowest Markowitz minimal damage
  * Scarcity-aware edge eliminations

* Stochastic methods

  * It is intended to optimize elimination sequences but written as
    universally as possible and can be applied to any problem where
    neighborhood relation and objective function are provided as functor
  * Metropolis with fixed temperature
  * Metropolis with fixed temperature

%package -n lib%name-devel
Summary: Development files of ANGEL
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
ANGEL stands for Automatic differentiation Nested Graph Elimination
Library. It implements graph elimination techniques in order to find the
cheapest accumulation of Jacobian matrices. It provides:

This package contains development files of ANGEL.

%package -n lib%name-devel-doc
Summary: Documentation for ANGEL
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
ANGEL stands for Automatic differentiation Nested Graph Elimination
Library. It implements graph elimination techniques in order to find the
cheapest accumulation of Jacobian matrices. It provides:

This package contains development documentation for ANGEL.

%prep
%setup

mkdir angel
ln -s ../include angel

%build
%add_optflags -I$PWD -fPIC -DPIC
export CPPFLAGS="%optflags"
%make_build_ext

g++ -shared -Wl,-whole-archive lib/lib%name.a -Wl,-no-whole-archive \
	-Wl,-soname,lib%name.so.0 -o lib/lib%name.so.0 -lxaifBoosterutils

doxygen

%install
install -d %buildroot%_libdir
install -m644 lib/lib%name.so.0 %buildroot%_libdir
ln -s lib%name.so.0 %buildroot%_libdir/lib%name.so

install -d %buildroot%_includedir/%name
install -m644 include/* %buildroot%_includedir/%name

install -d %buildroot%_docdir/%name
cp -fR doc/html examples %buildroot%_docdir/%name/
rm -fR doc/html doc/latex

%files -n lib%name
%doc COPYRIGHT doc/*
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Tue Apr 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.06.30-alt1
- Initial build for Sisyphus

