Group: Text tools
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif 
Name: hunspell-nl
Summary: Dutch hunspell dictionaries
Version: 2.20.19
Release: alt1_9
Source: https://github.com/OpenTaal/opentaal-hunspell/archive/2.20.19.tar.gz
URL: https://opentaal.org/
License: BSD-3-Clause OR CC-BY-3.0
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Dutch hunspell dictionaries.

%prep
%setup -q -n opentaal-hunspell-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p nl.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nl_NL.dic
cp -p nl.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nl_NL.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s nl_NL.aff $lang.aff
        ln -s nl_NL.dic $lang.dic
done


%files
%doc LICENSE.txt README.md
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 2.20.19-alt1_9
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 2.20.19-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_9
- update to new release by fcimport

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

