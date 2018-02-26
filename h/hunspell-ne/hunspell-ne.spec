# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ne
Summary: Nepali hunspell dictionaries
Version: 20080425
Release: alt2_4
Source: http://nepalinux.org/downloads/ne_NP_dict.zip
Group: Text tools
URL: http://nepalinux.org/downloads
License: LGPLv2
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Nepali hunspell dictionaries.

%prep
%setup -q -c -n ne_NP_dict

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ne_NP_aliases="ne_IN"
for lang in $ne_NP_aliases; do
        ln -s ne_NP.aff $lang.aff
        ln -s ne_NP.dic $lang.dic
done
popd

%files
%doc README_ne_NP.txt 
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20080425-alt1_2
- import from Fedora by fcimport

