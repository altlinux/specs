# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
Name: mythes-hu
Summary: Hungarian thesaurus
%define upstreamid 20101019
Version: 0.%{upstreamid}
Release: alt1_3
Source: http://extensions.services.openoffice.org/e-files/1283/8/dict-hu.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/project/hu_dicts
License: GPLv2+
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Hungarian thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_hu_HU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc README_th_hu_HU_v2.txt
%{_datadir}/mythes/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20101019-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20101019-alt1_2
- import by fcmass

