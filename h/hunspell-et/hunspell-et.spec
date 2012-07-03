# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-et
Summary: Estonian hunspell dictionaries
%define upstreamid 20030606
Version: 0.%{upstreamid}
Release: alt2_8
Source: http://www.meso.ee/~jjpp/speller/ispell-et_%{upstreamid}.tar.gz
Group: Text tools
URL: http://www.meso.ee/~jjpp/speller/
License: LGPLv2+ and LPPL
BuildArch: noarch

Requires: hunspell
Provides: hunspell-ee = 0.20030606-4
Obsoletes: hunspell-ee < 0.20030606-4
Source44: import.info

%description
Estonian hunspell dictionaries.

%package -n hyphen-et
Requires: libhyphen
Summary: Estonian hyphenation rules
Group: Text tools

%description -n hyphen-et
Estonian hyphenation rules.

%prep
%setup -q -n ispell-et-%{upstreamid}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p latin-1/et_EE.* $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_et.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_et_EE.dic

%files
%doc README COPYRIGHT ChangeLog
%{_datadir}/myspell/*

%files -n hyphen-et
%doc README COPYRIGHT ChangeLog
%{_datadir}/hyphen/*


%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20030606-alt2_8
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20030606-alt2_7
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20030606-alt1_7
- import from Fedora by fcimport

