# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sc
Summary: Sardinian hunspell dictionaries
%define upstreamid 20081101
Version: 0.%{upstreamid}
Release: alt2_8
Group: Text tools
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
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc registration/agpl3-en.txt
%{_datadir}/myspell/*

%changelog
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

