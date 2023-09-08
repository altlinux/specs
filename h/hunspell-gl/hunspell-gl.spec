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

Name: hunspell-gl
Summary: Galician hunspell dictionaries
%global upstreamid 20080515
Version: 0.%{upstreamid}
Release: alt2_29
Source: https://downloads.sourceforge.net/project/aoo-extensions/800/2/corrector_ooo3.oxt
URL: http://wiki.mancomun.org/index.php/Corrector_ortogr%%C3%%A1fico_para_OpenOffice.org#Descrici.C3.B3n
License: GPL-2.0-only
BuildArch: noarch
Source44: import.info


%description
Galician hunspell dictionaries.

%prep
%setup -q -c -n hunspell-gl


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/*.dic dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc dictionaries/README-gl-ES.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 0.20080515-alt2_29
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_16
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_13
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080515-alt1_4
- import from Fedora by fcimport

