# BEGIN SourceDeps(oneline):
BuildRequires: swig
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libitl
Version:        0.7.0 
Release:        alt3_26
Summary:        Libraries for The Islamic Tools and Libraries Project

License:        LGPLv2+
URL:            http://www.arabeyes.org/project.php?proj=ITL
Source0:        http://switch.dl.sourceforge.net/sourceforge/arabeyes/%{name}-%{version}.tar.gz

Patch0: %{name}-makefile-ld.patch
Patch1: %{name}-fedora-c99.patch
#BuildRequires:  autoconf

BuildRequires:  gcc
Source44: import.info
%description
The Islamic Tools and Libraries (ITL) is a project 
to provide a plethora of useful Islamic tools and 
applications as well as a comprehensive feature-full 
Islam-centric library. The ITL project currently 
includes Hijri date, Muslim prayer times, and Qibla. 

This package contains the libraries for applications using ITL

%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --disable-static
%make_build -j1


%install
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ $RPM_BUILD_ROOT/%{_includedir}/itl
cp build/libitl.so.0.0.7 $RPM_BUILD_ROOT/%{_libdir}/
ln -s libitl.so.0.0.7 $RPM_BUILD_ROOT/%{_libdir}/libitl.so.0
ln -s libitl.so.0.0.7 $RPM_BUILD_ROOT/%{_libdir}/libitl.so
cp prayertime/src/prayer.h hijri/src/hijri.h $RPM_BUILD_ROOT/%{_includedir}/itl/
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'






%files
%doc AUTHORS COPYING README
%{_libdir}/libitl.so.*

%files devel
%doc prayertime/doc/method-info.txt
%doc prayertime/README
%doc hijri/README
%{_libdir}/libitl.so
%{_includedir}/itl/


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.7.0-alt3_26
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_10
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_5
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_4
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_4
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_3
- initial import by fcimport

