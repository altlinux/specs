%define fedora 21
Name:		fbg2
Version:	0.4
Release:	alt3_12
Summary:	A falling block stacking game
Group:		Games/Other
# Code is GPLv2+, music and graphics are CC-BY-SA
License:	GPLv2+ and CC-BY-SA
URL:		http://sourceforge.net/projects/fbg/
# Cannot use this source as is. Need to remove
# fbg2-0.4/Data/Music/FallingBlockGameSndTrk.ogg
# because it is a sound trademark associated with a popular
# falling blocks game.
# rm -rf fbg2-0.4/Data/Music/FallingBlockGameSndTrk.ogg
# Source0:	http://downloads.sourceforge.net/project/fbg/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-clean.tar.gz
# http://www.jamendo.com/en/track/165311/russian
Source1:	RudySeb_-_russian.ogg
Source2:	README.music
# 64 x 64 public domain image for logo
Source3:	fbg2.png
Patch0:		fbg2-0.4-desktop-fix.patch
BuildRequires:	radius-engine-devel >= 0.7 desktop-file-utils zip
# rhbz#949506, also see rhbz#949167
%if 0%{?fedora} >= 19
Obsoletes:	fbg < 0.9.1-13
Provides:	fbg = 0.9.1-13
%endif
Source44: import.info

%description
Falling Block Game is a free, open source block stacking game. The object of 
the game is to move and rotate pieces in order to fill in complete rows. The 
more rows you clear at once, the more points you score! 

%prep
%setup -q
%patch0 -p1 -b .fix
cp %{SOURCE1} Data/Music/FallingBlockGameSndTrk.ogg
cp %{SOURCE2} .
mv fbg2.png fbg2-small.png
cp %{SOURCE3} .

chmod -x License.txt ChangeLog *.c

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/fbg2.desktop

%files
%doc License.txt ChangeLog README.music
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_9
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_8
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_5
- update to new release by fcimport

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_4
- rebuild with new radius-engine

* Mon Sep 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_3
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_1
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_3
- update to new release by fcimport

* Sun Jul 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_2
- initial release by fcimport

