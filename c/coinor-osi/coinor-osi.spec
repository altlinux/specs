%define        _gname coinor
%define        _name osi
%define        _Name Osi
%define        gname coin

Name:          %_gname-%_name
Version:       0.108.8
Release:       alt1
Summary:       Open Solver Interface
License:       EPL-2.0
Group:         System/Libraries
Url:           https://github.com/coin-or/Osi
Vcs:           https://github.com/coin-or/Osi.git
Source:        %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: chrpath
BuildRequires: texlive-collection-basic
BuildRequires: pkgconfig(coinutils)
BuildRequires: pkgconfig(lapack)
BuildRequires: pkgconfig(openblas)
#BuildRequires: libglpk-devel

Requires:      lib%_gname-%_name = %EVR

%description
Osi (Open Solver Interface) provides an abstract base class to a generic linear
programming (LP) solver, along with derived classes for specific solvers. Many
applications may be able to use the Osi to insulate themselves from a specific
LP solver. That is, programs written to the OSI standard may be linked to any
solver with an OSI interface and should produce correct results. The OSI has
been significantly extended compared to its first incarnation. Currently, the
OSI supports linear programming solvers and has rudimentary support for integer
programming. Among others the following operations are supported:

* creating the LP formulation;
* directly modifying the formulation by adding rows/columns;
* modifying the formulation by adding cutting planes provided by CGL;
* solving the formulation (and resolving after modifications);
* extracting solution information;
* invoking the underlying solver's branch-and-bound component.


%package       -n lib%_gname-%_name
Group:         Development/C++
Summary:       Development files for %name

%description   -n lib%_gname-%_name
Osi (Open Solver Interface) provides an abstract base class to a generic linear
programming (LP) solver, along with derived classes for specific solvers. Many
applications may be able to use the Osi to insulate themselves from a specific
LP solver. That is, programs written to the OSI standard may be linked to any
solver with an OSI interface and should produce correct results. The OSI has
been significantly extended compared to its first incarnation. Currently, the
OSI supports linear programming solvers and has rudimentary support for integer
programming. Among others the following operations are supported:

* creating the LP formulation;
* directly modifying the formulation by adding rows/columns;
* modifying the formulation by adding cutting planes provided by CGL;
* solving the formulation (and resolving after modifications);
* extracting solution information;
* invoking the underlying solver's branch-and-bound component.


%package       -n lib%_gname-%_name-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%_gname-%_name = %EVR
Requires:      gcc-c++

%description   -n lib%_gname-%_name-devel
Osi (Open Solver Interface) provides an abstract base class to a generic linear
programming (LP) solver, along with derived classes for specific solvers. Many
applications may be able to use the Osi to insulate themselves from a specific
LP solver. That is, programs written to the OSI standard may be linked to any
solver with an OSI interface and should produce correct results. The OSI has
been significantly extended compared to its first incarnation. Currently, the
OSI supports linear programming solvers and has rudimentary support for integer
programming. Among others the following operations are supported:

* creating the LP formulation;
* directly modifying the formulation by adding rows/columns;
* modifying the formulation by adding cutting planes provided by CGL;
* solving the formulation (and resolving after modifications);
* extracting solution information;
* invoking the underlying solver's branch-and-bound component.


%package       doc
Group:         Development/Documentation
Summary:       Documentation files for %name

Requires:      %{name} = %EVR

%description   doc
Osi (Open Solver Interface) provides an abstract base class to a generic linear
programming (LP) solver, along with derived classes for specific solvers. Many
applications may be able to use the Osi to insulate themselves from a specific
LP solver. That is, programs written to the OSI standard may be linked to any
solver with an OSI interface and should produce correct results. The OSI has
been significantly extended compared to its first incarnation. Currently, the
OSI supports linear programming solvers and has rudimentary support for integer
programming. Among others the following operations are supported:

* creating the LP formulation;
* directly modifying the formulation by adding rows/columns;
* modifying the formulation by adding cutting planes provided by CGL;
* solving the formulation (and resolving after modifications);
* extracting solution information;
* invoking the underlying solver's branch-and-bound component.


%prep
%setup

%build
%configure \
   --with-coin-instdir=%prefix \
   --with-blas-lib=-lblas \
   --with-blas-incdir=%_includedir/blas \
   --with-lapack-lib=-llapack \
   --with-lapack-incdir=%_includedir/lapack \
#   --with-glpk-lib=-lglpk \
#   --with-glpk-incdir=%_includedir/glpk \
%make

pushd %_Name/doxydoc
doxygen doxygen.conf
popd

%install
%makeinstall_std

chrpath -d $(echo $(find %buildroot -name '*.so.*'))


%files
%doc README*

%files         -n lib%_gname-%_name
%doc README*
%_libdir/lib%{_Name}*.so.*

%files         -n lib%_gname-%_name-devel
%doc README*
%_libdir/lib%{_Name}*.so
%_includedir/%gname/%{_Name}*
%_pkgconfigdir/%{_name}*.pc

%files         doc
%doc README*
%_datadir/%gname/doc/%{_Name}
%doc %_Name/doxydoc/doxydoc/html/*


%changelog
* Tue Jun 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.108.8-alt1
- initial build for Sisyphus
