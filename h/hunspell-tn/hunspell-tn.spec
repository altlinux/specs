Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-tn
Summary: Tswana hunspell dictionaries
%global upstreamid 20150904
Version: 0.%{upstreamid}
Release: alt1_14
Source: https://addons.mozilla.org/firefox/downloads/file/347396/tswana_spell_checker-%{upstreamid}-sm+tb+fx+an+fn.xpi
URL: https://addons.mozilla.org/en-US/firefox/addon/tswana-spell-checker/
License: GPL-3.0-or-later
BuildArch: noarch
Source44: import.info


%description
Tswana hunspell dictionaries.

%prep
%setup -q -c -n hunspell-tn


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/tn-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/tn_ZA.aff
cp -p dictionaries/tn-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/tn_ZA.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
tn_ZA_aliases="tn_BW"
for lang in $tn_ZA_aliases; do
        ln -s tn_ZA.aff $lang.aff
        ln -s tn_ZA.dic $lang.dic
done
popd


%files
%doc dictionaries/README_tn_ZA.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 0.20150904-alt1_14
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.20150904-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt1_2
- import from Fedora by fcimport

