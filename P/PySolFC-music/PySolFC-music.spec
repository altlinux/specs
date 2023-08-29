Group: Games/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define mainversion 1.1

Name:           PySolFC-music
Version:        4.50
Release:        alt1_11
Summary:        Music for PySolFC

License:        GPL-2.0-or-later
URL:            https://pysolfc.sourceforge.io/
Source0:        https://github.com/shlomif/pysol-music/archive/%{version}/pysol-music-%{version}.tar.gz
Requires:       PySolFC python3-module-PySolFC

BuildArch: noarch
Source44: import.info

%description
This package contains the background music for %{name}


%prep
%setup -q -n pysol-music-%{version}

%build

%install
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/PySolFC/music
cp -a data/music/* $RPM_BUILD_ROOT%{_datadir}/PySolFC/music

%files
%doc README NEWS COPYING
%dir %{_datadir}/PySolFC/music
%{_datadir}/PySolFC/music/*

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 4.50-alt1_11
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 4.50-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_15
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 4.40-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.40-alt1_8
- update to new release by fcimport

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 4.40-alt1_7
- initial release by fcimport

