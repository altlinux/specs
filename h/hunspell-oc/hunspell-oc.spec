Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define fedora 38
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-oc
Summary: Occitan hunspell dictionaries
Version: 1.5
Release: alt1_1
Source: https://addons.mozilla.org/firefox/downloads/file/4085695/diccionari_occitan_lengadocian-%{version}.xpi
URL: https://addons.mozilla.org/en-US/firefox/addon/diccionari-occitan-lengadocian/
# https://www.mozilla.org/en-US/MPL/2.0/combining-mpl-and-gpl/
# oc_FR.aff is MPL-2.0
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Occitan hunspell dictionaries.

%prep
%setup -q -c -n hunspell-oc


%build
# nothing here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/oc_FR.aff dictionaries/oc_FR.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.5-alt1_1
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.6.2-alt1_14
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_13
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_8
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4
- import from Fedora by fcimport

