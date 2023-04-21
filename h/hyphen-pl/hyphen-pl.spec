Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hyphen-pl
Summary: Polish hyphenation rules
%global upstreamid 20060726
Version: 0.%{upstreamid}
Release: alt1_28
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_pl_PL.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Polish hyphenation rules.

%prep
%setup -q -c -n hyphen-pl


%build
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
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.20060726-alt1_28
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_13
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_11
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20060726-alt1_5
- import by fcmass

