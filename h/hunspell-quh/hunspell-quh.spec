# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-quh
Summary: Quechua, South Bolivia hunspell dictionaries
%define upstreamid 20110816
Version: 0.%{upstreamid}
Release: alt1_2
Source: http://www.runasimipi.org/quh_BO-pack.zip
Group: Text tools
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
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_2
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110816-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20081017-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20081017-alt1_3
- import from Fedora by fcimport

