Name: hunspell-mi
Summary: Maori hunspell dictionaries
%define upstreamid 20080630
Version: 0.%{upstreamid}
Release: alt2_11
Source: http://packages.papakupu.maori.nz/hunspell/hunspell-mi-0.1.%{upstreamid}-beta.tar.gz
Group: Text tools
URL: http://papakupu.maori.nz/
License: GPLv3+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Maori hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mi-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mi.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/mi_NZ.aff
cp -p mi.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/mi_NZ.dic

%files
%doc mi.AUTHORS mi.LICENSE mi.README
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20080630-alt1_4
- import from Fedora by fcimport

