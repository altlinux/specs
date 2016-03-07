Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ms
Summary: Malay hunspell dictionaries
%global upstreamid 20050117
Version: 0.%{upstreamid}
Release: alt2_13
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/ms_MY.zip
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
License: GFDL and GPL+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Malay hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ms

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ms_MY_aliases="ms_BN"
for lang in $ms_MY_aliases; do
        ln -s ms_MY.aff $lang.aff
        ln -s ms_MY.dic $lang.dic
done


%files
%doc README_ms_MY.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050117-alt1_5
- import from Fedora by fcimport

