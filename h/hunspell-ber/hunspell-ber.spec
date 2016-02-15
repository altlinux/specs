Name: hunspell-ber
Summary: Amazigh hunspell dictionaries
%define upstreamid 20080210
Version: 0.%{upstreamid}
Release: alt2_11
Source: http://ayaspell.sourceforge.net/data/hunspell-am_test.tar.gz
Group: Text tools
URL: http://ayaspell.sourceforge.net/am.html
License: GPL+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Amazigh hunspell dictionaries.

%prep
%setup -q -n spelling_tifinagh

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p tifinagh.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ber_MA.dic
cp -p tifinagh.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ber_MA.aff

%files
%doc README
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080210-alt1_4
- import from Fedora by fcimport

