%global upstreamid 20111229
%global upstream_version 0.7.0

Name: hyphen-ta
Summary: Tamil hyphenation rules
Version: 0.%{upstreamid}
Release: alt1_2
Source: http://download.savannah.gnu.org/releases/smc/hyphenation/patterns/%{name}-%{upstream_version}.tar.bz2
Group: Text tools
URL: http://wiki.smc.org.in
License: LGPLv3+
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Tamil hyphenation rules.

%prep
%setup -q -n %{name}-%{upstream_version} 

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
install -m644 -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README COPYING ChangeLog
%{_datadir}/hyphen/*

%changelog
* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.20111229-alt1_2
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20111229-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100204-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100204-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100204-alt1_2
- import by fcmass

