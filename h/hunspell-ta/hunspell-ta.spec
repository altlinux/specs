Name: hunspell-ta
Summary: Tamil hunspell dictionaries
Version: 20100226
Release: alt2_4
Source: http://tamil.nrcfoss.au-kbc.org.in/files/hunspell/ta_IN-hunspell-Wordlist.tar.gz
Group: Text tools
URL: http://nrcfoss.au-kbc.org.in
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tamil hunspell dictionaries.

%prep
%setup -q -c -n ta_IN-hunspell-wordlist

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell

cp -p ta_IN-hunspell-wordlist/*.dic ta_IN-hunspell-wordlist/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc ta_IN-hunspell-wordlist/README ta_IN-hunspell-wordlist/LICENSE ta_IN-hunspell-wordlist/Copyright
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20100226-alt1_2
- import from Fedora by fcimport

