# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test.pm) perl-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Blitzed open proxy monitor library
Name:           libopm
Version:        0.1
Release:        alt3_33.20050731cvs
License:        GPLv2+
URL:            http://wiki.blitzed.org/BOPM
# cvs -z3 -d:pserver:anon@cvs.blitzed.org:/ co -D "20050731 23:59" libopm
# find libopm -type f -name .cvsignore -exec rm -f {} ';'
# find libopm -type d -name CVS -exec rm -rf {} 2>/dev/null ';'
# mv -f libopm libopm-$(grep AC_INIT libopm/configure.in | sed -e 's/.*\[\(.*\)\].*/\1/')
Source:         %{name}-%{version}.tar.gz
Patch1:         libopm-0.1-multilib.patch
Patch2:         libopm-configure-c99.patch
BuildRequires:  gcc
Source44: import.info

%description
An open proxy detection library, developed by the blitzed
IRC network team. Its original use was to detect open proxies
running on clients connecting to various IRC servers, but it
has evolved to become a generic open proxy detection library.

%package devel
Group: Development/Other
Summary:        Headers and development libraries for libopm
Requires:       %{name} = %{version}-%{release}

%description devel
The libopm-devel package contains the header files and libraries
necessary for developing applications which use libopm.

%if 0%{!?_without_doc:1}
%package doc
Group: System/Libraries
Summary:        Documentation files for libopm
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
This package contains the API documentation for developing
applications that use libopm, which is an open proxy detection
library. 
%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1


%build
%configure --disable-static
%make_build
%{!?_without_doc:cd doc && doxygen && mv -f api html}

%install
%makeinstall_std

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la



%files
%doc --no-dereference LICENSE
%doc ChangeLog
%{_libdir}/%{name}.so.*

%files devel
%doc doc/libopm-api.txt
%{_includedir}/opm*
%{_libdir}/%{name}.so

%if 0%{!?_without_doc:1}
%files doc
%doc doc/html/
%endif

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.1-alt3_33.20050731cvs
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_21.20050731cvs
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_19.20050731cvs
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_18.20050731cvs
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_17.20050731cvs
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_16.20050731cvs
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_15.20050731cvs
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_14.20050731cvs
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_13.20050731cvs
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_12.20050731cvs
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_11.20050731cvs
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_11.20050731cvs
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_10.20050731cvs
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_10.20050731cvs
- initial import by fcimport

