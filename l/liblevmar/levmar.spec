# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: libblas-devel
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname levmar
%define fedora 37
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# SOlib major and minor version
%global major 2
%global minor 6

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

Name:		liblevmar
Version:	2.6
Release:	alt1_12
Summary:	Levenberg-Marquardt nonlinear least squares algorithm
URL:		http://www.ics.forth.gr/~lourakis/levmar/

Source0:	http://www.ics.forth.gr/~lourakis/levmar/levmar-%{version}.tgz

# Patch to fix compilation of the shared library and compile the demo program
Patch0:		levmar-cmake-shared.patch

License:	GPLv2+
BuildRequires:	gcc
BuildRequires:	ctest cmake
BuildRequires:	dos2unix
BuildRequires:  chrpath
%if %{with flexiblas}
BuildRequires:	libflexiblas-devel
%else
BuildRequires:	libblas-devel libclapack-devel, liblapack-devel
%endif
Source44: import.info
Provides: levmar = %{version}-%{release}

%description
levmar is a native ANSI C implementation of the Levenberg-Marquardt
optimization algorithm.  Both unconstrained and constrained (under linear
equations, inequality and box constraints) Levenberg-Marquardt variants are
included.  The LM algorithm is an iterative technique that finds a local
minimum of a function that is expressed as the sum of squares of nonlinear
functions.  It has become a standard technique for nonlinear least-squares
problems and can be thought of as a combination of steepest descent and the
Gauss-Newton method.  When the current solution is far from the correct on,
the algorithm behaves like a steepest descent method: slow, but guaranteed
to converge.  When the current solution is close to the correct solution, it
becomes a Gauss-Newton method.

%package devel
Group: Development/Other
Summary:	Development files for levmar library, and demo program
Requires:	liblevmar = %{version}-%{release}
Provides: levmar-devel = %{version}-%{release}

%description devel
Development files for the levmar library, and demo program.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1

dos2unix -k README.txt

%if %{with flexiblas}
sed -i 's/lapack;blas/flexiblas;flexiblas/g' CMakeLists.txt
%endif

%build
%{fedora_v2_cmake} -DLINSOLVERS_RETAIN_MEMORY:BOOL=OFF -DNEED_F2C:BOOL=OFF
%fedora_v2_cmake_build

%install
install -D -p -m 755 "%{_vpath_builddir}/liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so.%{major}.%{minor}"
install -D -p -m 644 levmar.h "%{buildroot}%{_includedir}/levmar.h"
install -D -p -m 755 "%{_vpath_builddir}/lmdemo" "%{buildroot}%{_bindir}/lmdemo"
ln -s "liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so.%{major}"
ln -s "liblevmar.so.%{major}.%{minor}" "%{buildroot}%{_libdir}/liblevmar.so"
chrpath --delete "%{buildroot}%{_bindir}/lmdemo"



%check
"%{_vpath_builddir}/lmdemo"

%files
%doc README.txt LICENSE
%{_libdir}/liblevmar.so.%{major}.%{minor}
%{_libdir}/liblevmar.so.%{major}

%files devel
%{_includedir}/levmar.h
%{_libdir}/liblevmar.so
%{_bindir}/lmdemo

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 2.6-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_10
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_9
- new version

