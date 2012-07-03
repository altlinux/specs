# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ht
Summary: Haitian Creole hunspell dictionaries
Version: 0.06
Release: alt2_3
Group: Text tools
Source: http://extensions.services.openoffice.org/files/3247/3/%{name}-%{version}.oxt
URL: http://kok.logipam.org/
License: GPLv3+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Haitian Creole hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ht_HT.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc dictionaries/README_ht_HT.txt LICENSES-en.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- import from Fedora by fcimport

