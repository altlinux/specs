# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-tl
Summary: Tagalog hunspell dictionaries
%define upstreamid 20050109
Version: 0.%{upstreamid}
Release: alt2_6
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/tl_PH.zip
Group: Text tools
URL: http://borel.slu.edu/crubadan/apps.html
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tagalog hunspell dictionaries.

%prep
%setup -q -c -n hunspell-tl

%build
for i in README_tl_PH.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p tl_PH.* $RPM_BUILD_ROOT/%{_datadir}/myspell/
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
tl_PH_aliases="fil_PH"
for lang in $tl_PH_aliases; do
        ln -s tl_PH.aff $lang.aff
        ln -s tl_PH.dic $lang.dic
done
popd

%files
%doc README_tl_PH.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050109-alt1_5
- import from Fedora by fcimport

