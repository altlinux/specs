%define dicname stardict-english-czech
Name: stardict-dic-cs_CZ
Summary: Czech dictionaries for StarDict
Version: 20110801
Release: alt2_2
Group: Text tools
License: GFDL

URL: http://cihar.com/software/slovnik/
Source0: http://dl.cihar.com/slovnik/stable/%{dicname}-%{version}.tar.gz

BuildArch: noarch
Source44: import.info


%description
Czech-English and English-Czech translation dictionaries for StarDict, a
GUI-based dictionary software.

%prep
%setup -q -c -n %{dicname}-%{version}

%build

%install
rm -rf ${RPM_BUILD_ROOT}
install -m 0755 -p -d ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic
install -m 0644 -p  %{dicname}-%{version}/cz* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/
install -m 0644 -p  %{dicname}-%{version}/en* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/

%files
%doc %{dicname}-%{version}/README
%{_datadir}/stardict/dic/*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110801-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20110801-alt1_2
- update to new release by fcimport

* Thu Sep 01 2011 Igor Vlasenko <viy@altlinux.ru> 20110801-alt1_1
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 20100216-alt1_2
- initial release by fcimport

