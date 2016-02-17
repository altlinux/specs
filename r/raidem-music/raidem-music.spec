Name:           raidem-music
Version:        1.0
Release:        alt2_12
Summary:        Background music for the game raidem
Group:          Games/Other
License:        CC-BY
URL:            http://www.dilvie.com/
Source0:        http://www.dilvie.com/music/dilvie_-_the_dragonfly.ogg
# transcoded from: http://www.dilvie.com/music/dilvie_-_up_in_ashes.mp3
Source1:        dilvie_-_up_in_ashes.ogg
Source2:	http://www.dilvie.com/music/dilvie_-_half_baked.ogg
Source3:        http://www.dilvie.com/music/dilvie_-_east_of_the_sun.ogg
Source4:        license.txt
Buildarch:      noarch
Requires:       raidem >= 0.3.1
Source44: import.info

%description
Music created by Eric Hamilton (dilvie) for the game Raid'em


%prep
%setup -q -c -T
cp %{SOURCE4} .


%build
# nothing todo content only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/menu
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/raidem/music/menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level1
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level2
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level2
mkdir -p $RPM_BUILD_ROOT%{_datadir}/raidem/music/level3
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/raidem/music/level3


%files
%doc license.txt
%{_datadir}/raidem/music


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- initial release by fcimport

