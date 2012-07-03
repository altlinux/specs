# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ia
Summary: Interlingua hunspell dictionaries
%define upstreamid 20050226
Version: 0.%{upstreamid}
Release: alt2_6
Group: Text tools
Source: http://download.savannah.gnu.org/releases/interlingua/ia_myspell.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries#Interlingua_.28x-register.29
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Interlingua hunspell dictionaries.

%prep
%setup -q -c

%build
tr -d '\r' < README_ia.txt > README_ia.txt.new
touch -r README_ia.txt README_ia.txt.new
mv -f README_ia.txt.new README_ia.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ia.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_ia.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt1_5
- import from Fedora by fcimport

