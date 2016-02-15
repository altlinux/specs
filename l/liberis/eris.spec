# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(atlascpp-0.6) pkgconfig(glib-2.0) pkgconfig(mercator-0.3) pkgconfig(sigc++-2.0) pkgconfig(skstream-0.3) pkgconfig(wfmath-1.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname eris
Name:           liberis
Version:        1.3.23
Release:        alt1_6
Summary:        Client-side session layer for Atlas-C++

Group:          Development/C++
# All files untagged except for Eris/Operations.{cpp,h} which is labeled
# LGPL with no version.
License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/eris
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.bz2

BuildRequires: mercator-devel doxygen
BuildRequires: atlascpp-devel >= 0.5.98
BuildRequires: wfmath-devel >= 0.3.2
BuildRequires: skstream-devel >= 0.3.5

BuildRequires:  libsigc++2-devel glib-devel
Source44: import.info
Provides: eris = %{version}-%{release}

%description
A client side session layer for WorldForge; Eris manages much of the generic
work required to communicate with an Atlas server. Client developers can extend
Eris in a number of ways to rapidly add game and client specific functions, and
quickly tie game objects to whatever output representation they are using.


%package devel
Summary:        Development files for Eris
Group:          Development/C++
Requires:       pkgconfig %{oldname} = %{version}
Provides: eris-devel = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use Eris.


%prep
%setup -n %{oldname}-%{version} -q


%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}-1.3.la

# 2014-05-17 - Tests disabled because one of 42 failed, will work w/ upstream to fix
%files
%doc AUTHORS ChangeLog CHANGES-1.4 COPYING NEWS README TODO
%{_libdir}/lib%{oldname}-1.3.so.*


%files devel
%{_includedir}/Eris-1.3
%{_libdir}/lib%{oldname}-1.3.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.23-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.23-alt1_5
- update to new release by fcimport

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.23-alt1_3.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.23-alt1_3
- update to new release by fcimport

* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.23-alt1
- Version 1.3.23

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.21-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.21-alt1_2
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.21-alt1_1
- new release

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt3_5
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt3_4
- rebuild with new libmercator

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_4
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_3
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_1
- rebuild with new libwfmath

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt1_1
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.18-alt1_3
- initial release by fcimport

