%define        _unpackaged_files_terminate_build 1
%define        nomen cminpack
%define        original CMINPACK
%def_enable    check

Name:          lib%nomen
Version:       1.3.11
Release:       alt1
Summary:       Solver for nonlinear equations and nonlinear least squares problems
Group:         Development/Other
License:       BSD
Url:           http://devernay.free.fr/hacks/cminpack/cminpack.html
Vcs:           https://github.com/devernay/cminpack.git
Source:        %{name}-%{version}.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: libflexiblas-devel
%if_enabled check
BuildRequires: ctest
%endif
Provides:      %nomen = %EVR
Obsoletes:     %nomen < %EVR

%description
cminpack is an ISO C99 implementation of the FORTRAN Minpack solver package.
It is fully re-entrant and thread-safe.

%package       devel
Group:         Development/Other
Summary:       Header files and libraries for cminpack
Requires:      %name = %EVR
Provides:      %nomen-devel = %EVR

%description   devel
Contains the development headers and libraries needed to build a program with
cminpack.


%prep
%setup -q

%build
%cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_EXAMPLES=ON \
   -DBUILD_EXAMPLES_FORTRAN=ON \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   %nil
%cmake_build

%install
%cmake_install

%check
%ctest -E "tchkder|tfdjac2|tlmdif"

%files
%doc README.md
%doc docs/*.html docs/*.txt
%_libdir/lib%{nomen}*.so.*

%files devel
%doc README.md
%_includedir/%{nomen}-1
%_libdir/lib%{nomen}*.so
%_libdir/pkgconfig/%{nomen}*.pc
%_cmakedir/%original


%changelog
* Tue Jul 22 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.11-alt1
- ^ 1.3.8 -> 1.3.11
- * restore package

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.3.8-alt1_4
- update to new release by fcimport

* Thu Oct 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt2_5
- NMU: changed CMake Modules install path

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_2
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2
- initial fc import

