# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sl
Summary: Slovenian hunspell dictionaries
%define upstreamid 20070127
Version: 0.%{upstreamid}
Release: alt2_6
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/sl_SI.zip
Group: Text tools
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Slovenian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sl

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_sl_SI.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20070127-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20070127-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20070127-alt1_5
- import from Fedora by fcimport

