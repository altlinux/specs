# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-rw
Summary: Kinyarwanda hunspell dictionaries
%define upstreamid 20050109
Version: 0.%{upstreamid}
Release: alt2_5
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/rw_RW.zip
Group: Text tools
URL: http://borel.slu.edu/crubadan/apps.html
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Kinyarwanda hunspell dictionaries.

%prep
%setup -q -c -n hunspell-rw

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p rw_RW.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_rw_RW.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt1_4
- import from Fedora by fcimport

