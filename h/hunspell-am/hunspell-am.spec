# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-am
Summary: Amharic hunspell dictionaries
%define upstreamid 20090704
Version: 0.%{upstreamid}
Release: alt2_4
Source: http://www.cs.ru.nl/~biniam/geez/dict/am_ET.zip
Group: Text tools
URL: http://www.cs.ru.nl/~biniam/geez/index.php
License: GPL+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Amharic hunspell dictionaries.

%prep
%setup -q -n am_ET

%build
tr -d '\r' < README.txt > README.txt.new
touch -r README.txt README.txt.new
mv -f README.txt.new README.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p am_ET.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20090704-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090704-alt2_3
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20090704-alt1_3
- import from Fedora by fcimport

