# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
Name: mythes-ro
Summary: Romanian thesaurus
Version: 3.3
Release: alt1_4
Source: http://downloads.sourceforge.net/rospell/th_ro_RO.%{version}.zip
Group: Text tools
URL: http://rospell.sourceforge.net/
License: GPLv2+
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Romanian thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ro_RO.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ro_RO_v2.dat
cp -p th_ro_RO.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ro_RO_v2.idx

%files
%doc README COPYING.GPL 
%{_datadir}/mythes/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_3
- import by fcmass

