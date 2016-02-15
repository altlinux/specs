# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-tn
Summary: Tswana hunspell dictionaries
%define upstreamid 20091101
Version: 0.%{upstreamid}
Release: alt2_9
Source: http://releases.mozilla.org/pub/mozilla.org/addons/46617/tswana__south_africa__dictionary-%{upstreamid}-fx+tb.xpi
Group: Text tools
URL: http://www.translate.org.za/
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tswana hunspell dictionaries.

%prep
%setup -q -c -n hunspell-tn

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/tn-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/tn_ZA.aff
cp -p dictionaries/tn-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/tn_ZA.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
tn_ZA_aliases="tn_BW"
for lang in $tn_ZA_aliases; do
        ln -s tn_ZA.aff $lang.aff
        ln -s tn_ZA.dic $lang.dic
done
popd

%files
%doc README-tn-ZA.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt1_2
- import from Fedora by fcimport

