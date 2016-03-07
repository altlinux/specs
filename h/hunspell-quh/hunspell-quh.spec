Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-quh
Summary: Quechua, South Bolivia hunspell dictionaries
%global upstreamid 20110816
Version: 0.%{upstreamid}
Release: alt1_9
Source: http://www.runasimipi.org/quh_BO-pack.zip
URL: http://www.runasimipi.org/blanco-en.php?file=desarrollar-orto
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Quechua South Bolivia hunspell dictionaries.

%prep
%setup -q -n quh_BO-pack
unzip -qq quh_BO.zip

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p quh_BO/quh_BO.* $RPM_BUILD_ROOT/%{_datadir}/myspell/


%files
%doc README quh_BO/COPYING quh_BO/Copyright quh_BO/README_quh_BO.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_2
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20081017-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20081017-alt1_3
- import from Fedora by fcimport

