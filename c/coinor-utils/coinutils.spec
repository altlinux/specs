%define        _Oname CoinUtils
%define        _gname coinor
%define        _name utils
%define        _oname coinutils

Name:          %_gname-%_name
Version:       2.11.9
Release:       alt1
Summary:       COIN-OR Utilities
License:       EPL-2.0
Group:         System/Libraries
Url:           https://github.com/coin-or/CoinUtils
Vcs:           https://github.com/coin-or/CoinUtils.git
Source:        %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: doxygen

Provides:      %_oname = %EVR
Requires:      lib%name = %EVR

%description
CoinUtils is an open-source collection of classes and helper functions that are
generally useful to multiple COIN-OR projects. These utilities include:

* classes for storing and manipulating sparse matrices and vectors,
* performing matrix factorization,
* parsing input files in standard formats, e.g. MPS,
* building representations of mathematical programs,
* performing simple presolve operations,
* warm starting algorithms for mathematical programs,
* comparing floating point numbers with a tolerance
* classes for storing and manipulating conflict graphs, and
* classes for searching and storing cliques and odd cycles in conflict graphs,
  among others.

CoinUtils is written in C++ and is released as open source under the Eclipse
Public License 2.0.


%package       -n lib%{name}
Group:         System/Libraries
Summary:       Library for %name

%description   -n lib%{name}
CoinUtils is an open-source collection of classes and helper functions that are
generally useful to multiple COIN-OR projects. These utilities include:

* classes for storing and manipulating sparse matrices and vectors,
* performing matrix factorization,
* parsing input files in standard formats, e.g. MPS,
* building representations of mathematical programs,
* performing simple presolve operations,
* warm starting algorithms for mathematical programs,
* comparing floating point numbers with a tolerance
* classes for storing and manipulating conflict graphs, and
* classes for searching and storing cliques and odd cycles in conflict graphs,
  among others.

CoinUtils is written in C++ and is released as open source under the Eclipse
Public License 2.0.



%package       -n lib%{name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{name} = %EVR
Requires:      gcc-c++
Requires:      doxygen

%description   -n lib%{name}-devel
CoinUtils is an open-source collection of classes and helper functions that are
generally useful to multiple COIN-OR projects. These utilities include:

* classes for storing and manipulating sparse matrices and vectors,
* performing matrix factorization,
* parsing input files in standard formats, e.g. MPS,
* building representations of mathematical programs,
* performing simple presolve operations,
* warm starting algorithms for mathematical programs,
* comparing floating point numbers with a tolerance
* classes for storing and manipulating conflict graphs, and
* classes for searching and storing cliques and odd cycles in conflict graphs,
  among others.

CoinUtils is written in C++ and is released as open source under the Eclipse
Public License 2.0.



%package       doc
Group:         Development/Documentation
Summary:       Documentation files for %name

Requires:      lib%{name} = %EVR

%description   doc
CoinUtils is an open-source collection of classes and helper functions that are
generally useful to multiple COIN-OR projects. These utilities include:

* classes for storing and manipulating sparse matrices and vectors,
* performing matrix factorization,
* parsing input files in standard formats, e.g. MPS,
* building representations of mathematical programs,
* performing simple presolve operations,
* warm starting algorithms for mathematical programs,
* comparing floating point numbers with a tolerance
* classes for storing and manipulating conflict graphs, and
* classes for searching and storing cliques and odd cycles in conflict graphs,
  among others.

CoinUtils is written in C++ and is released as open source under the Eclipse
Public License 2.0.



%prep
%setup

%build
%configure
%make all doxydoc

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/doc/%_oname
cp -r ./doxydoc/html/ %buildroot%_datadir/doc/%name-%version

%files
%doc README*

%files         -n lib%name
%_libdir/lib%{_Oname}*.so.*

%files         doc
%_datadir/doc/%name-%version
%_datadir/coin/doc/
%exclude %_docdir/%name-%version/README*

%files         -n lib%name-devel
%_libdir/lib%{_Oname}*.so
%_includedir/coin/Coin*
%_pkgconfigdir/%_oname.pc


%changelog
* Tue Jun 27 2023 Pavel Skrylev <majioa@altlinux.org> 2.11.9-alt1
- initial build for Sisyphus
