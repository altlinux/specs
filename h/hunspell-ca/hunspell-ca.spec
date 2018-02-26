# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ca
Summary: Catalan hunspell dictionaries
Version: 2.3
Release: alt1_1
Source: http://www.softcatala.org/diccionaris/actualitzacions/OOo/catalan.oxt
Group: Text tools
URL: http://www.softcatala.org/wiki/Projectes/Corrector_ortogràfic
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Catalan hunspell dictionaries.

%prep
%setup -q -c

%build
tr -d '\r' < dictionaries/catalan.aff > ca_ES.aff
touch -r dictionaries/catalan.aff ca_ES.aff
tr -d '\r' < dictionaries/catalan.dic > ca_ES.dic
touch -r dictionaries/catalan.dic ca_ES.dic

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ca_ES.dic ca_ES.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s ca_ES.aff $lang.aff
        ln -s ca_ES.dic $lang.dic
done
popd

%files
%doc LICENSES-en.txt LLICENCIES-ca.txt       
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_2
- import from Fedora by fcimport

