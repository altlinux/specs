Name: hunspell-sw
Summary: Swahili hunspell dictionaries
%define upstreamid 20050819
Version: 0.%{upstreamid}
Release: alt2_12
Group: Text tools
Source: http://www.it46.se/downloads/openoffice/dictionary/dictionary_myspell_sw_TZ_1.1.tar.gz
URL: http://www.it46.se
License: LGPLv2+
BuildArch: noarch
BuildRequires: libhunspell-devel hunspell-utils

Requires: hunspell
Source44: import.info

%description
Swahili hunspell dictionaries.

%prep
%setup -q -c

%build
for i in README_sw_TZ.txt; do
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
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
sw_TZ_aliases="sw_KE"
for lang in $sw_TZ_aliases; do
        ln -s sw_TZ.aff $lang.aff
        ln -s sw_TZ.dic $lang.dic
done
popd

%files
%doc README_sw_TZ.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050819-alt1_5
- import from Fedora by fcimport

