# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-zu
Summary: Zulu hunspell dictionaries
%define upstreamid 20100126
Version: 0.%{upstreamid}
Release: alt2_4
Source: http://releases.mozilla.org/pub/mozilla.org/addons/46490/zulu__south_africa__dictionary-20100125-fx+tb.xpi
Group: Text tools
URL: http://www.translate.org.za/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Zulu hunspell dictionaries.

%prep
%setup -q -c

%build
for i in README-zu-ZA.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/zu-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/zu.aff
cp -p dictionaries/zu-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/zu.dic

%files
%doc README-zu-ZA.txt

%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100126-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100126-alt2_3
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100126-alt1_3
- import from Fedora by fcimport

