Group: Text tools
Name: hunspell-mt
Summary: Maltese hunspell dictionaries
%global upstreamid 20020708
Version: 0.%{upstreamid}
Release: alt2_13
Source: http://linux.org.mt/downloads/spellcheck-mt-0.3.tar.gz
URL: http://linux.org.mt/node/62
License: LGPLv2+
BuildArch: noarch
BuildRequires: libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Maltese hunspell dictionaries.

%prep
%setup -q -c

%build
export LANG=mt_MT.utf8
iconv -f ISO-8859-3 -t UTF-8 words.iso8859-3 > maltese.words
wordlist2hunspell maltese.words mt_MT

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mt_MT.dic mt_MT.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc readme.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20020708-alt1_5
- import from Fedora by fcimport

