# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libxnm
Version:        0.1.3
Release:        alt3_29
Summary:        A library for parsing the XNM format

License:        GPLv2+
URL:            http://xnm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/xnm/%{name}-%{version}.tar.gz
Patch0:         libxnm-c99.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel libgio libgio-devel
Source44: import.info
    
%description
XNM is a simple recursively defined serialization syntax for storing
and communicating of complex data structures

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1


%build
%configure --enable-static=no
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -rf %{buildroot}/usr/doc/libxnm/
find %{buildroot} -name '*.la' -exec rm -f {} ';'



%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/lib*.so.*

%files devel
%doc doxygen-doc/*
%{_includedir}/xnm/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.1.3-alt3_29
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_16
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_14
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_7
- update to new release by fcimport

* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_6
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2_5
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_5
- initial import by fcimport

