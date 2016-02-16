# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-is
Summary: Icelandic hyphenation rules
%define upstreamid 20030920
Version: 0.%{upstreamid}
Release: alt1_14
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_is_IS.zip
Patch0: hyphen-is-lppl-license-fix.patch
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+ or SISSL
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Icelandic hyphenation rules.

%prep
%setup -q -c
%patch0 -p1

%build
chmod -x *
for i in README_hyph_is_IS.txt; do
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
%doc README_hyph_is_IS.txt
%{_datadir}/hyphen/*

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_13
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20030920-alt1_6
- import by fcmass

