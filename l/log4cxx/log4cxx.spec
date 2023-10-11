BuildRequires: /usr/bin/dot
Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/zip qt5-base-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 3

%global sover 15

Name: log4cxx
Version: 1.1.0
Release: alt1_3
Summary: A port to C++ of the Log4j project

License: Apache-2.0
URL: http://logging.apache.org/log4cxx/index.html
Source0: http://www.apache.org/dist/logging/log4cxx/%{version}/apache-%{name}-%{version}.tar.gz

BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: ctest cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
Source44: import.info

%description
Log4cxx is a popular logging package written in C++. One of its distinctive
features is the notion of inheritance in loggers. Using a logger hierarchy it
is possible to control which log statements are output at arbitrary
granularity. This helps reduce the volume of logged output and minimize the
cost of logging.

%package devel
Group: Development/C
Requires: %{name} = %{version}-%{release}
Summary: Header files for Log4xcc - a port to C++ of the Log4j project

%description devel
Header files and documentation you can use to develop with %{name}.

%package doc
Group: System/Libraries
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
%setup -q -n apache-%{name}-%{version}


%build
%{fedora_v2_cmake} -DBUILD_SITE=ON
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%check
%fedora_v2_ctest

%files
%{_libdir}/liblog4cxx.so.%{sover}*

%doc NOTICE KEYS
%doc --no-dereference LICENSE


%files devel
%{_includedir}/log4cxx
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc
%{_libdir}/cmake/log4cxx

%if 0
%files doc
%doc --no-dereference LICENSE
%doc %{_vpath_builddir}/src/site/html/
%endif

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.1.0-alt1_3
- new version

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_25
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_23
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_19
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_17
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_16
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_15
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_14
- initial fc import

