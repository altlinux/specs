# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-kn
Summary: Kannada hunspell dictionaries
Version: 1.0.3
Release: alt2_4
Group: Text tools
Source: http://extensions.services.openoffice.org/files/2628/1/kannada.oxt
URL: http://extensions.services.openoffice.org/project/kannada
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Kannada hunspell dictionaries.

%prep
%setup -q -c -n hunspell-kn

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p kn_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_kn_IN.txt COPYING COPYING.MPL COPYING.GPL COPYING.LGPL

%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_3
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3
- import from Fedora by fcimport

