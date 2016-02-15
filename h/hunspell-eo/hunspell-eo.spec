# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-eo
Summary: Esperanto hunspell dictionaries
Version: 1.0
Release: alt2_0.10.dev
Group: Text tools
Source: http://extensions.services.openoffice.org/files/3377/1/1.0-dev.oxt
URL: http://extensions.services.openoffice.org/project/literumilo
License: LGPLv3
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Esperanto hunspell dictionaries.

%prep
%setup -q -c

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p literumilo.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.dic
cp -p literumilo.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.aff

%files
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.10.dev
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.9.dev
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.8.dev
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.7.dev
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.6.dev
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.5.dev
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.4.dev
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.3.dev
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.dev
- import from Fedora by fcimport

