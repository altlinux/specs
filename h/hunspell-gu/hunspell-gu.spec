# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-gu
Summary: Gujarati hunspell dictionaries
Version: 20061015 
Release: alt2_7
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/gu_IN.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Gujarati hunspell dictionaries.

%prep
%setup -q -c -n gu-IN

%build
chmod -x *.dic *.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_gu_IN.txt
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_6
- update to new release by fcimport

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20061015-alt1_4
- import from Fedora by fcimport

