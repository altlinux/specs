Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libuninameslist
Version:        20221022
Release:        alt1_1

Summary:        A library providing Unicode character names and annotations

License:        BSD
URL:            https://github.com/fontforge/libuninameslist
Source0:        https://github.com/fontforge/libuninameslist/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Source44: import.info

%description
libuninameslist provides applications with access to Unicode name and
annotation data from the official Unicode Character Database.

%package        devel
Group: Development/Other
Summary:        Header files and static libraries for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and static libraries for %{name}.


%prep
%setup -q


%build
autoreconf -i
automake --foreign -Wall
%configure --disable-static
make V=1 %{?_smp_mflags}


%install
%makeinstall_std incdir=$RPM_BUILD_ROOT%{_includedir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%files
%doc --no-dereference LICENSE
%doc ChangeLog README.md
%{_libdir}/*.so.*

%files devel
%{_mandir}/man3/libuninameslist.3*
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libuninameslist.pc

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 20221022-alt1_1
- update to new release by fcimport

* Tue Aug 02 2022 Igor Vlasenko <viy@altlinux.org> 20220701-alt1_2
- update to new release by fcimport

* Tue Nov 30 2021 Igor Vlasenko <viy@altlinux.org> 20211114-alt1_1
- update to new release by fcimport

* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 20210917-alt1_1
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 20210626-alt1_1
- update to new release by fcimport

* Fri Apr 17 2020 Igor Vlasenko <viy@altlinux.ru> 20200413-alt1_1
- update to new release by fcimport

* Thu Apr 02 2020 Igor Vlasenko <viy@altlinux.ru> 20200313-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 20190701-alt1_2
- update to new release by fcimport

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 20190305-alt1_1
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 20180701-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 20170701-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 20170701-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 20160701-alt1_2
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20160701-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 20150701-alt1_2
- update to new release by fcimport

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

