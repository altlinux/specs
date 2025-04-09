Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 38

Name:           nogravity-data
Version:        2.00
Release:        alt2_%autorelease
Summary:        Data files for No Gravity game
License:        GPL-2.0-or-later
URL:            https://www.realtech-vr.com/home/?page_id=948
Source0:        https://downloads.sourceforge.net/nogravity/rt-%{name}.zip
BuildArch:      noarch
# So that we get removed together with nogravity itself
Requires:       nogravity >= %{version}
Source44: import.info

%description
Data files (audio, maps, etc) for No Gravity.

%prep
%setup -q -c
sed -i 's/\r//g' GNU.TXT

%build
# nothing to build, data only

%install
install -D -p -m 0644 NOGRAVITY.RMX %{buildroot}%{_datadir}/nogravity/NOGRAVITY.RMX

%files
%doc --no-dereference GNU.TXT
%{_datadir}/nogravity/

%changelog
* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 2.00-alt2_38
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_15
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_8
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_7
- converted from Fedora by srpmconvert script

