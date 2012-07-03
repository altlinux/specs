# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ko
Summary: Korean hunspell dictionaries
Version: 0.5.5
Release: alt1_2
Source: http://spellcheck-ko.googlecode.com/files/hunspell-dict-ko-%{version}.tar.gz
Group: Text tools
URL: http://code.google.com/p/spellcheck-ko/
License: MPLv1.1 or GPLv2 or LGPLv2
BuildArch: noarch
BuildRequires: python-module-lxml hunspell
Requires: hunspell
Source44: import.info

%description
Korean hunspell dictionaries.

%prep
%setup -q -n hunspell-dict-ko-%{version}

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ko.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.aff
cp -p ko.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.dic

%check
make test

%files
%doc README LICENSE LICENSE.GPL LICENSE.LGPL LICENSE.MPL
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_1
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_1
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_1
- import from Fedora by fcimport

