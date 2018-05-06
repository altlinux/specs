# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname mythes-lb
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-lb
%define upstreamid 20180412
Version: 0.%{upstreamid}.1
Release: alt1_1
Source: http://downloads.spellchecker.lu/packages/OOo3/SpellcheckerLu.oxt#/%{oldname}-%{version}.oxt
Group:  Text tools
URL: http://spellchecker.lu
License: EUPL 1.1
BuildArch: noarch
Summary: Luxembourgish thesaurus
Requires: libmythes
Requires: locales-lb
Source44: import.info

%description
Luxembourgish thesaurus.

%prep
%setup -n %{oldname}-%{version} -q -c

%build

%install
mkdir -p %{buildroot}/%{_datadir}/mythes
cp -p th_lb_LU_v2.* %{buildroot}/%{_datadir}/mythes

%files
%doc registration/README_lb_LU.txt
%{_datadir}/mythes/th_lb_LU_v2.*


%changelog
* Sun May 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.20180412.1-alt1_1
- update by mgaimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_8
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_2
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.20121128-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110821-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110821-alt1_2
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110821-alt1_1
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110709-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110412-alt1_1
- rpm Group changed to Text tools

