# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-ro
Summary: Romanian hyphenation rules
Version: 3.3.6
Release: alt1_3
Source: http://downloads.sourceforge.net/rospell/hyph_ro_RO.3.3.6.zip
Group: Text tools
URL: http://rospell.sourceforge.net/
License: GPLv2+
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Romanian hyphenation rules.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/

%files
%doc COPYING.GPL README          
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_2
- import by fcmass

