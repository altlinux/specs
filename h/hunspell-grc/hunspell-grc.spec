# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-grc
Summary: Ancient Greek hunspell dictionaries
Version: 2.1.5
Release: alt2_4
Group: Text tools
Source: http://extensions.services.openoffice.org/e-files/2313/1/grc.oxt
URL: http://www.himeros.eu/
License: GPL+ or LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Ancient Greek hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/grc_GR.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/grc.aff
cp -p dictionaries/grc_GR.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/grf.dic

%files
%doc LICENSES-en.txt         

%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt1_2
- import from Fedora by fcimport

