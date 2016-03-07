Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sc
Summary: Sardinian hunspell dictionaries
%global upstreamid 20081101
Version: 0.%{upstreamid}
Release: alt2_15
Source: http://extensions.services.openoffice.org/files/1446/2/Dict_sc_IT03.oxt
URL: http://extensions.services.openoffice.org/project/Dict_sc
#The license included is AGPLv3 and pkg-desc/pkg-description.txt
#says AGPLv3 or later, but the sc_IT.aff header states "GPLv2"
License: AGPLv3+ and GPLv2
BuildArch: noarch
BuildRequires: libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Sardinian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sc

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p sc_IT.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sc_IT.aff
cp -p sc_it.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sc_IT.dic


%files
%doc registration/agpl3-en.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_10
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_9
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20081101-alt1_5
- import from Fedora by fcimport

