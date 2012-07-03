# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-mai
Summary: Maithili hunspell dictionaries
Version: 1.0.1
Release: alt2_4
Group: Text tools
Source: http://bhashaghar.googlecode.com/files/mai_IN.oxt
URL: http://bhashaghar.googlecode.com
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Maithili hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mai

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mai_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_mai_IN.txt COPYING COPYING.MPL COPYING.GPL COPYING.LGPL

%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- import from Fedora by fcimport

