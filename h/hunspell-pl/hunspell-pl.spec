# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-pl
Summary: Polish hunspell dictionaries
%define upstreamid 20120309
Version: 0.%{upstreamid}
Release: alt1_1
Source: http://sjp.pl/slownik/ort/sjp-myspell-pl-%{upstreamid}.zip
Group: Text tools
URL: http://www.kurnik.pl/dictionary/
License: LGPLv2+ or GPL+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Polish hunspell dictionaries.

%prep
%setup -q -c hunspell-pl

%build
unzip pl_PL.zip

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_pl_PL.txt
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20120309-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20111017-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20111017-alt1_1
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110808-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110609-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110318-alt2_1
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110318-alt1_1
- import from Fedora by fcimport

