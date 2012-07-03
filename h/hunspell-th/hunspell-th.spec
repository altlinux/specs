# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-th
Summary: Thai hunspell dictionaries
%define upstreamid 20061212
Version: 0.%{upstreamid}
Release: alt2_7
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/th_TH.zip
Group: Text tools
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Thai hunspell dictionaries.

%prep
%setup -q -c -n hunspell-th

%build
#set encoding to IANA prefered name
sed -i -e 's/TIS620-2533/TIS620/g' th_TH.aff
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_th_TH.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20061212-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20061212-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20061212-alt1_6
- import from Fedora by fcimport

