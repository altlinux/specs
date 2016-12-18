# BEGIN SourceDeps(oneline):
BuildRequires: libxml2-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libmetalink
Version:	0.1.3
Release:	alt1_1
Summary:	Metalink library written in C
Group:		System/Libraries
License:	MIT
URL:		https://launchpad.net/libmetalink
Source0:	https://launchpad.net/libmetalink/trunk/%{name}-%{version}/+download/%{name}-%{version}.tar.bz2
BuildRequires:	libexpat-devel
BuildRequires:	CUnit-devel
Source44: import.info

%description
libmetalink is a Metalink C library. It adds Metalink functionality such as
parsing Metalink XML files to programs written in C.

%package	devel
Summary:	Files needed for developing with %{name}
Group:		Development/Other
Requires:	%{name}%{?_isa} = %{version}

%description	devel
Files needed for building applications with libmetalink.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name *.la -exec rm {} \;

%files
%{!?_licensedir:%global license %%doc}
%doc COPYING
%doc README 
%{_libdir}/libmetalink.so.*


%files devel
%dir %{_includedir}/metalink/
%{_includedir}/metalink/metalink_error.h
%{_includedir}/metalink/metalink.h
%{_includedir}/metalink/metalink_parser.h
%{_includedir}/metalink/metalink_types.h
%{_includedir}/metalink/metalinkver.h
%{_libdir}/libmetalink.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*


%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_8
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_4
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_3
- update to new release by fcimport

* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt3_7
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2_7
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2_6
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_6
- initial import by fcimport

