# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-ga
Summary: Irish hyphenation rules
%define upstreamid 20040220
Version: 0.%{upstreamid}
Release: alt1_5
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_ga_IE.zip
Group: Text tools
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
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20040220-alt1_4
- import by fcmass

