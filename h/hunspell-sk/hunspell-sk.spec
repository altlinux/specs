Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sk
Summary: Slovak hunspell dictionaries
#Epoch: 1
%global upstreamid 20110228
Version: 0.%{upstreamid}
Release: alt2_9
Source: http://www.sk-spell.sk.cx/files/hunspell-sk-%{upstreamid}.zip
URL: http://www.sk-spell.sk.cx/
License: LGPLv2 or GPLv2 or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Slovak hunspell dictionaries.

%prep
%setup -q -n %{name}-%{upstreamid}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc doc/*
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt2_1
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110228-alt1_1
- import from Fedora by fcimport

