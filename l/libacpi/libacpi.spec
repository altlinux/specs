%add_optflags %optflags_shared
Name:           libacpi
Version:        0.2
Release:        alt2_25
Summary:        General purpose library for ACPI 

Group:          System/Libraries
License:        MIT
URL:            http://www.ngolde.de/libacpi.html
Source0:        http://www.ngolde.de/download/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-sysfs.patch
ExcludeArch:    ppc ppc64

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Source44: import.info

%description    
libacpi is a general purpose shared library for programs gathering 
ACPI data on Linux. Features: Thermal zones support, Battery support, 
Fan support, AC support

Note: This is no portable code, it will only run on i386/x86_64 Linux systems.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i "s|CFLAGS += .*|CFLAGS += -fPIC $RPM_OPT_FLAGS|;s&usr/local&usr&" config.mk
sed -i "s&\${PREFIX}/share/doc/%{name}&%{_docdir}/%{name}&g" Makefile


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%_libdir
chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}.so.*
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%{_mandir}/man3/*
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/CHANGES
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/LICENSE
%{_libdir}/*.so.*

%files devel
%dir %{_docdir}/%{name}/doc
%doc %{_docdir}/%{name}/doc/*
%{_bindir}/test-libacpi
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_25
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_24
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_21
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_19
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_18
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_17
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_16
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_15
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_15
- initial import by fcimport

