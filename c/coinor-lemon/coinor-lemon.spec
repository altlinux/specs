%define        _gname coinor
%define        _name lemon
%define        _Gname Coinor
%define        _Name Lemon

Name:          %{_gname}-%{_name}
Version:       1.3.2
Release:       alt0.1
Summary:       COIN-OR Library for Efficient Modeling and Optimization in Networks
License:       BSL-1.0
Group:         Sciences/Mathematics
Url:           https://lemon.cs.elte.hu/trac/lemon
Vcs:           https://github.com/amessing/lemon-copy.git

Source:        %name-%version.tar
Patch:         config.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: ghostscript
BuildRequires: pkgconfig(coinutils)
BuildRequires: pkgconfig(osi)
BuildRequires: pkgconfig(clp)
# TODO add support for ilog and soplex libs
BuildRequires: libglpk-devel

%description
LEMON stands for Library for Efficient Modeling and Optimization in Networks.
It is a C++ template library providing efficient implementations of common data
structures and algorithms with focus on combinatorial optimization tasks
connected mainly with graphs and networks.

LEMON is a member of the COIN-OR initiative, a collection of OR related open
source projects. You are free to use it in your commercial or non-commercial
applications under very permissive license terms.

The project was launched by the Egervary Research Group on Combinatorial
Optimization (EGRES) at the Department of Operations Research, Eotvos Lorand
University, Budapest, Hungary in 2003. Up to this point, the developers of the
library work at the Eotvos Lorand University, Budapest and at the Budapest
University of Technology and Economics.


%package       -n lib%{name}
Group:         System/Libraries
Summary:       Library files for %name

Provides:      %{_Gname}%{_Name} = %EVR
Provides:      lib%{_Gname}%{_Name} = %EVR

%description   -n lib%{name}
LEMON stands for Library for Efficient Modeling and Optimization in Networks.
It is a C++ template library providing efficient implementations of common data
structures and algorithms with focus on combinatorial optimization tasks
connected mainly with graphs and networks.

LEMON is a member of the COIN-OR initiative, a collection of OR related open
source projects. You are free to use it in your commercial or non-commercial
applications under very permissive license terms.

The project was launched by the Egervary Research Group on Combinatorial
Optimization (EGRES) at the Department of Operations Research, Eotvos Lorand
University, Budapest, Hungary in 2003. Up to this point, the developers of the
library work at the Eotvos Lorand University, Budapest and at the Budapest
University of Technology and Economics.


%package       -n lib%{name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{name} = %EVR
Requires:      cmake
Requires:      doxygen
Requires:      ghostscript
Requires:      pkgconfig(coinutils)
Requires:      pkgconfig(osi)
Requires:      pkgconfig(clp)
Requires:      libglpk-devel

%description   -n lib%{name}-devel
LEMON stands for Library for Efficient Modeling and Optimization in Networks.
It is a C++ template library providing efficient implementations of common data
structures and algorithms with focus on combinatorial optimization tasks
connected mainly with graphs and networks.

LEMON is a member of the COIN-OR initiative, a collection of OR related open
source projects. You are free to use it in your commercial or non-commercial
applications under very permissive license terms.

The project was launched by the Egervary Research Group on Combinatorial
Optimization (EGRES) at the Department of Operations Research, Eotvos Lorand
University, Budapest, Hungary in 2003. Up to this point, the developers of the
library work at the Eotvos Lorand University, Budapest and at the Budapest
University of Technology and Economics.


%prep
%setup
%patch

%build
%cmake -DCMAKE_INSTALL_DIR:STRING=%{_datadir}/cmake/%{_name}/ \
       -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
       -DTARGET_LIBRARY_NAME:STRING=%{_Gname}%{_Name} \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DCMAKE_FIND_LIBRARY_CUSTOM_LIB_SUFFIX:STRING="%_libsuff"

%cmake_build

%install
%cmakeinstall_std

%files
%doc README*
%_bindir/*

%files         -n lib%{name}
%_libdir/lib%{_Gname}%{_Name}*.so.*

%files         -n lib%{name}-devel
%_datadir/cmake/%{_name}/
%_includedir/%{_name}/
%_pkgconfigdir/%{_name}.pc
%_libdir/lib%{_Gname}%{_Name}*.so


%changelog
* Mon Jun 26 2023 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt0.1
- initial build for Sisyphus
