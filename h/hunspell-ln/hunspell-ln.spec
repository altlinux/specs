# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ln
Summary: Lingala hunspell dictionaries
Version: 0.02
Release: alt2_4
Group: Text tools
Source: http://downloads.sourceforge.net/lingala/hunspell-ln-0.02.zip
URL: http://lingala.sourceforge.net/
License: GPLv2+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Lingala hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ln_CD.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_ln_CD.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- import from Fedora by fcimport

