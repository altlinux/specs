# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-ca
Summary: Catalan hyphenation rules
#Epoch: 1
Version: 0.9.3
Release: alt1_3
Source: http://extensions.services.openoffice.org/e-files/2010/7/hyph-ca.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/project/ca_hyph
License: GPLv3
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Catalan hyphenation rules.

%prep
%setup -q -c

%build
for i in release-note_en.txt release-note_ca.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ca_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_ca_ES.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s hyph_ca_ES.dic hyph_$lang.dic
done
popd

%files
%doc release-note_en.txt release-note_ca.txt LICENSES-en.txt LLICENCIES-ca.txt
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_2
- import by fcmass

