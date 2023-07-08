%define        _gname coinor
%define        _name clp
%define        _Name Clp
%define        gname coin
%define        osiname osi
%define        osiName Osi

Name:          %{_gname}-%{_name}
Version:       1.17.6
Release:       alt1
Summary:       COIN-OR Linear Programming Solver 
License:       EPL-2.0
Group:         Sciences/Mathematics
Url:           https://github.com/coin-or/Clp
Vcs:           https://github.com/coin-or/Clp.git
Source:        %name-%version.tar
Packager:      Pavel Skrylev <majioa@altlinux.org>

BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: libcoinor-utils-devel
BuildRequires: libcoinor-osi-devel
BuildRequires: chrpath
BuildRequires: graphviz
#BuildRequires: libmumps-devel
#BuildRequires: libglpk-devel
BuildRequires: libblas-devel
BuildRequires: liblapack-devel

Provides:      %{_name} = %EVR
Requires:      lib%{name} = %EVR

%description
Clp (Coin-or linear programming) is an open-source linear programming solver.
It is primarily meant to be used as a callable library, but a basic,
stand-alone executable version is also available. It is designed to find
solutions of mathematical optimization problems of the form

minimize c'x such that lhs <= Ax <= rhs and lb <= x <= ub

CLP includes primal and dual Simplex solvers. Both dual and primal algorithms
can use matrix storage methods provided by the user (0-1 and network matrices
are already supported in addition to the default sparse matrix). The dual
algorithm has Dantzig and Steepest edge row pivot choices; new ones may be
provided by the user. The same is true for the column pivot choice of the
primal algorithm. The primal can also use a non linear cost which should work
for piecewise linear convex functions. CLP also includes a barrier method for
solving LPs.

Clp is written in C++ and is released as open source under the Eclipse Public
License 2.0.


%package       -n lib%{name}
Group:         System/Libraries
Summary:       Library files for %name

%description   -n lib%{name}
%summary.


%package       -n lib%{name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{name} = %EVR
Requires:      gcc-c++
Requires:      doxygen
Requires:      chrpath
Requires:      graphviz
Requires:      libcoinor-utils-devel
Requires:      libcoinor-osi-devel
Requires:      libblas-devel
Requires:      liblapack-devel

%description   -n lib%{name}-devel
%summary.


%package       -n lib%{name}-doc
Group:         Development/Documentation
Summary:       Documentation files for %name

Requires:      lib%{name} = %EVR

%description   -n lib%{name}-doc
%summary.


%package       -n lib%{_gname}-%{osiname}-%{_name}
Group:         System/Libraries
Summary:       Library files for %name

Requires:      lib%{name} = %EVR

%description   -n lib%{_gname}-%{osiname}-%{_name}
%summary.


%package       -n lib%{_gname}-%{osiname}-%{_name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{_gname}-%{osiname}-%{_name} = %EVR
Requires:      gcc-c++

%description   -n lib%{_gname}-%{osiname}-%{_name}-devel
%summary.


%prep
%setup

%build
%configure \
   --with-coin-instdir=%prefix \
   --with-lapack-lib=-llapack \
   --with-blas-lib=-lblas \
#   --with-glpk-lib=-lglpk \
#--with-mumps-lib="-ldmumps -lzmumps -lsmumps -lcmumps -lmumps_common -lpord" \
%make

pushd %_Name/doxydoc
doxygen doxygen.conf
popd

%install
%makeinstall_std

chrpath -d $(echo $(find %buildroot -name '*.so.*'))
chrpath -d $(echo $(find %buildroot%_bindir -type f))


%files
%doc README*
%_bindir/%{_name}

%files         -n lib%{name}
%_libdir/lib%{_Name}*.so.*

%files         -n lib%{name}-doc
%_datadir/%{gname}

%files         -n lib%{name}-devel
%_libdir/lib%{_Name}*.so
%_includedir/%{gname}/%{_Name}*
%_includedir/%{gname}/Cbc*
%_includedir/%{gname}/Idiot*
%_pkgconfigdir/%{_name}.pc

%files         -n lib%{_gname}-%{osiname}-%{_name}
%_libdir/lib%{osiName}%{_Name}*.so.*

%files         -n lib%{_gname}-%{osiname}-%{_name}-devel
%_libdir/lib%{osiName}%{_Name}*.so
%_includedir/%{gname}/%{osiName}%{_Name}*
%_pkgconfigdir/%{osiname}-%{_name}.pc


%changelog
* Fri Aug 7 2020 Pavel Skrylev <majioa@altlinux.org> 1.17.6-alt1
- initial build for Sisyphus
