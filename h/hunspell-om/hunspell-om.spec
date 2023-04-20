Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-om
Summary: Oromo hunspell dictionaries
#Epoch: 1
Version: 0.04
Release: alt2_27
# Following links are dead now
# Please don't report any bugs for it
Source: http://borel.slu.edu/obair/%{name}-%{version}.oxt
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-3.0-or-later
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Oromo hunspell dictionaries.

%prep
%setup -q -c


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/om_ET.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
om_ET_aliases="om_KE"
for lang in $om_ET_aliases; do
        ln -s om_ET.aff $lang.aff
        ln -s om_ET.dic $lang.dic
done


%files
%doc dictionaries/README_om_ET.txt
%doc --no-dereference LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.04-alt2_27
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_16
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_15
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- import from Fedora by fcimport

