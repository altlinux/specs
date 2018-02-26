# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-dsb
Summary: Lower Sorbian hunspell dictionaries
Version: 1.4.6
Release: alt1_1
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/3045/12/lower_sorbian_spelling_dictionary-1.4.6.oxt
URL: http://dsb-spell.sourceforge.net
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Lower Sorbian hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dsb_DE.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc description/desc_de.txt description/desc_en.txt description/desc_pl.txt registration/license_en.txt  

%{_datadir}/myspell/*

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.5-alt1_2
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.5-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_2
- import from Fedora by fcimport

