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
Name: hunspell-sq
Summary: Albanian hunspell dictionaries
Version: 1.6.4
Release: alt1_24
Source: http://www.shkenca.org/shkarkime/myspell-sq_AL-%{version}.zip
URL: http://www.shkenca.org/k6i/albanian_dictionary_for_myspell_en.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Albanian hunspell dictionaries.

%prep
%setup -q -n myspell-sq_AL-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p sq_AL.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc README.txt Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 1.6.4-alt1_24
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_2
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2
- import from Fedora by fcimport

