# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-id
Summary: Indonesian hunspell dictionaries
%define upstreamid 20040812
Version: 0.%{upstreamid}
Release: alt2_11
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/id_ID.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries#Indonesian_.28Indonesia.29
License: GPLv2
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Indonesian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-id

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_id_ID.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040812-alt1_4
- import from Fedora by fcimport

