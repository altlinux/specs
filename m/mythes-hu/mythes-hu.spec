# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: mythes-hu
Summary: Hungarian thesaurus
%define upstreamid 20101019
Version: 0.%{upstreamid}
Release: alt1_5
Source: http://extensions.services.openoffice.org/e-files/1283/8/dict-hu.oxt
Group: Text tools
URL: http://extensions.services.openoffice.org/project/hu_dicts
#bundled but unused spell-checking stuff is under GPLv2+ or LGPLv2+ or MPLv1.1
#base for bundled but unused hyphenation stuff is under GPLv2
#additional patch to unused hyphenation stuff is MPL/GPL/LGPL
License: GPLv2+ and (GPLv2+ or LGPLv2+ or MPLv1.1) and GPLv2 and (GPL+ or LGPLv2+ or MPLv1.1)
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
* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.20101019-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20101019-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20101019-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20101019-alt1_2
- import by fcmass

