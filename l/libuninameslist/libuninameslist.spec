%add_optflags %optflags_shared
Name:           libuninameslist
Version:        20150701
Release:        alt1_1

Summary:        A library providing Unicode character names and annotations

Group:          System/Libraries
License:        BSD
URL:            https://github.com/fontforge/libuninameslist
Source0:        https://github.com/fontforge/libuninameslist/archive/0.5.20150701.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Source44: import.info

%description
libuninameslist provides applications with access to Unicode name and
annotation data from the official Unicode Character Database.

%package        devel
Summary:        Header files and static libraries for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and static libraries for %{name}.


%prep
%setup -q -n libuninameslist-0.5.20150701

%build
autoreconf -i
automake --foreign -Wall
%configure --disable-static
make %{?_smp_mflags}


%install
%makeinstall incdir=$RPM_BUILD_ROOT%{_includedir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%files
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libuninameslist.pc

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 20150701-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20130501-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 20130501-alt1_3
- update to new release by fcimport

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 20130501-alt1_2
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 20130501-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20091231-alt3_7
- update to new release by fcimport

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 20091231-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20091231-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20091231-alt3_4
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 20091231-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20091231-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 20091231-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 20091231-alt1_2
- initial import by fcimport

