# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize texinfo
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:          Library to support IDNA2008 internationalized domain names
Name:             libidn2
Version:          0.11
Release:          alt1_1
License:          (GPLv2+ or LGPLv3+) and GPLv3+
Group:            System/Libraries
URL:              http://www.gnu.org/software/libidn/#libidn2
Source:           http://alpha.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz
Patch0:           libidn2-0.3-rpath.patch
Provides:         bundled(gnulib)
Source44: import.info

%description
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892 and 5893 for internationalized domain names (IDN).
It is a standalone library, without any dependency on libidn.

%package devel
Summary:          Development files for libidn2
Group:            Development/Other
Requires:         %{name}%{?_isa} = %{version}

%description devel
The libidn2-devel package contains libraries and header files for
developing applications that use libidn2.

%prep
%setup -q
%patch0 -p1 -b .rpath
touch -c -r configure.rpath configure
touch -c -r src/configure.rpath src/configure
touch -c -r m4/libtool.m4.rpath m4/libtool.m4

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install

# Clean-up examples for documentation
make %{?_smp_mflags} -C examples distclean
rm -f examples/Makefile*

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

# Remove example-only binaries for now
rm -f $RPM_BUILD_ROOT%{_bindir}/{lookup,register}

%check
make %{?_smp_mflags} -C tests check

%files
%{!?_licensedir:%global license %%doc}
%doc COPYING
%doc AUTHORS NEWS README
%{_bindir}/idn2
%{_mandir}/man1/idn2.1*
%{_libdir}/%{name}.so.*
%{_infodir}/%{name}.info*

%files devel
%doc doc/%{name}.html examples
%{_libdir}/%{name}.so
%{_includedir}/*.h
%{_mandir}/man3/*
%{_datadir}/gtk-doc/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3.1
- NMU: added BR: texinfo

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_4
- update to new release by fcimport

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- initial import by fcimport

