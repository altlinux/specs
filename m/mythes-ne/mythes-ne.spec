# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: mythes-ne
Summary: Nepali thesaurus
Version: 1.1
Release: alt1_9
Source0: http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/dictionaries/ne_NP/th_ne_NP_v2.zip
Source1: http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/dictionaries/ne_NP/README_th_ne_NP_v2.txt
Group: Text tools
URL: http://data.opentaal.org/opentaalbank/thesaurus
License: LGPLv2
BuildArch: noarch
BuildRequires: libmythes-devel
Requires: libmythes
Source44: import.info

%description
Nepali thesaurus.

%prep
%setup -q -c
cp -p %{SOURCE1} README_th_ne_NP_v2.txt

%build
th_gen_idx.pl < th_ne_NP_v2.dat > th_ne_NP_v2.idx

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ne_NP_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes/

%files
%doc README_th_ne_NP_v2.txt
%{_datadir}/mythes/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- import by fcmass

