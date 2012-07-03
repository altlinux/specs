# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-shs
Summary: Shuswap hunspell dictionaries
%define upstreamid 20090828
Version: 0.%{upstreamid}
Release: alt2_3
Group: Text tools
Source: http://secpewt.sd73.bc.ca/hunspell/hunspell-shs-ca.tar.gz
URL: http://secpewt.sd73.bc.ca/wordlist
License: GPLv2+
BuildArch: noarch
BuildRequires: libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Shuswap hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hunspell/shs_CA.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc hunspell/COPYING hunspell/Copyright hunspell/README
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20090828-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090828-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090828-alt1_2
- import from Fedora by fcimport

