# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-km
Summary: Khmer hunspell dictionaries
Version: 1.1
Release: alt2_4
Source: http://extensions.services.openoffice.org/files/2250/0/SBBIC-spellingchecker-OOo.1.1.oxt
Group: Text tools
URL: http://www.sbbic.org/
License: GPLv3
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Khmer hunspell dictionaries.

%prep
%setup -q -c -n hunspell-km

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/km_KH.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc dictionaries/CHANGELOG LICENCES-*.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_3
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- import from Fedora by fcimport

