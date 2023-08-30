Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: mythes-mi
Summary: Maori thesaurus
%global upstreamid 20080630
Version: 0.%{upstreamid}
Release: alt1_29
# Source is dead now
# Source: http://packages.papakupu.maori.nz/mythes/mythes-mi-0.1.%%{upstreamid}-beta.tar.gz
Source: mythes-mi-0.1.%{upstreamid}-beta.tar.gz
URL: http://papakupu.maori.nz/
License: LicenseRef-Fedora-Public-Domain
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Maori thesaurus.

%prep
%setup -q -c


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p mi.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.dat
cp -p mi.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.idx


%files
%doc mi.AUTHORS mi.README mi.LICENSE
%{_datadir}/mythes/*

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.20080630-alt1_29
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_5
- import by fcmass

