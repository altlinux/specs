# BEGIN SourceDeps(oneline):
BuildRequires: libacl-devel libattr-devel
# END SourceDeps(oneline)
%define rhelp_version 0.3.0

Name:           dd_rescue
Version:        1.42.1
Release:        alt2_3
Summary:        Fault tolerant "dd" utility for rescuing data from bad media
Group:          File tools
# No version specified
License:        GPL+
URL:            http://www.garloff.de/kurt/linux/ddrescue/
Source0:        http://www.garloff.de/kurt/linux/ddrescue/dd_rescue-%{version}.tar.gz
Source1:        http://www.kalysto.org/pkg/dd_rhelp-%{rhelp_version}.tar.gz
BuildRequires:  autoconf
Source44: import.info

%description
ddrescue is a utility similar to the system utility "dd" which copies
data from a file or block device to another. ddrescue does however
not abort on errors in the input file. This makes it suitable for
rescuing data from media with errors, e.g. a disk with bad sectors.

This package includes dd_rhelp, a wrapper script facilitating data 
recovery.

%prep
%setup -q -n %{name}
%setup -q -n %{name} -a 1 -D -T

%build
make RPM_OPT_FLAGS="%{optflags}" %{?_smp_mflags} LIBDIR=%{_libdir}
cp -p README.dd_rescue README
cp -p dd_rhelp-%{rhelp_version}/README README.dd_rhelp
cp -p dd_rhelp-%{rhelp_version}/FAQ FAQ.dd_rhelp

%install
make install DESTDIR=%{buildroot} INSTALLDIR=%{buildroot}/%{_bindir} INSTASROOT="" INSTALLFLAGS="" LIBDIR=%{_libdir}
install -D -m 755 dd_rhelp-%{rhelp_version}/dd_rhelp %{buildroot}%{_bindir}/dd_rhelp

%files
%doc COPYING README README.dd_rhelp FAQ.dd_rhelp
%{_bindir}/dd_rescue
%{_bindir}/dd_rhelp
%{_mandir}/man1/%{name}.*
%{_libdir}/libddr_MD5.so

%changelog
* Wed Apr 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.42.1-alt2_3
- moved to sisyphus for rescue iso

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.42.1-alt1_3
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_2
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_1
- update to new release by fcimport

* Fri Feb 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1_1
- update to new release by fcimport

* Fri Dec 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_2
- converted for ALT Linux by srpmconvert tools

