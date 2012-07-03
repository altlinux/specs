# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ga
Summary: Irish hunspell dictionaries
Version: 4.6
Release: alt1_2
Source0: http://gaelspell.googlecode.com/files/ispell-gaeilge-%{version}.tar.gz
Source1: myspell-header
Source2: hunspell-header
Group: Text tools
URL: http://borel.slu.edu/ispell/index.html
License: GPLv2+
BuildArch: noarch
Patch1: ispell-gaeilge-4.2-buildhunspell.patch

Requires: hunspell
Source44: import.info

%description
Irish hunspell dictionaries.

%prep
%setup -q -n ispell-gaeilge-%{version}
%patch1 -p1 -b .buildhunspell.patch

%build
make
cat %{SOURCE1} %{SOURCE2} > header
export LANG=en_IE.UTF-8
ispellaff2myspell gaeilge.aff --myheader header | sed -e "s/\"\"/0/g" | sed -e "s/\"//g" > ga_IE.aff
%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ga_IE.dic ga_IE.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README COPYING ChangeLog
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.6-alt1_2
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 4.6-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.5-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.5-alt1_2
- import from Fedora by fcimport

