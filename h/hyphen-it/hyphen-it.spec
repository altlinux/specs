Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 3

Name:           hyphen-it
Summary:        Italian hyphenation rules
Version:        5.1.1
Release:        alt1_3
# The license text is embedded within the README files
# Here we specify the thesaurus license only as other files are not packaged 
License:        LGPL-2.1-only
URL:            https://pagure.io/dizionario_italiano
Source:         https://pagure.io/dizionario_italiano/archive/%{version}/dizionario_italiano-%{version}.tar.gz

BuildArch:      noarch
Requires:       libhyphen
Provides:       hyphen-la = %{version}
Source44: import.info

%description
Italian hyphenation rules.


%prep
%setup -q -n dizionario_italiano-%{version}



%build
# Nothing to do


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_it_IT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
#http://extensions.services.openoffice.org/project/dict-la uses the it_IT for Latin
#so we'll do the same
it_IT_aliases="it_CH la_VA"
for lang in $it_IT_aliases; do
        ln -s hyph_it_IT.dic "hyph_"$lang".dic"
done


%files
%doc --no-dereference LICENSES/lgpl-2.1.txt
%doc CHANGELOG.txt README.md README_hyph_it_IT.txt
%{_datadir}/hyphen/hyph_it_IT.dic
%{_datadir}/hyphen/hyph_it_CH.dic
%{_datadir}/hyphen/hyph_la_VA.dic


%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_3
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.20071127-alt1_29
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_18
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_14
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_6
- import by fcmass

