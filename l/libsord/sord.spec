# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname sord
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global maj 0

Name:       libsord
Version:    0.16.14
Release:    alt1_2
Summary:    A lightweight Resource Description Framework (RDF) C library

License:    ISC
URL:        https://drobilla.net/software/%{oldname}.html
Source0:    https://download.drobilla.net/%{oldname}-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: libserd-devel >= 0.30.10
BuildRequires: gcc
BuildRequires: meson
BuildRequires: libpcre-devel libpcrecpp-devel
Source44: import.info
Provides: sord = %{version}-%{release}

%description
%{oldname} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory. %{oldname} and parent library serd form 
a lightweight RDF tool-set for resource limited or performance critical 
applications.

%package devel
Group: Development/Other
Summary:    Development libraries and headers for %{oldname}
Requires:   %{name} = %{version}-%{release}
Provides: sord-devel = %{version}-%{release}

%description devel
%{oldname} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory.

This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q


%build
%meson
%meson_build

%install
%meson_install

# Move devel docs to the right directory
install -d %{buildroot}%{_docdir}/%{oldname}
mv %{buildroot}%{_docdir}/%{oldname}-%{maj} %{buildroot}%{_docdir}/%{oldname}

%check
%meson_test

%files
%{_docdir}/%{oldname}
%exclude %{_docdir}/%{oldname}/%{oldname}-%{maj}/
%doc --no-dereference COPYING
%{_libdir}/lib%{oldname}-%{maj}.so.%{maj}*
%{_bindir}/sordi
%{_bindir}/sord_validate
%{_mandir}/man1/%{oldname}*.1*

%files devel
%{_docdir}/%{oldname}/%{oldname}-%{maj}/
%{_libdir}/lib%{oldname}-%{maj}.so
%{_libdir}/pkgconfig/%{oldname}-%{maj}.pc
%{_includedir}/%{oldname}-%{maj}/

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.16.14-alt1_2
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.16.8-alt1_2
- update to new release by fcimport

* Tue Jul 13 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.16.6-alt2_1
- Fixed gcc >= 10 optimization workaround (ALT#40471).

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.16.6-alt1_1
- update to new release by fcimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.16.4-alt1_5
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.16.4-alt1_3
- update to new release by fcimport

* Fri Dec 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.16.4-alt1_1
- update to new release by fcimport

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.16.2-alt1_3
- update to new release by fcimport

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_4
- removed boost form BR:

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_6
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_6
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_5
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.4-alt1_3
- fc import

