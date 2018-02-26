# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-hr
Summary: Croatian hunspell dictionaries
%define upstreamid 20040608
Version: 0.%{upstreamid}
Release: alt2_7
#Epoch: 1
Source: http://cvs.linux.hr/spell/myspell/hr_HR.zip
Group: Text tools
URL: http://cvs.linux.hr/spell/
License: LGPLv2+ or SISSL
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Croatian hunspell dictionaries.

%package -n hyphen-hr
Requires: libhyphen
Summary: Croatian hyphenation rules
Group: Text tools

%description -n hyphen-hr
Croatian hyphenation rules.

%prep
%setup -q -c -n hunspell-hr

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hr_HR.dic hr_HR.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hr_HR.dic

%files
%doc README_hr_HR.txt
%{_datadir}/myspell/*

%files -n hyphen-hr
%doc README_hr_HR.txt
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040608-alt1_6
- import from Fedora by fcimport

