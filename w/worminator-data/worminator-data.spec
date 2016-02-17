Name:           worminator-data
Version:        3.0R2.1
Release:        alt2_14
Summary:        Data for worminator the game
Group:          Games/Other
License:        GPLv2+
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://download.sourceforge.net/worminator/%{name}-%{version}.tar.gz
Source1:	license.txt
Source2:        license-change.txt
BuildArch:      noarch
Requires:       worminator
Source44: import.info

%description
Data for worminator the game where you play as The Worminator and fight your
way through many levels of madness and mayhem. Worminator features nine unique
weapons, visible character damage, full screen scrolling, sound and music, and
much more!


%prep
#put the docs where %doc wants them
install -p -m 0644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_DIR


%build
#empty / notthing to build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/worminator
tar xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/worminator
rm $RPM_BUILD_ROOT%{_datadir}/worminator/ICON.ICO


%files
%doc license.txt license-change.txt
%{_datadir}/worminator


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_8
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 3.0R2.1-alt1_7
- converted from Fedora by srpmconvert script

