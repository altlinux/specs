# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-bg
Summary: Bulgarian hunspell dictionaries
Version: 4.3
Release: alt2_3
Source: http://downloads.sourceforge.net/bgoffice/OOo-spell-bg-%{version}.zip
Group: Text tools
URL: http://bgoffice.sourceforge.net/
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Bulgarian hunspell dictionaries.

%prep
%setup -q -n OOo-spell-bg-%{version}

%build
for i in README.bulgarian GPL-2.0.txt MPL-1.1.txt ChangeLog Copyright LGPL-2.1.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

iconv -f WINDOWS-1251 -t UTF-8 bg_BG.dic > bg_BG.dic.new
mv -f bg_BG.dic.new bg_BG.dic
echo "SET UTF-8" > bg_BG.aff.new
tail -n +2 bg_BG.aff | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> bg_BG.aff.new
mv bg_BG.aff.new bg_BG.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.3-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_2
- import from Fedora by fcimport

