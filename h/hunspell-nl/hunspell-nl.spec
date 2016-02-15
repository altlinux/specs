# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-nl
Summary: Dutch hunspell dictionaries
Version: 2.10
Release: alt1_8
#http://www.opentaal.org/bestanden/doc_download/20-woordenlijst-v-210g-voor-openofficeorg-3
#annoying click through makes direct link apparently impossible
Source: OpenTaal-210G-LO.oxt
Group: Text tools
URL: http://www.opentaal.org/english.php
License: BSD or CC-BY
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Dutch hunspell dictionaries.

%prep
%setup -q -c

%build
chmod -x nl_NL.*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p nl_NL.aff nl_NL.dic $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s nl_NL.aff $lang.aff
        ln -s nl_NL.dic $lang.dic
done

%files
%doc description/desc_en_US.txt description/desc_nl_NL.txt README_nl_NL.txt license_en_EN.txt licentie_nl_NL.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_1
- update to new release by fcimport

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_3
- import from Fedora by fcimport

