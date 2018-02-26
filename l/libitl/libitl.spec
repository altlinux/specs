%add_optflags %optflags_shared
Name:           libitl
Version:        0.7.0 
Release:        alt3_4
Summary:        Libraries for The Islamic Tools and Libraries Project

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.arabeyes.org/project.php?proj=ITL
Source0:        http://switch.dl.sourceforge.net/sourceforge/arabeyes/%{name}-%{version}.tar.gz

Patch0: %{name}-makefile-ld.patch
Source44: import.info
#BuildRequires:  autoconf

%description
The Islamic Tools and Libraries (ITL) is a project 
to provide a plethora of useful Islamic tools and 
applications as well as a comprehensive feature-full 
Islam-centric library. The ITL project currently 
includes Hijri date, Muslim prayer times, and Qibla. 

This package contains the libraries for applications using ITL

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libitl = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make  %{?_smp_mflags} -j1


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
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_4
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_4
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_3
- initial import by fcimport

