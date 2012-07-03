# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ti
Summary: Tigrigna hunspell dictionaries
%define upstreamid 20090911
Version: 0.%{upstreamid}
Release: alt2_3
Source: http://www.cs.ru.nl/~biniam/geez/dict/ti_ER.zip
Group: Text tools
URL: http://www.cs.ru.nl/~biniam/geez/index.php
License: GPL+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tigrigna hunspell dictionaries.

%prep
%setup -q -c

%build
tr -d '\r' < README.txt > README.txt.new
touch -r README.txt README.txt.new
mv -f README.txt.new README.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ti_ER.* $RPM_BUILD_ROOT/%{_datadir}/myspell/
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ti_ER_aliases="ti_ET"
for lang in $ti_ER_aliases; do
        ln -s ti_ER.aff $lang.aff
        ln -s ti_ER.dic $lang.dic
done

%files
%doc README.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20090911-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090911-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090911-alt1_2
- import from Fedora by fcimport

