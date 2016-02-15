%add_optflags %optflags_shared
%define oldname unshield
# github: https://fedoraproject.org/wiki/Packaging:SourceURL
%global commit fe6338bd8ec0d9ff2148a134fabab5a0423a0b90
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libunshield
Version:        1.0
Release:        alt1_5
Summary:        Install InstallShield applications on a Pocket PC

Group:          Communications
License:        MIT
URL:            https://github.com/twogood/unshield
Source0:        https://github.com/twogood/unshield/archive/%{commit}/%{oldname}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
Source44: import.info
Provides: unshield = %{version}-%{release}

%description
This tool allows the extraction of InstallShield format cabinet files (which
are different from Microsoft cabinet files). It was initially developed as a
part of the SynCE project to aid with installing applications for Pocket PC
devices, which were often contained in InstallShield installers, but these days
that is rather less likely to be the primary use case.

%package devel
Group:          Development/C
Summary:        Files needed for software development with %{oldname}
Requires:       %{name} = %{version}
Requires:       pkgconfig
Provides: unshield-devel = %{version}-%{release}

%description devel
The %{oldname}-devel package contains the files needed for development with
%{oldname}.

%prep
%setup -q -n %{oldname}-%{commit}

%build
./bootstrap
%configure --disable-static --disable-rpath
make LIBTOOL=%{_bindir}/libtool %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libunshield.{,l}a

%files
%doc README LICENSE
%{_bindir}/unshield
%{_mandir}/man1/unshield.1*
%{_libdir}/libunshield.so.*

%files devel
%{_libdir}/libunshield.so
%{_includedir}/libunshield.h
%{_libdir}/pkgconfig/libunshield.pc

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_7
- update to new release by fcimport

* Wed Mar 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_6
- restored in Sisyphus as fc import

* Thu Jan 19 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt3
- drop RPATH
- minor spec cleanup

* Tue Oct 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt2
- rebuild with new openssl

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- 0.6

* Sat Oct 04 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sat Dec 08 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt3
- update to SVN 20071207 version

* Fri Oct 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt2
- fix #13081 (linking with crypto lib), thanks to Slava Semushin

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt1
- 0.5

* Fri Sep 03 2004 Michael Shigorin <mike@altlinux.ru> 0.4-alt1
- built for ALT Linux (synce-kde dependency)


