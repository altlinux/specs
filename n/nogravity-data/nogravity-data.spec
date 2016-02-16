# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           nogravity-data
Version:        2.00
Release:        alt2_14
Summary:        Data files for No Gravity
Group:          Games/Other
License:        GPLv2+
URL:            http://www.realtech-vr.com/nogravity/
Source0:        http://downloads.sourceforge.net/nogravity/rt-%{name}.zip
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
# nothing to build data only 


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/nogravity
install -p -m 644 NOGRAVITY.RMX $RPM_BUILD_ROOT%{_datadir}/nogravity


%files
%doc GNU.TXT
%{_datadir}/nogravity


%changelog
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

