# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-sk
Summary: Slovak hyphenation rules
%define upstreamid 20031227
Version: 0.%{upstreamid}
Release: alt1_7
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_sk_SK.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL+
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Slovak hyphenation rules.

%prep
%setup -q -c

%build
chmod -x *
for i in README_hyph_sk_SK.txt; do
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
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README_hyph_sk_SK.txt
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20031227-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20031227-alt1_6
- import by fcmass

