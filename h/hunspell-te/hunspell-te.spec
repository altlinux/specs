Name: hunspell-te
Summary: Telugu hunspell dictionaries
Version: 1.0.0
Release: alt1_4
#Epoch:   1
Group:          Text tools
##Upstream is unresponsive so unable to verify license version
License:        GPL+
URL:            https://gitorious.org/hunspell_dictionaries
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p te_IN/*.dic te_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files 
%doc te_IN/COPYING te_IN/Copyright te_IN/README 
%{_datadir}/myspell/*

%changelog
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

