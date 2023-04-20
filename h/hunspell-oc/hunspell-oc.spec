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
Name: hunspell-oc
Summary: Occitan hunspell dictionaries
Version: 0.6.2
Release: alt1_14
Source: https://addons.mozilla.org/firefox/downloads/file/233710/correcteur_occitan_languedocien-%{version}-tb+sm+fx.xpi
URL: https://addons.mozilla.org/en-US/firefox/addon/8235
License: GPL-3.0-or-later
BuildArch: noarch
BuildRequires: libredland

Requires: hunspell
Source44: import.info

%description
Occitan hunspell dictionaries.

%prep
%setup -q -c -n hunspell-oc


%build
rdfproc -s file hunspell-oc parse install.rdf
rdfproc -s file hunspell-oc print | grep install-manifest | grep -v targetApplication | sed -e 's/.*#//' | sed -e 's/], "/: /'| sed -e 's/"}//' > CREDITS

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/oc-FR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/oc_FR.aff
cp -p dictionaries/oc-FR.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/oc_FR.dic


%files
%doc CREDITS
%{_datadir}/%{dict_dirname}/*

%changelog
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

