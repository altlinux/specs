Name: hyphen-te
Summary: Telugu hyphenation rules
%define upstreamid 20100204
Version: 0.%{upstreamid}
Release: alt1_4
Source: http://git.savannah.gnu.org/cgit/smc.git/plain/hyphenation/hyph_te_IN.dic
Group: Text tools
URL: http://wiki.smc.org.in
License: LGPLv3+
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Telugu hyphenation rules.

%prep
%setup -T -q -c
cp -p %{SOURCE0} .

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%{_datadir}/hyphen/*

%changelog
* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100204-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100204-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100204-alt1_2
- import by fcmass

