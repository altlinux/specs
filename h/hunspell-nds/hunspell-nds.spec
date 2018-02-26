# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-nds
Summary: Lowlands Saxon hunspell dictionaries
Version: 0.1
Release: alt2_5
Source: http://downloads.sourceforge.net/aspell-nds/hunspell-nds-0.1.zip
Group: Text tools
URL: http://aspell-nds.sourceforge.net/
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Lowlands Saxon hunspell dictionaries.

%prep
%setup -q -n hunspell-nds

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p nds.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/nds_DE.aff
cp -p nds.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/nds_DE.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
nds_DE_aliases="nds_NL"
for lang in $nds_DE_aliases; do
        ln -s nds_DE.aff $lang.aff
        ln -s nds_DE.dic $lang.dic
done
popd

%files
%doc README_nds.txt Copyright COPYING
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_4
- import from Fedora by fcimport

