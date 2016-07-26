Group: Text tools
%define dicname stardict-english-czech
Name: stardict-dic-cs_CZ
Summary: Czech dictionaries for StarDict
Version: 20150213
Release: alt1_5
License: GFDL
Provides: stardict-dic-cs = %{?epoch:%{epoch}:}%{version}-%{release}

URL: http://cihar.com/software/slovnik/
Source0: http://dl.cihar.com/slovnik/stable/%{dicname}-%{version}.tar.gz

BuildArch: noarch
Requires: stardict stardict-plugin-espeak stardict-plugin-spell
Source44: import.info

%description
Czech-English and English-Czech translation dictionaries for StarDict, a
GUI-based dictionary software.

%prep
%setup -q -c -n %{dicname}-%{version}

%build

%install
install -m 0755 -p -d ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic
install -m 0644 -p  %{dicname}-%{version}/cz* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/
install -m 0644 -p  %{dicname}-%{version}/en* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/

%files
%doc %{dicname}-%{version}/README
%{_datadir}/stardict/dic/*

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20150213-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20150213-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 20150213-alt1_2
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20110801-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20110801-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20110801-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20110801-alt2_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110801-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110801-alt1_2
- update to new release by fcimport

* Thu Sep 01 2011 Igor Vlasenko <viy@altlinux.ru> 20110801-alt1_1
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 20100216-alt1_2
- initial release by fcimport

