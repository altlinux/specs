# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-fo
Summary: Faroese hyphenation rules
%define upstreamid 20040420
Version: 0.%{upstreamid}
Release: alt1_3
Source: http://fo.speling.org/filer/hyph_fo_FO-20040420a.zip
Group: Text tools
URL: http://fo.speling.org/
License: GPL+
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Faroese hyphenation rules.

%prep
%setup -q -c

%build
for i in README_hyph_fo_FO.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_fo_FO.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README_hyph_fo_FO.txt
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040420-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040420-alt1_2
- import by fcmass

