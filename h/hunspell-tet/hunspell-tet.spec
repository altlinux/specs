# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-tet
Summary: Tetum hunspell dictionaries
%define upstreamid 20050108
Version: 0.%{upstreamid}
Release: alt2_7
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/tet_ID.zip
Group: Text tools
URL: http://borel.slu.edu/crubadan/apps.html
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tetum hunspell dictionaries.

%prep
%setup -q -c

%build
for i in README_tet_ID.txt; do
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
cp -p tet_ID.* $RPM_BUILD_ROOT/%{_datadir}/myspell/
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
tet_ID_aliases="tet_TL"
for lang in $tet_ID_aliases; do
        ln -s tet_ID.aff $lang.aff
        ln -s tet_ID.dic $lang.dic
done
popd

%files
%doc README_tet_ID.txt
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050108-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050108-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050108-alt1_6
- import from Fedora by fcimport

