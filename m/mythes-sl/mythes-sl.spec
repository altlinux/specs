# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: mythes-sl
Summary: Slovenian thesaurus
%define upstreamid 20120413
Version: 0.%{upstreamid}
Release: alt1_1
Source: http://193.2.66.133:85/download/thes_sl_SI_v2.zip
Group: Text tools
URL: http://www.tezaver.si/
BuildRequires: perl
License: LGPLv2+
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Slovenian thesaurus.

%prep
%setup -q -c

%build
chmod -x *
for i in README_th_sl_SI_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sl_SI_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc README_th_sl_SI_v2.txt
%{_datadir}/mythes/*

%changelog
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

