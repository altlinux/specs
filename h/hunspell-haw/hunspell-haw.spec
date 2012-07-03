# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-haw
Summary: Hawaiian hunspell dictionaries
Version: 0.02
Release: alt1_1
Group: Text tools
Source: http://releases.mozilla.org/pub/mozilla.org/addons/204309/hawaiian_spell_checker-%{version}-tb+fx+sm.xpi
URL: http://borel.slu.edu/crubadan/
License: GPLv2+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Hawaiian hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/haw-US.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/haw.aff
cp -p dictionaries/haw-US.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/haw.dic

%files
%doc dictionaries/README_haw_US.txt
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_2
- update to new release by fcimport

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_1
- initial fedora import

