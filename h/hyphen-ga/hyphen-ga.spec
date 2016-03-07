Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-ga
Summary: Irish hyphenation rules
%global upstreamid 20040220
Version: 0.%{upstreamid}
Release: alt1_12
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_ga_IE.zip
URL: http://borel.slu.edu/fleiscin/index.html
License: GPL+
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Irish hyphenation rules.

%prep
%setup -q -c -n hyphen-ga

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ga_IE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_ga_IE.txt
%{_datadir}/hyphen/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_12
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_10
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_4
- import by fcmass

