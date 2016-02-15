# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-hsb
Summary: Upper Sorbian hunspell dictionaries
Version: 0.20060327.3
Release: alt2_8
Source: https://addons.mozilla.org/firefox/downloads/file/113003/upper_sorbian_spelling_dictionary-0.0.20060327.3-tb+fx+sm.xpi
Group: Text tools
URL: http://sorbzilla.de/
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Upper Sorbian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-hsb

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/hsb.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/hsb_DE.aff
cp -p dictionaries/hsb.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/hsb_DE.dic

%files
%doc COPYING README
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20060327.3-alt1_1
- import from Fedora by fcimport

