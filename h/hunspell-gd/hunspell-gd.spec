# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-gd
Summary: Scots Gaelic hunspell dictionaries
Version: 2.3
Release: alt1_2
Source: http://extensions.services.openoffice.org/e-files/4587/6/hunspell-gd-2.3.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/en/project/faclair-afb
License: GPLv3+
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

