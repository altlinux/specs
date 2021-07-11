# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:      libgta
Version:   1.2.1
%global so_version 1
Release:   alt1_5
Summary:   Library that implements the Generic Tagged Arrays file format
License:   LGPLv2+
URL:       https://marlam.de/gta/
Source0:   https://marlam.de/gta/releases/%{name}-%{version}.tar.xz
BuildRequires: ctest cmake
BuildRequires: gcc
BuildRequires: doxygen
Source44: import.info

%description
Libgta is a portable library that implements the GTA (Generic Tagged Arrays)
file format. It provides interfaces for C and C++.


%package devel
Group: Development/Other
Summary:  Development Libraries for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Group: Documentation
Summary:  API documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The %{name}-doc package contains HTML API documentation and
examples for %{name}.


%prep
%setup -q

%build
%{fedora_v2_cmake} -D GTA_BUILD_STATIC_LIB:BOOL=FALSE
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

# Remove documentation; will install it with doc macro
rm -rf %{buildroot}%{_docdir}


%check
%fedora_v2_ctest





%files 
%doc COPYING AUTHORS README
%{_libdir}/%{name}.so.%{so_version}
%{_libdir}/%{name}.so.%{so_version}.*

%files devel
%{_libdir}/cmake/GTA-%{version}
%{_libdir}/pkgconfig/gta.pc
%{_includedir}/gta
%{_libdir}/%{name}.so

%files doc
%doc doc/example*


%changelog
* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt1_5
- update to new release by fcimport

* Sun Apr 28 2019 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1_1.1
- BR: valgrind only where it's available

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_6
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_4
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_2
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_4
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- initial fc import

