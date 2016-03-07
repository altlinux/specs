Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-mk
Summary: Macedonian hunspell dictionaries
%global upstreamid 20051126
Version: 0.%{upstreamid}
Release: alt2_12
Source: http://mk.openoffice.org/files/documents/215/3053/mk_MK.zip
URL: http://mk.openoffice.org
License: GPL+
BuildArch: noarch
Patch0: hunspell-mk-iconv.patch

Requires: hunspell
Source44: import.info

%description
Macedonian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mk
#change encoding name to use the name that iconv knows this under
%patch0 -p1 -b .iconv.patch

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc README_mk_MK.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20051126-alt1_4
- import from Fedora by fcimport

