Group: Text tools
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 2

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name:         hunspell-it
Summary:      Italian hunspell dictionaries
Version:      5.1.1
Release:      alt1_2
# The license text is embedded within the README files
# Here we specify the hunspell files license only as other files are not packaged 
License:      GPL-3.0-only
URL:          https://pagure.io/dizionario_italiano
Source:       https://pagure.io/dizionario_italiano/archive/%{version}/dizionario_italiano-%{version}.tar.gz

BuildArch:    noarch
Source44: import.info

%description
Italian hunspell dictionaries.


%prep
%setup -q -n dizionario_italiano-%{version}



%build
# Nothing to do


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p it_IT.dic it_IT.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s it_IT.aff $lang.aff
        ln -s it_IT.dic $lang.dic
done



%files
%doc --no-dereference LICENSES/gpl-3.0.txt
%doc CHANGELOG.txt README.md README_it_IT.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.16.20070901
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.15.20070901
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.14.20070901
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.13.20070901
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.12.20070901
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.11.20070901
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.10.20070901
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.9.20070901
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.8.20070901
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.7.20070901
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.6.20070901
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_0.6.20070901
- import from Fedora by fcimport

