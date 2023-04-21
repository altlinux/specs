Group: Text tools
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-te
Summary: Telugu hunspell dictionaries
Version: 1.0.0
Release: alt1_21
#Epoch:   1
##Upstream is unresponsive so unable to verify license version
License:        GPL-1.0-or-later
URL:            https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
Source0:        http://anishpatil.fedorapeople.org/te_in.%{version}.tar.gz
BuildArch:      noarch

Requires:       hunspell
Source44: import.info

%description
Telugu hunspell dictionaries.

%prep
%setup -q -c -n te_IN


%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p te_IN/*.dic te_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files 
%doc --no-dereference te_IN/COPYING te_IN/Copyright
%doc te_IN/README
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 1.0.0-alt1_21
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_10
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_9
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_6
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_9
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050929-alt1_6
- import from Fedora by fcimport

