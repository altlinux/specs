# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-mos
Summary: Mossi hunspell dictionaries
%define upstreamid 20101130
Version: 0.%{upstreamid}
Release: alt2_3
Group: Text tools
Source: http://www.abcburkina.net/ancien/documents/lingu/DicoMoore.zip
URL: http://www.abcburkina.net/content/view/377/48/lang,fr
License: LGPLv3
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Mossi hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mos_BF.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc lgpl-3.0.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20101130-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20101130-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20101130-alt1_2
- import from Fedora by fcimport

