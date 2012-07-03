# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-af
Summary: Afrikaans hunspell dictionary
%define upstreamid 20080825
Version: 0.%{upstreamid}
Release: alt2_5
Source: http://downloads.translate.org.za/spellchecker/afrikaans/myspell-af_ZA-0.%{upstreamid}.zip
Group: Text tools
URL: http://www.translate.org.za/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Afrikaans hunspell dictionary

%prep
%setup -q -c -n hunspell-af_ZA

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
af_ZA_aliases="af_NA"
for lang in $af_ZA_aliases; do
        ln -s af_ZA.aff $lang.aff
        ln -s af_ZA.dic $lang.dic
done
popd

%files
%doc README_af_ZA.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080825-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080825-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080825-alt1_4
- import from Fedora by fcimport

