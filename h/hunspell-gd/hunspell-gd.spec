Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-gd
Summary: Scots Gaelic hunspell dictionaries
Version: 2.6
Release: alt1_7
Source: http://downloads.sourceforge.net/project/aoo-extensions/4587/8/hunspell-gd-2.6.oxt
URL: http://extensions.services.openoffice.org/en/project/faclair-afb
License: GPLv2+ and GPLv3+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Scots Gaelic hunspell dictionaries.

%prep
%setup -q -c hunspell-gd-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/gd_GB.dic dictionaries/gd_GB.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc dictionaries/README_gd_GB.txt LICENSES-en.txt
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_7
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_3
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_1
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_2
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_1
- update to new release by fcimport

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1
- import from Fedora by fcimport

