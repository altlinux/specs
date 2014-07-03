# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
Name:           libxnm
Version:        0.1.3
Release:        alt3_11
Summary:        A library for parsing the XNM format

License:        GPLv2+
URL:            http://xnm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/xnm/%{name}-%{version}.tar.gz

BuildRequires:  glib2-devel
Source44: import.info

    
%description
XNM is a simple recursively defined serialization syntax for storing
and communicating of complex data structures

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --enable-static=no
make %{?_smp_mflags}

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

