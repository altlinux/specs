# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ts
Summary: Tsonga hunspell dictionaries
%define upstreamid 20091101
Version: 0.%{upstreamid}
Release: alt2_3
Source: http://releases.mozilla.org/pub/mozilla.org/addons/46611/tsonga__south_africa__dictionary-%{upstreamid}-fx+tb.xpi
Group: Text tools
URL: http://www.translate.org.za/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tsonga hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ts

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ts-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ts_ZA.aff
cp -p dictionaries/ts-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ts_ZA.dic

%files
%doc README-ts-ZA.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt1_2
- import from Fedora by fcimport

