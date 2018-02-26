# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-hy
Summary: Armenian hunspell dictionaries
Version: 0.20.0
Release: alt2_3
Source: http://downloads.sourceforge.net/armspell/myspell-hy-%{version}.tar.gz
Group: Text tools
URL: http://sourceforge.net/projects/armspell
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Armenian hunspell dictionaries.

%prep
%setup -q -n myspell-hy-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hy_AM.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc Copyright ChangeLog COPYING
%{_datadir}/myspell/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_2
- import from Fedora by fcimport

