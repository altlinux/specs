Group: Text tools
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-si
Summary: Sinhala hunspell dictionaries
Version: 0.2.1
Release: alt2_28
Source: http://www.sandaru1.com/si-LK.tar.gz
#Following URL is down since few months informed to upstream
URL: http://www.sandaru1.com/2009/08/29/sinhala-spell-checker-for-firefox/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Sinhala hunspell dictionaries.

%prep
%setup -q -c -n hunspell-si

%build
#nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/si-LK.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/si_LK.aff
cp -p dictionaries/si-LK.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/si_LK.dic

%files
%doc LICENSE README
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.2.1-alt2_28
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_8
- update to new release by fcimport

* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_7
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_5
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_3
- import from Fedora by fcimport

