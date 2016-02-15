# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: mythes-nl
Summary: Dutch thesaurus
%define upstreamid 20130131
Version: 0.%{upstreamid}
Release: alt1_5
Source: http://data.opentaal.org/opentaalbank/thesaurus/download/thes_nl.oxt
Group: Text tools
URL: http://data.opentaal.org/opentaalbank/thesaurus
License: BSD or CC-BY
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Dutch thesaurus.

%prep
%setup -q -c

%build
for i in README_th_nl.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_nl_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_nl_NL_v2.dat
cp -p th_nl_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_nl_NL_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s th_nl_NL_v2.dat "th_"$lang"_v2.dat"
        ln -s th_nl_NL_v2.idx "th_"$lang"_v2.idx"
done

%files
%doc README_th_nl.txt
%{_datadir}/mythes/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20130131-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20130131-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20130131-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130131-alt1_2
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.20130131-alt1_1
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.20120912-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20120613-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.20120613-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20120413-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20111017-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20111017-alt1_1
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110808-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110609-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110318-alt1_1
- import by fcmass

