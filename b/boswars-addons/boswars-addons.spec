Name:		boswars-addons
Version:	2.6
Release:	alt2_4
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
Requires:	boswars < 2.7
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
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_4
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_4
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_3
- update to new release by fcimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_4
- converted from Fedora by srpmconvert script

