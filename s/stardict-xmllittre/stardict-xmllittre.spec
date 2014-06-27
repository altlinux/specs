Name:     stardict-xmllittre
Summary:  Authoritative 19th century French dictionary
Version:  1.0
Release:  alt1_8
Group:    File tools
License:  GPLv3
URL: http://francois.gannaz.free.fr/Littre/horsligne.php
Source0: http://francois.gannaz.free.fr/Littre/dlds/XMLittre_stardict_1.0.tar
BuildArchitectures: noarch
Requires: stardict >= 3.0.1
Source44: import.info


%description
"Le LittrA." is a well-known, authoritative 19th century French dictionary.
This package contains the original edition dictionary in StarDict format.


%prep
%setup -q -n XMLittre


%build


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p          ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/xmllittre
cp -rf XMLittre.* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/xmllittre
mv README README.western
iconv -f iso8859-1 -t utf-8 README.western > README


%files
%{_datadir}/stardict/dic/*
%doc README


%changelog
* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- initial fc import

