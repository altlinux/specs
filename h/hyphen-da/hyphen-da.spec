Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-da
Summary: Danish hyphenation rules
%global upstreamid 20070903
Version: 0.%{upstreamid}
Release: alt1_13
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_da_DK.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
Patch0: hyphen-da-lppl-license-fix.patch
License: LGPLv2+
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Danish hyphenation rules.

%prep
%setup -q -c -n hyphen-da
%patch0 -p1
chmod -x *

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_da_DK.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_da_DK.txt
%{_datadir}/hyphen/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_13
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_11
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20070903-alt1_4
- import by fcmass

