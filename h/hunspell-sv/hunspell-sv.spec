# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-sv
Summary: Swedish hunspell dictionaries
Version: 2.28
Release: alt1_4
Source: http://extensions.libreoffice.org/extension-center/swedish-spelling-dictionary-den-stora-svenska-ordlistan/releases/2.28/ooo_swedish_dict_2-28.oxt
Group: Text tools
URL: http://dsso.se/
License: LGPLv3
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Swedish hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sv

%build
sed -i 's/\r$//' LICENSE_sv_SE.txt
sed -i 's/\r$//' LICENSE_en_US.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/*.dic dictionaries/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc LICENSE_sv_SE.txt LICENSE_en_US.txt

%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.28-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.28-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.28-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.28-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_2
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1_2
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1_1
- update to new release by fcimport

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1_2
- import from Fedora by fcimport

