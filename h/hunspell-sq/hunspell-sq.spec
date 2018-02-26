# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sq
Summary: Albanian hunspell dictionaries
Version: 1.6.4
Release: alt1_2
Source: http://www.shkenca.org/shkarkime/myspell-sq_AL-%{version}.zip
Group: Text tools
URL: http://www.shkenca.org/k6i/albanian_dictionary_for_myspell_en.html
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Albanian hunspell dictionaries.

%prep
%setup -q -n myspell-sq_AL-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p sq_AL.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README.txt Copyright
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_2
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2
- import from Fedora by fcimport

