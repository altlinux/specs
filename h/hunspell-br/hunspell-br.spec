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

Name: hunspell-br
Summary: Breton hunspell dictionaries
#Epoch: 1
Version: 0.15
Release: alt1_14
URL: http://www.drouizig.org/
Source: https://downloads.sourceforge.net/project/aoo-extensions/2207/7/dict-br-0.15.oxt
License: LGPL-2.1-or-later
BuildArch: noarch
Source44: import.info


%description
Breton hunspell dictionaries.

%prep
%setup -q -c -n hunspell-br-%{version}


%build
chmod -x dictionaries/*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/br_FR.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc package-description.txt
%doc --no-dereference LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 0.15-alt1_14
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_2
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_12
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- import from Fedora by fcimport

