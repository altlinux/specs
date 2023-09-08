Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hr
Summary: Croatian hunspell dictionaries
%global upstreamid 20040608
Version: 0.%{upstreamid}
Release: alt2_30
#Epoch: 1
Source: http://cvs.linux.hr/spell/myspell/hr_HR.zip
URL: http://cvs.linux.hr/spell/
License: LGPL-2.1-or-later OR SISSL
BuildArch: noarch
Source44: import.info


%description
Croatian hunspell dictionaries.

%package -n hyphen-hr
Group: Text tools
Requires: libhyphen
Summary: Croatian hyphenation rules

%description -n hyphen-hr
Croatian hyphenation rules.

%prep
%setup -q -c -n hunspell-hr

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hr_HR.dic hr_HR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hr_HR.dic


%files
%doc README_hr_HR.txt
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-hr
%doc README_hr_HR.txt
%{_datadir}/hyphen/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 0.20040608-alt2_30
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_18
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt1_6
- import from Fedora by fcimport

