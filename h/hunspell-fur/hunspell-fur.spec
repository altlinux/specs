# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-fur
Summary: Friulian hunspell dictionaries
%define upstreamid 20050912
Version: 0.%{upstreamid}
Release: alt2_12
Source: http://digilander.libero.it/paganf/coretors/myspell-fur-12092005.zip
Group: Text tools
URL: http://digilander.libero.it/paganf/coretors/dizionaris.html
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Friulian hunspell dictionaries.

%prep
%setup -q -n myspell-fur-12092005

%build
chmod -x *
for i in COPYING.txt LICENCE.txt LEIMI.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-15 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p fur_IT.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc COPYING.txt LEIMI.txt LICENCE.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050912-alt1_5
- import from Fedora by fcimport

