# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-tk
Summary: Turkmen hunspell dictionaries
Version: 0.02
#Epoch: 1
Release: alt1_1
Source: http://releases.mozilla.org/pub/mozilla.org/addons/204314/turkmen_spell_checker-%{version}-tb+fx+sm.xpi
Group: Text tools
URL: http://borel.slu.edu/crubadan/apps.html
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Turkmen hunspell dictionaries.

%prep
%setup -q -c -n hunspell-tk

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/tk-TM.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/tk.aff
cp -p dictionaries/tk-TM.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/tk.dic

%files
%doc dictionaries/README_tk_TM.txt
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_2
- import from Fedora by fcimport

