# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-eo
Summary: Esperanto hunspell dictionaries
Version: 1.0
Release: alt2_0.4.dev
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
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.4.dev
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.3.dev
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.dev
- import from Fedora by fcimport

