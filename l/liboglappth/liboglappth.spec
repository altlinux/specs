# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           liboglappth
Summary:        An OpenGL wrapper library
Version:        0.98
Release:        alt2_18
License:        GPLv2+
Group:          Engineering
URL:            http://www.uku.fi/~thassine/ghemical
Source0:        http://www.uku.fi/~thassine/projects/download/current/%{name}-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
Source44: import.info

%description
Library for creating portable OpenGL applications with easy-to-code
scene setup and selection operations.

%package devel
Summary:    Libraries and header files from %{name}
Group:      Development/C
Requires:   %{name} = %{version}
Requires:   pkgconfig

%description devel
Libraries and header include files for developing programs
based on %{name}.

%prep
%setup -n %{name}-%{version} -q
[ -s NEWS ] && exit 1
[ -s README ] && exit 1

%build
autoreconf -v -f -i
%configure --disable-static
make %{?_smp_mflags} CCOPTIONS="%{optflags}" LIBS="-lGL -lGLU"

%install
make DESTDIR="%{buildroot}" INSTALL="install -p" install
find %{buildroot}%{_libdir} -name *.la -exec rm -rf {} \;

%files
%doc AUTHORS ChangeLog COPYING
%{_libdir}/liboglappth.so.*

%files devel
%{_includedir}/oglappth/
%{_libdir}/liboglappth.so
%{_libdir}/pkgconfig/liboglappth.pc


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_13
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_10
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_9
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_8
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_7
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1_7
- initial import by fcimport

