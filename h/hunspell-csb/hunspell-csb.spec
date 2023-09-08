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

Name: hunspell-csb
Summary: Kashubian hunspell dictionaries
# We are using here upstreamid date as upstream published source archive date
%global upstreamid 20190319
Version: 0.%{upstreamid}
Release: alt1_2
Source: https://addons.thunderbird.net/firefox/downloads/latest/kashubian-spell-checker-poland/addon-222511-latest.xpi
URL: https://addons.thunderbird.net/en-us/firefox/addon/kashubian-spell-checker-poland/
License: GPL-2.0-only
BuildArch: noarch
Source44: import.info


%description
Kashubian hunspell dictionaries.

%prep
%setup -q -c -n %{name}-%{version}


%build
# nothing here to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/Kaszebsczi.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/csb_PL.dic
cp -p dictionaries/Kaszebsczi.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/csb_PL.aff


%files
%doc dictionaries/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 0.20190319-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_9
- update to new release by fcimport

* Wed Nov 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050311-alt1_5
- import from Fedora by fcimport

