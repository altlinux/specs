Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hyphen-mi
Summary: Maori hyphenation rules
%global upstreamid 20080630
Version: 0.%{upstreamid}
Release: alt1_28
# Source is dead now
# Source: http://packages.papakupu.maori.nz/hunspell-hyphen/hunspell-hyphen-mi-0.1.%%{upstreamid}-beta.tar.gz
Source: hunspell-hyphen-mi-0.1.%{upstreamid}-beta.tar.gz
URL: http://papakupu.maori.nz/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Maori hyphenation rules.

%prep
%setup -q -c


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p mi.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_mi_NZ.dic


%files
%doc mi.LICENSE mi.README
%{_datadir}/hyphen/*

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.20080630-alt1_28
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_16
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_13
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_12
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_10
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_4
- import by fcmass

