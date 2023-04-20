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
Name: hunspell-qu
Summary: Quechua Ecuador hunspell dictionaries
Version: 0.9
Release: alt2_25
# Following links is dead now
Source: http://extensions.services.openoffice.org/e-files/2121/8/qu_EC-0.9.oxt
URL: http://extensions.services.openoffice.org/project/KichwaSpellchecker
License: AGPL-3.0-only
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Quechua Ecuador hunspell dictionaries.

%prep
%setup -q -c


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p qu_EC.aff qu_EC.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc CURRENTVERSION.txt README.txt REVISION.txt
%doc --no-dereference LICENSE.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.9-alt2_25
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_1
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1
- import from Fedora by fcimport

