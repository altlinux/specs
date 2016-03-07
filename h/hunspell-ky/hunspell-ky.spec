Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ky
Summary: Kirghiz hunspell dictionaries
%global upstreamid 20090415
Version: 0.%{upstreamid}
Release: alt2_12
Source: http://ftp.gnu.org/gnu/aspell/dict/ky/aspell6-ky-0.01-0.tar.bz2
URL: http://borel.slu.edu/crubadan/
License: GPLv2+
BuildArch: noarch
BuildRequires: aspell libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Kirghiz hunspell dictionaries.

%prep
%setup -q -n aspell6-ky-0.01-0

%build
export LANG=ky_KG.utf8
preunzip -d *.cwl
cat *.wl > kirghiz.wordlist
wordlist2hunspell kirghiz.wordlist ky_KG
cp -p ky_affix.dat ky_KG.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc COPYING Copyright README doc/Crawler.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090415-alt1_4
- import from Fedora by fcimport

