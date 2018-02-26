# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: mythes-sk
Summary: Slovak thesaurus
%define upstreamid 20120412
Version: 0.%{upstreamid}
Release: alt1_1
Source: http://www.sk-spell.sk.cx/thesaurus/download/OOo-Thesaurus2-sk_SK.zip
Group: Text tools
URL: http://www.sk-spell.sk.cx/thesaurus/
BuildRequires: perl
License: BSD
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Slovak thesaurus.

%prep
%setup -q -c

%build
for i in README_th_sk_SK_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sk_SK_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc README_th_sk_SK_v2.txt
%{_datadir}/mythes/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20120412-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20111016-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20111016-alt1_1
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110807-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110608-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110316-alt1_1
- import by fcmass

