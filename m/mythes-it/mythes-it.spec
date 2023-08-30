Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 2

Name:         mythes-it
Summary:      Italian thesaurus
Version:      5.1.1
Release:      alt1_2
# The license text is embedded within the README files
# Here we specify the thesaurus license only as other files are not packaged 
License:      GPL-3.0-only
URL:          https://pagure.io/dizionario_italiano
Source:       https://pagure.io/dizionario_italiano/archive/%{version}/dizionario_italiano-%{version}.tar.gz

BuildArch:    noarch
Requires:     libmythes
Source44: import.info

%description
Italian thesaurus.


%prep
%setup -q -n dizionario_italiano-%{version}



%build
# Nothing to do


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_it_IT_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.dat
cp -p th_it_IT_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s th_it_IT_v2.dat "th_"$lang"_v2.dat"
        ln -s th_it_IT_v2.idx "th_"$lang"_v2.idx"
done


%files
%doc --no-dereference LICENSES/gpl-3.0.txt
%doc CHANGELOG.txt README.md README_th_it_IT.txt
%{_datadir}/mythes/th_it_IT_v2.*
%{_datadir}/mythes/th_it_CH_v2.*

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_2
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 2.0.9l-alt1_29
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_18
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.9l-alt1_6
- import by fcmass

