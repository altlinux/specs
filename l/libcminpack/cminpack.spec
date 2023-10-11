# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: Development/Other
%add_optflags %optflags_shared
%define oldname cminpack
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%undefine __cmake_in_source_build
%global soversion 1

Name:           libcminpack
Version:        1.3.8
Release:        alt1_4
Summary:        Solver for nonlinear equations and nonlinear least squares problems

License:        BSD
URL:            http://devernay.free.fr/hacks/cminpack/cminpack.html
Source0:        https://github.com/devernay/%{oldname}/archive/v%{version}/%{oldname}-%{version}.tar.gz
# Update path to cblas.h for flexiblas, and fix cmake data install paths.
Patch1:         %{oldname}-1.3.8-blas.patch
# Use the target instead of the executable name in a custom command.
Patch2:         %{oldname}-1.3.8-cmake3.patch

BuildRequires:  ctest cmake
BuildRequires:  libflexiblas-devel
BuildRequires:  gcc
BuildRequires:  gcc-fortran
Source44: import.info
Provides: cminpack = %{version}-%{release}
Patch33: cminpack-1.3.0-alt-linkage.patch

%description
cminpack is an ISO C99 implementation of the FORTRAN Minpack solver package.
It is fully re-entrant and thread-safe.

%package devel
Group: Development/Other
Summary: Header files and libraries for cminpack
Requires: %{name} = %{version}-%{release}
Provides: cminpack-devel = %{version}-%{release}

%description devel
Contains the development headers and libraries needed to build a program with
cminpack.

%prep
%setup -n %{oldname}-%{version} -q
%patch1 -p0 -b .blas
%patch2 -p1 -b .cmake3
#patch33 -p1

%build
%{fedora_v2_cmake} \
  -DUSE_FPIC=ON \
  -DSHARED_LIBS=ON \
  -DBUILD_EXAMPLES=ON \
  -DBUILD_EXAMPLES_FORTRAN=ON \
  -DCMINPACK_LIB_INSTALL_DIR=%{_lib} \
  -DUSE_BLAS=ON \
  -DCMAKE_BUILD_TYPE=none
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%files
%doc --no-dereference CopyrightMINPACK.txt
%doc README.md
%{_libdir}/libcminpack.so.%{version}
%{_libdir}/libcminpack.so.%{soversion}
%{_libdir}/libcminpacks.so.%{version}
%{_libdir}/libcminpacks.so.%{soversion}
%ifnarch %arm
%{_libdir}/libcminpackld.so.%{version}
%{_libdir}/libcminpackld.so.%{soversion}
%endif

%files devel
%doc docs/*.html docs/*.txt
%{_includedir}/cminpack-1
%{_libdir}/pkgconfig/*
%{_libdir}/cminpack
%{_libdir}/libcminpack.so
%{_libdir}/libcminpacks.so
%ifnarch %arm
%{_libdir}/libcminpackld.so
%endif


%changelog
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

