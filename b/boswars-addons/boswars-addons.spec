Name:		boswars-addons
Version:	2.6
Release:	alt2_12
Summary:	Addon maps for Bos Wars real-time strategy game

Group:		Games/Other
License:	GPLv2+
URL:		http://www.boswars.org/addons/addons.shtml
Source0:	http://www.boswars.org/addons/maps/greenlands.map.tgz
Source1:	http://www.boswars.org/addons/maps/obese.map.tgz
Source2:	http://www.boswars.org/addons/maps/obese2.map.tgz
Source3:	http://www.boswars.org/addons/maps/wargrounds.map.tgz
Source4:	http://www.boswars.org/addons/maps/wetlands03.map.tgz
BuildArch:	noarch

Requires:	boswars >= 2.6
Source44: import.info

%description
A collection of addon maps for Bos Wars real-time strategy game.

%prep
%setup -q -c -n boswars-addons
%setup -q -c -n boswars-addons -T -D -a 1
%setup -q -c -n boswars-addons -T -D -a 2
%setup -q -c -n boswars-addons -T -D -a 3
%setup -q -c -n boswars-addons -T -D -a 4


%build
# Nothing to build


%install
install -d $RPM_BUILD_ROOT%{_datadir}/boswars/maps
cp -a * $RPM_BUILD_ROOT%{_datadir}/boswars/maps


%files
%{_datadir}/boswars/maps/*



%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_10
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_5
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_4
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_4
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_3
- update to new release by fcimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_4
- converted from Fedora by srpmconvert script

