# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-pl
Summary: Polish hyphenation rules
%define upstreamid 20060726
Version: 0.%{upstreamid}
Release: alt1_6
Source: http://pl.openoffice.org/pliki/hyph_pl_PL.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Polish hyphenation rules.

%prep
%setup -q -c -n hyphen-pl

%build
unzip hyph_pl_PL.zip
for i in README_hyph_pl_PL.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_pl_PL.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README_hyph_pl_PL.txt
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_5
- import by fcmass

