# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-as
Summary: Assamese hunspell dictionaries
Version: 1.0.3
Release: alt2_12
Group: Text tools
Source: http://extensions.services.openoffice.org/files/2318/4/as_IN.oxt
URL: http://extensions.services.openoffice.org/project/AssameseDict
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Assamese hunspell dictionaries.

%prep
%setup -q -c -n hunspell-as

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p as_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_as_IN.txt COPYING COPYING.MPL COPYING.GPL COPYING.LGPL

%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_7
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4
- import from Fedora by fcimport

